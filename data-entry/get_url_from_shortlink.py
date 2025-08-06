# Seems like shortlinks don't work on iOS.
# This script is to get all the shortlinks in the database and convert them to regular URLs

import csv      # Read respectthread_data.csv
import os       # To get the absolute path for importing
import praw 	# Interface with Reddit's API
import psycopg2 # Interface with PostgreSQL
import re       # Regular expressions
import sys      # For terminal arguments and to import from different folders
import time             # To make an interval for the bot to wait
sys.path.insert(1, "../main-bot")   # This path is to import modules the bot uses. It is relative to the shell script that runs the tests.

import config           # Login details


def bot_login() -> praw.Reddit:
    print("Logging in...")
    r = praw.Reddit(username = config.r_username,
                password = config.r_password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "respectthread responder v0.2")
    print("Logged in")
    return r


r = bot_login()
shortlink_pattern = re.compile(r"https://redd\.it/([a-zA-A0-9][a-zA-A0-9]{5,99})")
def parse_row(con, cur, row):
    link = row[-1]
    match = re.match(shortlink_pattern, link)

    # https://www.geeksforgeeks.org/python/re-match-in-python/
    if not match:
        print("{} is not a shortlink".format(link))
        return

    try:
        # https://stackoverflow.com/questions/67086726/how-to-retrieve-a-reddit-post-by-id-using-praw
        respectthread = r.submission(url=link)
        url = respectthread.url
        if url == "":
            return
        
        update_link_query = "UPDATE respectthread SET link = '{}' WHERE link = '{}';".format(url, link)
        print(update_link_query)
        cur.execute(update_link_query)
        con.commit()
        time.sleep(5)
    except:
        print("ERROR: Could not update for {}".format(link))

# Opening connection to database
con = psycopg2.connect(
    host = config.host,
    database = config.database,
    user = config.d_user,
    password = config.d_password
)
cur = con.cursor()


relative_import_path = "../csv-data"
import_path = os.path.abspath(relative_import_path)
with open("{}/respectthread_data.csv".format(import_path), "r", newline="", encoding="utf-8") as csvfile:
    respectthread_data = csv.reader(csvfile, delimiter=",", quotechar='"', escapechar="`")
    for row in respectthread_data:
        parse_row(con, cur, row)


con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

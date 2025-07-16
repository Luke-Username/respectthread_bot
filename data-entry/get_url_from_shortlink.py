# Seems like shortlinks don't work on iOS.
# This script is to get all the shortlinks in the database and convert them to regular URLs

import psycopg2 # Interface with PostgreSQL
import config   # Login details
import csv      # Read respectthread_data.csv
import praw 	# Interface with Reddit's API
import re       # Regular expressions
#sys.path.insert(1, "../csv-data")


def bot_login() -> praw.Reddit:
    print("Logging in...")
    r = praw.Reddit(username = config.r_username,
                password = config.r_password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "respectthread responder v0.2")
    print("Logged in")
    return r

r: praw.Reddit = bot_login()
shortlink_pattern = re.compile(r"https://redd\.it/([a-zA-A0-9][a-zA-A0-9]{5,99})")
def parse_row(row: list[str]):
    link: str = row[-1]
    match = re.match(shortlink_pattern, link)

    # https://www.geeksforgeeks.org/python/re-match-in-python/
    if not match:
        return

    # https://stackoverflow.com/questions/67086726/how-to-retrieve-a-reddit-post-by-id-using-praw
    respectthread: praw.models.Submission = r.submission(url=link)
    url: str = respectthread.url
    print(url)

relative_import_path = "../csv-data"
import_path = os.path.abspath(relative_import_path)
#with open("respectthread_data.csv") as csvfile:
with open("{}/respectthread_data.csv".format(import_path), "r", encoding="utf-8") as csvfile:
    respectthread_data = csv.reader(csvfile, delimiter=",", newline="", quotechar='"', escapechar="`")
    for row in respectthread_data:
        parse_row(row)

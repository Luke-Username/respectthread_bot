# Modules
import psycopg2                     # Interface with PostgreSQL
import sys                          # For terminal arguments and to import from different folders
sys.path.insert(1, "../main-bot")   # This path is to import modules the bot uses. It is relative to the shell script that runs the tests.

# Custom modules
import config       # Login details
import matchup_checker as mcr
import replier
import text_processing as tp

#print("Connecting to database...")
con = psycopg2.connect(
    host = config.host,
    database = config.database,
    user = config.d_user,
    password = config.d_password
)
#print("Connected to database")
cur = con.cursor()

# The first argument is the file name containing the post text to test on
filename = sys.argv[1]
f = open(filename, "r", encoding="utf-8")
title = f.readline()
post = title + " " + f.read()

character_list = mcr.search_characters(title, post, cur)
if character_list:
    print(replier.generate_comment(cur, character_list, False))

# Close the cursor and connection
cur.close()
con.close()
#print("Disconnected from database")

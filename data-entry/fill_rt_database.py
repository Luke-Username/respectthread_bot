# This script was used to insert respect thread links into the database. 
# It only had to be run when first creating the bot. The script is now commented out.
# It reads a file containing the contents of one of the respect thread master lists,
# and it inserts the links it finds into the database.
#
# For instance, to insert the contents found at
# https://www.reddit.com/r/respectthreads/wiki/anime,
# "wiki_source.txt" would be replaced by "respectthread-master-lists/anime.txt"
# (assuming anime.txt has the source content copied and pasted in it.)

"""
import psycopg2 # Interface with PostgreSQL
import config   # Login details
import praw 	# Interface with Reddit's API
import re       # Regular expressions

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.r_username,
                password = config.r_password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "respectthread responder v0.2")
    print("Logged in")
    return r

r = bot_login()

insert_query = "INSERT INTO respectthread (title, link) VALUES "
wiki_text = open("wiki_source.txt", "r", encoding="utf-8").read()
pattern = re.compile(r"\[.+]\((https://redd\.it/[a-zA-A0-9]{6})\)") # This regex pattern only matches Reddit shortlinks.
                                                                    # Non-shortlinks can be found with \[.+\]\((?!https://redd\.it/[a-zA-A0-9]{6})(.+)\)
matches = pattern.finditer(wiki_text)
for match in matches:
	shortlink = match.group(1)
	respectthread = r.submission(url=shortlink)
	title = respectthread.title.replace("'", "''")
	insert_query += "('{}', '{}'),".format(title, shortlink)
	print(title)

insert_query = insert_query.strip(',') + ';'                        # Replace trailing ',' with ';'


#connect to the database
con = psycopg2.connect(
			host = config.host,
			database = config.database,
			user = config.d_user,
			password = config.d_password
)
cur = con.cursor()

cur.execute(insert_query)
con.commit()
print("Inserted into database")

# Close the cursor and connection to prevent leaks
cur.close()
con.close()
"""

# This script is the main bot. It can be run with the shell script, runBotScript.sh.
# It is a Reddit bot that looks through new posts from a list of subreddit,
# and analyzes their contents for matches inside its database.
# If it finds a match, it will generate a comment linking the correct respect threads.
# More info on respect threads can be found here: https://www.reddit.com/r/respectthreads/

# Modules
import praw             # Interface with Reddit's API
import psycopg2         # Interface with PostgreSQL
import time             # To make an interval for the bot to wait

# Custom modules
import config           # Login details
import comment_reader   # To read and reply to comments
import file_io_manager  # For file input and output
import post_reader      # To read and reply to posts

posts_list = []
comments_list = []
blacklist = []

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.r_username,
                password = config.r_password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "respectthread responder v0.2")
    print("Logged in")
    if posts_list[-1] != "":
        file_io_manager.write_to("saved_posts.txt", "\n")
    return r

def check_inbox_for_optout_requests(r):
    unread_messages = []
    for reply in r.inbox.unread(limit=None):
        if reply.subject == "OPTOUTREQUEST":
            if reply.author.name not in blacklist:
                file_io_manager.write_to("blacklist.txt", reply.author.name + "\n")
                blacklist.append(reply.author)
            unread_messages.append(reply)
    r.inbox.mark_read(unread_messages)

def run_bot(r):
    print("Connecting to database...")
    con = psycopg2.connect(
        host = config.host,
        database = config.database,
        user = config.d_user,
        password = config.d_password
    )
    print("Connected to database")
    cur = con.cursor()

    comment_reader.read_comments(r, cur, comments_list)
    post_reader.read_posts(r, cur, posts_list, blacklist)

    # Close the cursor and connection
    cur.close()
    con.close()
    print("Disconnected from database")
    sleep_time = 30
    print("Sleeping for {} seconds...".format(sleep_time))
    time.sleep(sleep_time)

terminate_time = 40
posts_list = file_io_manager.get_content_as_list("saved_posts.txt")
comments_list = file_io_manager.get_content_as_list("saved_comments.txt")
blacklist = file_io_manager.get_content_as_list("blacklist.txt")
r = bot_login()
while True:
    check_inbox_for_optout_requests(r)
    run_bot(r)
    terminate_time -= 1
    if terminate_time <= 0:
        exit()

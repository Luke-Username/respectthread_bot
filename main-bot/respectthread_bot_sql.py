# This script is the main bot. It can be run with the shell script, runBotScript.sh.
# It is a Reddit bot taht looks through new posts from a list of subreddit,
# and analyzes their contents for matches inside its database.
# If it finds a match, it will generate a comment linking the correct respect threads.
# More info on respect threads can be found here: https://www.reddit.com/r/respectthreads/

# Modules
import os           # To check if a file exists
import praw         # Interface with Reddit's API
import psycopg2     # Interface with PostgreSQL
import time         # To make an interval for the bot to wait

# Custom modules
import config       # Login details
import matchup_checker as mcr
import replier
import text_processing as tp

subreddit_list = ["respectthread_bot"]
posts_list = []
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
        with open("saved_posts.txt", "a") as f:
            f.write('\n')
    return r

def get_saved_posts():
    # Make sure the file exists.
    if not os.path.isfile("saved_posts.txt"):
        posts_list = []
    else:
        # "r" is to read from saved_posts.txt as the variable f
        with open("saved_posts.txt", "r") as f:
            posts_list = f.read().split("\n")
    return posts_list

def check_inbox_for_optout_requests(r):
    unread_messages = []
    for reply in r.inbox.unread(limit=None):
        if reply.subject == "OPTOUTREQUEST":
            if reply.author.name not in blacklist:
                with open("blacklist.txt", "a") as f:
                    f.write(reply.author.name + "\n")
                blacklist.append(reply.author)
            unread_messages.append(reply)
    r.inbox.mark_read(unread_messages)

def get_blacklist():
    if not os.path.isfile("blacklist.txt"):
        blacklist = []
    else:
        with open("blacklist.txt", "r") as f:
            blacklist = f.read().split("\n")
    return blacklist

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

    for sub in subreddit_list:
        print("Obtaining new posts from r/{}".format(sub))
        submissions = r.subreddit(sub).new(limit=7)
        for submission in submissions:
            if submission.id not in posts_list and submission.author.name not in blacklist:
                title = tp.strip_accents(submission.title)
                post = title + " " + tp.strip_accents(submission.selftext)
                character_list = mcr.search_characters(title, post, cur)
                if character_list:
                    replier.reply_to_submission(r, submission, cur, character_list, True)
            if submission.id not in posts_list:
                with open("saved_posts.txt", "a") as f:
                    f.write(submission.id + '\n')
                posts_list.append(submission.id)

    # Close the cursor and connection
    cur.close()
    con.close()
    print("Disconnected from database")
    sleep_time = 30
    print("Sleeping for {} seconds...".format(sleep_time))
    time.sleep(sleep_time)

terminate_time = 40
posts_list = get_saved_posts()
blacklist = get_blacklist()
r = bot_login()
while True:
    check_inbox_for_optout_requests(r)
    run_bot(r)
    terminate_time -= 1
    if terminate_time <= 0:
        exit()

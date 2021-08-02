# This script grabs new posts from a specified subreddit and writes it to a file (post_data.txt).
# The purpose is to get real post data to test the bot on.

import praw
import config
import time
import os
import unicodedata
import psycopg2

def bot_login():
    print('Logging in...')
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'respectthread responder v0.1')
    print('Logged in')
    with open("saved_posts.txt", "a") as f:
        f.write('\n')
    return r

def get_saved_posts():
    # Make sure the file exists.
    if not os.path.isfile("saved_posts.txt"):
        saved_posts = []
    else:
        # "r" is to read from saved_posts.txt as the variable f
        with open("saved_posts.txt", "r") as f:
            saved_posts = f.read()
            saved_posts = saved_posts.split("\n")
    return saved_posts

r = bot_login()
text = ""
new_posts_obtained = False
saved_posts = get_saved_posts()

submissions = r.subreddit('whowouldwin').new(limit=10)
for submission in submissions:
    if submission.id not in saved_posts:
        new_posts_obtained = True
        saved_posts.append(submission.id)
        with open("saved_posts.txt", "a") as f:
            f.write(submission.id + '\n')
        with open("post_data.txt", "a") as f:
            f.write("#" + submission.title + "\n" + submission.selftext + "\n\n***\n\n")

if new_posts_obtained:
    print("Obtained new post data in post_data.txt")
else:
    print("No new posts found")

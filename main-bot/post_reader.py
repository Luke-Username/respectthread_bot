# This module has a function to run the loop that checks new Reddit posts and analyzes them to generate a reply.

# Modules
import datetime                 # To help measure how old a submission is.
from typing import List         # To allow for List type method arguments.

# Custom modules
import file_io_manager          # For file input and output
import matchup_checker as mcr   # To analyze the post's body for character names.
import replier                  # To generate replies to posts.
import text_processing as tp    # To do the text processing needed for analyzing posts. 

subreddit_list = ["respectthread_bot", "whowouldwin"]

def read_posts(r, cur, posts_list: List[str], blacklist: List[str]):
    for sub in subreddit_list:
        print("Obtaining new posts from r/{}".format(sub))
        submissions = r.subreddit(sub).new(limit=7)
        for submission in submissions:
            print("\tChecking post {}".format(sub))
            now = datetime.datetime.now(datetime.timezone.utc).timestamp()
            age = now - submission.created_utc

            # Check the age of the post is less than 20 minutes old, the bot hasn't checked it already, and the poster hasn't opted out
            if age < 1200 and submission.id not in posts_list and submission.author.name not in blacklist:
                title = tp.strip_accents(submission.title)
                post = title + " " + tp.strip_accents(submission.selftext)
                character_list = mcr.search_characters(title, post, cur)
                if character_list:
                    reply_text = replier.generate_comment(cur, character_list, True)
                    replier.reply_to_submission(submission, reply_text)
            if submission.id not in posts_list:
                file_io_manager.write_to("saved_posts.txt", submission.id + "\n")
                posts_list.append(submission.id)

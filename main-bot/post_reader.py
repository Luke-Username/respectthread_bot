# This module has a function to run the loop that checks new Reddit posts and analyzes them to generate a reply.

# Modules
from typing import List         # To allow for List type method arguments.

# Custom modules
import matchup_checker as mcr   # To analyze the post's body for character names.
import replier                  # To generate replies to posts.
import text_processing as tp    # To do the text processing needed for analyzing posts. 

subreddit_list = ["respectthread_bot"]

def read_posts(r, cur, posts_list: List[str], blacklist: List[str]):
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
                    f.write(submission.id + "\n")
                posts_list.append(submission.id)

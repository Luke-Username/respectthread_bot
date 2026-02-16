# This module has a function to run the loop that checks Reddit comments for anyone who wants to summon the bot.

# Modules
import datetime                 # To help measure how old a submission is.
from typing import List         # To allow for List type method arguments.

# Custom Modules
import file_io_manager          # For file input and output
import matchup_checker as mcr   # To analyze the post's body for character names.
import replier                  # To generate replies to posts.
import text_processing as tp    # To do the text processing needed for analyzing posts. 

keyword = "!respect"
subreddit_list = ["respectthread_bot", "whowouldwin"]

def read_comments(r, cur, comments_list: List[str]):
    # loop through every comment on a certain subreddit. Limits to 20 comments.
    quantity = 20
    for sub in subreddit_list:
        print("Obtaining {} comments from r/{}...".format(quantity, sub))
        comments = r.subreddit(sub).comments(limit=quantity)
        for comment in comments:
            now = datetime.datetime.now(datetime.timezone.utc).timestamp()
            age = now - comment.created_utc
            lowercase_comment = comment.body.lower()

            # Check comment is less than 4 days old, the comment isn't by the bot itself, the bot hasn't checked it already, and the comment has the summon keyword
            if age < 345600 and comment.author != r.user.me() and comment not in comments_list and (keyword in lowercase_comment):
                keyworded_comment = tp.get_keyworded_lines_from_comment(comment.body, keyword)
                if keyworded_comment != "":
                    character_list = mcr.search_characters("", keyworded_comment, cur)
                    if character_list:
                        reply_text = replier.generate_comment(cur, character_list, True)
                        replier.reply_to_submission(comment, reply_text)
                    else:
                        reply_text = replier.generate_comment_no_results_apology(True)
                        replier.reply_to_submission(comment, reply_text)
                file_io_manager.write_to("saved_comments.txt", comment.id + "\n")
                comments_list.append(comment.id)
                        

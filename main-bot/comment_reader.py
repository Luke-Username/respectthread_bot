# This module has a function to run the loop that checks Reddit comments for anyone who wants to summon the bot.

# Modules
from typing import List         # To allow for List type method arguments.

keyword = "!respect"
subreddit_list = ["whowouldwin", "respectthread_bot"]

def read_comments(r, cur, comments_list: List[str]):
    # loop through every comment on a certain subreddit. Limits to 20 comments.
    quantity = 20
    print("Obtaining {} comments from r/{}...".format(quantity, sub))
    if comment.author != r.user.me() and comment not in comments_list and keyword in comment.body.lower():
        pass

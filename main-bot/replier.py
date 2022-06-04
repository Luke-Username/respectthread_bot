# This module contains functions to generate a reply and leave a comment on the Reddit post.

# Modules
import datetime                 # To help measure how old a submission is.
from typing import List         # To allow for List type method arguments.

# Custom modules
from character import Character # For using the Character class.

def generate_comment(cur, character_list: List[Character], with_footer: bool) -> str:
    # The text to return, containing what to write in the reply comment
    reply_text = ""

    # Sort respect threads by character name and version
    sorted_list = sorted(character_list, key = lambda character: (character.default_name, character.version))

    # Write a query that gets respect threads from the database in the order they are stored in the array.
    # Then add them to the reply text in that order.
    for character in sorted_list:
        if character.respectthreads:
            reply_text += "**" + character.name
            if character.version != "":
                reply_text += " ({})".format(character.version)
            reply_text += "**\n\n"
            rt_query = "SELECT c.* FROM respectthread c JOIN (VALUES "
            for i in range(len(character.respectthreads)):
                rt_query += "({}, {}),".format(character.respectthreads[i], i)
            rt_query = rt_query.rstrip(",")
            rt_query += ") AS x (id, ordering) ON c.id = x.id ORDER BY x.ordering;"
            cur.execute(rt_query)
            respectthreads = cur.fetchall()
            for row in respectthreads:
                title = row[1].replace('[', '\[').replace(']', '\]')
                link = row[2]
                reply_text += "- [{}]({})\n\n".format(title, link)

    # If the reply text is not empty, add a footer to the comment to tell readers about the bot
    if reply_text != "" and with_footer:
        reply_text += generate_footer()

    return reply_text

def generate_comment_no_results_apology(with_footer: bool) -> str:
    # The text to return, containing what to write in the reply comment
    reply_text = "Sorry, I couldn't find any respect threads in my database for the character(s) you are looking for. Note: You may have to specify the version. "
    reply_text += "Please visit r/respectthreads if you'd like to request one or [make one yourself.](https://www.reddit.com/r/respectthreads/wiki/introduction_guide)\n\n"
    if with_footer:
        reply_text += generate_footer()
    
    return reply_text

# These links should be up to date
about_url = "https://redd.it/owgxtl"
code_url = "https://github.com/Luke-Username/respectthread_bot"
opt_out_url = "https://www.reddit.com/message/compose?to=respectthread_bot&subject=OPTOUTREQUEST"
report_url = "https://www.reddit.com/message/compose?to=Luke_Username&subject=respectthread_bot+feedback"
def generate_footer() -> str:
    footer_text = "***\n\n"
    footer_text += "^(I am a bot) ^| "
    footer_text += "[^(About)]({}) ^| ".format(about_url)
    footer_text += "[^(Code)]({}) ^| ".format(code_url)
    footer_text += "[^(Opt-out)]({}) ^| ".format(opt_out_url)
    footer_text += "^(Missing or wrong characters? Reply explaining the issue)"
    return footer_text

def reply_to_submission(submission, reply_text):
    now = datetime.datetime.now(datetime.timezone.utc).timestamp()
    age = now - submission.created_utc

    # Reply if the submission is less than 4 days old, and the reply text is not empty
    if age < 345600 and reply_text != "":
        try:
            submission.reply(reply_text)
            print(reply_text)
        except:
            print('ERROR: Can not reply')
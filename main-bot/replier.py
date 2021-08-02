# This module contains functions to generate a reply and leave a comment on the Reddit post.

# Custom modules
from character import Character
from typing import List

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
                reply_text += "- [{}]({})\n\n".format(row[1], row[2])

    # If the reply text is not empty, add a footer to the comment to tell readers about the bot
    if reply_text != "" and with_footer:
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
    footer_text += "^(Missing or wrong characters?) [^(Report here)]({})".format(report_url)
    return footer_text

def reply_to_submission(r, submission, cur, character_list, with_footer: bool):
    reply_text = generate_comment(cur, character_list, with_footer)
    if reply_text != "":
        submission.reply(reply_text)
        print(reply_text)

# Modules
import psycopg2                     # Interface with PostgreSQL
import sys                          # For terminal arguments and to import from different folders
sys.path.insert(1, "../main-bot")   # This path is to import modules the bot uses. It is relative to the shell script that runs the tests.

# Custom modules
import config       # Login details
import matchup_checker as mcr
import replier
import text_processing as tp

# This function removes links from generated comments.
# The point is to test that the bot knows which characters to link,
# not if it will link a specific respect thread.
# Doing things this way means we will rarely have to update a test case if an RT is updated.
def remove_links_from_comment(comment: str) -> str:
    no_link_comment = ""
    for line in comment.split("\n"):
        if len(line) > 0 and line[0] == "-":
            no_link_comment += "-\n"
        else:
            no_link_comment += line + "\n"
    return no_link_comment

# Tell users how to run the code. 'python3' may need to be replaced with 'python',
# depending on the version of python they have installed
if len(sys.argv) < 2:
    print("Usage: python3 test_output_given_text.py <path to input file>")
    sys.exit()

# The first argument is the file name containing the post text to test on
filename = sys.argv[1]
f = open(filename, "r", encoding="utf-8")
title = f.readline()
post = title + " " + f.read()

#print("Connecting to database...")
con = psycopg2.connect(
    host = config.host,
    database = config.database,
    user = config.d_user,
    password = config.d_password
)
#print("Connected to database")
cur = con.cursor()

character_list = mcr.search_characters(title, post, cur, True)
if character_list:
    comment = replier.generate_comment(cur, character_list, False)
    print(remove_links_from_comment(comment).strip())

# Close the cursor and connection
cur.close()
con.close()
#print("Disconnected from database")


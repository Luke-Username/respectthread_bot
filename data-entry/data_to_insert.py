"""
# This script is used to enter new characters into the database when a respect thread is written of them.
# New respect threads are found at this link: https://www.reddit.com/r/respectthreads/new/
# An example of how to enter a new character is as follows.

id = get_rt_id(cur, 'Respect Sully (Monsters, Inc.)', 'https://redd.it/d2kwip')
add_data(['Sully'],
'Sully',
False,
False,
[
    ['Monsters,? Inc']
],
'Monsters, Inc.',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/d2kwip/respect_sully_monsters_inc/

# The following function call is an example of how to update the database when a respect thread is reposted.
# Refer to the CSV of respect threads to find the correct ID.
# Take the title and URL from the post itself.
update_respectthread(cur, 1189, 'Respect Beowulf (2007 Film)', 'https://redd.it/dspz5z')
"""

import psycopg2         # Interface with PostgreSQL
import re               # Regular expressions
import sys                          # For terminal arguments and to import from different folders
sys.path.insert(1, "../main-bot")   # This path is to import modules the bot uses. It is relative to the shell script that runs the tests.

import config           # Login details

name_lists = []
default_names = []
is_team_list = []
is_default_list = []
version_lists = []
displayed_version_names = []
rt_id_arrays = []
num_chars = []
default_chars = []

def get_rt_id(cur, title, link):
    query = "SELECT COUNT(*) FROM respectthread WHERE link = '{}';".format(link)
    cur.execute(query)
    rowCount = cur.fetchone()[0];
    if (rowCount >= 1):
        query = "SELECT id FROM respectthread WHERE link = '{}';".format(link)
        cur.execute(query)
        return cur.fetchone()[0];
    else:
        query = "INSERT INTO respectthread (title, link) VALUES ('{}', '{}');".format(title, link)
        cur.execute(query)
        cur.execute("SELECT id FROM respectthread WHERE link = '{}'".format(link))
        return cur.fetchone()[0];

def is_valid_regex(string: str) -> bool:
    try:
        re.compile(string)
        return True
    except re.error:
        print("WARNING: {} is not a valid regular expression!".format(string))
        return False

def add_data(name_list, default_name, is_team, is_default, version_list, displayed_version_name, rt_id_array):
    # Check if the names are valid regular expressions
    formatted_name_list = []
    for name in name_list:
        if not is_valid_regex(name):
            return
        else:
            # Turn the name into a string acceptable for PostgreSQL
            formatted_name_list.append(name.replace('\\', '\\\\'))

    formatted_version_list = []
    for version in version_list:
        version_array_string = '{'
        for regex in version:
            if not is_valid_regex(regex):
                return
            else:
                version_array_string += '"{}",'.format(regex.replace('\\', '\\\\'))
        
        version_array_string = version_array_string.strip(',') + '}'
        formatted_version_list.append(version_array_string)

    name_lists.append(formatted_name_list)
    default_names.append(default_name)
    is_team_list.append(is_team)
    is_default_list.append(is_default)
    version_lists.append(formatted_version_list)
    displayed_version_names.append(displayed_version_name)
    rt_id_arrays.append(rt_id_array)
    num_chars.append(True)

def update_respectthread(cur, id, title, link):
    cur.execute("UPDATE respectthread SET title='{}', link='{}' WHERE id={}".format(title, link, id))
    print("Successfully updated respectthread at id={}".format(id))

# Opening connection to database
con = psycopg2.connect(
    host = config.host,
    database = config.database,
    user = config.d_user,
    password = config.d_password
)
cur = con.cursor()

########################################

update_respectthread(cur, 20970, 'Respect Yor Forger, the Thorn Princess! (Spy x Family)', 'https://redd.it/znnlk2')

########################################

add_data(['Scaler'],
'Scaler',
False,
False,
[
    ['Scaler ?\(Scaler']
],
'',
'{9319}'
)
#https://www.reddit.com/r/whowouldwin/comments/znm605/which_countrys_military_is_the_strongest_based/

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['\(Marvel\)']
],
'Marvel',
'{1981}'
)
#https://www.reddit.com/r/whowouldwin/comments/znq1we/kratosgod_of_war_asuraasuras_wrath_vs_thor/j0ikeck/?context=3

########################################

add_data(['T\.?(-| )Rex'],
'Tyrannosaurus Rex',
False,
False,
[
    ['Grimlock']
],
'Grimlock',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/znvvtz/grimlock_transformers_vs_beast_titan_aot/j0jfok6/?context=3

########################################

id = get_rt_id(cur, 'Respect Michonne Hawthorne (The Walking Dead)', 'https://redd.it/zne559')
add_data(['Michonne Hawthorne'],
'Michonne Hawthorne',
False,
True,
[
    ['Wa(lk|kl)ing Dead']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zne559/respect_michonne_hawthorne_the_walking_dead/

########################################

id = get_rt_id(cur, 'Respect Lor-Zod (Young Justice)', 'https://redd.it/zni8oi')
add_data(['Lor(-| )Zod'],
'Lor-Zod',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Black Adam! (Young Justice)', 'https://redd.it/znjzh3')
add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/znjzh3/respect_black_adam_young_justice/

########################################

id = get_rt_id(cur, 'Respect Razorbeast (Transformers Beast Wars) [IDW, 2006]', 'https://redd.it/zno8qr')
add_data(['Razorbeast'],
'Razorbeast',
False,
True,
[
    ['Transformers'], ['IDW']
],
'Transformers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zno8qr/respect_razorbeast_transformers_beast_wars_idw/

########################################

id = get_rt_id(cur, 'Respect Thunderwing (Transformers) [IDW Hasbroverse]', 'https://redd.it/zns5t3')
add_data(['Thunderwing'],
'Thunderwing',
False,
False,
[
    ['IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zns5t3/respect_thunderwing_transformers_idw_hasbroverse/

########################################

id = get_rt_id(cur, 'Respect Bojack (Dragon Ball Z: Bojack Unbound)', 'https://redd.it/znu8u1')
add_data(['Bojack'],
'Bojack',
False,
False,
[
    ['Dragon ?Ball'], ['DB(Z|S)'], ['Broly'], ['Bojack Unbound'], ['Perfect cell'], ['Saiyan'], ['Tyrant']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/znu8u1/respect_bojack_dragon_ball_z_bojack_unbound/

########################################

id = get_rt_id(cur, 'Respect the Fallen (Transformers) [Dreamwave G1]', 'https://redd.it/znycw2')
add_data(['Fallen '],
'Fallen',
False,
False,
[
    ['Transformers', 'Dreamwave']
],
'Dreamwave',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/znycw2/respect_the_fallen_transformers_dreamwave_g1/

########################################

def insert_character_name(cur, name_list, default_name, is_team):
    rows_inserted = 0
    query = "INSERT INTO character_name (name, default_name, is_team) VALUES "
    for name in name_list:
        cur.execute("SELECT COUNT(*) FROM character_name WHERE name='{}' AND default_name='{}';".format(name, default_name))
        num_results = cur.fetchone()
        if num_results[0] == 0:
            query += "('{}', '{}', '{}'),".format(name, default_name, is_team)
            rows_inserted += 1

    if rows_inserted != 0:
        query = query.rstrip(",") + ";"
        cur.execute(query)
        print("Successfully inserted {} into TABLE character_name ({} rows)".format(default_name, rows_inserted))
                
def insert_character(cur, default_name, version_list, is_default, rt_id_array, displayed_version_name):
    rows_inserted = 0
    query = "INSERT INTO character (default_name, version, is_default, rt_id_array, displayed_version_name) VALUES "
    for version in version_list:
        cur.execute("SELECT COUNT(*) FROM character WHERE default_name='{}' AND version='{}';".format(default_name, version))
        num_results = cur.fetchone()
        if num_results[0] == 0:
            query += "('{}', '{}', {}, '{}', '{}'),".format(default_name, version, is_default, rt_id_array, displayed_version_name)
            rows_inserted += 1
    
    if rows_inserted != 0:
        query = query.rstrip(",") + ";"
        cur.execute(query)
        print("Successfully inserted {} into TABLE character ({} rows)".format(default_name, rows_inserted))

for i in range(len(num_chars)):
    insert_character_name(cur, name_lists[i], default_names[i], is_team_list[i])
    insert_character(cur, default_names[i], version_lists[i], is_default_list[i], rt_id_arrays[i], displayed_version_names[i])

    if is_default_list[i]:
        default_chars.append({ "name": default_names[i], "version": version_lists[i] })

con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

if len(default_chars) > 0:
    print()
    print('These characters are set to default. Please double check this is correct:')
    for character in default_chars:
        print(character["name"])
        print("\t" + str(character["version"]))

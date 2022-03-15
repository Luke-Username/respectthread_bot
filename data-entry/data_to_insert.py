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

add_data(['Apocalypse'],
'Apocalypse',
False,
False,
[
    ['Oscar Isaac']
],
'FOX',
'{8554}'
)
#https://www.reddit.com/r/whowouldwin/comments/tdotmp/josh_brolin_thanos_vs_oscar_isaac_apocalypse/

########################################

add_data(['Mei'],
'Mei',
False,
False,
[
    ['Turning Red']
],
'Turning Red',
'{21561}'
)
#https://www.reddit.com/r/respectthreads/comments/td9jcv/respect_the_red_panda_spirit_turning_red/

########################################

add_data(['Hal'],
'Hal',
False,
False,
[
    ['Green Lantern', '\(DC( Comics)?\)'],
    ['Green Lantern', '\[DC( Comics)?\]']
],
'DC',
'{7394, 1680}'
)
#https://www.reddit.com/r/whowouldwin/comments/tee76s/silver_surfer_vs_green_lantern/i0pflkj/?context=3

add_data(['Hal'],
'Hal',
False,
False,
[
    ['Green Lantern', 'PC'],
    ['Green Lantern', 'Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{1680}'
)
#https://www.reddit.com/r/whowouldwin/comments/tee76s/silver_surfer_vs_green_lantern/i0pflkj/?context=3

add_data(['Hal'],
'Hal',
False,
False,
[
    ['Green Lantern', 'New(-| )?52'],
    ['Green Lantern', 'Nu?-?52'],
    ['Green Lantern', 'Rebirth']
],
'New 52 / Rebirth',
'{7394}'
)
#https://www.reddit.com/r/whowouldwin/comments/tee76s/silver_surfer_vs_green_lantern/i0pflkj/?context=3

########################################

id = get_rt_id(cur, 'Respect Dementors (Harry Potter and the Methods of Rationality)', 'https://redd.it/tdq9p7')
add_data(['Dementors?'],
'Dementor',
False,
False,
[
    ['Methods of Rationality']
],
'Harry Potter and the Methods of Rationality',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdq9p7/respect_dementors_harry_potter_and_the_methods_of/

########################################

id = get_rt_id(cur, 'Respect Opa-Opa (Fantasy Zone)', 'https://redd.it/tdxhey')
add_data(['Opa-Opa'],
'Opa-Opa',
False,
False,
[
    ['Fantasy Zone']
],
'Fantasy Zone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdxhey/respect_opaopa_fantasy_zone/

########################################

id = get_rt_id(cur, 'Respect Hector Hammond (Green Lantern movie)', 'https://redd.it/te80xp')
add_data(['Hector Hammond'],
'Hector Hammond',
False,
False,
[
    ['Live(-| )Action Green Lantern|Green Lantern Live(-| )Action'], ['Green Lantern (Movie|Film)']
],
'Green Lantern, 2011',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/te80xp/respect_hector_hammond_green_lantern_movie/

########################################

id = get_rt_id(cur, 'Respect Saber, the Wandering King! (Fate/Strange Fake)', 'https://redd.it/teu9gm')
add_data(['Saber'],
'Saber',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/teu9gm/respect_saber_the_wandering_king_fatestrange_fake/

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

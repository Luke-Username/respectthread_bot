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

id = get_rt_id(cur, 'Respect Princess Audrey (Descendants)', 'https://redd.it/177qdb1')
add_data(['Princess Audrey'],
'Princess Audrey',
False,
True,
[
    ['Descendants']
],
'Descendants',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/CasualRespectThreads/comments/177qdb1/respect_princess_audrey_descendants/

########################################

id = get_rt_id(cur, 'Respect Cats (Bayonetta)', 'https://redd.it/177nfay')
add_data(['Cats'],
'Cats',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/177nfay/respect_cats_bayonetta/

########################################

id = get_rt_id(cur, 'Respect the Smile Room! (Trevor Henderson Mythos)', 'https://redd.it/177ycs9')
add_data(['Smile Room'],
'Smile Room',
False,
True,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/177ycs9/respect_the_smile_room_trevor_henderson_mythos/

########################################

id = get_rt_id(cur, 'Respect Long Horse! (Trevor Henderson Mythos)', 'https://redd.it/17842pr')
add_data(['Long Horse'],
'Long Horse',
False,
False,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17842pr/respect_long_horse_trevor_henderson_mythos/

########################################

id = get_rt_id(cur, 'Respect the Upside-Down Face Man! (Trevor Henderson Mythos)', 'https://redd.it/178lb3a')
add_data(['Upside(-| )?Down Face Man'],
'Upside-Down Face Man',
False,
True,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/178lb3a/respect_the_upsidedown_face_man_trevor_henderson/

add_data(['Man with the Upside(-| )?Down Face'],
'Upside-Down Face Man',
False,
True,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/178lb3a/respect_the_upsidedown_face_man_trevor_henderson/

add_data(['Upside(-| )?Down Man'],
'Upside-Down Man',
False,
False,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/178lb3a/respect_the_upsidedown_face_man_trevor_henderson/

########################################

id = get_rt_id(cur, 'Respect The Night Detective (Outcast Comics)', 'https://redd.it/177zhxe')
add_data(['Night Detective'],
'Night Detective',
False,
False,
[
    ['Outcast Comics']
],
'Outcast Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/177zhxe/respect_the_night_detective_outcast_comics/

########################################

id = get_rt_id(cur, 'Respect the Shrewster (Godzilla: The Series)', 'https://redd.it/178svha')
add_data(['Shrewster'],
'Shrewster',
False,
True,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/178svha/respect_the_shrewster_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect John Jameson! (Marvel Comics, 616)', 'https://redd.it/1795pw1')
add_data(['John( Jonah)? Jameson'],
'John Jonah Jameson',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1795pw1/respect_john_jameson_marvel_comics_616/

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

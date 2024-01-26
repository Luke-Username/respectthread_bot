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

########################################

add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Minus 1']
],
'Minus One',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/19dquk9/godzilla_minus_1_arrives_in_the_dceu_can_he_be/kj89fv9/?context=3

########################################

id = get_rt_id(cur, 'Respect Iron Kiba (Tough)', 'https://redd.it/19d669a')
add_data(['Iron Kiba'],
'Iron Kiba',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gordon Grancie (Tough)', 'https://redd.it/19fkp2c')
add_data(['Gordon Grancie'],
'Gordon Grancie',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Edgar C. Garcia (Tough)', 'https://redd.it/19eu2xr')
add_data(['Edgar C\.? Garcia'],
'Edgar C. Garcia',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19eu2xr/respect_edgar_c_garcia_tough/

########################################

id = get_rt_id(cur, 'Respect Galhad Suanpahkti (Tough)', 'https://redd.it/19dxete')
add_data(['Galhad Suanpahkti'],
'Galhad Suanpahkti',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19dxete/respect_galhad_suanpahkti_tough/

########################################

id = get_rt_id(cur, 'Respect The Astronomy Club (A Trip to the Moon)', 'https://redd.it/19d9t4j')
add_data(['Astronomy Club'],
'Astronomy Club',
True,
False,
[
    ['A Trip to the Moon']
],
'A Trip to the Moon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19d9t4j/respect_the_astronomy_club_a_trip_to_the_moon/

########################################

id = get_rt_id(cur, 'Respect Perceval the Welshman (Arthurian Mythology)', 'https://redd.it/19ffjkq')
add_data(['Perceval the Welshman'],
'Perceval the Welshman',
False,
True,
[
    ['Arthurian']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19ffjkq/respect_perceval_the_welshman_arthurian_mythology/

########################################

id = get_rt_id(cur, 'Respect Australium! (Team Fortress 2)', 'https://redd.it/19dxm6b')
add_data(['Australium'],
'Australium',
False,
True,
[
    ['TF2'], ['Team Fortress']
],
'TF2',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19dxm6b/respect_australium_team_fortress_2/

########################################

id = get_rt_id(cur, 'Respect Spacegodzilla (Pipeworks Godzilla Games)', 'https://redd.it/19dvsmd')
add_data(['Space ?godzilla'],
'Spacegodzilla',
False,
False,
[
    ['Pipeworks'], ['Games']
],
'Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19dvsmd/respect_spacegodzilla_pipeworks_godzilla_games/

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

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

update_respectthread(cur, 1155, 'Respect Moana Waialiki! (Moana)', 'https://redd.it/1cy740i')

########################################

add_data(['Elsa'],
'Elsa',
False,
False,
[
    ['Freeze'], ['Moana']
],
'Frozen',
'{1205}'
)
#https://www.reddit.com/r/whowouldwin/comments/1cx38xz/moana_vs_elsa_vs_repunzel_who_of_the_superpowered/l4zubg2/?context=3

add_data(['R(a|e)punzel'],
'Rapunzel',
False,
False,
[
    ['Elsa']
],
'Tangled',
'{1179}'
)
#https://www.reddit.com/r/whowouldwin/comments/1cx38xz/moana_vs_elsa_vs_repunzel_who_of_the_superpowered/l4zubg2/?context=3

########################################

id = get_rt_id(cur, 'CW Arsenal Respect Thread', 'https://comicvine.gamespot.com/forums/gen-discussion-1/cw-arsenal-respect-thread-1878512/')
add_data(['Arsenal'],
'Arsenal',
False,
False,
[
    ['Arsenal ?\(CW'], ['CW Arsenal'], ['CW', 'Team Arrow'], ['CW Hero team']
],
'CW Arrowverse',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect UMA Spring! (Undead Unluck)', 'https://redd.it/1cvbs70')
add_data(['UMA Spring'],
'UMA Spring',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cvbs70/respect_uma_spring_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect UMA Language! (Undead Unluck)', 'https://redd.it/1cvcdl4')
add_data(['UMA Language'],
'UMA Language',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mui! (Undead Unluck)', 'https://redd.it/1cvnmy7')
add_data(['Mui'],
'Mui',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cvnmy7/respect_mui_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect the Superior Master Rules (Undead Unluck)', 'https://redd.it/1cwfgro')
add_data(['Superior Master Rules'],
'Superior Master Rules',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cwfgro/respect_the_superior_master_rules_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Deadpool (Deadpool (2013))', 'https://redd.it/1cvwcku')
add_data(['Deadpool'],
'Deadpool',
False,
False,
[
    ['Deadpool ?\((Video )?Game\)'], ['Deadpool \(2013\)']
],
'2013',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect General Zaroff (The Most Dangerous Game)', 'https://redd.it/1cxctvo')
add_data(['General Zaroff'],
'General Zaroff',
False,
True,
[
    ['The Most Dangerous Game']
],
'The Most Dangerous Game',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cxctvo/respect_general_zaroff_the_most_dangerous_game/

########################################

id = get_rt_id(cur, 'Respect Mecha Sonic! (Sonic the Hedgehog)', 'https://redd.it/1cy9gx6')
add_data(['Mecha Sonic'],
'Mecha Sonic',
False,
True,
[
    ['Sonic the Hedgehog']
],
'Sonic the Hedgehog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cy9gx6/respect_mecha_sonic_sonic_the_hedgehog/

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

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

update_respectthread(cur, 2595, 'Respect Hit-Girl! (Kick-Ass)', 'https://redd.it/wuqvw9')
update_respectthread(cur, 13486, "Respect Black Noir (Amazon''s The Boys)", 'https://redd.it/wv3cvi')

########################################

add_data(['Lucifer'],
'Lucifer',
False,
False,
[
    ['Gwendol(i|y)ne? Christie']
],
'The Sandman, 2022',
'{}'
)
#

add_data(['Lucifer Morningstar'],
'Lucifer Morningstar',
False,
False,
[
    ['Gwendol(i|y)ne? Christie']
],
'The Sandman, 2022',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zuko (Avatar: The Last Airbender Pilot)', 'https://redd.it/wsqxfu')
add_data(['Zuko'],
'Zuko',
False,
False,
[
    ['Last Airbender Pilot']
],
'Avatar: The Last Airbender Pilot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wsqxfu/respect_zuko_avatar_the_last_airbender_pilot/

########################################

id = get_rt_id(cur, 'Respect Waluigi! (Brawl In The Family)', 'https://redd.it/ws2amm')
add_data(['Waluigi'],
'Waluigi',
False,
False,
[
    ['Brawl In The Family']
],
'Brawl In The Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ws2amm/respect_waluigi_brawl_in_the_family/

########################################

id = get_rt_id(cur, 'Respect Doctor Livesey (1988 Treasure Island)', 'https://redd.it/wsygzr')
add_data(['D(octo)?r\.? Livesey'],
'Dr. Livesey',
False,
False,
[
    ['Treasure Island', '1988']
],
'Treasure Island, 1988',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wsygzr/respect_doctor_livesey_1988_treasure_island/

########################################

id = get_rt_id(cur, 'Respect Black Adam (Justice League Action)', 'https://redd.it/wt8m2m')
add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['Justice League Action']
],
'Justice League Action',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wt8m2m/respect_black_adam_justice_league_action/

########################################

id = get_rt_id(cur, 'Respect Santa Claus (American Dad!)', 'https://redd.it/wtlkmx')
add_data(['Santa Claus'],
'Santa Claus',
False,
False,
[
    ['American Dad']
],
'American Dad!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wtlkmx/respect_santa_claus_american_dad/

########################################

id = get_rt_id(cur, 'Respect Mab, the Queen of Air and Darkness (The Dresden Files)', 'https://redd.it/wtnaek')
add_data(['Mab'],
'Mab',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wtnaek/respect_mab_the_queen_of_air_and_darkness_the/

########################################

id = get_rt_id(cur, 'Respect Thomas Raith (The Dresden Files)', 'https://redd.it/wugwsh')
add_data(['Thomas Raith'],
'Thomas Raith',
False,
True,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wugwsh/respect_thomas_raith_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Superman (DC Animated Movie Universe)', 'https://redd.it/wuen6p')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['DC Animated Film Universe'], ['DCA(F|M)U'], ['DC Animated Movies?']
],
'DC Animated Movie Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect General Zod (DC, Pre-Crisis)', 'https://redd.it/wu0d3f')
add_data(['Zod'],
'General Zod',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wu0d3f/respect_general_zod_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Subject One (DC Comics, Flashpoint Timeline)', 'https://redd.it/wuxigc')
add_data(['Subject One'],
'Subject One',
False,
False,
[
    ['DC'], ['Flash(-| )?point']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wuxigc/respect_subject_one_dc_comics_flashpoint_timeline/

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

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

update_respectthread(cur, 544, 'Respect RoboCop (RoboCop I-III)', 'https://redd.it/175i6hw')
update_respectthread(cur, 449, 'Respect Oddjob (James Bond - Goldfinger)', 'https://redd.it/175ojos')
update_respectthread(cur, 475, 'Respect Jaws (James Bond - The Spy Who Loved Me, Moonraker)', 'https://redd.it/175okxo')

########################################

id = get_rt_id(cur, "Respect Bucky O''Hare! (Bucky O''Hare [Continuity Comics])", 'https://redd.it/174wknb')
id2 = get_rt_id(cur, "Respect Bucky O''Hare! (Bucky O''Hare and the Toad Wars)", 'https://redd.it/174wkba')
id3 = get_rt_id(cur, "Respect Bucky O''Hare! (Bucky O''Hare Tie-In Games)", 'https://redd.it/174wkvw')
add_data(["Bucky O''Hare"],
"Bucky O''Hare",
False,
True,
[
    ['comics'], ['Toad Wars']
],
'',
'{' + '{}, {}, {}'.format(id, id2, id3) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/174wkvw/respect_bucky_ohare_bucky_ohare_tiein_games/

########################################

id = get_rt_id(cur, 'Respect Shades (Shadows for Silence in the Forests of Hell)', 'https://redd.it/174wz1h')
add_data(['Shades'],
'Shades',
False,
False,
[
    ['Shadows for Silence in the Forests of Hell']
],
'Shadows for Silence in the Forests of Hell',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Johnathan Crane, the Scarecrow (Arkhamverse)', 'https://redd.it/175e43u')
add_data(['Scare ?crow'],
'Scarecrow',
False,
False,
[
    ['Arkham(-| )?verse'], ['\(Arkham\)'], ['Arkham (ga(m|n)es?|series)'], ['Batman: Arkham']
],
'Batman: Arkham',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/175e43u/respect_johnathan_crane_the_scarecrow_arkhamverse/

########################################

id = get_rt_id(cur, '[NSFW] Respect Exentera! (Vitiators)', 'https://redd.it/175izxl')
add_data(['Exentera'],
'Exentera',
False,
True,
[
    ['Vitiators']
],
'Vitiators',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, '[NSFW] Respect Pontius Prell! (Vitiators)', 'https://redd.it/17698mm')
add_data(['Pontius Prell'],
'Pontius Prell',
False,
True,
[
    ['Vitiators']
],
'Vitiators',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17698mm/nsfw_respect_pontius_prell_vitiators/

########################################

id = get_rt_id(cur, 'Respect Darkheart and the Wyld Wolves (Wereworld)', 'https://redd.it/175p2o5')
add_data(['Darkheart'],
'Darkheart',
False,
False,
[
    ['Wereworld']
],
'Wereworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/175p2o5/respect_darkheart_and_the_wyld_wolves_wereworld/

add_data(['Wyld Wolves'],
'Wyld Wolves',
False,
True,
[
    ['Wereworld']
],
'Wereworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/175p2o5/respect_darkheart_and_the_wyld_wolves_wereworld/

########################################

id = get_rt_id(cur, 'Respect the Cryolophosaurus (M e d i c b a g)', 'https://redd.it/175x4wv')
add_data(['Cryolophosaurus'],
'Cryolophosaurus',
False,
False,
[
    ['M e d i c b a g']
],
'M e d i c b a g',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/175x4wv/respect_the_cryolophosaurus_m_e_d_i_c_b_a_g/

########################################

id = get_rt_id(cur, 'Respect the Nanuqsaurus (M e d i c b a g)', 'https://redd.it/175x4yl')
add_data(['Nanuqsaurus'],
'Nanuqsaurus',
False,
False,
[
    ['M e d i c b a g']
],
'M e d i c b a g',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/175x4yl/respect_the_nanuqsaurus_m_e_d_i_c_b_a_g/

########################################

id = get_rt_id(cur, 'Respect RPC-398, Spooky Scary Skeletons (RPC Authority))', 'https://redd.it/176alec')
add_data(['RCP ?(-| )? ?398'],
'RPC-398',
False,
True,
[
    ['Spooky Scary Skeletons']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/176alec/respect_rpc398_spooky_scary_skeletons_rpc/

########################################

id = get_rt_id(cur, 'Respect: Marvelous Man! (The Guardians of Justice)', 'https://redd.it/176h67m')
add_data(['Marvelous Man'],
'Marvelous Man',
False,
False,
[
    ['Guardians of Justice']
],
'The Guardians of Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/176h67m/respect_marvelous_man_the_guardians_of_justice/

########################################

id = get_rt_id(cur, 'Respect Jason Voorhees (Robot Chicken)', 'https://redd.it/176xgyz')
add_data(['Jason Voo?rhee?s'],
'Jason Voorhees',
False,
False,
[
    ['Robot Chicken']
],
'Robot Chicken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/176xgyz/respect_jason_voorhees_robot_chicken/

########################################

id = get_rt_id(cur, "Respect The Nazi Frankenstein''s Monster (Marvel, 616)", 'https://redd.it/177701a')
add_data(["Nazi Frankenstein''?s Monster"],
"Nazi Frankenstein''s Monster",
False,
True,
[
    ['Marvel|616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

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

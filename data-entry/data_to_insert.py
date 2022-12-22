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

update_respectthread(cur, 184, 'Respect Godzilla (Shin Godzilla)', 'https://redd.it/zs4px7')

########################################

id = get_rt_id(cur, 'Respect Klarienne the Witch-Girl (DC Comics, Earth-11)', 'https://redd.it/zqigag')
add_data(['Klarienne'],
'Klarienne',
False,
True,
[
    ['Earth(-| )11'], ['DC Comics']
],
'Earth-11',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Supergirl (DC Comics, Earth-11)', 'https://redd.it/zqiz4z')
add_data(['Supergirl'],
'Supergirl',
False,
False,
[
    ['Earth(-| )11']
],
'Earth-11',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zqiz4z/respect_supergirl_dc_comics_earth11/

########################################

id = get_rt_id(cur, 'Respect: The first Bizarro! (Pre-Crisis DC Comics)', 'https://redd.it/zrtvug')
add_data(['The First Bizarro'],
'The First Bizz?arr?o',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zrtvug/respect_the_first_bizarro_precrisis_dc_comics/

add_data(['Bizz?arr?o( |-)Superboy'],
'Bizarro Superboy',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zrtvug/respect_the_first_bizarro_precrisis_dc_comics/

########################################

id = get_rt_id(cur, 'Respect: Black Adam! (The Kid Super Power Hour with Shazam!)', 'https://redd.it/zqtvep')
add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['Kid Super Power Hour']
],
'The Kid Super Power Hour with Shazam!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zqtvep/respect_black_adam_the_kid_super_power_hour_with/

########################################

id = get_rt_id(cur, 'Respect Cyclops! (Marvel Anime)', 'https://redd.it/zs6u18')
add_data(['Cyclops'],
'Cyclops',
False,
False,
[
    ['Marvel Anime']
],
'Marvel Anime',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zs6u18/respect_cyclops_marvel_anime/

########################################

id = get_rt_id(cur, 'Respect Cell Max! (Dragon Ball Super: Super Hero)', 'https://redd.it/zr20s2')
add_data(['Cell Max'],
'Cell Max',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zr20s2/respect_cell_max_dragon_ball_super_super_hero/

########################################

id = get_rt_id(cur, "Respect Grimm! (American McGee''s Grimm)", 'https://redd.it/zscqab')
add_data(['Grimm'],
'Grimm',
False,
False,
[
    ['American McGees?']
],
'American McGee',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zscqab/respect_grimm_american_mcgees_grimm/

########################################

id = get_rt_id(cur, 'Respect the Krang (Rise of the Teenage Mutant Ninja Turtles)', 'https://redd.it/zsncaw')
add_data(['Krang'],
'Krang',
False,
False,
[
    ['Rise of the', 'Turtles'], ['Rise of the', 'TMNT'], ['ROT ?TMNT']
],
'Rise of the Teenage Mutant Ninja Turtles',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zsncaw/respect_the_krang_rise_of_the_teenage_mutant/

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

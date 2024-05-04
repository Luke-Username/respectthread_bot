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

add_data(['Dominic'],
'Dominic',
False,
False,
[
    ['Rangers', 'Jungle Fury']
],
'Power Rangers Jungle Fury',
'{24018}'
)
#

add_data(['Lily'],
'Lily',
False,
False,
[
    ['Rangers', 'Jungle Fury']
],
'Power Rangers Jungle Fury',
'{24099}'
)
#https://www.reddit.com/r/whowouldwin/comments/1akq80s/tai_lung_kung_fu_panda_takes_on_the_jungle_fury/l27qgi3/?context=3

########################################

id = get_rt_id(cur, 'Respect The Alaskan Bull Worm! (Spongebob Squarepants)', 'https://redd.it/1chbwp8')
add_data(['Alaskan Bull Worms?'],
'Alaskan Bull Worm',
False,
True,
[
    ['Spongebob']
],
'Spongebob',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chbwp8/respect_the_alaskan_bull_worm_spongebob/

########################################

id = get_rt_id(cur, "Respect Juiz d''Arc! (Undead Unluck)", 'https://redd.it/1chkoq6')
add_data(["Juiz d''Arc"],
"Juiz d''Arc",
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chkoq6/respect_juiz_darc_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Void Volks! (Undead Unluck)', 'https://redd.it/1cj6nqi')
add_data(['Void Volks'],
'Void Volks',
False,
True,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cj6nqi/respect_void_volks_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Red (NES Godzilla Creepypasta)', 'https://redd.it/1cja7y6')
add_data(['Red'],
'Red',
False,
False,
[
    ['NES Godzilla Creepypastak']
],
'NES Godzilla Creepypasta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cja7y6/respect_red_nes_godzilla_creepypasta/

########################################

id = get_rt_id(cur, 'Respect Phil Hawkins! (Undead Unluck)', 'https://redd.it/1cifxx2')
add_data(['Phil Hawkins'],
'Phil Hawkins',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cifxx2/respect_phil_hawkins_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Steel (CW, Earth-TUD22/TUD25)', 'https://redd.it/1chm03o')
add_data(['Steel'],
'Steel',
False,
False,
[
    ['TUD2(2|5)'], ['Steel ?\(Superman (&|and) Lois\)']
],
'Superman & Lois',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Molly Millions (Sprawl Trilogy)', 'https://redd.it/1chr7ud')
add_data(['Molly Millions'],
'Molly Millions',
False,
False,
[
    ['Sprawl']
],
'Sprawl Trilogy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chr7ud/respect_molly_millions_sprawl_trilogy/

########################################

id = get_rt_id(cur, 'Respect Rei Suwa (Buddy Daddies)', 'https://redd.it/1chs66t')
add_data(['Rei Suwa'],
'Rei Suwa',
False,
True,
[
    ['Buddy Daddies']
],
'Buddy Daddies',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chs66t/respect_rei_suwa_buddy_daddies/

########################################

id = get_rt_id(cur, "Respect Eve (Birdie Wing: Golf Girls'' Story)", 'https://redd.it/1chs6ca')
add_data(['Eve'],
'Eve',
False,
False,
[
    ['Birdie Wing']
],
'Birdie Wing',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chs6ca/respect_eve_birdie_wing_golf_girls_story/

########################################

id = get_rt_id(cur, 'Respect Vahram (Prince of Persia: The Lost Crown)', 'https://redd.it/1chs6f0')
add_data(['Vahram'],
'Vahram',
False,
False,
[
    ['Prince of Persia']
],
'Prince of Persia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chs6f0/respect_vahram_prince_of_persia_the_lost_crown/

########################################

id = get_rt_id(cur, "Respect Baragon (Toho''s Godzilla Franchise, Composite)", 'https://redd.it/1chvuga')
add_data(['Baragon'],
'Baragon',
False,
True,
[
    ['Godzilla']
],
'Godzilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1chvuga/respect_baragon_tohos_godzilla_franchise_composite/

########################################

id = get_rt_id(cur, 'Respect Zane Lofton (Slayers X: Terminal Aftermath: Vengance of the Slayer)', 'https://redd.it/1ciha85')
add_data(['Zane Lofton'],
'Zane Lofton',
False,
True,
[
    ['Slayers X|Terminal Aftermath|Vengance of the Slayer']
],
'Slayers X: Terminal Aftermath: Vengance of the Slayer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ciha85/respect_zane_lofton_slayers_x_terminal_aftermath/

########################################

id = get_rt_id(cur, 'Respect Hatsune Miku! (VOCALOID)', 'https://redd.it/1cio0n6')
add_data(['Hatsune Miku'],
'Hatsune Miku',
False,
True,
[
    ['VOCALOID']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cio0n6/respect_hatsune_miku_vocaloid/

########################################

id = get_rt_id(cur, 'Respect Iskat Akaris, the Thirteenth Sister (Star Wars Canon)', 'https://redd.it/1civxyk')
add_data(['Iskat Akaris'],
'Iskat Akaris',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1civxyk/respect_iskat_akaris_the_thirteenth_sister_star/

add_data(['Thirteenth Sister'],
'Thirteenth Sister',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1civxyk/respect_iskat_akaris_the_thirteenth_sister_star/

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

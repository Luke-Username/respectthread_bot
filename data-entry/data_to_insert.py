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

update_respectthread(cur, 14828, 'Respect Zarbon (Dragon Ball Manga)', 'https://redd.it/14svv0x')
update_respectthread(cur, 20476, 'Respect Jarrod/Dai Shi [Power Rangers Jungle Fury]', 'https://redd.it/14tfe2j')

########################################

add_data(['Sannin'],
'Sannin',
False,
False,
[
    ['Naruto'], ['(The|Three|3|Legendary) Sannin']
],
'Naruto',
'{3951, 3977, 3969}'
)
#https://www.reddit.com/r/whowouldwin/comments/14tr3i6/the_triumvirate_worm_vs_the_sannin_naruto/

########################################

add_data(['Rudeus'],
'Rudeus',
False,
False,
[
    ['Mushoku Tensei'], ['Jobless Reincarnation']
],
'Jobless Reincarnation',
'{5853}'
)
#https://www.reddit.com/r/whowouldwin/comments/14svo5g/rudeus_vs_gabimaru/jqzcuoc/?context=3

########################################

add_data(['Tensen'],
'Tensen',
True,
False,
[
    ["Hell''?s Paradise"]
],
"Hell''s Paradise: Jigokuraku",
'{21252}'
)
#https://www.reddit.com/r/whowouldwin/comments/14v45th/could_joseph_joestar_pretty_much_solo_every/jras93m/?context=3

########################################

id = get_rt_id(cur, 'Respect the Turbo Megazord (Power Rangers Turbo)', 'https://redd.it/14snlhc')
add_data(['Turbo Megazord'],
'Turbo Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14snlhc/respect_the_turbo_megazord_power_rangers_turbo/

########################################

id = get_rt_id(cur, 'Respect Mag Agent: Torture! (Madness Combat)', 'https://redd.it/14t8r01')
add_data(['Mag Agent:? Torture'],
'Mag Agent: Torture',
False,
True,
[
    ['Madness Combat']
],
'Madness Combat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14t8r01/respect_mag_agent_torture_madness_combat/

########################################

id = get_rt_id(cur, 'Respect Mystery Inc. (Brian Levant films)', 'https://redd.it/14t90f9')
add_data(['Mystery Inc(orporated)?'],
'Mystery Inc.',
False,
False,
[
    ['Brian Levant']
],
'Brian Levant',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14t90f9/respect_mystery_inc_brian_levant_films/

########################################

id = get_rt_id(cur, 'Respect Baku Madarame, The Lie Eater (Usogui)', 'https://redd.it/14tnmc5')
add_data(['Madarame Baku|Baku Madarame'],
'Madarame Baku',
False,
True,
[
    ['Usogui']
],
'Usogui',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14tnmc5/respect_baku_madarame_the_lie_eater_usogui/

########################################

id = get_rt_id(cur, 'Respect Dominic Hargan, the Jungle Fury Rhino Ranger! (Power Rangers Jungle Fury)', 'https://redd.it/14tosyy')
add_data(['Jungle Fury Rhino Ranger'],
'Jungle Fury Rhino Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14tosyy/respect_dominic_hargan_the_jungle_fury_rhino/

add_data(['Dominic Hargan'],
'Dominic Hargan',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14tosyy/respect_dominic_hargan_the_jungle_fury_rhino/

########################################

id = get_rt_id(cur, 'Respect Daphne and Velma (Daphne and Velma)', 'https://redd.it/14tq1xu')
add_data(['Daphne (&|and) Velma'],
'Daphne & Velma',
True,
False,
[
    ['2018'], ['Daphne (&|and) Velma ?\(Daphne (&|and) Velma']
],
'2018',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14tq1xu/respect_daphne_and_velma_daphne_and_velma/

########################################

id = get_rt_id(cur, 'Respect Baccarat, Dice, and Tanaka (One Piece)', 'https://redd.it/14tszps')
add_data(['Baccarat'],
'Baccarat',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14tszps/respect_baccarat_dice_and_tanaka_one_piece/

########################################

id = get_rt_id(cur, 'Respect Danielle "Danny" Tozer, AKA Dreadnought (Nemesis Series)', 'https://redd.it/14u8q08')
add_data(['Dreadnought'],
'Dreadnought',
False,
False,
[
    ['Nemesis Series']
],
'Nemesis Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14u8q08/respect_danielle_danny_tozer_aka_dreadnought/

########################################

id = get_rt_id(cur, 'Respect Aiolin and Morit Astarte (Star Wars Canon)', 'https://redd.it/14ukriw')
add_data(['Aiolin'],
'Aiolin',
False,
False,
[
    ['S(tar )?Wars'], ['Astarte']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ukriw/respect_aiolin_and_morit_astarte_star_wars_canon/

add_data(['Morit'],
'Morit',
False,
False,
[
    ['S(tar )?Wars'], ['Astarte']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ukriw/respect_aiolin_and_morit_astarte_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Sir Zephyr (Reincarnation of a Suicidal Battle God)', 'https://redd.it/14v90d6')
add_data(['Sir Zephyr'],
'Sir Zephyr',
False,
False,
[
    ['Reincarnation of a Suicidal Battle God']
],
'Reincarnation of a Suicidal Battle God',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14v90d6/respect_sir_zephyr_reincarnation_of_a_suicidal/

########################################

id = get_rt_id(cur, 'Respect Frau Totenkinder, The Black Forest Witch! (Fables)', 'https://redd.it/14vuw96')
add_data(['Frau Totenkinder'],
'Frau Totenkinder',
False,
True,
[
    ['Fables']
],
'Fables',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14vuw96/respect_frau_totenkinder_the_black_forest_witch/

########################################

id = get_rt_id(cur, 'Respect Chin (Hong Kong 97)', 'https://redd.it/14w9ure')
add_data(['Chin'],
'Chin',
False,
False,
[
    ['Hong Kong 97']
],
'Hong Kong 97',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14w9ure/respect_chin_hong_kong_97/

########################################

id = get_rt_id(cur, 'Respect Captain Sivana (DC, Earth S)', 'https://redd.it/14wwpch')
add_data(['Captain Sivana'],
'Captain Sivana',
False,
False,
[
    ['Earth S']
],
'Earth S',
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

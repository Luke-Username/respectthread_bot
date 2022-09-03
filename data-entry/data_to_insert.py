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

add_data(['Mob'],
'Mob',
False,
False,
[
    ['Mob.*Mob Psycho 100']
],
'Mob Psycho 100',
'{3906,3905}'
)
#https://www.reddit.com/r/whowouldwin/comments/x3vo8t/mob_from_mob_psycho_100_vs_saiki_kusuo_from_saikik/

########################################

add_data(['Predator'],
'Predator',
False,
False,
[
    ['Xenomorphs?']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/x4pk6r/thanos_vs_horror_characters/imwln9z/?context=3

add_data(['Predators'],
'Predators',
False,
False,
[
    ['Xenomorphs?']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/x4pk6r/thanos_vs_horror_characters/imwln9z/?context=3

########################################

add_data(['Luban'],
'Luban',
False,
False,
[
    ['Leprechaun']
],
'Leprechaun film series',
'{9214}'
)
#

########################################

id = get_rt_id(cur, "Respect Red (Genndy Tartakovsky''s Primal)", 'https://redd.it/x2tj7n')
add_data(['Red'],
'Red',
False,
False,
[
    ['Primal', 'Tartakovskys?']
],
'Primal',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2tj7n/respect_red_genndy_tartakovskys_primal/

########################################

id = get_rt_id(cur, 'Respect Crazy Jane (DC, Post-Crisis)', 'https://redd.it/x2vo6s')
add_data(['Crazy Jane'],
'Crazy Jane',
False,
True,
[
    ['Doom Patrol'], ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2vo6s/respect_crazy_jane_dc_postcrisis/

add_data(['Crazy Jane'],
'Crazy Jane',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2vo6s/respect_crazy_jane_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect the Lord God (Pearl of Great Price)', 'https://redd.it/x2w7cd')
add_data(['God'],
'God',
False,
False,
[
    ['Pearl of Great Price']
],
'Pearl of Great Price',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2w7cd/respect_the_lord_god_pearl_of_great_price/

########################################

id = get_rt_id(cur, 'Respect Captain Falcon (DEATH BATTLE!)', 'https://redd.it/x2wqc1')
add_data(['Ca?pt(ain)?\.? Falcon'],
'Captain Falcon',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2wqc1/respect_captain_falcon_death_battle/

########################################

id = get_rt_id(cur, 'Respect Spider-Man! (Spider-Man: The Animated Series 1994)', 'https://redd.it/s5f4c4')
add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Animated', '1994'], ['Spider(-| )?Man:? The Animated Series']
],
'Spider-Man: The Animated Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Davriel Cane (Magic: The Gathering)', 'https://redd.it/x3olht')
add_data(['Davriel Cane'],
'Davriel Cane',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x3olht/respect_davriel_cane_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Tlano, The Batman of Zur-En-Arrh (DC, Pre-Crisis)', 'https://redd.it/x41kbh')
add_data(['Tlano'],
'Tlano',
False,
False,
[
    ['Pre(-| )?Crisis'], ['Batman of Zur(-| )En(-| )Arrh']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x41kbh/respect_tlano_the_batman_of_zurenarrh_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Roron Corobb (Star Wars Legends)', 'https://redd.it/x4ay0q')
add_data(['Roron Corobb'],
'Roron Corobb',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
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

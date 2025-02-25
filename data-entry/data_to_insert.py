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

update_respectthread(cur, 24890, 'Respect Mysterio! (Marvel Comics)', 'https://redd.it/1ivwb95')
update_respectthread(cur, 6120, 'Respect King Arthur (Arthurian Legend)', 'https://redd.it/1iwti78')
update_respectthread(cur, 10829, 'Respect Wired Beck (Jojo’s Bizarre Adventure)', 'https://redd.it/1ix1bi6')

########################################

id = get_rt_id(cur, 'Respect The Shadow (Garth Ennis Version, Dynamite Entertainment 2012)', 'https://redd.it/1ivjxo6')
add_data(['Shadow'],
'Shadow',
False,
False,
[
    ['Garth Ennis']
],
'Garth Ennis',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect G-28 (Tough)', 'https://redd.it/1ivpekj')
add_data(['G-?28'],
'G-28',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ivpekj/respect_g28_tough/

########################################

id = get_rt_id(cur, 'Respect Ryusei Nagaoka (Tough)', 'https://redd.it/1iwfbtj')
add_data(['Ryuu?sei Nagaoka'],
'Ryusei Nagaoka',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwfbtj/respect_ryusei_nagaoka_tough/

add_data(['Ryuu?sei'],
'Ryusei',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwfbtj/respect_ryusei_nagaoka_tough/

########################################

id = get_rt_id(cur, 'Respect Coin Coffer (Super Mario)', 'https://redd.it/1iw4feb')
add_data(['Coin Coffer'],
'Coin Coffer',
False,
False,
[
    ['Mario']
],
'Mario',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Holy Roller (Image Comics, The Holy Roller)', 'https://redd.it/1iwa5ov')
add_data(['Holy Roller'],
'Holy Roller',
False,
False,
[
    ['Image']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwa5ov/respect_the_holy_roller_image_comics_the_holy/

########################################

id = get_rt_id(cur, 'Respect Nidoking (Pokemon Anime)', 'https://redd.it/1iwbjwi')
add_data(['Nidoking'],
'Nidoking',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwbjwi/respect_nidoking_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Nidoqueen (Pokemon Anime)', 'https://redd.it/1iwbjyf')
add_data(['Nidoqueen'],
'Nidoqueen',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwbjyf/respect_nidoqueen_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Gunbuster (Gunbuster: Aim for the Top!)', 'https://redd.it/1iwkox6')
add_data(['Gunbuster'],
'Gunbuster',
False,
True,
[
    ['Aim for the Top'], ['Top o Nerae']
],
'Gunbuster: Aim for the Top!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iwkox6/respect_the_gunbuster_gunbuster_aim_for_the_top/

########################################

id = get_rt_id(cur, 'Respect Jack Beans (A Calculated Man, Aftershock Comics)', 'https://redd.it/1ix0ryq')
add_data(['Jack Beans'],
'Jack Beans',
False,
False,
[
    ['Calculated Man']
],
'A Calculated Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ix0ryq/respect_jack_beans_a_calculated_man_aftershock/

########################################

id = get_rt_id(cur, 'Respect Sabine (Order of the Stick)', 'https://redd.it/1ix6zet')
add_data(['Sabine'],
'Sabine',
False,
False,
[
    ['Order of the Stick'], ['OOTS']
],
'Order of the Stick',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ix6zet/respect_sabine_order_of_the_stick/

########################################

id = get_rt_id(cur, 'Respect Hell (Hell and Back)', 'https://redd.it/1ixa4w3')
add_data(['Hell'],
'Hell',
False,
False,
[
    ['Hell ?\(Hell and Back']
],
'Hell and Back',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ixa4w3/respect_hell_hell_and_back/

########################################

id = get_rt_id(cur, 'Respect Sam Carpenter (Scream)', 'https://redd.it/1ixesrc')
add_data(['Sam Carpenter'],
'Sam Carpenter',
False,
False,
[
    ['Scream']
],
'Scream',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ixesrc/respect_sam_carpenter_scream/

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

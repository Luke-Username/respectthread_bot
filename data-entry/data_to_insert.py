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

update_respectthread(cur, 1253, "Respect Dracula! (Netflix''s Castlevania)", 'https://www.reddit.com/r/respectthreads/comments/1olaph5/respect_dracula_netflixs_castlevania/')
update_respectthread(cur, 1255, "Respect Sypha Belnades (Netflix''s Castlevania)", 'https://www.reddit.com/r/respectthreads/comments/1olcp80/respect_sypha_belnades_netflixs_castlevania/')
update_respectthread(cur, 16028, "Respect Trevor Belmont! (Netflix''s Castlevania)", 'https://www.reddit.com/r/respectthreads/comments/1oldkbv/respect_trevor_belmont_netflixs_castlevania/')
update_respectthread(cur, 2107, 'Respect the Beyonder (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1olwl16/respect_the_beyonder_marvel_comics_616/')


########################################

add_data(['Predator'],
'Predator',
False,
False,
[
    ['1987']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/1om4382/the_cast_of_shrek_2_has_48_hours_and_the_full/nmn1sdv/?context=3

########################################

id = get_rt_id(cur, 'Respect Android 13 (Dragon Ball Z: Super Android 13!)', 'https://www.reddit.com/r/respectthreads/comments/y6oe53/respect_android_13_dragon_ball_z_super_android_13/')
add_data(['Androids 13, 14,?(&|and)? 15'],
'Androids 13, 14, and 15',
True,
True,
[
    ['Dragon Ball']
],
'Dragon Ball',
'{' + '{}, 22719'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1omefuj/dragon_ball_z_movie_villain_battle_royale/nmoplku/?context=3
########################################

id = get_rt_id(cur, 'Respect Maximillian (Vampire in Brooklyn)', 'https://www.reddit.com/r/respectthreads/comments/1okw8km/respect_maximillian_vampire_in_brooklyn/')
add_data(['Maximillian'],
'Maximillian',
False,
False,
[
    ['Vampire in Brooklyn']
],
'Vampire in Brooklyn',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Growlie (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1ola2ib/respect_growlie_pokemon_anime/')
add_data(['Growlie'],
'Growlie',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#
########################################

id = get_rt_id(cur, 'Respect Krypto the Superdog (DCU)', 'https://www.reddit.com/r/respectthreads/comments/1ollxku/respect_krypto_the_superdog_dcu/')
add_data(['Krypto'],
'Krypto',
False,
False,
[
    ['DCU']
],
'DCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Superman (DCU)', 'https://www.reddit.com/r/respectthreads/comments/1ollxz3/respect_superman_dcu/')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['DCU']
],
'DCU',
'{' + '{}'.format(id) + '}'
)
#
########################################

id = get_rt_id(cur, 'Respect Deltandal (Ultraman Blazar)', 'https://www.reddit.com/r/respectthreads/comments/1olomp1/respect_deltandal_ultraman_blazar/')
add_data(['Deltandal'],
'Deltandal',
False,
False,
[
    ['Ultraman']
],
'Ultraman',
'{' + '{}'.format(id) + '}'
)
#
########################################

id = get_rt_id(cur, 'Respect Alexander Power/Zero-G (Marvel Comics, Earth-5631)', 'https://www.reddit.com/r/respectthreads/comments/1olp8c7/respect_alexander_powerzerog_marvel_comics/')
add_data(['Alexander Power'],
'Alexander Power',
False,
False,
[
    ['5631']
],
'5631',
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

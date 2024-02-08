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

update_respectthread(cur, 2615, 'Respect the League of Evil Exes! (Scott Pilgrim)', 'https://redd.it/1akf3dp')
update_respectthread(cur, 2616, 'Respect Ramona Flowers! (Scott Pilgrim)', 'https://redd.it/1ai2vaq')
update_respectthread(cur, 2614, 'Respect Knives Chau! (Scott Pilgrim Franchise, Composite)', 'https://redd.it/1aix71a')
update_respectthread(cur, 3687, 'Respect Mikazuchi Rei, "The Lightning God" (Kengan)', 'https://redd.it/1ajd79i')

########################################

add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['From The Series']
],
'Godzilla: The Series',
'{24472}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ah6od4/how_will_civilizations_act_against_a_massively/kolmlp3/?context=3

########################################

add_data(['Jim Gordon'],
'Jim Gordon',
False,
False,
[
    ['Jim Gordon,? Batman']
],
'Post-Flashpoint',
'{24032}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ajhn3e/spiderham_vs_jim_gordon_batman/kp10ogc/?context=3

########################################

id = get_rt_id(cur, 'Respect the Playable Characters! (Scott Pilgrim vs. The World: The Game)', 'https://redd.it/1ah6las')
add_data(['Playable Characters'],
'Playable Characters',
True,
False,
[
    ['Scott Pilgrim']
],
'Scott Pilgrim',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ah6las/respect_the_playable_characters_scott_pilgrim_vs/

########################################

id = get_rt_id(cur, 'Respect Koichi Yamano, Babel II [Babel II original manga]', 'https://redd.it/1ahzbt9')
add_data(['Koichi Yamano'],
'Koichi Yamano',
False,
False,
[
    ['Babel (II|2)']
],
'Babel II',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ahzbt9/respect_koichi_yamano_babel_ii_babel_ii_original/

########################################

id = get_rt_id(cur, 'Respect Vegeta, the Super Saiyan God (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/1aji9de')
add_data(['Vegeta'],
'Vegeta',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1aji9de/respect_vegeta_the_super_saiyan_god_hyourinjutsu/

########################################

id = get_rt_id(cur, 'Respect Marcio "Jet" Naito (Tough)', 'https://redd.it/1ajkfco')
add_data(['Marcio "Jet" Naito'],
'Marcio "Jet" Naito',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ajkfco/respect_marcio_jet_naito_tough/

########################################

id = get_rt_id(cur, 'Respect Albert (Marvel, 616)', 'https://redd.it/1ak1d2b')
add_data(['Albert'],
'Albert',
False,
False,
[
    ['Albert ?\(616\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ak1d2b/respect_albert_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Seal! (Undead Unluck)', 'https://redd.it/1al6trs')
add_data(['Seal'],
'Seal',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1al6trs/respect_seal_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect The Predators (Predator Eyes Of The Demon)', 'https://redd.it/1aljoy5')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Eyes Of The Demon']
],
'Predator: Eyes Of The Demon',
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

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

update_respectthread(cur, 6303, 'Respect Littlepip! (Fallout: Equestria)', 'https://redd.it/1fh8kfi')
update_respectthread(cur, 5500, 'Respect Frisk (Undertale)', 'https://redd.it/1fhbg7q')

########################################

id = get_rt_id(cur, 'Respect The Circle of Nine (Legacy of Kain)', 'https://redd.it/1fec74u')
add_data(['Circle of Nine'],
'Circle of Nine',
False,
False,
[
    ['Legacy of Kain']
],
'Legacy of Kain',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fec74u/respect_the_circle_of_nine_legacy_of_kain/

########################################

id = get_rt_id(cur, 'Respect Juzo Ogami (Kill Blue)', 'https://redd.it/1felbdy')
add_data(['Juzo Ogami'],
'Juzo Ogami',
False,
True,
[
    ['Kill Blue']
],
'Kill Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1felbdy/respect_juzo_ogami_kill_blue/

########################################

id = get_rt_id(cur, 'Respect Inutade (Dungeon Meshi)', 'https://redd.it/1feo6cj')
add_data(['Inutade'],
'Inutade',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1feo6cj/respect_inutade_dungeon_meshi/

add_data(['Tade'],
'Tade',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1feo6cj/respect_inutade_dungeon_meshi/

########################################

id = get_rt_id(cur, 'Respect Universa! (Image Comics)', 'https://redd.it/1ff0yfs')
add_data(['Universa'],
'Universa',
False,
False,
[
    ['Image Comics'], ['Invincible']
],
'Invincible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ff0yfs/respect_universa_image_comics/

########################################

id = get_rt_id(cur, 'Respect Screw-On Head (The Amazing Screw-On Head)', 'https://redd.it/1ff1h7z')
add_data(['Screw(-| )On Head'],
'Screw-On Head',
False,
False,
[
    ['Amazing(-| )Screw-On Head']
],
'The Amazing Screw-On Head',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Vicious 6 (Despicable Me)', 'https://redd.it/1ff7gl9')
add_data(['Vicious 6'],
'Vicious 6',
True,
False,
[
    ['Despicable Me'], ['Minions']
],
'Despicable Me',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Culex (Super Mario RPG)', 'https://redd.it/1ffyw84')
add_data(['Culex'],
'Culex',
False,
False,
[
    ['Mario']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ffyw84/respect_culex_super_mario_rpg/

########################################

id = get_rt_id(cur, 'Respect Kakugo Kusakabe (Tough)', 'https://redd.it/1fgn5xk')
add_data(['Kakugo Kusakabe'],
'Kakugo Kusakabe',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fgn5xk/respect_kakugo_kusakabe_tough/

########################################

id = get_rt_id(cur, 'Respect Phantom Joe (Tough)', 'https://redd.it/1fhevqd')
add_data(['Phantom Joe'],
'Phantom Joe',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fhevqd/respect_phantom_joe_tough/

########################################

id = get_rt_id(cur, 'Respect Anxiety (Inside Out)', 'https://redd.it/1fhecsj')
add_data(['Anxiety'],
'Anxiety',
False,
False,
[
    ['Inside Out']
],
'Inside Out',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fhecsj/respect_anxiety_inside_out/

########################################

id = get_rt_id(cur, 'Respect the Self-Slitted Maiden of a Thousand Souls (Dark Gathering)', 'https://redd.it/1fhdo3v')
add_data(['Self(-| )Slitted Maiden of a Thousand Souls'],
'Self-Slitted Maiden of a Thousand Souls',
False,
True,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fhdo3v/respect_the_selfslitted_maiden_of_a_thousand/

########################################

id = get_rt_id(cur, 'Respect The High Priest of the Evil Sutra (Dark Gathering)', 'https://redd.it/1fhd7fk')
add_data(['High Priest of the Evil Sutra'],
'High Priest of the Evil Sutra',
False,
True,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fhd7fk/respect_the_high_priest_of_the_evil_sutra_dark/

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

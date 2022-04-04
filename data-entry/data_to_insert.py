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

update_respectthread(cur, 5686, 'Respect the Boxers (Punch-Out!!)', 'https://redd.it/tv6icm')
update_respectthread(cur, 5645, 'Respect Sir Daniel Fortesque (MediEvil)', 'https://redd.it/tw29p5')

########################################

add_data(['Norman Osborne?'],
'Norman Osborn',
False,
False,
[
    ['616']
],
'616',
'{2264}'
)
#https://www.reddit.com/r/whowouldwin/comments/tvy6ju/norman_osborn_marvel_616_vs_lex_luthor_mainstream/i3c1a0x/?context=3

########################################

add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['Morbio?us ?\(Morbio?us']
],
'MCU',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/tw0m68/morbius_morbius_vs_blade_blade_movies/

########################################

add_data(['Elsa'],
'Elsa',
False,
False,
[
    ['Arr?endelle']
],
'Frozen',
'{1205}'
)
#https://www.reddit.com/r/whowouldwin/comments/tw1ocy/albus_percival_wulfric_brian_dumbledore_vs_elsa/

########################################

id = get_rt_id(cur, 'Respect Kirei Kotomine! (Fate)', 'https://redd.it/tv0178')
add_data(['Kirei Kotomine|Kotomine Kirei'],
'Kirei Kotomine',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tv0178/respect_kirei_kotomine_fate/

########################################

id = get_rt_id(cur, 'Respect Atom (Real Steel)', 'https://redd.it/tv6ib9')
add_data(['Atom'],
'Atom',
False,
False,
[
    ['Real Steel']
],
'Real Steel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tv6ib9/respect_atom_real_steel/

########################################

########################################

id = get_rt_id(cur, 'Respect Brogy and Dorry! (One Piece)', 'https://redd.it/tvoc2a')
add_data(['Brogy'],
'Brogy',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tvoc2a/respect_brogy_and_dorry_one_piece/

add_data(['Dorry'],
'Dorry',
False,
False,
[
    ['One ?Piece?'], ['Brogy']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tvoc2a/respect_brogy_and_dorry_one_piece/

########################################

id = get_rt_id(cur, 'Respect Mr. 5 and Miss Valentine! (One Piece)', 'https://redd.it/tvot9c')
add_data(['Mr\.? 5'],
'Mr. 5',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tvot9c/respect_mr_5_and_miss_valentine_one_piece/

add_data(['Miss Valentine'],
'Miss Valentine',
False,
False,
[
    ['One ?Piece?'], ['Mikita']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tvot9c/respect_mr_5_and_miss_valentine_one_piece/

########################################

id = get_rt_id(cur, 'Respect Galacta Knight! (Kirby)', 'https://redd.it/tw0po7')
add_data(['Galacta Knight'],
'Galacta Knight',
False,
True,
[
    ['Kirby']
],
'Kirby',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tw0po7/respect_galacta_knight_kirby/

########################################

id = get_rt_id(cur, "Respect Team Rocket''s Pelipper (Pokemon Anime)", 'https://redd.it/tw81w2')
add_data(['Pelipper'],
'Pelipper',
False,
False,
[
    ['Team Rockets?']
],
'Team Rocket',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tw81w2/respect_team_rockets_pelipper_pokemon_anime/

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

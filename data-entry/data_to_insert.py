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

update_respectthread(cur, 13479, 'Respect Ghostface (Scream 1996)', 'https://redd.it/1jfv4is')

########################################


add_data(['Homura'],
'Homura',
False,
False,
[
    ['Time Stop', 'Gojo']
],
'Madoka Magica',
'{4422}'
)
#https://www.reddit.com/r/whowouldwin/comments/1jhj63a/who_would_win_gojo_or_homura/mjcqt15/?context=3

########################################

id = get_rt_id(cur, 'Respect Kreia (Star Wars)', 'https://redd.it/1jibrjb')
add_data(['Kreia'],
'Kreia',
False,
False,
[
    ['S(tar )?Wars'], ['Yoda'], ['KOTOR'], ['Force Sensitive'], ['Darth'], ['Knights of the Old Republic'], ['Luke']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Darth Traya'],
'Darth Traya',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Darkrai (Pokemon Anime: The Rise of Darkrai)', 'https://redd.it/1jhysyf')
add_data(['Darkrai'],
'Darkrai',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jhysyf/respect_darkrai_pokemon_anime_the_rise_of_darkrai/

########################################

id = get_rt_id(cur, 'Respect Snow White (The Huntsman)', 'https://redd.it/1jh5ti6')
add_data(['Snow White'],
'Snow White',
False,
False,
[
    ['The Huntsman']
],
'The Huntsman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jh5ti6/respect_snow_white_the_huntsman/

########################################

id = get_rt_id(cur, 'Respect the Szlachta! (Vampire: the Masquerade)', 'https://redd.it/1jh5f9r')
add_data(['Szlachta'],
'Szlachta',
False,
False,
[
    ['Vampire:? The Masquerade']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jh5f9r/respect_the_szlachta_vampire_the_masquerade/

########################################

id = get_rt_id(cur, 'Respect the Skelesaurs (Extreme Dinosaurs)', 'https://redd.it/1jggjhj')
add_data(['Skelesaurs'],
'Skelesaurs',
True,
False,
[
    ['Extreme Dinosaurs']
],
'Extreme Dinosaurs',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jggjhj/respect_the_skelesaurs_extreme_dinosaurs/

########################################

id = get_rt_id(cur, 'Respect the Party (Super Mario RPG)', 'https://redd.it/1jgfvs4')
add_data(['Party'],
'Party',
True,
False,
[
    ['Mario RPG']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mario'],
'Mario',
False,
False,
[
    ['Mario.*Mario RPG']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mallow'],
'Mallow',
False,
False,
[
    ['Mario RPG']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)

add_data(['Geno'],
'Geno',
False,
False,
[
    ['Mario RPG']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)

add_data(['Bowser'],
'Bowser',
False,
False,
[
    ['Mario RPG']
],
'Super Mario RPG',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Dewey Riley (Scream)', 'https://redd.it/1jgvt5z')
add_data(['Dewey Riley'],
'Dewey Riley',
False,
True,
[
    ['Scream']
],
'Scream',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Dewey'],
'Dewey',
False,
False,
[
    ['Scream']
],
'Scream',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ghostface (Scream 6 Anime Promotional Trailer)', 'https://redd.it/1ji2cxp')
add_data(['Ghostface'],
'Ghostface',
False,
False,
[
    ['Scream 6 Anime Promotional Trailer']
],
'Scream 6 Anime Promotional Trailer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ghostface (Terrordrome)', 'https://redd.it/1ji1csc')
add_data(['Ghostface'],
'Ghostface',
False,
False,
[
    ['Terrordrome']
],
'Terrordrome',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ji1csc/respect_ghostface_terrordrome/

########################################

id = get_rt_id(cur, 'Respect Ghostface (Mortal Kombat)', 'https://redd.it/1jhi5u7')
add_data(['Ghostface'],
'Ghostface',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gale Weathers (Scream)', 'https://redd.it/1jhbdfk')
add_data(['Gale Weathers'],
'Gale Weathers',
False,
True,
[
    ['Scream']
],
'Scream',
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

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

update_respectthread(cur, 808, 'Respect Avatar Korra (The Legend of Korra)', 'https://redd.it/1afi5zj')
update_respectthread(cur, 2617, 'Respect Scott Pilgrim! (Scott Pilgrim)', 'https://redd.it/1ageeyi')

########################################

add_data(['King'],
'King',
False,
False,
[
    ['King from One Punch Man'], ['One Punch Man', 'scare|luck']
],
"One Punch Man",
'{4113}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ah0f5f/king_from_one_punch_man/
#https://www.reddit.com/r/whowouldwin/comments/1agfclc/who_is_the_strongest_character_that_king_from_one/

########################################

id = get_rt_id(cur, "Respect Flint Abrahams (Cabela''s Dangerous Hunts 2009)", 'https://redd.it/1af7pwd')
add_data(['Flint Abrahams'],
'Flint Abrahams',
False,
True,
[
    ['Cabela''?s Dangerous Hunts']
],
"Cabela''s Dangerous Hunts",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1af7pwd/respect_flint_abrahams_cabelas_dangerous_hunts/

########################################

id = get_rt_id(cur, 'Respect Peter Griffin (Fortnite)', 'https://redd.it/1affi1b')
add_data(['Peter Griffin'],
'Peter Griffin',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1affi1b/respect_peter_griffin_fortnite/

########################################

id = get_rt_id(cur, 'Respect Black Mariah (Marvel, 616)', 'https://redd.it/1afl751')
add_data(['Black Mariah'],
'Black Mariah',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1afl751/respect_black_mariah_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Oil Man (Mega Man)', 'https://redd.it/1afoq0l')
add_data(['Oil Man'],
'Oil Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1afoq0l/respect_oil_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Sanae Kikuta (Tough)', 'https://redd.it/1afpboz')
add_data(['Sanae Kikuta'],
'Sanae Kikuta',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1afpboz/respect_sanae_kikuta_tough/

########################################

id = get_rt_id(cur, 'Respect the Spiders! (Spider Earth)', 'https://redd.it/1afzdl9')
add_data(['Spiders'],
'Spiders',
False,
False,
[
    ['Spider Earth', 'Creepypasta']
],
'Spider Earth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1afzdl9/respect_the_spiders_spider_earth/

########################################

id = get_rt_id(cur, 'Respect the Robo-Mecha Wobbuffet (Pokemon Anime)', 'https://redd.it/1agbo5p')
add_data(['Robo-Mecha Wobbuffet'],
'Robo-Mecha Wobbuffet',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1agbo5p/respect_the_robomecha_wobbuffet_pokemon_anime/

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

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

update_respectthread(cur, 14781, 'Respect Bongo Bongo (The Legend of Zelda)', 'https://redd.it/162p72o')

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 47 Armor (Marvel, 616)', 'https://redd.it/1628b93')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 47']
],
'Model 47',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1628b93/respect_iron_man_model_47_armor_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 70 (Marvel 616)', 'https://redd.it/1628b93')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 70']
],
'Model 70',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Spot (Spider-Man: Across The Spider-Verse)', 'https://redd.it/162c3g4')
add_data(['Spot'],
'Spot',
False,
False,
[
    ['Spider(-| )?Verse'], ['The Spot', 'ATSV']
],
'Into the Spider-Verse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/162c3g4/respect_the_spot_spiderman_across_the_spiderverse/

########################################

add_data(['All For One'],
'All For One',
False,
False,
[
    ['vs\.? All For One'], ['All For One vs']
],
'My Hero Academia',
'{3916}'
)
#

########################################

id = get_rt_id(cur, "Respect the Sparrow Academy (Netflix''s Umbrella Academy)", 'https://redd.it/162xg8n')
add_data(['Sparrow Academy'],
'Sparrow Academy',
True,
True,
[
    ['Umbrella Academy']
],
'The Umbrella Academy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/162xg8n/respect_the_sparrow_academy_netflixs_umbrella/

########################################

id = get_rt_id(cur, "Respect the Guardians (Netflix''s Umbrella Academy)", 'https://redd.it/162ykxm')
add_data(['Guardians'],
'Guardians',
False,
False,
[
    ['Umbrella Academy']
],
'The Umbrella Academy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/162ykxm/respect_the_guardians_netflixs_umbrella_academy/

########################################

id = get_rt_id(cur, 'Respect Firestorm, the Nuclear Man! (DC Comics, Post-Flashpoint)', 'https://redd.it/162xgrc')
add_data(['Firestorm'],
'Firestorm',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/162xgrc/respect_firestorm_the_nuclear_man_dc_comics/

add_data(['Firestorm'],
'Firestorm',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'],
    ['vs\.? Firestorm'], ['Firestorm vs'], ['Ronnie'], ['Human Torch']
],
'DC',
'{' + '{}, 1647'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/162xgrc/respect_firestorm_the_nuclear_man_dc_comics/

########################################

id = get_rt_id(cur, 'Respect the Robo-Yeti (Godzilla: The Series)', 'https://redd.it/163qh6r')
add_data(['Robo(-| )Yeti'],
'Robo-Yeti',
False,
False,
[
    ['Godzilla']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/163qh6r/respect_the_roboyeti_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Momoshiki Otsutsuki (Boruto: Naruto Next Generations [Manga])', 'https://redd.it/1649zsw')
add_data(['Momoshiki'],
'Momoshiki',
False,
True,
[
    ['Naruto'], ['Boruto']
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1649zsw/respect_momoshiki_otsutsuki_boruto_naruto_next/

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

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

add_data(['Night ?crawler'],
'Nightcrawler',
False,
False,
[
    ['Louis Bloom']
],
'Louis Bloom',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/x8qum2/louis_bloom_nightcrawler_vs_patrick_bateman/injtx6f/?context=3

########################################

add_data(['Black Widow'],
'Black Widow',
False,
False,
[
    ['vs.*Black Widow', 'John Wick']
],
'616',
'{1989}'
)
#https://www.reddit.com/r/whowouldwin/comments/x941ql/yorspy_x_family_vs_dutch_john_wick_james_bond/

########################################

add_data(['Lara Croft'],
'Lara Croft',
False,
False,
[
    ['movie Lara']
],
'Lara Croft: Tomb Raider',
'{21699}'
)
#https://www.reddit.com/r/whowouldwin/comments/xaencv/lara_croft_tomb_raider_vs_hermione_granger_harry/intacxd/?context=3

########################################

id = get_rt_id(cur, 'Respect Lashawn Baez, Peek-a-Boo (DC, Post Crisis)', 'https://redd.it/x89azb')
add_data(['Lashawn Baez'],
'Lashawn Baez',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x89azb/respect_lashawn_baez_peekaboo_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect Megalo (Fossil Fighters)', 'https://redd.it/x8iqt6')
add_data(['Megalo'],
'Megalo',
False,
False,
[
    ['Fossil Fighters']
],
'Fossil Fighters',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Usagi Yojimbo (Teenage Mutant Ninja Turtles 1987)', 'https://redd.it/x9typt')
add_data(['Usagi Yojimbo'],
'Usagi Yojimbo',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '1987'], ['TMNT', '1987'], ['TMNT', '87'], ['original TMNT cartoon']
],
'TMNT 1987',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x9typt/respect_usagi_yojimbo_teenage_mutant_ninja/

########################################

id = get_rt_id(cur, 'Respect Super-Batman (Batman: The Brave and The Bold)', 'https://redd.it/x8pya5')
add_data(['Super(-| )Batman'],
'Super-Batman',
False,
False,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x8pya5/respect_superbatman_batman_the_brave_and_the_bold/

########################################

id = get_rt_id(cur, 'Respect ToyAgumon (Digimon Frontier)', 'https://redd.it/x8t72z')
add_data(['ToyAgumon'],
'ToyAgumon',
False,
False,
[
    ['Digimon Frontier']
],
'Digimon Frontier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x8t72z/respect_toyagumon_digimon_frontier/

########################################

id = get_rt_id(cur, 'Respect Robin Hood (Traditional Robin Hood Ballads)', 'https://redd.it/xacxxw')
add_data(['Robin Hood'],
'Robin Hood',
False,
True,
[
    ['Folk ?(lore|tale)'], ['Ballads?']
],
'',
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

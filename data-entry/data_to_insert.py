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

id = get_rt_id(cur, 'Respect Hassan of the Hundred Personas! (Fate)', 'https://redd.it/rtbb37')
add_data(['Hassan'],
'Hassan',
False,
False,
[
    ['Hundred', 'Faces?']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbb37/respect_hassan_of_the_hundred_personas_fate/

########################################

id = get_rt_id(cur, 'Respect Hassan of the Hundred Personas! (Fate)', 'https://redd.it/rtbb37')
add_data(['Lancelot'],
'Lancelot',
False,
False,
[
    ['\(Fate'], ['Berserker'], ['Serv(a|e)nts?'], ['Fate', 'Zero']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbfov/respect_sir_lancelot_the_knight_of_the_lake_fate/

########################################

id = get_rt_id(cur, 'Respect the Valkyrie, the Daughters of the Great God! (Fate)', 'https://redd.it/rtc0oa')
add_data(['Valkyries'],
'Valkyries',
False,
False,
[
    ['Valkyries \(Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtc0oa/respect_the_valkyrie_the_daughters_of_the_great/

########################################

id = get_rt_id(cur, 'Respect Adam Szalinski! (Honey, I Blew Up the Kid)', 'https://redd.it/rtbxnx')
add_data(['Adam'],
'Adam',
False,
False,
[
    ['Adam Szalinski'], ['Blew Up the Kid']
],
'Honey, I Blew Up the Kid',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbxnx/respect_adam_szalinski_honey_i_blew_up_the_kid/

add_data(['Baby'],
'Baby',
False,
False,
[
    ['Blew Up the Kid']
],
'Honey, I Blew Up the Kid',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbxnx/respect_adam_szalinski_honey_i_blew_up_the_kid/

add_data(['Toddler'],
'Toddler',
False,
False,
[
    ['Blew Up the Kid']
],
'Honey, I Blew Up the Kid',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbxnx/respect_adam_szalinski_honey_i_blew_up_the_kid/

########################################

id = get_rt_id(cur, 'Respect Breakdown, Roland Norcutt! (DC Post-Flashpoint)', 'https://redd.it/rtbz8e')
add_data(['Breakdown'],
'Breakdown',
False,
False,
[
    ['Norcutt'], ['Blew Up the Kid']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rtbz8e/respect_breakdown_roland_norcutt_dc_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect the Avengers (Marvel, Earth-14325)', 'https://redd.it/rth3ng')
add_data(['Avengers'],
'The Avengers',
True,
False,
[
    ['14325']
],
'14325',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rth3ng/respect_the_avengers_marvel_earth14325/

########################################

add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Battle Of New York']
],
'MCU',
'{261}'
)
#

add_data(['(Doctor|Dr\.?) Strange'],
'Doctor Strange',
False,
False,
[
    ['Battle Of New York']
],
'MCU',
'{13351}'
)
#https://www.reddit.com/r/whowouldwin/comments/rt4f5q/the_new_avengers_replaces_the_original_avengers/hqseb97/?context=3

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

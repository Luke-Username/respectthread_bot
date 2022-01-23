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

update_respectthread(cur, 3684, 'Respect Kure Raian, "The Taboo Descendant" (Kengan Asura/Omega)', 'https://redd.it/s9uaat')

########################################

id = get_rt_id(cur, 'Respect Kotomine Kirei (Fate/Zero and Fate/Stay Night)', 'https://redd.it/3ktbhf')
add_data(['Kotomine Kirei|Kirei Kotomine'],
'Kotomine Kirei',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/3ktbhf/respect_kotomine_kirei_fatezero_and_fatestay_night/
#https://www.reddit.com/r/whowouldwin/comments/sar4zb/deathstroke_new_52_slade_wilson_vs_kirei_kotomine/htv8ifg/?context=3

########################################

id = get_rt_id(cur, 'Respect Death Knights (Overlord, Light Novel)', 'https://redd.it/sa7dd0')
add_data(['Death Knights'],
'Death Knights',
False,
False,
[
    ['Overlord']
],
'Overlord',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sa7dd0/respect_death_knights_overlord_light_novel/

add_data(['Death Knight'],
'Death Knight',
False,
False,
[
    ['Overlord']
],
'Overlord',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sa7dd0/respect_death_knights_overlord_light_novel/

########################################

id = get_rt_id(cur, 'Respect the Avengers (Marvel Cinematic Universe / Rogers: The Musical)', 'https://redd.it/sa8cqi')
add_data(['Avengers'],
'The Avengers',
True,
False,
[
    ['Rogers:? The Musical']
],
'Rogers: The Musical',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sa8cqi/respect_the_avengers_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Spider-Man (Spider-Man 1969 fan film)', 'https://redd.it/sag5at')
add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Spider(-| )?Mans?.*1969'], ['Don(ald)?', 'Glut']
],
'1969',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sag5at/respect_spiderman_spiderman_1969_fan_film/

########################################

id = get_rt_id(cur, 'Respect Gigantamax Lapras (Terminalmontage)', 'https://redd.it/sataka')
add_data(['Lapras'],
'Lapras',
False,
False,
[
    ['Terminal ?Montage']
],
'Terminalmontage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sataka/respect_gigantamax_lapras_terminalmontage/

########################################

id = get_rt_id(cur, 'Respect This Random Formed One (Dreamwalker)', 'https://redd.it/satr8r')
add_data(['Formed One'],
'Formed One',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/satr8r/respect_this_random_formed_one_dreamwalker/

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

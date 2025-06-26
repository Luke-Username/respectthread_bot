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

update_respectthread(cur, 21249, "Respect Gabimaru the Hollow (Jigokuraku - Hell''s Paradise)", 'https://redd.it/1lj341i')
update_respectthread(cur, 13094, "Respect Chucky (Child''s Play)", 'https://redd.it/1ljdwyi')

########################################

add_data(['Koichi'],
'Koichi',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
'Jojo''s Bizarre Adventure',
'{3579}'
)
#

########################################

add_data(['Kris'],
'Kris',
False,
False,
[
    ['Deltarune']
],
'Deltarune',
'{5499}'
)
#

add_data(['Ralsei'],
'Ralsei',
False,
False,
[
    ['Deltarune']
],
'Deltarune',
'{5499}'
)
#

add_data(['Susie'],
'Susie',
False,
False,
[
    ['Deltarune']
],
'Deltarune',
'{5499}'
)
#

########################################

add_data(['Kurama'],
'Kurama',
False,
False,
[
    ['Yoko Kurama']
],
'Yu Yu Hakusho',
'{4641}'
)
#


########################################

id = get_rt_id(cur, 'Respect Starscream (The Transformers 1984)', 'https://redd.it/1lioask')
add_data(['Starscream'],
'Starscream',
False,
True,
[
    ['The Transformers'], ['198(4|0s?)']
],
'The Transformers, 1984',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lioask/respect_starscream_the_transformers_1984/

########################################

id = get_rt_id(cur, 'Respect Soundwave (The Transformers 1984)', 'https://redd.it/1lioatp')
add_data(['Soundwave'],
'Soundwave',
False,
False,
[
    ['The Transformers'], ['Transformers', '198(4|0s?)'], ['Soundwave ?\(Transformers\)']
],
'The Transformers, 1984',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lioatp/respect_soundwave_the_transformers_1984/

########################################

########################################

id = get_rt_id(cur, 'Respect Bumblebee (The Transformers 1984)', 'https://redd.it/1ljkxqp')
add_data(['Bumblebee'],
'Bumblebee',
False,
False,
[
    ['The Transformers'], ['Transformers', '198(4|0s?)'], ['Bumblebee ?\(Transformers\)']
],
'The Transformers, 1984',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ljkxqp/respect_bumblebee_the_transformers_1984/

########################################

id = get_rt_id(cur, 'Respect Unicron (The Transformers 1984)', 'https://redd.it/1ljkxs8')
add_data(['Unicron'],
'Unicron',
False,
True,
[
    ['The Transformers'], ['Transformers', '198(4|0s?)'], ['Unicron ?\(Transformers\)']
],
'The Transformers, 1984',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ljkxs8/respect_unicron_the_transformers_1984/

########################################

id = get_rt_id(cur, 'Respect Uranos the Undying (Marvel Comics Earth 616)', 'https://redd.it/1lj3lbq')
add_data(['Uranos'],
'Uranos',
False,
False,
[
    ['616'], ['Uranos the Undying'], ['The Eternals']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lj3lbq/respect_uranos_the_undying_marvel_comics_earth_616/

########################################

id = get_rt_id(cur, 'Respect William Afton, The Animatronic (Dead By Daylight)', 'https://redd.it/1lje92y')
add_data(['William Afton'],
'William Afton',
False,
False,
[
    ['Dead by Daylight']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lje92y/respect_william_afton_the_animatronic_dead_by/

########################################

id = get_rt_id(cur, 'Respect Jinu Saja (KPop Demon Hunters)', 'https://redd.it/1lkdn2n')
add_data(['Jinu Saja'],
'Jinu Saja',
False,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lkdn2n/respect_jinu_saja_kpop_demon_hunters/

add_data(['Jinu'],
'Jinu',
False,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lkdn2n/respect_jinu_saja_kpop_demon_hunters/

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

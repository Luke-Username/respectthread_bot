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

update_respectthread(cur, 12431, 'Respect Mumen Rider (One-Punch Man)', 'https://redd.it/1jseio8')
update_respectthread(cur, 196, 'Respect Mechagodzilla (Godzilla, Heisei)', 'https://redd.it/1jsejpm')
update_respectthread(cur, 21041, 'Respect General Thaddeus "Thunderbolt" Ross, The Hulk (What If General Ross Had Become the Hulk? Earth-523000)', 'https://redd.it/1jtbtfz')

########################################

add_data(['Billy Batson'],
'Billy Batson',
False,
True,
[
    ['Shazam', 'DC']
],
'DC',
'{1653,22688}'
)
#https://www.reddit.com/r/whowouldwin/comments/1jre5pw/green_lantern_guy_gardner_dc_vs_billy_batson/mldwi7i/?context=3

########################################

id = get_rt_id(cur, 'Respect Rena Mamiya/Uca Worm (Kamen Rider Kabuto)', 'https://redd.it/1jr2jpe')
add_data(['Rena Mamiya'],
'Rena Mamiya',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider Kabuto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jr2jpe/respect_rena_mamiyauca_worm_kamen_rider_kabuto/

add_data(['Uca Worm'],
'Uca Worm',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider Kabuto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jr2jpe/respect_rena_mamiyauca_worm_kamen_rider_kabuto/

########################################

id = get_rt_id(cur, 'Respect Imperator Furiosa (Mad Max)', 'https://redd.it/1jrd0ep')
add_data(['Imperator Furiosa'],
'Imperator Furiosa',
False,
True,
[
    ['Mad Max']
],
'Mad Max',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jrd0ep/respect_imperator_furiosa_mad_max/

########################################

id = get_rt_id(cur, 'Respect Freya of the Frost (The Huntsman)', 'https://redd.it/1js093i')
add_data(['Freya'],
'Freya ',
False,
False,
[
    ['The Huntsman']
],
'The Huntsman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1js093i/respect_freya_of_the_frost_the_huntsman/

########################################

id = get_rt_id(cur, 'Respect Queen Ravenna (The Huntsman)', 'https://redd.it/1js0iqx')
add_data(['Ravenna'],
'Ravenna ',
False,
False,
[
    ['The Huntsman']
],
'The Huntsman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1js0iqx/respect_queen_ravenna_the_huntsman/

########################################

id = get_rt_id(cur, "Respect Godzilla (Godzilla''s Monsterpiece Theatre)", 'https://redd.it/1jsx77v')
add_data(['Godzilla'],
'Godzilla ',
False,
False,
[
    ['Monsterpiece Theatre']
],
"Godzilla''s Monsterpiece Theatre",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Nue (Nue''s Exorcist)", 'https://redd.it/1jt7abp')
add_data(['Nue'],
'Nue',
False,
False,
[
    ["Nue''?s Exorcist"], ['Nue no Onmy(ō|0)ji']
],
"Nue''s Exorcist",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jt7abp/respect_nue_nues_exorcist/

########################################

id = get_rt_id(cur, "Respect Gakuro Yajima (Nue''s Exorcist)", 'https://redd.it/1jta0c4')
add_data(['Gakuro Yajima'],
'Gakuro Yajima',
False,
False,
[
    ["Nue"]
],
"Nue''s Exorcist",
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

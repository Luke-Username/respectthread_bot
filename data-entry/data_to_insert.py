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

update_respectthread(cur, 21232, 'Respect Light Yagami (Death Note)', 'https://redd.it/18321nl')
update_respectthread(cur, 1958, 'Respect Battle Beast (Image Comics)', 'https://redd.it/1847jk9')

########################################

add_data(['Edelgard'],
'Edelgard',
False,
False,
[
    ['Fire Emblem']
],
'Fire Emblem',
'{13333}'
)
#https://www.reddit.com/r/whowouldwin/comments/1854v59/stark_frieren_vs_edelgard_isekai_maou/kazcj23/?context=3

########################################

add_data(['Seiya'],
'Seiya',
False,
False,
[
    ['Seiya \(Saint Seiya\)']
],
'Saint Seiya',
'{4493,13142}'
)
#https://www.reddit.com/r/whowouldwin/comments/1820kwq/goku_dragon_ball_vs_seiya_saint_seya/

########################################

id = get_rt_id(cur, 'Respect Chase (Fighting Foodons)', 'https://redd.it/181n67l')
add_data(['Chase'],
'Chase',
False,
False,
[
    ['Fighting Foodons']
],
'Fighting Foodons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/181n67l/respect_chase_fighting_foodons/

########################################

id = get_rt_id(cur, 'Respect Jungle Cat (Generator Rex)', 'https://redd.it/182vi3z')
add_data(['Jungle Cat'],
'Jungle Cat',
False,
False,
[
    ['Generator Rex']
],
'Generator Rex',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/182vi3z/respect_jungle_cat_generator_rex/

########################################

id = get_rt_id(cur, 'Respect the Four Lords (Resident Evil Village)', 'https://redd.it/183byya')
add_data(['(Lady|Alcina) Dimitrescu'],
'Lady Dimitrescu',
False,
True,
[
    ['Resident Evil']
],
'Resident Evil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/183byya/respect_the_four_lords_resident_evil_village/

add_data(['Four Lords'],
'Four Lords',
True,
False,
[
    ['Resident Evil']
],
'Resident Evil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/183byya/respect_the_four_lords_resident_evil_village/

add_data(['(Lord|Karl) Heisenberg'],
'Lord Heisenberg',
False,
True,
[
    ['Resident Evil']
],
'Resident Evil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/183byya/respect_the_four_lords_resident_evil_village/

########################################

id = get_rt_id(cur, 'Respect Ronald McDonald (Deep Fried Fury)', 'https://redd.it/1842enn')
add_data(['Ronald McDonald'],
'Ronald McDonald',
False,
False,
[
    ['Deep Fried Fury']
],
'Deep Fried Fury',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1842enn/respect_ronald_mcdonald_deep_fried_fury/

########################################

id = get_rt_id(cur, "Respect \"Mad Jack\" Jack O'' Lantern (Marvel, 616)", 'https://redd.it/1849nm1')
add_data(['Mad Jack'],
'Mad Jack',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1849nm1/respect_mad_jack_jack_o_lantern_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Dinodroid No. 1 (Dragon Ball Super - Manga)', 'https://redd.it/184p97a')
add_data(['Dinodroid 1'],
'Dinodroid 1',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/184p97a/respect_dinodroid_no_1_dragon_ball_super_manga/

########################################

id = get_rt_id(cur, 'Respect the Doctor! (Doctor Who: Full Fathom Five)', 'https://redd.it/184tmmj')
add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['Full Fathom Five']
],
'Doctor Who: Full Fathom Five',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/184tmmj/respect_the_doctor_doctor_who_full_fathom_five/

########################################

id = get_rt_id(cur, 'Respect Gorgon, the Queen of Demonic Beasts (Fate Franchise)', 'https://redd.it/184vcpw')
add_data(['Gorgon'],
'Gorgon',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/184vcpw/respect_gorgon_the_queen_of_demonic_beasts_fate/

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

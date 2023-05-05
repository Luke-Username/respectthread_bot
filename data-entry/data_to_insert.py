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

update_respectthread(cur, 299, 'Respect Dr. Octopus (Raimi)', 'https://redd.it/135shck')
update_respectthread(cur, 21845, 'Respect Finn! (Star Wars (Canon))', 'https://redd.it/135yi28')
update_respectthread(cur, 4049, 'Respect Monkey D. Luffy, Captain of the Straw Hat Pirates! (One Piece)', 'https://redd.it/138i0cu')

########################################

add_data(['Domino'],
'Domino',
False,
False,
[
    ['Deadpool 2']
],
'FOX X-Men',
'{145}'
)
#https://www.reddit.com/r/whowouldwin/comments/136jf25/domino_from_deadpool_2_is_now_in_the_mcu_who_is/jiousie/?context=3

########################################

add_data(['Dante'],
'Dante',
False,
False,
[
    ['Dante Alighieri']
],
'Dante Alighieri',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/136w0bg/fights_between_some_famous_authors_dante/jiqg8sg/?context=3

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['The Batman', 'Reeves']
],
'The Batman, 2022',
'{22590}'
)
#https://www.reddit.com/r/whowouldwin/comments/138b9dt/john_wick_vs_the_batman_reeves/jixmxvs/?context=3

########################################

id = get_rt_id(cur, 'Respect PAL! (The Mitchells vs. the Machines)', 'https://redd.it/135m7c2')
add_data(['PAL'],
'PAL',
False,
False,
[
    ['Mitchell?s?', 'Machines?'], ['PAL Max']
],
'The Mitchells vs. the Machines',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/135m7c2/respect_pal_the_mitchells_vs_the_machines/

########################################

id = get_rt_id(cur, 'Respect Rita Repulsa (Power Rangers)', 'https://redd.it/136gfw0')
add_data(['Rita Repulsa'],
'Rita Repulsa',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136gfw0/respect_rita_repulsa_power_rangers/

########################################

id = get_rt_id(cur, 'Respect the Putty Patrol (Power Rangers)', 'https://redd.it/136gg0v')
add_data(['Putty Patrol(lers?)?'],
'Putty Patrol',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136gg0v/respect_the_putty_patrol_power_rangers/

########################################

add_data(['Kang the Conqueror'],
'Kang the Conqueror',
False,
True,
[
    ['comics? versions?']
],
'616',
'{2016}'
)
#https://www.reddit.com/r/whowouldwin/comments/1386azy/mcu_kang_the_conqueror_vs_high_evolutionary/jiwq4m9/?context=3

########################################

id = get_rt_id(cur, 'Respect Belief, Second Sphere Power (Bayonetta)', 'https://redd.it/136jx7e')
add_data(['Belief'],
'Belief',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136gg0v/respect_the_putty_patrol_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Beloved, Second Sphere Power (Bayonetta)', 'https://redd.it/136jyu6')
add_data(['Beloved'],
'Beloved',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136jyu6/respect_beloved_second_sphere_power_bayonetta/

########################################

id = get_rt_id(cur, 'Respect Valiance and Valor, First Sphere Cherubim (Bayonetta)', 'https://redd.it/136k5tx')
add_data(['Valiance'],
'Valiance',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136k5tx/respect_valiance_and_valor_first_sphere_cherubim/

add_data(['Valor'],
'Valor',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136k5tx/respect_valiance_and_valor_first_sphere_cherubim/

########################################

id = get_rt_id(cur, 'Respect Glamor, First Sphere Seraphim (Bayonetta)', 'https://redd.it/136kafb')
add_data(['Glamor'],
'Glamor',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136kafb/respect_glamor_first_sphere_seraphim_bayonetta/

########################################

id = get_rt_id(cur, 'Respect The Cardinal Virtues, Auditio (Bayonetta)', 'https://redd.it/136mwu6')
add_data(['Auditio'],
'Auditio',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136mwu6/respect_the_cardinal_virtues_auditio_bayonetta/

add_data(['Cardinal Virtues'],
'Cardinal Virtues',
True,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136mwu6/respect_the_cardinal_virtues_auditio_bayonetta/

########################################

id = get_rt_id(cur, 'Respect Jubileus, the Creator (Bayonetta)', 'https://redd.it/136sdqm')
add_data(['Jubileus'],
'Jubileus',
False,
True,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/136sdqm/respect_jubileus_the_creator_bayonetta/

########################################

id = get_rt_id(cur, 'Respect Jimmy Yee (Demon)', 'https://redd.it/137kwlv')
add_data(['Jimmy Yee'],
'Jimmy Yee',
False,
False,
[
    ['Demon']
],
'Demon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/137kwlv/respect_jimmy_yee_demon/

########################################

id = get_rt_id(cur, 'Respect Perry the Platypus (INUbis)', 'https://redd.it/137lw6b')
add_data(['Perry the Platypus'],
'Perry the Platypus',
False,
False,
[
    ['INUbis']
],
'INUbis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/137lw6b/respect_perry_the_platypus_inubis/


########################################

id = get_rt_id(cur, 'Respect Darth Vader! (Super Power Beat Down)', 'https://redd.it/137lwcs')
add_data(['Vader'],
'Darth Vader',
False,
False,
[
    ['Super Power Beat Down']
],
'Super Power Beat Down',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/137lwcs/respect_darth_vader_super_power_beat_down/

########################################

id = get_rt_id(cur, 'Respect Sherdog Holmes (Sherlock Bones)', 'https://redd.it/137qoou')
add_data(['Sherdog Holmes'],
'Sherdog Holmes',
False,
False,
[
    ['Sherlock Bones']
],
'Sherlock Bones',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/137qoou/respect_sherdog_holmes_sherlock_bones/

########################################

id = get_rt_id(cur, 'Respect Birthday Boy! (DC Comics: Earth One)', 'https://redd.it/1387jvn')
add_data(['Birthday Boy'],
'Birthday Boy',
False,
False,
[
    ['Earth One']
],
'Earth One',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1387jvn/respect_birthday_boy_dc_comics_earth_one/

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

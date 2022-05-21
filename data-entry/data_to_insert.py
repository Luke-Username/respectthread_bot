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

update_respectthread(cur, 1151, 'Respect Tai Lung! (Kung Fu Panda)', 'https://redd.it/uu0pi2')
update_respectthread(cur, 118, 'Respect Aquaman (DC Extended Universe)', 'https://redd.it/uudk8g')

########################################

add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Snyders?']
],
'DCEU',
'{130}'
)
#https://www.reddit.com/r/whowouldwin/comments/uu4nvz/can_strange_and_wanda_mom_defeat_snyders_jl/

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['\(MoM\)', 'Strange']
],
'MCU',
'{270}'
)
#https://www.reddit.com/r/whowouldwin/comments/uu4nvz/can_strange_and_wanda_mom_defeat_snyders_jl/

########################################

add_data(['(Doctor|Dr\.?) Manhattan'],
'Doctor Manhattan',
False,
False,
[
    ['Watchmen (movie|film)s?']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/utftx8/dormammu_mcu_vs_dr_manhattan_watchmen_movie/i99lrap/?context=3

########################################

id = get_rt_id(cur, 'Respect Ganondorf (Hyrule Warriors)', 'https://redd.it/ut4hlf')
add_data(['Ganon(dorf)?'],
'Ganondorf',
False,
False,
[
    ['Hyrule Warriors']
],
'Hyrule Warriors',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ut4hlf/respect_ganondorf_hyrule_warriors/

########################################

id = get_rt_id(cur, 'Respect Dr. Michael Morbius (Morbius)', 'https://redd.it/ut58oo')
add_data(['Morbius'],
'Morbius',
False,
False,
[
    ['Morbius ?\(Morbius\)'], ['ut58oo'], ['2022'], ['Sony'], ['Jared Letos?'], ['MCU'],
    ['Morbius.*(movie|film)s?'], ['(movie|film) Morbius']
],
'2022',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ut58oo/respect_dr_michael_morbius_morbius/

########################################

id = get_rt_id(cur, 'Respect Milo Morbius (Morbius)', 'https://redd.it/ut593e')
add_data(['Milo'],
'Milo',
False,
False,
[
    ['Morbius']
],
'Morbius',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ut593e/respect_milo_morbius_morbius/

########################################

id = get_rt_id(cur, 'Respect Kid Icarus (Captain N: The Game Master)', 'https://redd.it/utgmzu')
add_data(['Kid Icarus'],
'Kid Icarus',
False,
False,
[
    ['Captain N']
],
'Captain N: The Game Master',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/utgmzu/respect_kid_icarus_captain_n_the_game_master/

########################################

id = get_rt_id(cur, 'Respect Jonathan Chase (Manimal)', 'https://redd.it/utrbyo')
add_data(['Jonathan Chase'],
'Jonathan Chase',
False,
False,
[
    ['Manimal']
],
'Manimal',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/utrbyo/respect_jonathan_chase_manimal/

########################################

id = get_rt_id(cur, 'Respect Rend (Pokemon ReBurst)', 'https://redd.it/uuft0x')
add_data(['Rend'],
'Rend',
False,
False,
[
    ['Pok(e|é)m(o|a)n ReBurst']
],
'Pocket Monsters RéBURST',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uuft0x/respect_rend_pokemon_reburst/

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

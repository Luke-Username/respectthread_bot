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

add_data(['Daredevil'],
'Daredevil',
False,
False,
[
    ['MCU']
],
'MCU',
'{1289}'
)
#https://www.reddit.com/r/whowouldwin/comments/tmoxc4/a_series_of_unusual_mcu_matchups/

add_data(['Electro'],
'Electro',
False,
False,
[
    ['MCU']
],
'The Amazing Spider-Man',
'{110}'
)
#https://www.reddit.com/r/whowouldwin/comments/tmoxc4/a_series_of_unusual_mcu_matchups/

########################################

add_data(['Lucifer'],
'Lucifer',
False,
False,
[
    ['DC']
],
'DC',
'{1616}'
)
#https://www.reddit.com/r/whowouldwin/comments/tnwiyy/lucifer_dc_and_michael_demiurgos_dc_vs/

########################################

id = get_rt_id(cur, 'Respect the Class Cards! (Fate)', 'https://redd.it/tlmx87')
add_data(['Class Cards'],
'Class Cards',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tlmx87/respect_the_class_cards_fate/

add_data(['Class Card'],
'Class Card',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tlmx87/respect_the_class_cards_fate/

########################################

id = get_rt_id(cur, 'Respect Fei Long! (Udon Comics Street Fighter)', 'https://redd.it/tm32i4')
add_data(['Fei Long'],
'Fei Long',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tm32i4/respect_fei_long_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Karin Kanzuki! (Udon Comics Street Fighter)', 'https://redd.it/tnj4hc')
add_data(['Karin Kanzuki'],
'Karin Kanzuki',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tnj4hc/respect_karin_kanzuki_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Ken Masters! (Udon Comics Street Fighter)', 'https://redd.it/tomnch')
add_data(['Ken Masters'],
'Ken Masters',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tomnch/respect_ken_masters_udon_comics_street_fighter/

add_data(['Ken'],
'Ken',
False,
False,
[
    ['Street Fighter', 'UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tomnch/respect_ken_masters_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Rick Jones, The Hulk (Marvel, 616)', 'https://redd.it/tmi2jf')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Rick Jones']
],
'Rick Jones',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tmi2jf/respect_rick_jones_the_hulk_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Etherow (APOSIMZ)', 'https://redd.it/tmmlw7')
add_data(['Etherow'],
'Etherow',
False,
False,
[
    ['APOSIMZ']
],
'APOSIMZ',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tmmlw7/respect_etherow_aposimz/

########################################

id = get_rt_id(cur, 'Respect: Superman! (JLA: The Nail)', 'https://redd.it/tmz10h')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['JLA:? The Nail']
],
'JLA: The Nail',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tmz10h/respect_superman_jla_the_nail/

########################################

id = get_rt_id(cur, 'Respect Lucretia Popescu! (SCP Foundation)', 'https://redd.it/tn7pg0')
add_data(['Lucretia Popescu'],
'Lucretia Popescu',
False,
True,
[
    ['SCP']
],
'SCP',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tn7pg0/respect_lucretia_popescu_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Ouken! (Ranking of Kings)', 'https://redd.it/tnp4x7')
add_data(['Ouken'],
'Ouken',
False,
False,
[
    ['Ranking of Kings']
],
'Ranking of Kings',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tnp4x7/respect_ouken_ranking_of_kings/

########################################

id = get_rt_id(cur, 'Respect Jake Sully! (Avatar)', 'https://redd.it/tna5rk')
add_data(['Jake Sully'],
'Jake Sully',
False,
True,
[
    ['Avatar']
],
'Avatar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tna5rk/respect_jake_sully_avatar/

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

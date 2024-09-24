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

update_respectthread(cur, 20564, 'Respect El Macho! (Despicable Me)', 'https://redd.it/1fngt0u')
update_respectthread(cur, 5633, 'Respect Sackboy (LittleBigPlanet)', 'https://redd.it/1fnhsee')
update_respectthread(cur, 4463, 'Respect The Brawler, Sanosuke Sagara (Rurouni Kenshin) [Manga]', 'https://redd.it/1fo1goq')

########################################

add_data(['Balthazar Bratt'],
'Balthazar Bratt',
False,
True,
[
    ['Despicable Me']
],
'Despicable Me',
'{25275}'
)
#https://www.reddit.com/r/whowouldwin/comments/1fmtxyn/scott_pilgrim_vs_balthazar_bratt_despicable_me/lod2wqc/?context=3

########################################

id = get_rt_id(cur, 'Respect the Black Asura of the Eclipse (Dark Gathering)', 'https://redd.it/1fm15zw')
add_data(['Black Asura of the Eclipse'],
'Black Asura of the Eclipse',
False,
True,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fm15zw/respect_the_black_asura_of_the_eclipse_dark/

########################################

id = get_rt_id(cur, 'Respect Manji (Blade of the Immortal)', 'https://redd.it/1fm1cii')
add_data(['Manji'],
'Manji',
False,
False,
[
    ['Blade of the Immortal']
],
'Blade of the Immortal',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fm1cii/respect_manji_blade_of_the_immortal/

########################################

id = get_rt_id(cur, 'Respect Kanzan Hishida (Tough)', 'https://redd.it/1fm5wll')
add_data(['Kanzan Hishida'],
'Kanzan Hishida',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fm5wll/respect_kanzan_hishida_tough/

########################################

id = get_rt_id(cur, 'Respect The Predator Dark (AVP 2010)', 'https://redd.it/1fm9793')
add_data(['Dark'],
'Dark',
False,
False,
[
    ['Dark ?\(Aliens vs\.? Predator', '2010']
],
'Aliens vs. Predator, 2010',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fm9793/respect_the_predator_dark_avp_2010/

########################################

id = get_rt_id(cur, 'Respect Shimo, the Ancient Titan! (Godzilla x Kong: The New Empire) [MonsterVerse]', 'https://redd.it/1flxap4')
add_data(['Shimo'],
'Shimo',
False,
False,
[
    ['MonsterVerse'], ['Godzilla x Kong'], ['Skar King']
],
'MonsterVerse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1flxap4/respect_shimo_the_ancient_titan_godzilla_x_kong/

########################################

id = get_rt_id(cur, 'Respect Taikan Kimura (Tough)', 'https://redd.it/1fmyyar')
add_data(['Taikan Kimura'],
'Taikan Kimura',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fmyyar/respect_taikan_kimura_tough/

########################################

id = get_rt_id(cur, 'Respect Kaisergreymon (Digimon Frontier)', 'https://redd.it/1fnrpl7')
add_data(['Kaiser ?greymon'],
'KaiserGreymon',
False,
True,
[
    ['Digimon']
],
'Digimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fnrpl7/respect_kaisergreymon_digimon_frontier/

########################################

id = get_rt_id(cur, 'Respect Taira no Masakado (Dark Gathering)', 'https://redd.it/1fo8aq5')
add_data(['Taira no Masakado'],
'Taira no Masakado',
False,
False,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fo8aq5/respect_taira_no_masakado_dark_gathering/

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

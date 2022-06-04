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

add_data(['M(iste)?r\.? Bean'],
'Mr. Bean',
False,
True,
[
    ['(Mr\.? Bean \(Mr\.? Bean\)']
],
'',
'{21102}'
)
#https://www.reddit.com/r/whowouldwin/comments/v3op39/could_king_one_punch_man_outlast_mr_bean_mr_bean/

########################################

add_data(['Rengoku'],
'Rengoku',
False,
True,
[
    ['Demon ?Slayer'], ['Kimetsu no Yaiba'], ['KnY'], ['DS']
],
'Demon Slayer',
'{17375}'
)
#https://www.reddit.com/r/whowouldwin/comments/v4aprs/shota_aizawaeraserhead_my_hero_academia_vs/ib3df0l/?context=3

########################################

add_data(['Calvin (and|&) Hobbes'],
'Calvin and Hobbes',
True,
True,
[
    ['default']
],
'',
'{1479, 1480, 1481}'
)
#https://www.reddit.com/r/whowouldwin/comments/v4487t/spy_x_family_but_anya_is_replaced_by_calvin_and/

########################################

add_data(['Johnny'],
'Johnny',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{5284}'
)
#https://www.reddit.com/r/whowouldwin/comments/v43g8z/johnny_vs_johnny_guilty_gear_vs_mortal_kombat/

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Rune King']
],
'Rune King',
'{21155}'
)
#https://www.reddit.com/r/whowouldwin/comments/v4644a/thor_rune_king_vs_death_marvel_comics616/

########################################

id = get_rt_id(cur, 'Respect Mata Hari, the Witch of Secrets! (The War of Greedy Witches)', 'https://redd.it/v3q0dq')
add_data(['Mata Hari'],
'Mata Hari',
False,
False,
[
    ['War of Greedy Witches'], ['Majo Taisen']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3q0dq/respect_mata_hari_the_witch_of_secrets_the_war_of/

########################################

id = get_rt_id(cur, 'Respect Mary Read, the Witch of the Seas! (The War of Greedy Witches)', 'https://redd.it/v3q0f8')
add_data(['Mary Read'],
'Mary Read',
False,
False,
[
    ['War of Greedy Witches'], ['Majo Taisen']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3q0f8/respect_mary_read_the_witch_of_the_seas_the_war/

########################################

id = get_rt_id(cur, 'Respect Jiji! (Dandadan)', 'https://redd.it/v4b49n')
add_data(['Jiji'],
'Jiji',
False,
False,
[
    ['Dandadan']
],
'Dandadan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4b49n/respect_jiji_dandadan/

########################################

id = get_rt_id(cur, 'Respect Aira Shiratori! (Dandadan)', 'https://redd.it/v4be6h')
add_data(['Aira Shiratori'],
'Aira Shiratori',
False,
False,
[
    ['Dandadan']
],
'Dandadan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4be6h/respect_aira_shiratori_dandadan/

########################################

id = get_rt_id(cur, 'Respect Momo Ayase! (Dandadan)', 'https://redd.it/v4e46l')
add_data(['Momo Ayase'],
'Momo Ayase',
False,
True,
[
    ['Dandadan']
],
'Dandadan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4e46l/respect_momo_ayase_dandadan/

########################################

id = get_rt_id(cur, 'Respect Ken "Okarun" Takakura! (Dandadan)', 'https://redd.it/v4efhr')
add_data(['Okarun'],
'Okarun',
False,
True,
[
    ['Dandadan']
],
'Dandadan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4efhr/respect_ken_okarun_takakura_dandadan/

########################################

id = get_rt_id(cur, 'Respect Blue Marsalis! (Alien: Cold Forge / Into Charybdis)', 'https://redd.it/v4c0zo')
add_data(['Blue Marsalis'],
'Blue Marsalis',
False,
True,
[
    ['Alien']
],
'Alien',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4c0zo/respect_blue_marsalis_alien_cold_forge_into/

########################################

id = get_rt_id(cur, 'Respect Snatchers! (Alien: The Cold Forge)', 'https://redd.it/v4c7hh')
add_data(['Snatchers'],
'Snatchers',
False,
False,
[
    ['Cold Forge']
],
'Alien: The Cold Forge',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4c7hh/respect_snatchers_alien_the_cold_forge/

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

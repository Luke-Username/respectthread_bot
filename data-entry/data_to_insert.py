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

update_respectthread(cur, 4981, '[NSFW] Respect Masane Amaha! (Witchblade)', 'https://redd.it/rg94x0')
update_respectthread(cur, 2130, 'Respect Thaddeus E. “Thunderbolt” Ross, The Red Hulk (Marvel, 616)', 'https://redd.it/rg9hfn')
update_respectthread(cur, 20484, 'Respect Tang Sanzang (Xi Xing Ji)', 'https://redd.it/rg9ign')

########################################

id = get_rt_id(cur, 'Respect Anastasia Nikolaevna Romanova, the Grand Duchess! (Fate)', 'https://redd.it/rggqyv')
add_data(['Anastasia'],
'Anastasia',
False,
False,
[
    ['Fate'],
    ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Aśvatthāman! (Fate)', 'https://redd.it/rggypz')
add_data(['A(ś|s)vatth(ā|a)man'],
'Aśvatthāman',
False,
False,
[
    ['Fate'],
    ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rggypz/respect_a%C5%9Bvatth%C4%81man_fate/

add_data(['Ashwatthama'],
'Ashwatthama',
False,
False,
[
    ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rggypz/respect_a%C5%9Bvatth%C4%81man_fate/

########################################

id = get_rt_id(cur, 'Respect Carmine Esclados (RWBY)', 'https://redd.it/rg98xz')
add_data(['Carmine Esclados'],
'Carmine Esclados',
False,
True,
[
    ['RWBY']
],
'RWBY',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rg98xz/respect_carmine_esclados_rwby/

########################################

id = get_rt_id(cur, 'Respect the Chaos Emeralds (Sonic the Hedgehog)', 'https://redd.it/rgk2cn')
add_data(['Chaos Emeralds?'],
'Chaos Emeralds',
False,
True,
[
    ['Sonic']
],
'Sonic the Hedgehog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rgk2cn/respect_the_chaos_emeralds_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Blaze the Cat! (Sonic the Hedgehog)', 'https://redd.it/rh7wuz')
add_data(['Blaze the Cat'],
'Blaze the Cat',
False,
True,
[
    ['Sonic']
],
'Sonic the Hedgehog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rh7wuz/respect_blaze_the_cat_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Yamato (One Piece)', 'https://redd.it/rgzr4i')
add_data(['Yamato'],
'Yamato',
False,
False,
[
    ['Yamato ?\(One ?Piece?'],
    ['One Piece', 'Nami']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Leonard Burns (Fire Force Anime)', 'https://redd.it/rh95bl')
add_data(['Leonard Burns'],
'Leonard Burns',
False,
True,
[
    ['Fire ?Force']
],
'Fire Force',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rh95bl/respect_leonard_burns_fire_force_anime/

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
        default_chars.append(default_names[i])

con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

if len(default_chars) > 0:
    print()
    print('These characters are set to default. Please double check this is correct:')
    for character in default_chars:
        print(character)

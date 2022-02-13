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

add_data(['Hit'],
'Hit',
False,
False,
[
    ['Hit vs|vs\.? Hit', 'Naruto']
],
'Dragon Ball',
'{3295}'
)
#https://www.reddit.com/r/whowouldwin/comments/sr9l3d/hit_vs_naruto_sasuke_and_one_other_naruto/hwqipa0/?context=3

########################################

add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Paramount']
],
'2020 film',
'{8607}'
)
#https://www.reddit.com/r/whowouldwin/comments/sr022i/sonic_paramount_vs_mcu_avengers/hwqsui0/?context=3

########################################

add_data(['Jean'],
'Jean',
False,
False,
[
    ['Dark Phoenix']
],
'616',
'{2368}'
)
#https://www.reddit.com/r/whowouldwin/comments/srawjy/whowhat_is_the_most_powerful_lovevraftian_being/

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Thor ?\(Avengers Assemble'], ['Avengers Assemble Thor']
],
'Avengers Assemble',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/srift1/avengers_assemble_thor_vs_justice_league/hwrw1v3/?context=3

########################################

id = get_rt_id(cur, 'Shinji Matou (Fate)', 'https://redd.it/sr8k5b')
add_data(['Shinji Matou'],
'Shinji Matou',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sr8k5b/shinji_matou_fate/

########################################

id = get_rt_id(cur, 'Respect Sue, the Zombie Tyrannosaur (The Dresden Files)', 'https://redd.it/sra0ua')
add_data(['Sue'],
'Sue',
False,
False,
[
    ['Harry Dresden|Dresden Files']
],
'Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sra0ua/respect_sue_the_zombie_tyrannosaur_the_dresden/

########################################

id = get_rt_id(cur, 'Respect the Smiling Friends! (Smiling Friends)', 'https://redd.it/srjqv3')
add_data(['Smiling Friends'],
'Smiling Friends',
True,
True,
[
    ['Adult Swim']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/srjqv3/respect_the_smiling_friends_smiling_friends/

########################################

id = get_rt_id(cur, 'Respect The Dinosaur King Game', 'https://redd.it/srkkb2')
add_data(['Dinosaur King'],
'Dinosaur King',
False,
True,
[
    ['card']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/srkkb2/respect_the_dinosaur_king_game/

########################################

id = get_rt_id(cur, "Respect the D''Bari (FOX X-Men)", 'https://redd.it/srl14m')
add_data(["D''Bari"],
"D''Bari",
False,
False,
[
    ['FOX', 'X(-| )?Men'], ['Dark Phoenix']
],
'FOX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/srl14m/respect_the_dbari_fox_xmen/

add_data(['Vuk'],
'Vuk',
False,
False,
[
    ['FOX', 'X(-| )?Men'], ['Dark Phoenix']
],
'FOX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/srl14m/respect_the_dbari_fox_xmen/

########################################

id = get_rt_id(cur, 'Respect Hector Doyle (Baki)', 'https://redd.it/srlaq9')
add_data(['Hector Doyle'],
'Hector Doyle',
False,
False,
[
    ['Baki']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/srlaq9/respect_hector_doyle_baki/

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

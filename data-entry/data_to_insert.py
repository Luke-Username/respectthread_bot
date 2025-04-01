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

update_respectthread(cur, 14422, 'Respect the Ninth Sister (Star Wars Canon)', 'https://redd.it/1jmw7y2')

########################################

id = get_rt_id(cur, "Respect Brobding (Man''s Arrogance by 105697)", 'https://redd.it/1jjc00g')
add_data(['Brobding'],
'Brobding',
False,
False,
[
    ['Man''s Arrogance by 105697']
],
"Man''s Arrogance by 105697",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jjc00g/respect_brobding_mans_arrogance_by_105697/

########################################

id = get_rt_id(cur, 'Respect T-Bone (Extreme Dinosaurs)', 'https://redd.it/1jk9sjf')
add_data(['T(-| )Bone'],
'T-Bone',
False,
False,
[
    ['Extreme Dinosaurs']
],
'Extreme Dinosaurs',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ghostface (Ghostface vs Jeff the Killer)', 'https://redd.it/1jkcwlh')
add_data(['Ghostface'],
'Ghostface',
False,
False,
[
    ['Ghostface vs\.? Jeff the Killer']
],
'Ghostface vs Jeff the Killer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tigra (Spidey Super Stories, Earth-57780)', 'https://redd.it/1jktb6m')
add_data(['Tigra'],
'Tigra',
False,
False,
[
    ['Spidey Super Stories']
],
'Spidey Super Stories',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Tadpole Dinosaur (Spidey Super Stories, Earth-57780)', 'https://redd.it/1jl9bwk')
add_data(['Tadpole Dinosaur'],
'Tadpole Dinosaur',
False,
False,
[
    ['Spidey Super Stories']
],
'Spidey Super Stories',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Lizard (Spidey Super Stories, Earth-57780)', 'https://redd.it/1jleckm')
add_data(['Lizard'],
'Lizard',
False,
False,
[
    ['Spidey Super Stories']
],
'Spidey Super Stories',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Lizard (Spidey Super Stories, Earth-57780)', 'https://redd.it/1jleckm')
add_data(['Stegron'],
'Stegron',
False,
False,
[
    ['Spidey Super Stories']
],
'Spidey Super Stories',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ryu Hayabusa (Ninja Gaiden) [NES]', 'https://redd.it/1jlurr8')
id2 = get_rt_id(cur, 'Respect Ryu Hayabusa (Ninja Gaiden) [Modern]', 'https://redd.it/1jmqlrd')
add_data(['Ryu Hayabusa'],
'Ryu Hayabusa',
False,
True,
[
    ['Ninja Gaiden']
],
'Ninja Gaiden',
'{' + '{}, {}'.format(id, id2) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Prince Naveen (The Princess and the Frog)', 'https://redd.it/1jlvsmy')
add_data(['Prince Naveen'],
'Prince Naveen',
False,
True,
[
    ['Princess and the Frog']
],
'The Princess and the Frog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jlvsmy/respect_prince_naveen_the_princess_and_the_frog/

########################################

id = get_rt_id(cur, 'Respect Princess Tiana (The Princess and the Frog)', 'https://redd.it/1jlvt0h')
add_data(['Princess Tiana'],
'Princess Tiana',
False,
True,
[
    ['Princess and the Frog']
],
'The Princess and the Frog',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tiana'],
'Tiana',
False,
False,
[
    ['Prince(ss)?', 'Frog'], ['Mulan'], ['Disney']
],
'The Princess and the Frog',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Daigo Tachikawa (Kamen Rider Kabuto)', 'https://redd.it/1jmdqyb')
add_data(['Daigo Tachikawa'],
'Daigo Tachikawa',
False,
True,
[
    ['Kamen Rider']
],
'Kamen Rider Kabuto',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, '[NSFW] Respect Takeru Ibaraki, the Witchblade! (Top Cow Comics)', 'https://redd.it/1jn49zr')
add_data(['Takeru Ibaraki'],
'Takeru Ibaraki',
False,
True,
[
    ['Witchblade']
],
'Witchblade',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Oropo, the last Eliotrope! (Wakfu)', 'https://redd.it/1jnkohr')
add_data(['Oropo'],
'Oropo',
False,
False,
[
    ['Wakfu'], ['Eliotrope']
],
'Wakfu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jnkohr/respect_oropo_the_last_eliotrope_wakfu/

########################################

id = get_rt_id(cur, 'Respect Party People No.1 (No.1 Sentai Gozyuger)', 'https://redd.it/1jo5l18')
add_data(['Party People No\.? ?1'],
'Party People No.1',
False,
False,
[
    ['Sentai Gozyuger']
],
'No.1 Sentai Gozyuger',
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

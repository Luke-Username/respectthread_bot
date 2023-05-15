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

update_respectthread(cur, 4107, 'Respect Metal Bat! (One-Punch Man Manga)', 'https://redd.it/13gutej')
update_respectthread(cur, 4114, "Respect Speed-O''-Sound Sonic! (One-Punch Man Manga)", 'https://redd.it/13gv296')
update_respectthread(cur, 4102, 'Respect Fubuki! (One-Punch Man Manga)', 'https://redd.it/13gv9xr')
update_respectthread(cur, 12453, 'Respect Superalloy Darkshine! (One-Punch Man Manga)', 'https://redd.it/13gvfz8')
update_respectthread(cur, 4112, 'Respect Saitama! (One-Punch Man Manga)', 'https://redd.it/13gvk0i')

########################################

add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['MAX Comics?']
],
'Punisher MAX',
'{2226}'
)
#https://www.reddit.com/r/whowouldwin/comments/13gzjqt/punisher_marvel_vs_sawyer_family_the_texas/jk2ky35/?context=3

########################################

id = get_rt_id(cur, "Respect Xx_Fresh_xX Time Trio (Xx_Fresh_xX Time Trio [PD_ZF''s Take])", 'https://redd.it/13enrz4')
add_data(['Xx_Fresh_xX Time Trio'],
'Xx_Fresh_xX Time Trio',
True,
True,
[
    ["PD_ZF''s Take"]
],
"PD_ZF''s Take",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13enrz4/respect_xx_fresh_xx_time_trio_xx_fresh_xx_time/

########################################

id = get_rt_id(cur, 'Respect The Supreme Monstrosity (Dinosaurs Attack!)', 'https://redd.it/13er0km')
add_data(['Supreme Monstrosity'],
'Supreme Monstrosity',
False,
False,
[
    ['Dinosaurs Attack!']
],
'Dinosaurs Attack!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13er0km/respect_the_supreme_monstrosity_dinosaurs_attack/

########################################

id = get_rt_id(cur, "Respect Xx_Fresh_xX Time Trio (Xx_Fresh_xX Time Trio [PD_ZF''s Take])", 'https://redd.it/13enrz4')
add_data(['Gisa and Geralf'],
'Gisa and Geralf',
True,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13et11a/respect_gisa_and_geralf_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Aisha Campbell, the Yellow Ranger (Mighty Morphin'' Power Rangers)', 'https://redd.it/13eyt8i')
add_data(['Aisha'],
'Aisha',
False,
False,
[
    ['Aisha Campbell'], ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13eyt8i/respect_aisha_campbell_the_yellow_ranger_mighty/

########################################

id = get_rt_id(cur, 'Respect Rocky DeSantos (Power Rangers)', 'https://redd.it/13gf6p4')
add_data(['Rocky DeSantos'],
'Rocky DeSantos',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Katherine Hillard (Power Rangers)', 'https://redd.it/13gf9z7')
add_data(['Katherine'],
'Katherine',
False,
False,
[
    ['Katherine Hillard'], ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13gf9z7/respect_katherine_hillard_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Norman Osborn, the Red Goblin (Marvel, Earth-616)', 'https://redd.it/13gsjrz')
add_data(['Red Goblin'],
'Red Goblin',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13gsjrz/respect_norman_osborn_the_red_goblin_marvel/

########################################

id = get_rt_id(cur, 'Respect Grodd! (DCAU)', 'https://redd.it/13ho2gu')
add_data(['Grodd'],
'Gorilla Grodd',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ho2gu/respect_grodd_dcau/

########################################

id = get_rt_id(cur, 'Respect Ultra-Humanite (DCAU)', 'https://redd.it/13i7b6a')
add_data(['Ultra(-| )Humanite'],
'Ultra-Humanite',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13i7b6a/respect_ultrahumanite_dcau/

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

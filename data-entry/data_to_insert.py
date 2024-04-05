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

add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Super(-| )?man from Superman (&|and) Lois'], ['Superman ?\(Superman (&|and) Lois\)']
],
'Superman & Lois',
'{}'
)
#

########################################

add_data(['Snake Eyes'],
'Snake Eyes',
False,
False,
[
    ['G\.?I\.? Joe', 'Movies?']
],
'G.I. Joe Movies',
'{442}'
)
#https://www.reddit.com/r/whowouldwin/comments/1bvvosz/snake_eyes_vs_the_shredder_gi_joe_vs_tmnt/ky21hzi/?context=3

########################################

id = get_rt_id(cur, "Respect Aura the Guillotine (Frieren: Beyond Journey''s End)", 'https://redd.it/1bufyy9')
add_data(['Aura'],
'Aura',
False,
False,
[
    ['Aura ?\(Frieren\)'], ['Aura the Guillotine']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bufyy9/respect_aura_the_guillotine_frieren_beyond/

########################################

id = get_rt_id(cur, 'Respect BJ Blazkowicz (Wolfenstein) (id Software)', 'https://redd.it/1btzs97')
id2 = get_rt_id(cur, 'Respect BJ Blazkowicz (Wolfenstein) (Activision)', 'https://redd.it/1burg1m')
id3 = get_rt_id(cur, 'Respect BJ Blazkowicz (Wolfenstein RPG)', 'https://redd.it/1burgn5')
id4 = get_rt_id(cur, 'Respect BJ Blazkowicz (Wolfenstein) (MachineGames)', 'https://redd.it/1bvlgps')
id5 = get_rt_id(cur, 'Respect BJ Blazkowicz (Quake Champions)', 'https://redd.it/1btzstm')
add_data(['B\.?J\.? Blazkowicz'],
'B.J. Blazkowicz',
False,
True,
[
    ['Wolfenstein']
],
'Wolfenstein',
'{' + '{}, {}, {}, {}, {}'.format(id, id2, id3, id4, id5) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1btzs97/respect_bj_blazkowicz_wolfenstein_id_software/
#https://www.reddit.com/r/respectthreads/comments/1burg1m/respect_bj_blazkowicz_wolfenstein_activision/
#https://www.reddit.com/r/respectthreads/comments/1burgn5/respect_bj_blazkowicz_wolfenstein_rpg/
#https://www.reddit.com/r/respectthreads/comments/1bvlgps/respect_bj_blazkowicz_wolfenstein_machinegames/

########################################

id = get_rt_id(cur, 'Respect Raya (Raya and the Last Dragon)', 'https://redd.it/1burvpx')
add_data(['Raya'],
'Raya',
False,
False,
[
    ['Raya (and|&) the Last Dragon']
],
'Raya and the Last Dragon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1burvpx/respect_raya_raya_and_the_last_dragon/

########################################

id = get_rt_id(cur, 'Respect X-50, "Aaron Stack" (Marvel, 616)', 'https://redd.it/1bv0x96')
add_data(['X-50'],
'X-50',
False,
False,
[
    ['Aaron Stack', '616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bv0x96/respect_x50_aaron_stack_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Troglor (Smiling Friends)', 'https://redd.it/1bv0yiw')
add_data(['Troglor'],
'Troglor',
False,
False,
[
    ['Smiling Friends']
],
'Smiling Friends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bv0yiw/respect_troglor_smiling_friends/

########################################

id = get_rt_id(cur, 'Respect James (Smiling Friends)', 'https://redd.it/1bv12jy')
add_data(['James'],
'James',
False,
False,
[
    ['Smiling Friends']
],
'Smiling Friends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bv12jy/respect_james_smiling_friends/

########################################

id = get_rt_id(cur, 'Respect Anti-Pops (Regular Show)', 'https://redd.it/1bwiqf4')
add_data(['Anti(-| )Pops'],
'Anti-Pops',
False,
True,
[
    ['Regular Show']
],
'Regular Show',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwiqf4/respect_antipops_regular_show/

########################################

id = get_rt_id(cur, 'Respect Angstrom Levy (Image Comics)', 'https://redd.it/1bwiqgf')
add_data(['Angstrom Levy'],
'Angstrom Levy',
False,
True,
[
    ['Image Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwiqgf/respect_angstrom_levy_image_comics/

########################################

id = get_rt_id(cur, 'Respect Psycrow (Earthworm Jim)', 'https://redd.it/1bwiqha')
add_data(['Psy-?Crow'],
'Psy-Crow',
False,
True,
[
    ['Earthworm Jim']
],
'Earthworm Jim',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwiqha/respect_psycrow_earthworm_jim/

########################################

id = get_rt_id(cur, 'Respect Mizu (Blue Eye Samurai)', 'https://redd.it/1bwmc90')
add_data(['Mizu'],
'Mizu',
False,
False,
[
    ['Blue Eye Samurai']
],
'Blue Eye Samurai',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwmc90/respect_mizu_blue_eye_samurai/

########################################

id = get_rt_id(cur, 'Respect Soldier-169 (FIGHTERS)', 'https://redd.it/1bwp008')
add_data(['Soldier-169'],
'Soldier-169',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwp008/respect_soldier169_fighters/

########################################

id = get_rt_id(cur, 'Respect Namaari (Raya and the Last Dragon)', 'https://redd.it/1bwppnv')
add_data(['Namaari'],
'Namaari',
False,
True,
[
    ['Raya']
],
'Raya and the Last Dragon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bwppnv/respect_namaari_raya_and_the_last_dragon/

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

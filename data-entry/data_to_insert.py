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

update_respectthread(cur, 23075, 'Respect David Martinez! (Cyberpunk: Edgerunners)', 'https://www.reddit.com/r/respectthreads/comments/zmfhi2/respect_david_martinez_cyberpunk_edgerunners/')
update_respectthread(cur, 22687, 'Respect Adam Smasher (Cyberpunk)', 'https://www.reddit.com/r/respectthreads/comments/y0wryy/respect_adam_smasher_cyberpunk/')
update_respectthread(cur, 21047, 'Respect Marisa Kirisame (Touhou)', 'https://www.reddit.com/r/respectthreads/comments/r5qi72/respect_marisa_kirisame_touhou/')
update_respectthread(cur, 23994, 'Respect Reed Richards (Marvel, 616)', 'https://www.reddit.com/r/iridescence_stuff/comments/b73oq7/respect_reed_richards_marvel_616/')
update_respectthread(cur, 7484, 'Respect the Infinity Gauntlet (Marvel: Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/e46vif/respect_the_infinity_gauntlet_marvel_earth616/')
update_respectthread(cur, 14893, 'Respect Chris Redfield (Resident Evil)', 'https://www.reddit.com/r/respectthreads/comments/cl603b/respect_chris_redfield_resident_evil/')
update_respectthread(cur, 25832, 'Respect Spawn! (DEATH BATTLE!)', 'https://www.reddit.com/r/respectthreads/comments/1j26seg/respect_spawn_death_battle/')
update_respectthread(cur, 13479, 'Respect Ghostface (Scream 1996)', 'https://www.reddit.com/r/respectthreads/comments/1jfv4is/respect_ghostface_scream_1996/')
update_respectthread(cur, 25883, 'Respect Ghostface (Scream 2)', 'https://www.reddit.com/r/respectthreads/comments/1jhbg1e/respect_ghostface_scream_2/')
update_respectthread(cur, 25884, 'Respect Ghostface (Scream 3)', 'https://www.reddit.com/r/respectthreads/comments/1jfvbyp/respect_ghostface_scream_3/')
update_respectthread(cur, 25885, 'Respect Ghostface (Scream 4)', 'https://www.reddit.com/r/respectthreads/comments/1jg6de6/respect_ghostface_scream_4/')
update_respectthread(cur, 25886, 'Respect Ghostface (Scream 2022)', 'https://www.reddit.com/r/respectthreads/comments/1jfvoww/respect_ghostface_scream_2022/')
update_respectthread(cur, 25887, 'Respect Ghostface (Scream 6)', 'https://www.reddit.com/r/respectthreads/comments/1jfvm0a/respect_ghostface_scream_6/')
update_respectthread(cur, 24551, 'Respect The Man in the Suit (Unknowingly/Godzilla Analog Horror)', 'https://www.reddit.com/r/respectthreads/comments/18bloxy/respect_the_man_in_the_suit_unknowinglygodzilla/')

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 20: the Tin Man Armor (Marvel, 616)', 'https://www.reddit.com/r/respectthreads/comments/1mbfp7o/respect_iron_man_model_20_the_tin_man_armor/')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 20'], ['Tin Man Armor']
],
'Tin Man Armor',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Iron Man''s Prison Escape Armor (Marvel, Earth-616)", 'https://www.reddit.com/r/respectthreads/comments/1mcots5/respect_iron_mans_prison_escape_armor_marvel/')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Prison Escape Armor']
],
'Prison Escape Armor',
'{' + '{}'.format(id) + '}'
)
#


########################################

########################################

id = get_rt_id(cur, 'Respect the Man in the Suit (Xeno)', 'https://www.reddit.com/r/respectthreads/comments/1mc09zr/respect_the_man_in_the_suit_xeno/')
add_data(['Man in the Suit'],
'Man in the Suit',
False,
False,
[
    ['Xeno']
],
'Xeno',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Altirhinus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mc2vfa/respect_altirhinus_dinosaur_king/')
add_data(['Altirhinus'],
'Altirhinus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mapusaurus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mc35hx/respect_mapusaurus_dinosaur_king/')
add_data(['Mapusaurus'],
'Mapusaurus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Carcharodontosaurus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mdlwu2/respect_carcharodontosaurus_dinosaur_king/')
add_data(['Carcharodontosaurus'],
'Carcharodontosaurus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect B''wana Beast (DC Comics, Post-Crisis)", 'https://www.reddit.com/r/respectthreads/comments/1mc9r1v/respect_bwana_beast_dc_comics_postcrisis/')
add_data(["B''?wana Beast"],
"B''wana Beast",
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(["B''?wana Beast"],
"B''wana Beast",
False,
False,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#

add_data(["B''?wana Beast"],
"B''wana Beast",
False,
True,
[
    ['DC Comics'], ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mr. Crocket (Mr. Crocket)', 'https://www.reddit.com/r/respectthreads/comments/1mdagyf/respect_mr_crocket_mr_crocket/')
add_data(['Mr\.? Crocket'],
'Mr. Crocket',
False,
True,
[
    ['Mr. Crocket ?\(Mr. Crocket\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1mdagyf/respect_mr_crocket_mr_crocket/

########################################

id = get_rt_id(cur, 'Respect Geiz (Kamen Rider Zi-O)', 'https://www.reddit.com/r/respectthreads/comments/1mdlovi/respect_geiz_kamen_rider_zio/')
add_data(['Geiz'],
'Geiz',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#4

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

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

update_respectthread(cur, 6105, 'Respect Skitter, Warlord of Brockton Bay (Worm)', 'https://www.reddit.com/r/respectthreads/comments/7ukfsm/respect_skitter_warlord_of_brockton_bay_worm/')
update_respectthread(cur, 6067, 'Respect Contessa [Worm]', 'https://www.reddit.com/r/respectthreads/comments/66sxiz/respect_contessa_worm/')
update_respectthread(cur, 8445, 'Respect Homelander! (The Boys, Dynamite)', 'https://www.reddit.com/r/respectthreads/comments/d2ib3k/respect_homelander_the_boys_dynamite/')
update_respectthread(cur, 13117, "Respect Homelander (Amazon''s The Boys)", 'https://www.reddit.com/r/respectthreads/comments/x1ibg9/respect_homelander_amazons_the_boys/')
update_respectthread(cur, 1503, 'Respect: Cassandra Cain, Batgirl ! (DC, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1lqd5qa/respect_cassandra_cain_batgirl_dc_postflashpoint/')
update_respectthread(cur, 5098, 'Respect John-117, The Master Chief (Halo)', 'https://www.reddit.com/r/respectthreads/comments/fbv3cr/respect_john117_the_master_chief_halo/')
update_respectthread(cur, 21139, 'Respect Space Marines (Warhammer 40k)', 'https://www.reddit.com/r/Thevexarecool/comments/jbsqpz/respect_space_marines_warhammer_40k/')
update_respectthread(cur, 6466, 'The humble Space Marine (Xpost /r/whowouldwin)', 'https://www.reddit.com/r/respectthreads/comments/1sq5al/the_humble_space_marine_xpost_rwhowouldwin/')
update_respectthread(cur, 12490, 'Respect Yuji Itadori! (Jujutsu Kaisen)', 'https://www.reddit.com/r/respectthreads/comments/1fs37f9/respect_yuji_itadori_jujutsu_kaisen/')
update_respectthread(cur, 4709, 'Respect Denji, the Chainsaw Man! (Chainsaw Man)', 'https://www.reddit.com/r/respectthreads/comments/vw7tm4/respect_denji_the_chainsaw_man_chainsaw_man/')
update_respectthread(cur, 2175, 'Respect Iron Man Model 37: the Bleeding Edge Armor (Marvel, 616)', 'https://www.reddit.com/r/respectthreads/comments/1lzmw33/respect_iron_man_model_37_the_bleeding_edge_armor/')
update_respectthread(cur, 1962, 'Respect Omni-Man (Image Comics)', 'https://www.reddit.com/r/respectthreads/comments/mtf5fv/respect_omniman_image_comics/')
update_respectthread(cur, 16453, 'Respect Omni-Man (Invincible)', 'https://www.reddit.com/r/respectthreads/comments/n70nig/respect_omniman_invincible/')

########################################

id = get_rt_id(cur, 'Respect Styracosaurus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1lz7fjt/respect_styracosaurus_dinosaur_king/')
add_data(['Styracosaurus'],
'Styracosaurus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lz7fjt/respect_styracosaurus_dinosaur_king/

########################################

id = get_rt_id(cur, 'Respect the Imagined (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1lzxcer/respect_the_imagined_fortnite/')
add_data(['The Imagined'],
'The Imagined',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
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

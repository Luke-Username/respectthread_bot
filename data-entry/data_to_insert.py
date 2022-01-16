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

update_respectthread(cur, 4686, 'Respect Orthrus! (Ben-To) (anime)', 'https://redd.it/s2k8z9')
update_respectthread(cur, 5048, 'Respect The Alpha and the Omega, Vergil (Devil May Cry)', 'https://redd.it/s2mqcc')
update_respectthread(cur, 1722, 'Respect Khalid Nassour, Doctor Fate (DC Comics, Rebirth)', 'https://redd.it/s31kq8')
update_respectthread(cur, 4403, 'Respect Ryouga (Pokemon ReBurst)', 'https://redd.it/s3yqjy')

########################################

id = get_rt_id(cur, 'Respect Spartan 1337 (Halo)', 'https://redd.it/3bcm7w')
add_data(['Spartan(-| )1337'],
'Spartan-1337',
False,
True,
[
    ['Halo']
],
'Halo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/3bcm7w/respect_spartan_1337_halo/
#https://www.reddit.com/r/whowouldwin/comments/s3kwvf/spartan_1337_halo_legends_vs_caboose_red_vs_blue/hslftzd/?context=3

########################################

id = get_rt_id(cur, "Respect Elma (Miss Kobayashi''s Dragon Maid)!", 'https://redd.it/bcqasy')
add_data(['Elma'],
'Elma',
False,
False,
[
    ['Dragon Maid'], ['Kobayashi']
],
'Miss Kobayashi''s Dragon Maid',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/bcqasy/respect_elma_miss_kobayashis_dragon_maid/

########################################

id = get_rt_id(cur, "Respect King Rion (Arthurian Myth)", 'https://redd.it/s2p42w')
add_data(['King Rion'],
'King Rion',
False,
True,
[
    ['Arthurian']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s2p42w/respect_king_rion_arthurian_myth/

########################################

id = get_rt_id(cur, "Respect Jarro! (DC Post Rebirth)", 'https://redd.it/s2zmk9')
add_data(['Jarro'],
'Jarro',
False,
False,
[
    ['DC'], ['Rebirth']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s2zmk9/respect_jarro_dc_post_rebirth/

########################################

id = get_rt_id(cur, "Respect: Superman! (Raj Comics)", 'https://redd.it/s34nag')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Raj Comics']
],
'Raj Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s34nag/respect_superman_raj_comics/

########################################

id = get_rt_id(cur, "Respect the G.I. Jeff team (Community)", 'https://redd.it/s39vp7')
add_data(['G\.?I\.? Jeff'],
'G.I. Jeff',
True,
True,
[
    ['Community']
],
'Community',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s39vp7/respect_the_gi_jeff_team_community/

########################################

id = get_rt_id(cur, "Respect Hariru (Pokemon ReBurst)", 'https://redd.it/s4md6c')
add_data(['Hariru'],
'Hariru',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pocket Monsters RéBURST',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s4md6c/respect_hariru_pokemon_reburst/

########################################

id = get_rt_id(cur, "Respect Chiharu Shiba (Baki)", 'https://redd.it/s3ywe9')
add_data(['Chiharu Shiba'],
'Chiharu Shiba',
False,
True,
[
    ['Baki']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s3ywe9/respect_chiharu_shiba_baki/

########################################

id = get_rt_id(cur, "Respect Gamera, the Friend to All Children! (Gamera, Showa Era)", 'https://redd.it/s4kmad')
add_data(['Gamera'],
'Gamera',
False,
True,
[
    ['Gamera.*Showa|Showa Gamera']
],
'Showa Era',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s4kmad/respect_gamera_the_friend_to_all_children_gamera/

########################################

add_data(['Green Goblin'],
'Green Goblin',
False,
False,
[
    ['MCU']
],
'Miss Kobayashi''s Dragon Maid',
'{300}'
)
#https://www.reddit.com/r/whowouldwin/comments/s49vvb/daredevil_punisher_and_elektra_mcu_vs_green/hspsp90/?context=3

########################################

add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['TSS']
],
'DCEU',
'{20353}'
)
#https://www.reddit.com/r/whowouldwin/comments/s4dlz6/peacemaker_tss_and_show_vs_the_punisher_netflix/hsqg9r4/?context=3

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['House of M']
],
'616',
'{1997}'
)
#https://www.reddit.com/r/respectthreads/comments/kpmkhq/respect_wanda_maximoff_the_scarlet_witch_marvel/
#https://www.reddit.com/r/whowouldwin/comments/s4ggp6/rune_king_thor_vs_house_of_m_wanda/hss0443/?context=3

########################################

add_data(['Cable'],
'Cable',
False,
False,
[
    ['Deadpool 2']
],
'FOX',
'{140}'
)
#https://www.reddit.com/r/whowouldwin/comments/s4pvf2/cable_deadpool_2_vs_bloodsport_and_peacemaker/hssmh7u/?context=3

########################################

add_data(['Game Sonic'],
'Game Sonic',
False,
True,
[
    ['Sonic the Hedgehog']
],
'',
'{8276,8277}'
)
#https://www.reddit.com/r/whowouldwin/comments/s4umxc/z_goku_vs_game_sonic/

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

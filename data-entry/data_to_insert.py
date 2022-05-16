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

update_respectthread(cur, 16555, 'Respect MechaMew2 (Pokemon Live!)', 'https://redd.it/uor69h')
update_respectthread(cur, 1213, 'Respect Owlman (Justice League: Crisis on Two Earths)', 'https://redd.it/uovq7k')
update_respectthread(cur, 1081, 'Respect Magneto (The New Fantastic Four)', 'https://redd.it/uplwdn')
update_respectthread(cur, 13131, "Respect Judge Claude Frollo (Disney''s The Hunchback of Notre Dame)", 'https://redd.it/upv1rc')

########################################

add_data(['Ultron'],
'Ultron',
False,
False,
[
    ['Ultron ?\(EMH']
],
"Earth''s Mightiest Heroes",
'{21353}'
)
#https://www.reddit.com/r/whowouldwin/comments/uqbmrz/ultron_emh_vs_ultron_mcu/i8q0x59/?context=3

########################################

add_data(['Scarlett? Witch'],
'Scarlet Witch',
False,
False,
[
    ['Scarlet Witch.*MoM']
],
'MCU',
'{270}'
)
#https://www.reddit.com/r/whowouldwin/comments/uqayri/scarlet_witch_mom_vs_a_few_marvel_characters/i8pz1ku/?context=3

########################################

add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Sonic ?\((Movie|Film)s?']
],
'2020 film',
'{8607}'
)
#https://www.reddit.com/r/whowouldwin/comments/uq8fed/anne_boonchuy_amphibia_vs_sonic_movie/i8peeff/?context=3

########################################

add_data(['Shang(-| )Chi'],
'Shang-Chi',
False,
True,
[
    ['comics']
],
'616',
'{2104}'
)
#https://www.reddit.com/r/whowouldwin/comments/upb0ji/which_mcu_or_dceu_characters_beat_their_comics/i8mt10m/?context=3

########################################

add_data(['Terraria'],
'Terraria',
False,
False,
[
    ['Playable character']
],
'',
'{5497}'
)
#https://www.reddit.com/r/whowouldwin/comments/uoexvj/terraria_playable_character_vs_minecraft_steve/

########################################

id = get_rt_id(cur, 'Respect Kai (Ninjago)', 'https://redd.it/uoepgg')
add_data(['Kai'],
'Kai',
False,
False,
[
    ['Ninjago']
],
'Ninjago',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uoepgg/respect_kai_ninjago/

########################################

id = get_rt_id(cur, 'Respect Izou Motobe (Grappler Baki)', 'https://redd.it/uogiu3')
add_data(['Izou Motobe'],
'Izou Motobe',
False,
False,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uogiu3/respect_izou_motobe_grappler_baki/

########################################

id = get_rt_id(cur, 'Respect Voyager! (Fate)', 'https://redd.it/uoj2b5')
add_data(['Voyager'],
'Voyager',
False,
False,
[
    ['Voyager.*Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uoj2b5/respect_voyager_fate/

########################################

id = get_rt_id(cur, "Respect Beowulf''s Dragon (Beowulf)", 'https://redd.it/uov9tz')
add_data(["Beowulf''s Dragon"],
"Beowulf''s Dragon",
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uov9tz/respect_beowulfs_dragon_beowulf/

########################################

id = get_rt_id(cur, 'Respect Mega Man (Captain N: The Game Master)', 'https://redd.it/uoz5fx')
add_data(['Mega ?Man'],
'Mega Man',
False,
False,
[
    ['Captain N']
],
'Captain N: The Game Master',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uoz5fx/respect_mega_man_captain_n_the_game_master/

########################################

id = get_rt_id(cur, 'Respect Imperiex! (Legion of Super Heroes)', 'https://redd.it/upaoue')
add_data(['Imperiex'],
'Imperiex',
False,
False,
[
    ['Legion of Super(-| )Heroes']
],
'Legion of Super Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upaoue/respect_imperiex_legion_of_super_heroes/

########################################

id = get_rt_id(cur, 'Respect the Swarms (Prey)', 'https://redd.it/upr570')
add_data(['Swarms'],
'Swarms',
False,
False,
[
    ['Swarms ?\(Prey']
],
'Prey',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upr570/respect_the_swarms_prey/

########################################

id = get_rt_id(cur, 'Respect Silver the Hedgehog (Sonic the Hedgehog) [Archie Comics, Pre Genesis]', 'https://redd.it/upvv26')
add_data(['Silver'],
'Silver',
False,
False,
[
    ['Archie Silver'], ['Sonic', '\(Archie']
],
'Archie Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upvv26/respect_silver_the_hedgehog_sonic_the_hedgehog/

add_data(['Silver the Hedgehog'],
'Silver the Hedgehog',
False,
False,
[
    ['Archie']
],
'Archie Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upvv26/respect_silver_the_hedgehog_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Shadow the Hedgehog (Sonic the Hedgehog) [Archie Comics, Pre Genesis]', 'https://redd.it/upvvh5')
add_data(['Shadow'],
'Shadow',
False,
False,
[
    ['Archie Shadow'], ['Sonic', '\(Archie']
],
'Archie Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upvv26/respect_silver_the_hedgehog_sonic_the_hedgehog/

add_data(['Shadow the Hedgehog'],
'Shadow the Hedgehog',
False,
False,
[
    ['Archie']
],
'Archie Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/upvvh5/respect_shadow_the_hedgehog_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Flint Marko, the Sandman (The Spectacular Spider-Man)', 'https://redd.it/uq4iv6')
add_data(['Sand(-| )?man'],
'Sandman',
False,
False,
[
    ['Spectacular Spider-?Man']
],
'Spectacular Spider-Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uq4iv6/respect_flint_marko_the_sandman_the_spectacular/

########################################

id = get_rt_id(cur, 'Respect The Fantastic Four (Marvel, 7712)', 'https://redd.it/uq5w3d')
add_data(['Fantastic Four'],
'Fantastic Four',
False,
True,
[
    ['7712']
],
'7712',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uq5w3d/respect_the_fantastic_four_marvel_7712/

########################################

id = get_rt_id(cur, 'Respect Evo (Space Station Silicon Valley)', 'https://redd.it/uqaajt')
add_data(['Evo'],
'Evo',
False,
False,
[
    ['Space Station Silicon Valley']
],
'Space Station Silicon Valley',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uqaajt/respect_evo_space_station_silicon_valley/

########################################

id = get_rt_id(cur, 'Jack Danner, Hawk-Owl (Marvel, 1610)', 'https://redd.it/uqkqsx')
add_data(['Hawk(-| )Owl'],
'Hawk-Owl',
False,
False,
[
    ['1610'], ['Jack Danner']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uqkqsx/jack_danner_hawkowl_marvel_1610/

########################################

id = get_rt_id(cur, 'Respect Clayface (DCAU)', 'https://redd.it/uqt82o')
add_data(['Clayface'],
'Clayface',
False,
False,
[
    ['DC Animated Universe'], ['DCAU']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uqt82o/respect_clayface_dcau/

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

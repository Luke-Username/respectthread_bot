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

update_respectthread(cur, 3416, 'Respect Dante (Fullmetal Alchemist 2003)', 'https://redd.it/16bayip')
update_respectthread(cur, 1965, 'Respect Norman Osborn, the Super-Adaptoid (Marvel Comics, 616)', 'https://redd.it/16cpwrn')
update_respectthread(cur, 6554, 'Respect Billy Batson, Shazam (DC Extended Universe)', 'https://redd.it/16bmuk0')
update_respectthread(cur, 6555, 'Respect the Shazam Family (DC Extended Universe)', 'https://redd.it/16bmxf5')
update_respectthread(cur, 5977, 'Respect Kaladin Stormblessed (The Stormlight Archive)', 'https://redd.it/16dej6r')
update_respectthread(cur, 5978, 'Respect Szeth-son-son-Vallano, Truthless of Shinovar (The Stormlight Archive)', 'https://redd.it/16dbwb8')
update_respectthread(cur, 16016, "Respect Bumblebee! (Michael Bay''s Transformers)", 'https://redd.it/16copl7')
update_respectthread(cur, 4766, 'Respect Major Motoko Kusagani (Ghost in the Shell Stand Alone Complex)', 'https://redd.it/16c26ss')
update_respectthread(cur, 3980, 'Respect Evangelion Unit-00 (Neon Genesis Evangelion)', 'https://redd.it/16c19ag')
update_respectthread(cur, 23500, 'Respect Evangelion Unit-02 (Neon Genesis Evangelion)', 'https://redd.it/16c18ew')
update_respectthread(cur, 3983, 'Respect Evangelion Unit-01 (Neon Genesis Evangelion)', 'https://redd.it/16c1686')

########################################

add_data(['Yoyo'],
'Yoyo',
False,
False,
[
    ["Hyun''?s Dojo"]
],
'RHG',
'{17370}'
)
#

########################################

add_data(['Mashle'],
'Mashle',
False,
False,
[
    ['Mashle vs'], ['vs\.? Mashle']
],
'Mashle: Magic and Muscles',
'{14512}'
)
#

########################################

add_data(['Belos'],
'Belos',
False,
False,
[
    ['Owl House']
],
'The Owl House',
'{20613}'
)
#https://www.reddit.com/r/whowouldwin/comments/16aqz4t/could_the_doctor_doctor_who_stop_the_day_of_unity/jz9v2oh/?context=3

########################################

add_data(['Steve Austin'],
'Steve Austin',
False,
False,
[
    ['Bionic Man'], ['Dynamite Entertainment']
],
'Dynamite Comics',
'{21266}'
)
#

########################################

add_data(['Rumbling'],
'Rumbling',
False,
False,
[
    ['The Rumbling', 'Eren']
],
'Attack on Titan',
'{12492}'
)
#

########################################

id = get_rt_id(cur, "Respect Arlong (Netflix''s One Piece, Live Action)", 'https://redd.it/16apjxn')
add_data(['Arlong'],
'Arlong',
False,
False,
[
    ["(Netflix(''?s?)?|Live(-| )Action) ?One Piece"]
],
"Netflix''s One Piece",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Spirit (Spirit: Stallion of the Cimarron)', 'https://redd.it/16aad5y')
add_data(['Spirit'],
'Spirit',
False,
False,
[
    ['Stallion of the Cimarron']
],
'Spirit: Stallion of the Cimarron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16aad5y/respect_spirit_spirit_stallion_of_the_cimarron/

########################################

id = get_rt_id(cur, 'Respect Dimitri Alexandre Blaiddyd! (DEATH BATTLE!)', 'https://redd.it/16ar5k0')
add_data(['Dimitri'],
'Dimitri',
False,
False,
[
    ['DEATH BATTLE', 'Fire Emblem']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16ar5k0/respect_dimitri_alexandre_blaiddyd_death_battle/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 24: the Iron Secretary, MK I (Marvel Comics, 616)', 'https://redd.it/16bb2cc')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 24'], ['Iron Secretary']
],
'Model 24',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16bb2cc/respect_iron_man_model_24_the_iron_secretary_mk_i/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 65: the Ultronbuster! (Marvel, 616)', 'https://redd.it/16blx0l')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 65'], ['Ultronbuster']
],
'Ultronbuster',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 58: the Nano Iron Man Armor! (Marvel, 616)', 'https://redd.it/16blf1g')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 58']
],
'Model 58',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16blf1g/respect_iron_man_model_58_the_nano_iron_man_armor/

########################################

id = get_rt_id(cur, 'Respect The Fusion of Superman, Batman and Green Lantern (DC, Rebirth)', 'https://redd.it/16bhpm6')
add_data(['Fusion of Superman, Batman and Green Lantern'],
'Fusion of Superman, Batman and Green Lantern',
False,
True,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16bhpm6/respect_the_fusion_of_superman_batman_and_green/

########################################

id = get_rt_id(cur, 'Respect Roxy Rocket (DC Comics)', 'https://redd.it/16d9qn4')
add_data(['Roxy Rocket'],
'Roxy Rocket',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16d9qn4/respect_roxy_rocket_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Roxy Rocket (DCAU)', 'https://redd.it/16d9nnc')
add_data(['Roxy Rocket'],
'Roxy Rocket',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16d9nnc/respect_roxy_rocket_dcau/

########################################

id = get_rt_id(cur, 'Respect Dalinar Kholin (The Stormlight Archive)', 'https://redd.it/16bv97c')
add_data(['Dalinar Kholin'],
'Dalinar Kholin',
False,
True,
[
    ['Storm ?light']
],
'The Stormlight Archive',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16bv97c/respect_dalinar_kholin_the_stormlight_archive/

########################################

id = get_rt_id(cur, "Respect The Girl Gamer (De_dust2: Hacker''s Wrath Tribute)", 'https://redd.it/16d91ud')
add_data(['Girl Gamer'],
'Girl Gamer',
False,
False,
[
    ['De_dust2']
],
"De_dust2: Hacker''s Wrath Tribute",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect The Hacker (De_dust2: Hacker''s Wrath Tribute)", 'https://redd.it/16d91fp')
add_data(['Hacker'],
'Hacker',
False,
False,
[
    ['De_dust2']
],
"De_dust2: Hacker''s Wrath Tribute",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16d91fp/respect_the_hacker_de_dust2_hackers_wrath_tribute/

########################################

id = get_rt_id(cur, 'Respect General Rilldo (Dragon Ball GT)', 'https://redd.it/16c1dvj')
add_data(['General Rilldo'],
'General Rilldo',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16c1dvj/respect_general_rilldo_dragon_ball_gt/

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

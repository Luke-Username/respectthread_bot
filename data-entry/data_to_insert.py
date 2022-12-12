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

add_data(['Black Goku'],
'Black Goku',
False,
False,
[
    ['SSJ9K']
],
'SSJ9K',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/zi3sah/goku_dbs_vs_black_goku_ssj9k_original_character/izpf8j0/?context=3

########################################

id = get_rt_id(cur, 'Respect Phineas and Ferb (Phineas and Ferb) Draft', 'https://redd.it/df9hsm')
add_data(['Phineas (and|&) Ferb'],
'Phineas and Ferb',
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/zhw7qh/phineas_and_ferb_with_6_months_prep_time_vs/izo6nz7/?context=3

########################################

id = get_rt_id(cur, 'Respect the Starship Hulk (Marvel, Earth-616)', 'https://redd.it/zhqu59')
add_data(['Starship Hulk'],
'Starship Hulk',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhqu59/respect_the_starship_hulk_marvel_earth616/

add_data(['Smashtronaut'],
'Smashtronaut',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhqu59/respect_the_starship_hulk_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect Mr. Terrific (DCAU)', 'https://redd.it/zhqwg7')
add_data(['(Mr\.?|Mister) Terrific'],
'Mister Terrific',
False,
False,
[
    ['DC Animated Universe'], ['DCAU']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhqwg7/respect_mr_terrific_dcau/

########################################

id = get_rt_id(cur, 'Respect Lyle Corley, The Clown (DC, Pre-Crisis)', 'https://redd.it/zhtjm0')
add_data(['Lyle Corley'],
'Lyle Corley',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhtjm0/respect_lyle_corley_the_clown_dc_precrisis/

add_data(['Lyle Corley'],
'Lyle Corley',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhtjm0/respect_lyle_corley_the_clown_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Mary Marvel! (DC Comics, Post-Crisis)', 'https://redd.it/zi7vfd')
add_data(['Mary Marvel'],
'Mary Marvel',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhtjm0/respect_lyle_corley_the_clown_dc_precrisis/

add_data(['Mary Marvel'],
'Mary Marvel',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zi7vfd/respect_mary_marvel_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Black Mary (Young Justice)', 'https://redd.it/zhwi2y')
add_data(['Black Mary'],
'Black Mary',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhwi2y/respect_black_mary_young_justice/

########################################

id = get_rt_id(cur, 'Respect Leonard Snart, Citizen Cold (DC Comics, Flashpoint Timeline)', 'https://redd.it/zivllc')
add_data(['Citizen Cold'],
'Citizen Cold',
False,
True,
[
    ['Flashpoint']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zivllc/respect_leonard_snart_citizen_cold_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Priscilla (Claymore)', 'https://redd.it/zhvi08')
add_data(['Priscilla'],
'Priscilla',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zhvi08/respect_priscilla_claymore/

########################################

id = get_rt_id(cur, 'Respect Teresa of the Faint Smile (Claymore)', 'https://redd.it/ziyyac')
add_data(['Teresa'],
'Teresa',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ziyyac/respect_teresa_of_the_faint_smile_claymore/

########################################

id = get_rt_id(cur, 'Respect Garrett (Thief)', 'https://redd.it/zipzsc')
add_data(['Garrett'],
'Garrett',
False,
False,
[
    ['Garrett.*Thief']
],
'Thief',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zipzsc/respect_garrett_thief/

########################################

id = get_rt_id(cur, 'Respect Grenade Man (Mega Man)', 'https://redd.it/ziby56')
add_data(['Grenade Man'],
'Grenade Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ziby56/respect_grenade_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Frost Man (Mega Man)', 'https://redd.it/zicnkl')
add_data(['Frost Man'],
'Frost Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zicnkl/respect_frost_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Clown Man (Mega Man)', 'https://redd.it/zie7c9')
add_data(['Clown Man'],
'Clown Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zie7c9/respect_clown_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Nitro Man (Mega Man)', 'https://redd.it/ziha6k')
add_data(['Nitro Man'],
'Nitro Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ziha6k/respect_nitro_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Chill Man (Mega Man)', 'https://redd.it/zihduk')
add_data(['Chill Man'],
'Chill Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zihduk/respect_chill_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Sheep Man (Mega Man)', 'https://redd.it/zihhxy')
add_data(['Sheep Man'],
'Sheep Man',
False,
True,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zihhxy/respect_sheep_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Strike Man (Mega Man)', 'https://redd.it/zjfk62')
add_data(['Strike Man'],
'Strike Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjfk62/respect_strike_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Commando Man (Mega Man)', 'https://redd.it/zjgjfn')
add_data(['Commando Man'],
'Commando Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Blade Man (Mega Man)', 'https://redd.it/zjgo76')
add_data(['Blade Man'],
'Blade Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjgo76/respect_blade_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Wood Man (Mega Man)', 'https://redd.it/zjjpgv')
add_data(['Wood Man'],
'Wood Man',
False,
True,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjjpgv/respect_wood_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Top Man (Mega Man)', 'https://redd.it/zjjpji')
add_data(['Top Man'],
'Top Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjjpji/respect_top_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Hard Man (Mega Man)', 'https://redd.it/zjjq2p')
add_data(['Hard Man'],
'Hard Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjjpji/respect_top_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Zero.EXE (Mega Man Network Transmission)', 'https://redd.it/zj8b9d')
add_data(['Zero\.EXE'],
'Zero.EXE',
False,
True,
[
    ['Network Transmission'], ['Battle Network']
],
'Mega Man Battle Network',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zj8b9d/respect_zeroexe_mega_man_network_transmission/

########################################

id = get_rt_id(cur, 'Respect Ryokugyu! (One Piece)', 'https://redd.it/zjkqfz')
add_data(['Ryokugyu'],
'Ryokugyu',
False,
True,
[
    ['One ?Piece?'], ['Admirals?'], ['Logia']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjkqfz/respect_ryokugyu_one_piece/

########################################

id = get_rt_id(cur, 'Respect Thirteen (Young Justice)', 'https://redd.it/zj7rlu')
add_data(['Thirteen'],
'Thirteen',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zj7rlu/respect_thirteen_young_justice/

########################################

id = get_rt_id(cur, 'Respect Green Arrow (Young Justice)', 'https://redd.it/zjlpm9')
add_data(['Green Arrow'],
'Green Arrow',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zjlpm9/respect_green_arrow_young_justice/

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

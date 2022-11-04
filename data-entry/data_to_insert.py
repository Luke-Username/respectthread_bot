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

update_respectthread(cur, 6067, 'Respect Contessa [Worm]', 'https://redd.it/66sxiz')

########################################

add_data(['Chainsaw(-| )?Man'],
'Chainsaw Man',
False,
False,
[
    ['Chainsaw(-| )?Man vs']
],
'',
'{4709}'
)
#https://www.reddit.com/r/whowouldwin/comments/yj8blx/chainsaw_man_vs_all_might/iumrhm0/?context=3

########################################

add_data(['Falcon'],
'Falcon',
False,
False,
[
    ['Falcon ?\((Marvel)? ?616']
],
'616',
'{17672}'
)
#https://www.reddit.com/r/whowouldwin/comments/yl1nbt/hawks_mha_vs_falcon_marvel_616/iuxf45y/?context=3

########################################

add_data(['John Walker'],
'John Walker',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{21271}'
)
#https://www.reddit.com/r/whowouldwin/comments/ykgseo/steve_rogers_john_walker_and_sam_wilson_mcu_vs/iut5so2/?context=3

########################################

id = get_rt_id(cur, 'Respect Naoya Zenin! (Jujutsu Kaisen)', 'https://redd.it/yjawqc')
add_data(['Naoya'],
'Naoya',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yjawqc/respect_naoya_zenin_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Caretaker (Marvel 616)', 'https://redd.it/yjhx88')
add_data(['Caretaker'],
'Caretaker',
False,
False,
[
    ['Blood', '616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yjhx88/respect_caretaker_marvel_616/

########################################

id = get_rt_id(cur, 'Respect the Gods of Amonkhet! (Magic: The Gathering)', 'https://redd.it/yl4h5u')
add_data(['Gods of Amonkhet'],
'Gods of Amonkhet',
True,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yl4h5u/respect_the_gods_of_amonkhet_magic_the_gathering/

add_data(['Hazoret'],
'Hazoret',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yl4h5u/respect_the_gods_of_amonkhet_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect: He-Man! (Fall Of Grayskull)', 'https://redd.it/ylcngo')
add_data(['He(-| )?Man'],
'He-Man',
False,
False,
[
    ['Fall Of Grayskull']
],
'Fall Of Grayskull',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ylcngo/respect_heman_fall_of_grayskull/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 61: The Godkiller Mark II (Marvel, Earth-616)', 'https://redd.it/yldaig')
add_data(['Godkiller Mark II'],
'Godkiller Mark II',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yldaig/respect_iron_man_model_61_the_godkiller_mark_ii/

########################################

id = get_rt_id(cur, 'Armor Variants/Mechanized Armors', 'https://redd.it/859e71')
add_data(['Final Bat(-| )?Suit'],
'Final Bat-Suit',
False,
True,
[
    ['DC']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/BatmanMegaRT/comments/859e71/armor_variantsmechanized_armors/

add_data(['HellBat'],
'HellBat',
False,
False,
[
    ['Suit'], ['Bat(-| )?mans?']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/BatmanMegaRT/comments/859e71/armor_variantsmechanized_armors/

add_data(['Hell Bat'],
'Hell Bat',
False,
False,
[
    ['Suit'], ['Bat(-| )?mans?']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/BatmanMegaRT/comments/859e71/armor_variantsmechanized_armors/

########################################

id = get_rt_id(cur, 'Respect Scaramouche, The Balladeer! (Genshin Impact)', 'https://redd.it/ylhvfg')
add_data(['Scaramouche'],
'Scaramouche',
False,
False,
[
    ['Genshin']
],
'Genshin Impact',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ylhvfg/respect_scaramouche_the_balladeer_genshin_impact/

########################################

id = get_rt_id(cur, 'Respect Nadine Hurley (Twin Peaks)', 'https://redd.it/ylrbuy')
add_data(['Nadine'],
'Nadine',
False,
False,
[
    ['Nadine Hurley'], ['Twin Peaks']
],
'Twin Peaks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ylrbuy/respect_nadine_hurley_twin_peaks/

########################################

id = get_rt_id(cur, 'Respect the Red Chalk (ChalkZone)', 'https://redd.it/ylyhjp')
add_data(['Red Chalk'],
'Red Chalk',
False,
False,
[
    ['Chalk ?Zone']
],
'ChalkZone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ylyhjp/respect_the_red_chalk_chalkzone/

########################################

id = get_rt_id(cur, 'Respect Hunter Rose, Grendel (Grendel)', 'https://redd.it/ym0utl')
add_data(['Hunter Rose'],
'Hunter Rose',
False,
True,
[
    ['Grendel']
],
'Grendel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ym0utl/respect_hunter_rose_grendel_grendel/

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

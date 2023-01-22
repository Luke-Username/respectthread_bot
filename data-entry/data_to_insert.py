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

update_respectthread(cur, 5654, 'Respect A2 (Nier: Automata)', 'https://redd.it/10h2h4m')
update_respectthread(cur, 1020, 'Respect The Team (Young Justice)', 'https://redd.it/10hxs6d')

########################################

add_data(['Shinso'],
'Shinso',
False,
False,
[
    ['My Hero Academia'], ['(M|BN?)HA'], ['Boku no Hero'], ['Brainwash(ing|er)'], ['Quirks?']
],
'My Hero Academia',
'{17325}'
)
#https://www.reddit.com/r/whowouldwin/comments/10hbx6m/a_brainwasher_studies_under_the_ingenious_mind/j57jaeu/?context=3

########################################

add_data(['Galen Marek'],
'Galen Marek',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{5728}'
)
#https://www.reddit.com/r/whowouldwin/comments/10hohsn/jean_grey_vs_forcesensitives/

########################################

id = get_rt_id(cur, 'Respect Eric Myers, the Quantum Ranger! (Power Rangers Time Force)', 'https://redd.it/10gl0ot')
add_data(['Eric Myers'],
'Eric Myers',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gl0ot/respect_eric_myers_the_quantum_ranger_power/

add_data(['Quantum Ranger'],
'Quantum Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gl0ot/respect_eric_myers_the_quantum_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Prince Caspian! (The Chronicles of Narnia)', 'https://redd.it/10gm7pu')
add_data(['Prince Caspian'],
'Prince Caspian',
False,
True,
[
    ['Narnia']
],
'The Chronicles of Narnia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gm7pu/respect_prince_caspian_the_chronicles_of_narnia/

add_data(['Caspian'],
'Caspian',
False,
False,
[
    ['Narnia']
],
'The Chronicles of Narnia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gm7pu/respect_prince_caspian_the_chronicles_of_narnia/

########################################

id = get_rt_id(cur, 'Respect Edmund Pevensie (The Chronicles of Narnia)', 'https://redd.it/10gmf62')
add_data(['Edmund'],
'Edmund',
False,
False,
[
    ['Narnia'], ['Pevensie']
],
'The Chronicles of Narnia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Susan Pevensie (The Chronicles of Narnia)', 'https://redd.it/10gmhkq')
add_data(['Susan'],
'Susan',
False,
False,
[
    ['Narnia'], ['Pevensie']
],
'The Chronicles of Narnia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gmhkq/respect_susan_pevensie_the_chronicles_of_narnia/

########################################

id = get_rt_id(cur, "Respect Batman''s Superman-suit (DC Comics, Post-Crisis)", 'https://redd.it/10gmt1n')
add_data(["Bat(-| )?man''?s Super(-| )?man(-| )suit"],
"Batman''s Superman-suit",
False,
True,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gmt1n/respect_batmans_supermansuit_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, "Respect Batman''s Justice Buster (DC Comics, New52)", 'https://redd.it/10h6qa1')
add_data(['Justice Buster'],
'Justice Buster',
False,
True,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth']
],
'New 52',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10h6qa1/respect_batmans_justice_buster_dc_comics_new52/

########################################

id = get_rt_id(cur, 'Respect: Vulkan (Warhammer 40k)', 'https://redd.it/10gokqg')
add_data(['Vulkan'],
'Vulkan',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10gokqg/respect_vulkan_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect White Lantern Batman (DC Comics, Rebirth)', 'https://redd.it/10hh441')
add_data(['White Lantern Batman'],
'White Lantern Batman',
False,
True,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hh441/respect_white_lantern_batman_dc_comics_rebirth/

########################################

id = get_rt_id(cur, 'Respect The Bizzare Batman Genie (DC, Pre-Crisis)', 'https://redd.it/10hs97t')
add_data(['Bizzare Batman(-| )Genie'],
'Bizzare Batman-Genie',
False,
True,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hs97t/respect_the_bizzare_batman_genie_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect: Overman! (DC Comics, Post Crisis Earth 10/Earth X)', 'https://redd.it/10hy45g')
add_data(['Overman'],
'Overman',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth'], ['Earth(-| )(10|X)']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hy45g/respect_overman_dc_comics_post_crisis_earth/

add_data(['Overman'],
'Overman',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}, 23212'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hy45g/respect_overman_dc_comics_post_crisis_earth/

########################################

id = get_rt_id(cur, 'Respect Arthur, King of the Britons! (BOOM! Studios, Once & Future)', 'https://redd.it/10hixg6')
add_data(['Arthur'],
'Arthur',
False,
False,
[
    ['Once (&|and) Future']
],
'Once & Future',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hixg6/respect_arthur_king_of_the_britons_boom_studios/

########################################

id = get_rt_id(cur, 'Respect Kinshiki Otsutsuki (Boruto: Naruto Next Generations [Manga])', 'https://redd.it/10ho688')
add_data(['Kinshiki'],
'Kinshiki',
False,
True,
[
    ['Naruto'], ['Boruto'], ['(Ō|O)tsutsuki'], ['Momoshiki']
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10ho688/respect_kinshiki_otsutsuki_boruto_naruto_next/

########################################

id = get_rt_id(cur, 'Respect Denzel Crocker! (The Fairly OddParents)', 'https://redd.it/10hvsus')
add_data(['Crocker'],
'Crocker',
False,
False,
[
    ['Fairly Odd ?parents'], ['FOP'], ['Timmy|Cosmo|Wanda'], ['Denzel'], ['Fair(y|ies)'], ['Muffin'], ['Mr\.? Crocker'], ['Abra Catastrophe']
],
'Fairly OddParents',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10hvsus/respect_denzel_crocker_the_fairly_oddparents/

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

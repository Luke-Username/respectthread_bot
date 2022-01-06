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

update_respectthread(cur, 3058, 'Respect Levi Ackerman (Attack On Titan)', 'https://redd.it/d2tr8g')

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['MCU']
],
'MCU',
'{130}'
)
#https://www.reddit.com/r/whowouldwin/comments/rwg8vx/mcu_wanda_and_agatha_vs_mandalorian_lukecanon/hrbnuvi/?context=3

########################################

add_data(['Levi'],
'Levi',
False,
False,
[
    ['Mikasa'], ['Captain Levi'], ['Eren']
],
'Attack on Titan',
'{3058}'
)
#https://www.reddit.com/r/whowouldwin/comments/rx25ud/avengers_vs_justice_league_but_with_their_actors/hrfm6ju/?context=3

########################################

add_data(['Green Lantern'],
'Green Lantern',
False,
False,
[
    ['Reynolds?']
],
'2011',
'{20535}'
)
#https://www.reddit.com/r/whowouldwin/comments/rwtvtr/strongest_member_of_the_justice_league_dceu_that/hre1ouu/?context=3

########################################

id = get_rt_id(cur, 'Respect the Eradicator! (DC Comics, New 52/Rebirth)', 'https://redd.it/rwin0a')
add_data(['Eradicator'],
'Eradicator',
False,
False,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwin0a/respect_the_eradicator_dc_comics_new_52rebirth/

add_data(['Eradicator'],
'Eradicator',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwin0a/respect_the_eradicator_dc_comics_new_52rebirth/

########################################

id = get_rt_id(cur, 'Respect Sha Xin Guan Yin (Xi Xing Ji)', 'https://redd.it/rwp54q')
add_data(['Guan Yin'],
'Guan Yin',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwp54q/respect_sha_xin_guan_yin_xi_xing_ji/

########################################

id = get_rt_id(cur, 'Respect Gautama (Xi Xing Ji)', 'https://redd.it/rx0r6d')
add_data(['Gautama'],
'Gautama',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rx0r6d/respect_gautama_xi_xing_ji/

########################################

id = get_rt_id(cur, 'Respect the Family Madrigal (Encanto)', 'https://redd.it/rwpblt')
add_data(['Family Madrigal|Madrigal Family', 'The Madrigals'],
'Family Madrigal',
True,
True,
[
    ['Encanto']
],
'Encanto',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mirabel'],
'Mirabel',
False,
False,
[
    ['Encanto'], ['Madrigal']
],
'Encanto',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Isabela'],
'Isabela',
False,
False,
[
    ['Encanto'], ['Madrigal']
],
'Encanto',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Bruno'],
'Bruno',
False,
False,
[
    ['Encanto'], ['Madrigal']
],
'Encanto',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Luisa'],
'Luisa',
False,
False,
[
    ['Encanto'], ['Madrigal']
],
'Encanto',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Fat Bastard (Austin Powers)', 'https://redd.it/rws9r0')
add_data(['Fat Bastard'],
'Fat Bastard',
False,
False,
[
    ['Austin Powers'], ['Mike Myers'], ['Goldmember']
],
'Austin Powers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rws9r0/respect_fat_bastard_austin_powers/

########################################

id = get_rt_id(cur, 'Respect Pyro (Dreamwalker)', 'https://redd.it/rwuvp2')
add_data(['Pyro'],
'Pyro',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gun Robot (Trollhunters: Rise of the Titans)', 'https://redd.it/rwyfib')
add_data(['Gun Robot'],
'Gun Robot',
False,
False,
[
    ['Trollhunters'], ['Rise of the Titans']
],
'Trollhunters: Rise of the Titans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwyfib/respect_gun_robot_trollhunters_rise_of_the_titans/

########################################

id = get_rt_id(cur, 'Respect Byron Williams (Mars Attacks!)', 'https://redd.it/rx2xsw')
add_data(['Byron Williams'],
'Byron Williams',
False,
False,
[
    ['Mars Attacks']
],
'Mars Attacks!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yagyu Munenori! (Fate)', 'https://redd.it/rx5j9y')
add_data(['Yagyu Munenori'],
'Yagyu Munenori',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rx5j9y/respect_yagyu_munenori_fate/

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

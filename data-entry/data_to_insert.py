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

update_respectthread(cur, 4403, 'Respect Ryouga (Pokemon ReBurst)', 'https://redd.it/1j5ohy6')
update_respectthread(cur, 8117, 'Respect Din Djarin, the Mandalorian (Star Wars)', 'https://redd.it/1j6fhjv')

########################################

id = get_rt_id(cur, 'Respect Black Battler! (Umineko: When They Cry [Manga])', 'https://redd.it/1j336o7')
add_data(['Black Battler'],
'Black Battler',
False,
True,
[
    ['Umineko'], ['When they Cry']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j336o7/respect_black_battler_umineko_when_they_cry_manga/

########################################

id = get_rt_id(cur, 'Respect Sam Temple (Gone)', 'https://redd.it/1j33afi')
add_data(['Sam Temple'],
'Sam Temple',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j33afi/respect_sam_temple_gone/

########################################

id = get_rt_id(cur, 'Respect Himeji Onizuka (Tough)', 'https://redd.it/1j3d7pd')
add_data(['Himeji Onizuka'],
'Himeji Onizuka',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j3d7pd/respect_himeji_onizuka_tough/

########################################

id = get_rt_id(cur, 'Respect Jim Snuka (Tough)', 'https://redd.it/1j44qxq')
add_data(['Jim Snuka'],
'Jim Snuka',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j44qxq/respect_jim_snuka_tough/

########################################

id = get_rt_id(cur, 'Respect Todar (Tough)', 'https://redd.it/1j50h6i')
add_data(['Todar'],
'Todar',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j50h6i/respect_todar_tough/

########################################

id = get_rt_id(cur, 'Respect D-51 (Tough)', 'https://redd.it/1j5ts2n')
add_data(['D-51'],
'D-51',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j5ts2n/respect_d51_tough/

########################################

id = get_rt_id(cur, 'Respect Sam Strong (Beneath the Trees Where Nobody Sees)', 'https://redd.it/1j47ktn')
add_data(['Sam Strong'],
'Sam Strong',
False,
False,
[
    ['Beneath the Trees Where Nobody Sees']
],
'Beneath the Trees Where Nobody Sees',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Great Doughnut Ball King (CookieRun: Ovenbreak)', 'https://redd.it/1j5mngv')
add_data(['Great Doughnut Ball King'],
'Great Doughnut Ball King',
False,
True,
[
    ['Cookie ?Run']
],
'CookieRun',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j5mngv/respect_great_doughnut_ball_king_cookierun/

########################################

id = get_rt_id(cur, 'Respect Adrian Chase, The Vigilante! (DC Comics, Post Crisis)', 'https://redd.it/1j5pzg9')
add_data(['Adrian Chase'],
'Adrian Chase',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Adrian Chase'],
'Adrian Chase',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['Vigilante']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#


add_data(['Adrian Chase'],
'Adrian Chase',
False,
False,
[
    ['(Fl)?arrow(-| )?verse'], ['(DC)?CW'], ['DC ?TV']
],
'CW Arrowverse',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Treasure Hunt No.1 (No.1 Gozyuger)', 'https://redd.it/1j5rpdy')
add_data(['Treasure Hunt No\.? ?1'],
'Treasure Hunt No.1',
False,
True,
[
    ['Gozyuger']
],
'No.1 Gozyuger',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shin Soru (The Ability to Shift Anything is Convenient, Even in Another World! [Web Novel])', 'https://redd.it/1j6jl5b')
add_data(['Shin Soru'],
'Shin Soru',
False,
False,
[
    ['Ability to Shift Anything is Convenient']
],
'The Ability to Shift Anything is Convenient, Even in Another World!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Armored All Might (My Hero Academia)', 'https://redd.it/1j6qy3z')
add_data(['Armored All Might'],
'Armored All Might',
False,
True,
[
    ['My Hero Academia'], ['\(My Hero\)'], ['(M|BN?)HA'], ['Boku no Hero'], ['Class ?1(-| )?a']
],
'My Hero Academia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Original Gray Hulk! (Marvel, 616)', 'https://redd.it/1j6s4aa')
add_data(['Gray Hulk'],
'Gray Hulk',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j6s4aa/respect_the_original_gray_hulk_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Meltan and Melmetal (Pokémon)', 'https://redd.it/1j6xcf8')
add_data(['Meltan'],
'Meltan',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j6xcf8/respect_meltan_and_melmetal_pok%C3%A9mon/

add_data(['Melmetal'],
'Melmetal',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j6xcf8/respect_meltan_and_melmetal_pok%C3%A9mon/

########################################

id = get_rt_id(cur, 'Respect Firefly (Honkai: Star Rail)', 'https://redd.it/1j774rr')
add_data(['Firefly'],
'Firefly',
False,
False,
[
    ['Honkai']
],
'Honkai: Star Rail',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tianhai Divine Empress! (Ze Tian Ji | Way of Choices)', 'https://redd.it/1j7m9r9')
add_data(['Tianhai Divine Empress'],
'Tianhai Divine Empress',
False,
True,
[
    ['Ze Tian Ji'], ['Way of Choices']
],
'Ze Tian Ji | Way of Choices',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pyotr! (Hunter: the Parenting)', 'https://redd.it/1j7mh9g')
add_data(['Pyotr'],
'Pyotr',
False,
False,
[
    ['Hunter:? the Parenting']
],
'Hunter: the Parenting',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j7mh9g/respect_pyotr_hunter_the_parenting/

########################################

id = get_rt_id(cur, 'Respect Caine Soren (Gone)', 'https://redd.it/1j7pkcc')
add_data(['Caine Soren'],
'Caine Soren',
False,
True,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j7pkcc/respect_caine_soren_gone/

########################################

id = get_rt_id(cur, 'Respect Popular No.1 (No.1 Sentai Gozyuger)', 'https://redd.it/1j99ph5')
add_data(['Popular No\.? ?1'],
'Popular No.1',
False,
False,
[
    ['Sentai Gozyuger']
],
'No.1 Sentai Gozyuger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1j99ph5/respect_popular_no1_no1_sentai_gozyuger/

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

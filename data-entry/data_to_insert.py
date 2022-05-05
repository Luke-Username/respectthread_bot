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

add_data(['Omnidrone'],
'Omnidrone',
False,
False,
[
    ['Incredibles']
],
'The Incredibles',
'{1132}'
)
#https://www.reddit.com/r/whowouldwin/comments/ui1a9k/eve_walle_vs_syndromes_omnidrone_incredibles/

########################################

id = get_rt_id(cur, 'Respect Green Lantern (DC Comics, Earth-9)', 'https://redd.it/ui5ne5')
add_data(['Green Lantern'],
'Green Lantern',
False,
False,
[
    ['Earth-9']
],
'Earth-9',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ui5dw6/respect_buck_bumble_buck_bumble/

########################################

id = get_rt_id(cur, 'Respect Thor Odinson, the Herald of Galactus (Marvel, Earth-717)', 'https://redd.it/ui8d5j')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['717']
],
'717',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ui8d5j/respect_thor_odinson_the_herald_of_galactus/

########################################

id = get_rt_id(cur, 'Respect Semiramis, the Empress of Assyria (Fate)', 'https://redd.it/ui8vpp')
add_data(['Semiramis'],
'Semiramis',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ui8vpp/respect_semiramis_the_empress_of_assyria_fate/

########################################

id = get_rt_id(cur, 'Respect the Questing Beast (Arthurian Myth)', 'https://redd.it/uibq81')
add_data(['Questing Beast'],
'Questing Beast',
False,
False,
[
    ['Arthurian']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uibq81/respect_the_questing_beast_arthurian_myth/

########################################

id = get_rt_id(cur, 'Respect The Cheetah (Catwoman: Hunted)', 'https://redd.it/uii2ak')
add_data(['Cheetah'],
'Cheetah',
False,
False,
[
    ['Catwoman:? Hunted']
],
'Catwoman: Hunted',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uii2ak/respect_the_cheetah_catwoman_hunted/

########################################

id = get_rt_id(cur, 'Respect Sai (One Piece)', 'https://redd.it/uimvjc')
add_data(['Sai'],
'Sai',
False,
False,
[
    ['Sai ?(One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uimvjc/respect_sai_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Nanotyrannus (Jurassic Fight Club)', 'https://redd.it/uitx1n')
add_data(['Nanotyrannus'],
'Nanotyrannus',
False,
False,
[
    ['Jurassic Fight Club']
],
'Jurassic Fight Club',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uitx1n/respect_the_nanotyrannus_jurassic_fight_club/

########################################

id = get_rt_id(cur, 'Respect Gar Saxon! (Star Wars Canon)', 'https://redd.it/uiwioz')
add_data(['Gar Saxon'],
'Gar Saxon',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uiwioz/respect_gar_saxon_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect the Martians (Mars Attacks!)', 'https://redd.it/uiwvsi')
add_data(['Martians'],
'Martians',
False,
False,
[
    ['Mars Attacks']
],
'Mars Attacks!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uiwvsi/respect_the_martians_mars_attacks/

########################################

id = get_rt_id(cur, 'Respect KISS (Marvel, 616)', 'https://redd.it/uiwz17')
add_data(['KISS'],
'KISS',
False,
False,
[
    ['KISS ?\(616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uiwz17/respect_kiss_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Thor Odinson, the Lord of Midgard (Marvel, Earth-3515)', 'https://redd.it/uj2ijd')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['3515']
],
'3515',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uj2ijd/respect_thor_odinson_the_lord_of_midgard_marvel/

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

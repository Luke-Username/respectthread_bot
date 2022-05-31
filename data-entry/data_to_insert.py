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

update_respectthread(cur, 300, 'Respect The Green Goblin! (Raimi)', 'https://redd.it/v0w2vv')

########################################

add_data(['X'],
'X',
False,
False,
[
    ['\(Mega Man X\)']
],
'Mega Man X',
'{12145}'
)
#https://www.reddit.com/r/whowouldwin/comments/v0b3bp/so_me_and_my_little_brother_has_gotten_into_an/

########################################

add_data(['Kong'],
'Kong',
False,
False,
[
    ['\(KOTM\)']
],
'MonsterVerse',
'{281}'
)
#https://www.reddit.com/r/whowouldwin/comments/v1d9a7/gundams_vs_ghidora_kotm/ials1xv/?context=3

########################################

add_data(['Akatsuki'],
'Akatsuki',
False,
False,
[
    ['Orochimaru']
],
'Naruto',
'{3964,3967,3960,3950,3959,3972,3942,3948,3956}'
)
#

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla vs Kong Final Battle… But The Roles Are Reversed)', 'https://redd.it/v0npmb')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Godzilla vs Kong Final Battle', 'But The Roles Are Reversed']
],
'Godzilla vs Kong Final Battle… But The Roles Are Reversed',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0npmb/respect_godzilla_godzilla_vs_kong_final_battle/

########################################

id = get_rt_id(cur, 'Respect Ouma Kurogane, (Rakudai Kishi No Calvary)', 'https://redd.it/v0rjg2')
add_data(['Ouma Kurogane'],
'Ouma Kurogane',
False,
True,
[
    ['Chivalry of a Failed Knight'], ['Rakudai']
],
'Chivalry of a Failed Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0rjg2/respect_ouma_kurogane_rakudai_kishi_no_calvary/

########################################

id = get_rt_id(cur, 'Respect M.O.R.B.I.U.S (Marvel Earth-14512)', 'https://redd.it/v0xgj0')
add_data(['M\.O\.R\.B\.I\.U\.S'],
'M.O.R.B.I.U.S',
False,
False,
[
    ['14512']
],
'14512',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0xgj0/respect_morbius_marvel_earth14512/

########################################

id = get_rt_id(cur, 'Respect the Hulk (Hulk: Ultimate Destruction)', 'https://redd.it/v0z96d')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Hulk:? Ultimate Destruction']
],
'Hulk: Ultimate Destruction',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0z96d/respect_the_hulk_hulk_ultimate_destruction/

########################################

id = get_rt_id(cur, 'Respect Adolf Hitler (Danger 5)', 'https://redd.it/v10v0h')
add_data(['Hitler'],
'Hitler',
False,
False,
[
    ['Danger 5']
],
'Danger 5',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v10v0h/respect_adolf_hitler_danger_5/

########################################

id = get_rt_id(cur, 'Respect Alien Jones (BOSS Coffee)', 'https://redd.it/v130c9')
add_data(['Alien Jones'],
'Alien Jones',
False,
False,
[
    ['BOSS Coffee']
],
'BOSS Coffee',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v130c9/respect_alien_jones_boss_coffee/

########################################

id = get_rt_id(cur, 'Respect HUNK (Resident Evil)', 'https://redd.it/v140ym')
add_data(['Hunk'],
'Hunk',
False,
False,
[
    ['Resident Evil']
],
'Resident Evil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v140ym/respect_hunk_resident_evil/

########################################

id = get_rt_id(cur, 'Respect Mickey Mouse (Mickey, Donald, Goofy: The Three Musketeers)', 'https://redd.it/v1dq73')
add_data(['Mickey'],
'Mickey',
False,
False,
[
    ['Donald', 'Goofy', 'Musketeers']
],
'Mickey, Donald, Goofy: The Three Musketeers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v1dq73/respect_mickey_mouse_mickey_donald_goofy_the/

add_data(['Mickey Mouse'],
'Mickey Mouse',
False,
False,
[
    ['Three Musketeers']
],
'Mickey, Donald, Goofy: The Three Musketeers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v1dq73/respect_mickey_mouse_mickey_donald_goofy_the/

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

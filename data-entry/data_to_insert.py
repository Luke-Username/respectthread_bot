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

add_data(['Santa Clause?'],
'Santa Claus',
False,
False,
[
    ['CSM']
],
'Chainsaw Man',
'{15324}'
)
#https://www.reddit.com/r/whowouldwin/comments/174nffz/mahitojjk_vs_santa_clauscsm/k4a6ixa/?context=3

########################################

add_data(['C\.?A\.?S\.? Superman'],
'Cosmic Armor',
False,
True,
[
    ['DC']
],
'DC',
'{1777}'
)
#https://www.reddit.com/r/whowouldwin/comments/174g63n/cas_superman_vs_beyonder_who_would_win/

add_data(['Beyonder'],
'Beyonder',
False,
False,
[
    ['C\.?A\.?S\.? Superman']
],
'Marvel',
'{2108,2107}'
)
#https://www.reddit.com/r/whowouldwin/comments/174g63n/cas_superman_vs_beyonder_who_would_win/

########################################

id = get_rt_id(cur, 'Respect Daniel Hatchid! (Tower of God)', 'https://redd.it/1739et9')
add_data(['Daniel Hatchid'],
'Daniel Hatchid',
False,
True,
[
    ['Tower of God']
],
'Tower of God',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1739et9/respect_daniel_hatchid_tower_of_god/

########################################

id = get_rt_id(cur, 'Respect SCP-ZH-002, Taiwanese Unicorn (SCP Foundation)', 'https://redd.it/173hy0l')
add_data(['SCP ?(-| )? ?ZH ?(-| )? ?002'],
'SCP-ZH-002',
False,
True,
[
    ['Taiwanese Unicorn']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/173hy0l/respect_scpzh002_taiwanese_unicorn_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect CRP-5550, Pencilneck! (The CRP Institute)', 'https://redd.it/1744ig8')
add_data(['SCP ?(-| )? ?5550'],
'CRP-5550',
False,
True,
[
    ['Pencilneck']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alex Mercer! (DEATH BATTLE!)', 'https://redd.it/173k069')
add_data(['Alex Mercer'],
'Alex Mercer',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/173k069/respect_alex_mercer_death_battle/

########################################

id = get_rt_id(cur, 'Respect Cole MacGrath! (DEATH BATTLE!)', 'https://redd.it/173k0xj')
add_data(['Cole Ma?c?Grath'],
'Cole MacGrath',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/173k0xj/respect_cole_macgrath_death_battle/

########################################

id = get_rt_id(cur, 'Respect The Roots (The Seed from the Sepulcher)', 'https://redd.it/173q7q4')
add_data(['The Roots'],
'The Roots',
False,
False,
[
    ['Seed from the Sepulcher']
],
'The Seed from the Sepulcher',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/173q7q4/respect_the_roots_the_seed_from_the_sepulcher/

########################################

id = get_rt_id(cur, 'Respect The Powerpuff Girls (Cancelled CW Pilot Script)', 'https://redd.it/1741vs6')
add_data(['Power ?puff Girls'],
'Powerpuff Girls',
True,
False,
[
    ['CW', 'Script']
],
'CW Script',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1741vs6/respect_the_powerpuff_girls_cancelled_cw_pilot/

########################################

id = get_rt_id(cur, 'Respect Jeff the Killer! (Jeff the Killer 2011)', 'https://redd.it/1743rzy')
add_data(['Jeff the Killer'],
'Jeff the Killer',
False,
True,
[
    ['2011']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 25: the Iron Secretary Mark II (Marvel, Earth-616)', 'https://redd.it/1746va8')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 25']
],
'Model 25',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1746va8/respect_iron_man_model_25_the_iron_secretary_mark/

########################################

id = get_rt_id(cur, 'Respect the Concavenator (M e d i c b a g)', 'https://redd.it/174d0we')
add_data(['Concavenator'],
'Concavenator',
False,
False,
[
    ['M e d i c b a g']
],
'M e d i c b a g',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/174d0we/respect_the_concavenator_m_e_d_i_c_b_a_g/

########################################

id = get_rt_id(cur, 'Respect the Alioramus (M e d i c b a g)', 'https://redd.it/174dbbh')
add_data(['Alioramus'],
'Alioramus',
False,
False,
[
    ['M e d i c b a g']
],
'M e d i c b a g',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/174dbbh/respect_the_alioramus_m_e_d_i_c_b_a_g/

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

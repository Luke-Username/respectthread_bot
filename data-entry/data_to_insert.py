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

update_respectthread(cur, 565, 'Respect The Monstars! (Space Jam)', 'https://redd.it/yevxgk')

########################################

add_data(['Chainsaw(-| )?Man'],
'Chainsaw Man',
False,
False,
[
    ['vs\.? Chainsaw(-| )?Man']
],
'',
'{4709}'
)
#https://www.reddit.com/r/whowouldwin/comments/yef5wz/cloud_strife_vs_chainsaw_man/

########################################

add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe'], ['Dwayne'], ['The Rock']
],
'DCEU',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/yeq8bh/black_adam_dceu_vs_wonder_woman_dceu/itzqczv/?context=3

########################################

add_data(['D(octo)?r\.? Fate'],
'Doctor Fate',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/ycrutt/doctor_fate_vs_doctor_strange/itv9lm8/?context=3

add_data(['(Doctor|Dr\.?|Stephen) ?Strange'],
'Doctor Strange',
False,
False,
[
    ['MoM.*Strange'], ['Strange.*MoM']
],
'MCU',
'{13351}'
)
#https://www.reddit.com/r/whowouldwin/comments/ycrutt/doctor_fate_vs_doctor_strange/itv9lm8/?context=3

########################################

id = get_rt_id(cur, 'Respect Maniac Harry (Maniac of New York)', 'https://redd.it/ydxtke')
add_data(['Maniac Harry'],
'Maniac Harry',
False,
True,
[
    ['Maniac of New York']
],
'Maniac of New York',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ydxtke/respect_maniac_harry_maniac_of_new_york/

########################################

id = get_rt_id(cur, "Respect Hughie Campbell (Amazon''s The Boys)", 'https://redd.it/yeie68')
add_data(['Hughie Campbell'],
'Hughie Campbell',
False,
True,
[
    ['The Boys']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yeie68/respect_hughie_campbell_amazons_the_boys/

########################################

id = get_rt_id(cur, 'Respect Anthony Lupus, The Werewolf (DC, Pre-Crisis)', 'https://redd.it/yesopk')
add_data(['Anthony Lupus'],
'Anthony Lupus',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yesopk/respect_anthony_lupus_the_werewolf_dc_precrisis/

add_data(['Anthony Lupus'],
'Anthony Lupus',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yesopk/respect_anthony_lupus_the_werewolf_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect the Juggernaut (Spider-Man: Shattered Dimensions)', 'https://redd.it/yeu2fz')
add_data(['Juggernaut'],
'Juggernaut',
False,
False,
[
    ['Spider(-| )?Man:? ?Shattered Dimensions']
],
'Spider-Man: Shattered Dimensions',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yeu2fz/respect_the_juggernaut_spiderman_shattered/

########################################

id = get_rt_id(cur, 'Respect Roland (After the Revolution)', 'https://redd.it/yey3h4')
add_data(['Roland'],
'Roland',
False,
False,
[
    ['After the Revolution']
],
'After the Revolution',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yey3h4/respect_roland_after_the_revolution/

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

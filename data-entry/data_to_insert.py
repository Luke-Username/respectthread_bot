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

update_respectthread(cur, 3975, 'Respect A, the Third Raikage (Naruto)', 'https://redd.it/t81577')

########################################

id = get_rt_id(cur, 'Respect Sonic.EXE/X (Creepypasta)', 'https://redd.it/t7opfo')
add_data(['Sonic(\.| )EXE'],
'Sonic.EXE',
False,
True,
[
    ['Creepypasta']
],
'Creepypasta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t7opfo/respect_sonicexex_creepypasta/

########################################

id = get_rt_id(cur, 'Respect Kenji Lance (Blaze Core)', 'https://redd.it/t7qasj')
add_data(['Kenji Lance'],
'Kenji Lance',
False,
False,
[
    ['Blaze Core']
],
'Blaze Core',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t7qasj/respect_kenji_lance_blaze_core/

########################################

id = get_rt_id(cur, 'Respect Captain Boomerang! (Injustice)', 'https://redd.it/t7tcm8')
add_data(['Captain Boomerang'],
'Captain Boomerang',
False,
False,
[
    ['Injustice(verse)?']
],
'Injustice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t7tcm8/respect_captain_boomerang_injustice/

########################################

id = get_rt_id(cur, 'Respect the Lostbelts! (Fate)', 'https://redd.it/t7u48p')
add_data(['Lostbelts'],
'Lostbelts',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t7u48p/respect_the_lostbelts_fate/

########################################

id = get_rt_id(cur, "Respect April O''Neil (Teenage Mutant Ninja Turtles 2012)", 'https://redd.it/t84fr3')
add_data(["April O''Neil"],
"April O''Neil",
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t84fr3/respect_april_oneil_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Miyamoto Usagi (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t84fse')
add_data(['Miyamoto Usagi|Usagi Miyamoto'],
'Miyamoto Usagi',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t84fse/respect_miyamoto_usagi_teenage_mutant_ninja/

########################################

id = get_rt_id(cur, 'Respect Princess Zelda! (The Legend of Zelda CD-i Games)', 'https://redd.it/t8d3ze')
add_data(['Zelda'],
'Zelda',
False,
False,
[
    ['Zelda.*CD-?i']
],
'CD-i',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t8d3ze/respect_princess_zelda_the_legend_of_zelda_cdi/

########################################

id = get_rt_id(cur, 'Respect C890.L! (The Terminator)', 'https://redd.it/t8gimx')
add_data(['C890\.L'],
'C890.L',
False,
True,
[
    ['Terminator']
],
'The Terminator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t8gimx/respect_c890l_the_terminator/

########################################

id = get_rt_id(cur, 'RESPECT Tahno (Legend of Korra)', 'https://redd.it/t8jcxa')
add_data(['Tahno'],
'Tahno',
False,
False,
[
    ['Avatar'], ['A?TLA'], ['Korra'], ['A?T?LOK']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t8jcxa/respect_tahno_legend_of_korra/

########################################

id = get_rt_id(cur, "RESPECT Amon''s Lieutenant (Legend of Korra)", 'https://redd.it/t8jfmv')
add_data(['Lieutenant'],
'Lieutenant',
False,
False,
[
    ['The Lieutenant', 'Avatar'], ['Amon'], ['The Lieutenant', 'Korra'], ['The Lieutenant', 'A?T?LOK']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t8jfmv/respect_amons_lieutenant_legend_of_korra/

########################################

id = get_rt_id(cur, 'Respect The Unicorn (The Last Unicorn)', 'https://redd.it/t8s0ey')
add_data(['The Last Unicorn'],
'The Last Unicorn',
False,
True,
[
    ['Beagle']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t8s0ey/respect_the_unicorn_the_last_unicorn/

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

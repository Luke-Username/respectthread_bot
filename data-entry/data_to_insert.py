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

add_data(['Goliath'],
'Goliath',
False,
False,
[
    ["Gargoyle''s"]
],
'Gargoyles',
'{783}'
)
#https://www.reddit.com/r/whowouldwin/comments/178awu7/bruce_wayne_dc_vs_goliath_gargoyles/

########################################

add_data(['Ben'],
'Ben',
False,
False,
[
    ['Ben Florian'], ['Descendants']
],
'Descendants',
'{24423}'
)
#https://www.reddit.com/r/respectthreads/comments/18v3o02/respect_captain_gutt_ice_age/kfyr9pr/?context=3

add_data(['Jay'],
'Jay',
False,
False,
[
    ['Prince Sultan Jay'], ['Descendants']
],
'Descendants',
'{24423}'
)
#https://www.reddit.com/r/respectthreads/comments/18v3o02/respect_captain_gutt_ice_age/kfyr9pr/?context=3

add_data(['Gil'],
'Gil',
False,
False,
[
    ['Gil(bert)? LeGume'], ['Gil ?\(Descendants\)']
],
'Descendants',
'{24423}'
)
#https://www.reddit.com/r/respectthreads/comments/18v3o02/respect_captain_gutt_ice_age/kfyr9pr/?context=3

add_data(['Lonnie'],
'Lonnie',
False,
False,
[
    ['Li Lonnie'], ['Descendants']
],
'Descendants',
'{24423}'
)
#https://www.reddit.com/r/respectthreads/comments/18v3o02/respect_captain_gutt_ice_age/kfyr9pr/?context=3

add_data(['Chad Charming'],
'Chad Charming',
False,
True,
[
    ['Descendants']
],
'Descendants',
'{24423}'
)
#https://www.reddit.com/r/respectthreads/comments/18v3o02/respect_captain_gutt_ice_age/kfyr9pr/?context=3

########################################

id = get_rt_id(cur, 'Respect the Demon! (The Drowned Man)', 'https://redd.it/18vpquj')
add_data(['The Demon'],
'The Demon',
False,
False,
[
    ['The Drowned Man']
],
'The Drowned Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect John Carver! (Thanksgiving)', 'https://redd.it/18vv58l')
add_data(['John Carver'],
'John Carver',
False,
False,
[
    ['Thanksgiving']
],
'Thanksgiving',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18vv58l/respect_john_carver_thanksgiving/

########################################

id = get_rt_id(cur, 'Respect Godzilla! (Godzilla vs Justice League vs Kong)', 'https://redd.it/18vvv7o')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Justice League vs Godzilla vs Kong'], ['Godzilla vs Justice League vs Kong']
],
'Justice League vs Godzilla vs Kong',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18vvv7o/respect_godzilla_godzilla_vs_justice_league_vs/

########################################

id = get_rt_id(cur, 'Respect Mitsuhide Kuroda (Tough)', 'https://redd.it/18w3e4d')
add_data(['Mitsuhide Kuroda'],
'Mitsuhide Kuroda',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18w3e4d/respect_mitsuhide_kuroda_tough/

########################################

id = get_rt_id(cur, 'Respect War Machine Model 3: the Initiative Armor (Marvel, Earth-616)', 'https://redd.it/18we9g7')
add_data(['War Machine'],
'War Machine',
False,
False,
[
    ['Model 3'], ['Initiative Armor']
],
'Model 3',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18we9g7/respect_war_machine_model_3_the_initiative_armor/

########################################

id = get_rt_id(cur, 'Respect Nayuta! (Chainsaw Man)', 'https://redd.it/18wenw4')
add_data(['Nayuta'],
'Nayuta',
False,
False,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18wenw4/respect_nayuta_chainsaw_man/

########################################

id = get_rt_id(cur, 'Barem (Chainsaw Man)', 'https://redd.it/18wf46n')
add_data(['Barem'],
'Barem',
False,
False,
[
    ['Chainsaw(-| )?Man'], ['Barem Bridge']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18wf46n/barem_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Naz (Dragon Ball AF, Young Jijii)', 'https://redd.it/18wj2mt')
add_data(['Naz'],
'Naz',
False,
False,
[
    ['Dragon Ball AF']
],
'Dragon Ball AF',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18wj2mt/respect_naz_dragon_ball_af_young_jijii/

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

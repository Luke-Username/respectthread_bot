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

update_respectthread(cur, 4870, 'Respect Casshern (Neo Human Casshern)', 'https://redd.it/13dijbm')

########################################

id = get_rt_id(cur, 'Respect Garfield (Garfield Live Action Films)', 'https://redd.it/13clcr8')
add_data(['Garfield'],
'Garfield',
False,
False,
[
    ['live(-| )action']
],
'Live-Action',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13clcr8/respect_garfield_garfield_live_action_films/

########################################

id = get_rt_id(cur, 'Respect: Gregor Eisenhorn (Warhammer 40k)', 'https://redd.it/13czqp5')
add_data(['Gregor Eisenhorn'],
'Gregor Eisenhorn',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13czqp5/respect_gregor_eisenhorn_warhammer_40k/


########################################

id = get_rt_id(cur, 'Respect Belinda "Lindy" White! (The Candy Shop War)', 'https://redd.it/13d3pbd')
add_data(['Belinda White'],
'Belinda White',
False,
False,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13d3pbd/respect_belinda_lindy_white_the_candy_shop_war/

########################################

id = get_rt_id(cur, 'Respect Luigi (The Super Mario Bros. Movie)', 'https://redd.it/13dehd4')
add_data(['Luigi'],
'Luigi',
False,
False,
[
    ['Mario( Bros\.?)? Movie'], ['Illumination']
],
'The Super Mario Bros. Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13dehd4/respect_luigi_the_super_mario_bros_movie/

########################################

id = get_rt_id(cur, 'Respect Princess Peach (The Super Mario Bros. Movie)', 'https://redd.it/13dejiy')
add_data(['Princess Peach'],
'Princess Peach',
False,
False,
[
    ['Mario( Bros\.?)? Movie'], ['Illumination']
],
'The Super Mario Bros. Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13dejiy/respect_princess_peach_the_super_mario_bros_movie/

add_data(['Peach'],
'Peach',
False,
False,
[
    ['Mario( Bros\.?)? Movie'], ['Illumination']
],
'The Super Mario Bros. Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13dejiy/respect_princess_peach_the_super_mario_bros_movie/

########################################

id = get_rt_id(cur, 'Respect Bowser (The Super Mario Bros. Movie)', 'https://redd.it/13dem7g')
add_data(['Bowser'],
'Bowser',
False,
False,
[
    ['Mario( Bros\.?)? Movie'], ['Illumination']
],
'The Super Mario Bros. Movie',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Legion (The Blueballs Incident)', 'https://redd.it/13dytsg')
add_data(['Legion'],
'Legion',
False,
False,
[
    ['Blueballs Incident'], ['Friday Night Funkin']
],
'The Blueballs Incident',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13dytsg/respect_legion_the_blueballs_incident/

########################################

id = get_rt_id(cur, 'Respect The Titans! (God of War)', 'https://redd.it/13e9bs3')
add_data(['Titans'],
'Titans',
True,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Gaia'],
'Gaia',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Cronos'],
'Cronos',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Atlas'],
'Atlas',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Oceanus'],
'Oceanus',
False,
False,
[
    ['God of War']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Epimetheus'],
'Epimetheus',
False,
False,
[
    ['God of War']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

add_data(['Perses'],
'Perses',
False,
False,
[
    ['God of War']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13e9bs3/respect_the_titans_god_of_war/

########################################

id = get_rt_id(cur, 'Respect Polymar [Hurricane Polymar]', 'https://redd.it/13eea7q')
add_data(['Polymar'],
'Polymar',
False,
True,
[
    ['Hurricane Polymar']
],
'Hurricane Polymar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13eea7q/respect_polymar_hurricane_polymar/

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

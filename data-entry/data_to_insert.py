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

update_respectthread(cur, 1686, 'Respect Larfleeze, the Orange Lantern! (DC Comics, Post-Crisis)', 'https://redd.it/v53md3')
update_respectthread(cur, 1764, 'Respect Bizarro (DC, Rebirth)', 'https://redd.it/v5o680')
update_respectthread(cur, 1357, 'Respect Yang Xiao Long! (RWBY)', 'https://redd.it/v6b5pe')

########################################

add_data(['Griffith'],
'Griffith',
False,
False,
[
    ['Guts']
],
'Berserk',
'{12088}'
)
#https://www.reddit.com/r/whowouldwin/comments/v57cdq/mr_t_vs_nightrider_vs_airwolf_vs_andy_griffith/ib8d4x1/?context=3

########################################

id = get_rt_id(cur, 'Respect The Demons (Aliens: Phalanx)', 'https://redd.it/v4rnk4')
add_data(['Demons'],
'Demons',
False,
False,
[
    ['Aliens:? Phalanx']
],
'Aliens: Phalanx',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v4rnk4/respect_the_demons_aliens_phalanx/

########################################

id = get_rt_id(cur, 'Respect The Eternity Devil (Chainsaw Man)', 'https://redd.it/v5163x')
add_data(['Eternity Devil'],
'Eternity Devil',
False,
True,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5163x/respect_the_eternity_devil_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Dagon (Godzilla: Lord of the Galaxy)', 'https://redd.it/v53zmz')
add_data(['Dagon'],
'Dagon',
False,
False,
[
    ['Godzilla:? Lord of the Galaxy']
],
'Godzilla: Lord of the Galaxy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v53zmz/respect_dagon_godzilla_lord_of_the_galaxy/

########################################

id = get_rt_id(cur, 'Respect Ellen Ripley (Alien)', 'https://redd.it/v5drkt')
add_data(['Ellen Ripley'],
'Ellen Ripley',
False,
True,
[
    ['Aliens?']
],
'Alien',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5drkt/respect_ellen_ripley_alien/

########################################

id = get_rt_id(cur, 'Respect The Party (Die)', 'https://redd.it/v5hc1c')
add_data(['Dominic Ash'],
'Dominic Ash',
False,
False,
[
    ['DIE']
],
'DIE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5hc1c/respect_the_party_die/

add_data(['Angela Ash'],
'Angela Ash',
False,
False,
[
    ['DIE']
],
'DIE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5hc1c/respect_the_party_die/

add_data(['Matt'],
'Matt',
False,
False,
[
    ['Grief Knight']
],
'DIE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5hc1c/respect_the_party_die/

########################################

id = get_rt_id(cur, "Respect Quasimodo, the Hunchback of Notre Dame (Disney''s The Hunchback of Notre Dame)", 'https://redd.it/v5jofi')
add_data(['Quasimodo'],
'Quasimodo',
False,
True,
[
    ['Disney'], ['Hunchback of Notre Dame'], ['1996']
],
'The Hunchback of Notre Dame',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5jofi/respect_quasimodo_the_hunchback_of_notre_dame/

########################################

id = get_rt_id(cur, 'Respect Thunderbird (The Gifted)', 'https://redd.it/v5sfby')
add_data(['Thunderbird'],
'Thunderbird',
False,
False,
[
    ['Gifted']
],
'The Gifted',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v5sfby/respect_thunderbird_the_gifted/

########################################

id = get_rt_id(cur, 'Respect Thaal Sinestro! (DC Comics, Pre-Crisis)', 'https://redd.it/v6lb0l')
add_data(['Sinestro'],
'Sinestro',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v6lb0l/respect_thaal_sinestro_dc_comics_precrisis/

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

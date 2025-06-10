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

add_data(['Disney Princess'],
'Disney Princess',
True,
False,
[
    ['(which|every|strongest|most powerful) Disney Princess'], ['Disney Princess battle royale?']
],
'',
'{26057}'
)
#https://www.reddit.com/r/whowouldwin/comments/1knc2ac/which_disney_princess_has_the_strongest/

########################################

id = get_rt_id(cur, 'Respect the RED Engineer (Meet the Gunslinger)', 'https://redd.it/1l3zk6m')
add_data(['RED Engineer'],
'RED Engineer',
False,
False,
[
    ['Meet the Gunslinger']
],
'Meet the Gunslinger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l3zk6m/respect_the_red_engineer_meet_the_gunslinger/

########################################

id = get_rt_id(cur, 'Respect Zhou Yu (Fate/Samurai Remnant)', 'https://redd.it/1l3zns0')
add_data(['Zhou Yu'],
'Zhou Yu',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l3zns0/respect_zhou_yu_fatesamurai_remnant/

########################################

id = get_rt_id(cur, 'Featuring Big D! (Hunter: the Parenting)', 'https://redd.it/1l3507o')
add_data(['Big D'],
'Big D',
False,
False,
[
    ['Hunter:? the Parenting']
],
'Hunter: the Parenting',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1l69p9o/scp001ex_and_big_d_vs_the_wod/mwn2t9x/?context=3

########################################

id = get_rt_id(cur, 'Respect Dreamer (DC Comics, Post-Flashpoint)', 'https://redd.it/1l4vmrs')
add_data(['Dreamer'],
'Dreamer',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Nia Nal'],
'Nia Nal',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#


########################################

add_data(['Nia Nal'],
'Nia Nal',
False,
False,
[
    ['(Fl)?arrow(-| )?verse']
],
'CW Arrowverse',
'{}'
)
#

add_data(['Dreamer'],
'Dreamer',
False,
False,
[
    ['(Fl)?arrow(-| )?verse']
],
'CW Arrowverse',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Superman! (DC Comics, Absolute Universe)', 'https://redd.it/1l6l3fz')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Absolute Universe']
],
'Absolute Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l6l3fz/respect_superman_dc_comics_absolute_universe/

########################################

id = get_rt_id(cur, 'Respect: Ultimate Beetle (Marvel, 1610)', 'https://redd.it/1l7juav')
add_data(['Ultimate Beetle'],
'Ultimate Beetle',
False,
False,
[
    ['1610']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l7juav/respect_ultimate_beetle_marvel_1610/

########################################

id = get_rt_id(cur, 'Respect the Serverblight (Serverblight)', 'https://redd.it/1l775yi')
add_data(['Serverblight'],
'Serverblight',
False,
True,
[
    ['Serverblight series']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l775yi/respect_the_serverblight_serverblight/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla Found Footage)', 'https://redd.it/1l791tc')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Gryphon', 'Godzilla Found Footage']
],
'Godzilla Found Footage',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Predators (Predator Killer Of Killers)', 'https://redd.it/1l7ljfp')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Killer Of Killers']
],
'Predator: Killer Of Killers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l7ljfp/respect_the_predators_predator_killer_of_killers/

########################################

id = get_rt_id(cur, 'Respect Amaki Sena! (Blue Ursus)', 'https://redd.it/1l7m9xg')
add_data(['Amaki Sena'],
'Amaki Sena',
False,
False,
[
    ['Blue Ursus']
],
'Blue Ursus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l7m9xg/respect_amaki_sena_blue_ursus/

########################################

id = get_rt_id(cur, 'Respect Torosaurus (Dinosaur King)', 'https://redd.it/1l7pgqz')
add_data(['Torosaurus'],
'Torosaurus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l7pgqz/respect_torosaurus_dinosaur_king/

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

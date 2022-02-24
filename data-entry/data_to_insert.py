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

update_respectthread(cur, 1240, 'Respect Princess Diana (Wonder Woman 2009)', 'https://redd.it/t0ie85')

########################################

add_data(['Monkey King'],
'Monkey King',
False,
False,
[
    ['Journey to the West']
],
'Journey to the West',
'{6170}'
)
#https://www.reddit.com/r/whowouldwin/comments/t034o4/monkey_kingjourney_to_the_west_vs_voldermortharry/

########################################

id = get_rt_id(cur, 'Respect Revenant (Apex Legends)', 'https://redd.it/szafpw')
add_data(['Revenant'],
'Revenant',
False,
False,
[
    ['Apex']
],
'Apex Legends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/szafpw/respect_revenant_apex_legends/

########################################

id = get_rt_id(cur, 'Respect Cuphead and Mugman! (Cuphead)', 'https://redd.it/szg07v')
add_data(['Cup ?head'],
'Cuphead',
False,
True,
[
    ['Mug ?man']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/szg07v/respect_cuphead_and_mugman_cuphead/

########################################

id = get_rt_id(cur, 'Respect Roswaal Mathers (Re:Zero, Anime)', 'https://redd.it/szimjg')
add_data(['Roswaal'],
'Roswaal',
False,
True,
[
    ['Re:? ?Zero'], ['Mathers']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/szimjg/respect_roswaal_mathers_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Ultraman! (DC Pre-Crisis)', 'https://redd.it/szqf4g')
add_data(['Ultraman'],
'Ultraman',
False,
False,
[
    ['Ultraman.*Pre(-| )?Crisis|Pre(-| )?Crisis.*Ultraman']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/szqf4g/respect_ultraman_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Rhino (Spectacular Spider-Man)', 'https://redd.it/szx70d')
add_data(['Rhino'],
'Rhino',
False,
False,
[
    ['Spectacular Spider(-| )Man']
],
'Spectacular Spider-Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/szx70d/respect_rhino_spectacular_spiderman/

########################################

id = get_rt_id(cur, 'Respect Watatsuki no Yorihime (Touhou)', 'https://redd.it/t0d2th')
add_data(['Yorihime'],
'Yorihime',
False,
True,
[
    ['Watatsuki no Yorihime'], ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ho6alo/respect_watatsuki_no_toyohime_touhou/

########################################

id = get_rt_id(cur, 'Respect the Extremis Henchmen (Marvel Cinematic Universe)', 'https://redd.it/t0fl78')
add_data(['Extremis (Soldiers?|Henchmen)'],
'Extremis Soldiers',
False,
True,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t0fl78/respect_the_extremis_henchmen_marvel_cinematic/
#https://www.reddit.com/r/whowouldwin/comments/nqmcvd/someone_with_every_biological_enhancement_in_the/

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

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

update_respectthread(cur, 180, 'Respect Godzilla, The King of the Monsters (Godzilla, 1954)', 'https://redd.it/10o986s')
update_respectthread(cur, 22432, 'Respect Kamen Rider Ichigo (Kamen Rider)', 'https://redd.it/10ob9cq')
update_respectthread(cur, 1008, 'Respect The Justice League (Young Justice)', 'https://redd.it/10phypt')

########################################

add_data(['Cyclops'],
'Cyclops',
False,
False,
[
    ['Scott Summers'], ['X(-| )?Men']
],
'616',
'{2354}'
)
#https://www.reddit.com/r/whowouldwin/comments/10pijfy/name_a_character_that_cyclops_could_defeat_most/j6l4e2s/?context=3

########################################

add_data(['Willow'],
'Willow',
False,
False,
[
    ['Buffy|Vampire Slayer']
],
'Buffy the Vampire Slayer',
'{7490}'
)
#https://www.reddit.com/r/whowouldwin/comments/10qbf7w/willow_vs_charmed/j6ozxee/?context=3

########################################

id = get_rt_id(cur, 'Respect Suwako Moriya (Touhou)', 'https://redd.it/10o7qam')
add_data(['Suwako Moriya'],
'Suwako Moriya',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10o7qam/respect_suwako_moriya_touhou/

########################################

id = get_rt_id(cur, 'Respect Ogra (Gorgo)', 'https://redd.it/10o97ee')
add_data(['Ogra'],
'Ogra',
False,
False,
[
    ['Gorgo']
],
'Gorgo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10o97ee/respect_ogra_gorgo/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 52: the Hulkbuster Mark VI (Marvel, Earth-616)', 'https://redd.it/10onbnw')
add_data(['Hulk ?buster'],
'Hulkbuster',
False,
False,
[
    ['616'], ['Comics? Hulk ?buster'], ['Mark VI']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10onbnw/respect_iron_man_model_52_the_hulkbuster_mark_vi/

add_data(['Hulk ?buster'],
'Hulkbuster',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU'], ['Marvel Future Avengers'], ['Ultimates? Marvel'], ['Age of Ultron']
],
'MCU',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/10onbnw/respect_iron_man_model_52_the_hulkbuster_mark_vi/


########################################

id = get_rt_id(cur, 'Respect Tamara Blake, Iron Cat (Marvel, 616)', 'https://redd.it/10q0gfu')
add_data(['Iron Cat'],
'Iron Cat',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10q0gfu/respect_tamara_blake_iron_cat_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Zilla (Among Kaiju)', 'https://redd.it/10ov6ek')
add_data(['Zilla'],
'Zilla',
False,
False,
[
    ['Among Kaiju']
],
'Among Kaiju',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10ov6ek/respect_zilla_among_kaiju/

########################################

id = get_rt_id(cur, 'Respect Riki (Xenoblade Chronicles)', 'https://redd.it/10p45ol')
add_data(['Riki'],
'Riki',
False,
False,
[
    ['Xenoblade']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dunban (Xenoblade Chronicles)', 'https://redd.it/10pyrps')
add_data(['Dunban'],
'Dunban',
False,
False,
[
    ['Xenoblade']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10pyrps/respect_dunban_xenoblade_chronicles/

########################################

id = get_rt_id(cur, 'Respect Reyn (Xenoblade Chronicles)', 'https://redd.it/10p46ae')
add_data(['Reyn'],
'Reyn',
False,
False,
[
    ['Xenoblade'], ['Shulk']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10p46ae/respect_reyn_xenoblade_chronicles/

########################################

id = get_rt_id(cur, 'Respect Kamen Rider ZX (Birth of the 10th! Kamen Riders All Together!!)', 'https://redd.it/10p5qon')
add_data(['Kamen Rider ZX'],
'Kamen Rider ZX',
False,
True,
[
    ['Ryo Murasame']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10p5qon/respect_kamen_rider_zx_birth_of_the_10th_kamen/

########################################

id = get_rt_id(cur, 'Respect Akaboshi Bisco! (Sabikui Bisco)', 'https://redd.it/10plhdq')
add_data(['Bisco Akaboshi|Akaboshi Bisco'],
'Bisco Akaboshi',
False,
True,
[
    ['Ryo Murasame']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10plhdq/respect_akaboshi_bisco_sabikui_bisco/

########################################

id = get_rt_id(cur, 'Respect the Neutronic Monster Maker (The Adventures of Jimmy Neutron, Boy Genius)', 'https://redd.it/10q2u1c')
add_data(['Neutronic Monster Maker'],
'Neutronic Monster Maker',
False,
True,
[
    ['Jimmy Neutron']
],
'Jimmy Neutron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10q2u1c/respect_the_neutronic_monster_maker_the/

########################################

id = get_rt_id(cur, 'Respect Gix! (Magic: The Gathering)', 'https://redd.it/10q5fog')
add_data(['Gix'],
'Gix',
False,
False,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10q5fog/respect_gix_magic_the_gathering/

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

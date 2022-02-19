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

update_respectthread(cur, 6255, 'Respect Rin Tohsaka! (Fate)', 'https://redd.it/suw47k')
update_respectthread(cur, 21410, 'Respect Zeus (Percy Jackson and the Olympians/Heroes of Olympus)', 'https://redd.it/svs1st')

########################################

add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['TV S(how|eries)']
],
'DCEU',
'{20353}'
)
#https://www.reddit.com/r/whowouldwin/comments/sw4ctf/peacemaker_vs_daredevil/hxjyjfp/?context=3

########################################

add_data(['Infinity Stones'],
'Infinity Stones',
False,
True,
[
    ['616']
],
'616',
'{7484}'
)
#https://www.reddit.com/r/whowouldwin/comments/swd3u8/triforce_vs_infinity_stones/

########################################

id = get_rt_id(cur, "A look at Noctis Lucis Caelum''s combat profile", 'https://redd.it/8lxf6o')
add_data(['Noctis'],
'Noctis',
False,
False,
[
    ['Noctis Lucis Caelum'], ['Final Fantasy'], ['FF\d?\d?'], ['FF\w\w?\w?']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/suvekh/noctis_lucis_caelum_vs_akame_akame_ga_kill/hxc7qh6/?context=3

########################################

id = get_rt_id(cur, 'Respect Shilo Norman, Mister Miracle (DC Post-Flashpoint)', 'https://redd.it/suo3ty')
add_data(['Shilo Norman'],
'Shilo Norman',
False,
True,
[
    ['\(DC( Comics?)?\)']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/suo3ty/respect_shilo_norman_mister_miracle_dc/

add_data(['Shilo Norman'],
'Shilo Norman',
False,
False,
[
    ['(Post(-| ))?Flash(-| )?point']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/suo3ty/respect_shilo_norman_mister_miracle_dc/

########################################

id = get_rt_id(cur, 'Respect the Tiny clone of Superman he shoots out of a rainbow from his hands (DC Pre-Crisis)', 'https://redd.it/svku21')
add_data(['Tiny Super(-| )?man'],
'Tiny Superman',
False,
False,
[
    ['clone|rainbow'], ['Pre(-| )?Crisis'], ['Silver(-| )?Age'], ['Earth(-| )(1|One)']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/svku21/respect_the_tiny_clone_of_superman_he_shoots_out/

########################################

id = get_rt_id(cur, 'Respect Patrasche (Re:Zero, Anime)', 'https://redd.it/suqiyb')
add_data(['Patrasche'],
'Patrasche',
False,
True,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/suqiyb/respect_patrasche_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Sakura Matou! (Fate)', 'https://redd.it/sw28qx')
add_data(['Sakura Matou'],
'Sakura Matou',
False,
True
,
[
    ['Fate'], ['TYPE(-| )?MOON'], ['Nasu(-| )?verse']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sw28qx/respect_sakura_matou_fate/

########################################

id = get_rt_id(cur, 'Respect Kirima, the Graceful Mist (Avatar: The Kyoshi Novels)', 'https://redd.it/suxkqu')
add_data(['Kirima'],
'Kirima',
False,
False
,
[
    ['Avatar'], ['A?TLA'], ['Kyoshi'], ['Bend(er|ing)']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/suxkqu/respect_kirima_the_graceful_mist_avatar_the/

########################################

id = get_rt_id(cur, 'Respect Avatar Kuruk (Avatar: The Last Airbender)', 'https://redd.it/svz7sf')
add_data(['Kuruk'],
'Kuruk',
False,
False
,
[
    ['Avatar'], ['A?TLA'], ['Bend(er|ing)']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/svz7sf/respect_avatar_kuruk_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'Respect Mystique (FOX X-Men)', 'https://redd.it/swccdb')
add_data(['Mystique'],
'Mystique',
False,
False
,
[
    ['Fox(verse)?'], ['X(-| )?Men (Movie|Film)s?'], ['X-?Men Cinematic Universe'], ['XCU']
],
'FOX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/swccdb/respect_mystique_fox_xmen/

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

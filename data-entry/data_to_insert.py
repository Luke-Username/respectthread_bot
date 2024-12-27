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

update_respectthread(cur, 788, 'Respect Breach (Generator Rex)', 'https://redd.it/1hma6iu')

########################################

add_data(['Gojo'],
'Gojo',
False,
False,
[
    ['Hollow Purple']
],
'Jujutsu Kaisen',
'{14809}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hlwd7u/how_far_does_gojo_get_in_the_bleach_gauntlet/m3xhepz/?context=3

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['Zatanna', 'Jean']
],
'616',
'{1997}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hncjh4/how_would_fans_rank_these_fictional_women_based/

add_data(['Jean'],
'Jean',
False,
False,
[
    ['Zatanna', 'Wanda']
],
'616',
'{2368}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hncjh4/how_would_fans_rank_these_fictional_women_based/


########################################

add_data(['Atreides'],
'Atreides',
False,
False,
[
    ['Fremen'], ['Dune']
],
'Dune',
'{6144}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hm4geb/fremen_and_atreides_had_access_to_toyota_hilux/

########################################

add_data(['Fuuko'],
'Fuuko',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{22336}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hmpr01/fuuko_undead_unluck_vs_qrow_rwby/

########################################


id = get_rt_id(cur, 'Respect Andros, the Red Space Ranger (Power Rangers in Space)', 'https://redd.it/1hlq3in')
add_data(['Andros'],
'Andros',
False,
False,
[
    ['(Power|Space) ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Red Space Ranger'],
'Red Space Ranger',
False,
True,
[
    ['(Power|Space) ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#


########################################


id = get_rt_id(cur, 'Respect Gomi Bako Grumer (Bakuage Sentai BoonBoomger)', 'https://redd.it/1hm0a2s')
add_data(['Gomi Bako Grumer'],
'Gomi Bako Grumer',
False,
False,
[
    ['Bakuage Sentai BoonBoomger']
],
'Bakuage Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hm0a2s/respect_gomi_bako_grumer_bakuage_sentai/

########################################

id = get_rt_id(cur, 'Respect the Phantom Ranger (Power Rangers)', 'https://redd.it/1hm5yd0')
add_data(['Phantom Ranger'],
'Phantom Ranger',
False,
False,
[
    ['Power ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Phantom Rangers'],
'Phantom Rangers',
False,
False,
[
    ['Power ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hm5yd0/respect_the_phantom_ranger_power_rangers/

########################################

id = get_rt_id(cur, 'Respect the Astro Megazord (Power Rangers In Space)', 'https://redd.it/1hn1vw6')
add_data(['Astro Megazord'],
'Astro Megazord',
False,
True,
[
    ['Power ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hn1vw6/respect_the_astro_megazord_power_rangers_in_space/

########################################

id = get_rt_id(cur, 'Respect the Mega Voyager (Power Rangers In Space)', 'https://redd.it/1hn1vx2')
add_data(['Mega Voyager'],
'Mega Voyager',
False,
True,
[
    ['Power ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hn1vx2/respect_the_mega_voyager_power_rangers_in_space/

########################################

id = get_rt_id(cur, 'Respect The Kong of the Planet of the Apes (Kong on the Planet of the Apes)', 'https://redd.it/1hmqx52')
add_data(['Kong'],
'Kong',
False,
False,
[
    ['Kong on the Planet of the Apes']
],
'Kong on the Planet of the Apes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hmqx52/respect_the_kong_of_the_planet_of_the_apes_kong/

########################################

id = get_rt_id(cur, 'Respect Ultimate Dazzler (Marvel, Earth-1610)', 'https://redd.it/1hn0xh3')
add_data(['Dazzler'],
'Dazzler',
False,
False,
[
    ['Ultimates? Dazzler']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hn0xh3/respect_ultimate_dazzler_marvel_earth1610/

########################################

id = get_rt_id(cur, 'Respect Superman (The Dark Knight Returns Animated)', 'https://redd.it/1hn8xzq')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Dark Knight Returns Animated']
],
'The Dark Knight Returns Animated',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hn8xzq/respect_superman_the_dark_knight_returns_animated/

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

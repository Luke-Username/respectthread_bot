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

update_respectthread(cur, 2382, 'Respect Rogue (Marvel, 616)', 'https://redd.it/ukfh1s')

########################################

add_data(['Homelander'],
'Homelander',
False,
False,
[
    ['show']
],
'The Boys, 2019',
'{13117}'
)
#https://www.reddit.com/r/whowouldwin/comments/ukp77u/to_prove_a_point_mcu_hulk_vs_homelander/i7qi1pn/?context=3

########################################

add_data(['Tanjiro'],
'Tanjiro',
False,
False,
[
    ['Demon ?Slayer'], ['Kimetsu no Yaiba'], ['KnY']
],
'Demon Slayer',
'{4828}'
)
#https://www.reddit.com/r/whowouldwin/comments/uk2xr1/spiderman_616_vs_demon_slayer_heroes/i7mogm3/?context=3

########################################

id = get_rt_id(cur, 'Respect Raihan! (Pokemon Anime)', 'https://redd.it/uk9ncz')
add_data(['Raihan'],
'Raihan',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uk9ncz/respect_raihan_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Elrik Vonreg! (Star Wars Canon)', 'https://redd.it/ukapkq')
add_data(['Elrik Vonreg'],
'Elrik Vonreg',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukapkq/respect_elrik_vonreg_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect the Marked Ninja (Mark of the Ninja)', 'https://redd.it/ukax6v')
add_data(['Ninja'],
'Ninja',
False,
False,
[
    ['Mark of the Ninja']
],
'Mark of the Ninja',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukax6v/respect_the_marked_ninja_mark_of_the_ninja/

########################################

id = get_rt_id(cur, 'Respect Volstagg, The War Thor (Marvel, Earth-616)', 'https://redd.it/ukh5zz')
add_data(['Volstagg'],
'Volstagg',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukh5zz/respect_volstagg_the_war_thor_marvel_earth616/

add_data(['Volstagg'],
'Volstagg',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/ukh5zz/respect_volstagg_the_war_thor_marvel_earth616/


########################################

id = get_rt_id(cur, "Respect \"Noland''s\" Articuno (Pokemon Anime)", 'https://redd.it/ukj3hh')
add_data(['Articuno'],
'Articuno',
False,
False,
[
    ['Nolands?']
],
'Noland',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukj3hh/respect_nolands_articuno_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Lara Croft, the Tomb Raider! (Top Cow Comics, Composite)', 'https://redd.it/ukk5lo')
add_data(['Lara Croft'],
'Lara Croft',
False,
False,
[
    ['Top Cow']
],
'Top Cow',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukk5lo/respect_lara_croft_the_tomb_raider_top_cow_comics/

########################################

id = get_rt_id(cur, 'Respect Miles "Tails" Prower (Sonic the Hedgehog (Paramount Movies))', 'https://redd.it/uklxbw')
add_data(['Tails'],
'Tails',
False,
False,
[
    ['Sonic', '202(0|2)'], ['Sonic Movies?'], ['Sonic', 'Paramount']
],
'Sonic the Hedgehog, Paramount',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uklxbw/respect_miles_tails_prower_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Knuckles the Echidna! (Sonic the Hedgehog (Paramount Movies))', 'https://redd.it/ukm2bi')
add_data(['Knuckles'],
'Knuckles',
False,
False,
[
    ['Sonic', '202(0|2)'], ['Sonic Movies?'], ['Sonic', 'Paramount']
],
'Sonic the Hedgehog, Paramount',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukm2bi/respect_knuckles_the_echidna_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect Machete Cortez (Machete)', 'https://redd.it/ukop8w')
add_data(['Machete Cortez'],
'Machete Cortez',
False,
False,
[
    ['\(Machete\)']
],
'Machete',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ukop8w/respect_machete_cortez_machete/

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

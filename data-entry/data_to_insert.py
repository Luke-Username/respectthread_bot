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

update_respectthread(cur, 5653, 'Respect 2B (Nier: Automata)', 'https://redd.it/z1k28f')
update_respectthread(cur, 6029, 'Respect: Magnus the Red (Warhammer 40k)', 'https://redd.it/z1r7ra')
update_respectthread(cur, 8598, 'Respect Bor Burison, The Father of The All-Father (Marvel, 616)', 'https://redd.it/z1ydyk')

########################################

add_data(['Heroe?s? Association'],
'Hero Association',
False,
False,
[
    ['My Hero Academia'], ['\(My Hero\)'], ['(M|BN?)HA'], ['Boku no Hero']
],
'My Hero Academia',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/z143b6/madara_naruto_shippuden_vs_hero_association_mha/ix8tkss/?context=3

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['God of War Thor']
],
'God of War',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/z1xwui/thor_replaces_kratos_which_god_can_stop_him/ixgbjfc/?context=3

add_data(['Thor'],
'Thor',
False,
False,
[
    ['God of War', 'Pantheons?']
],
'God of War',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/z2myy3/god_of_war_war_of_the_pantheons/ixh364y/?context=3

########################################

add_data(['Nemesis'],
'Nemesis',
False,
False,
[
    ['Nemesis ?\(RE']
],
'Resident Evil',
'{5373}'
)
#https://www.reddit.com/r/whowouldwin/comments/z28x8t/nemisis_re_vs_bruce_wayne_arkham/ixf4tbb/?context=3

########################################

id = get_rt_id(cur, 'Respect Cynthia (Pokemon Anime)', 'https://redd.it/z0zplp')
add_data(['Cynthia'],
'Cynthia',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z0zplp/respect_cynthia_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Kendra Sorenson! (Fablehaven)', 'https://redd.it/z19ia5')
add_data(['Kendra Sorenson'],
'Kendra Sorenson',
False,
True,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z19ia5/respect_kendra_sorenson_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Jack "The Ripper" Hanma (Grappler Baki)', 'https://redd.it/z1daxc')
add_data(['Jack Hanma'],
'Jack Hanma',
False,
True,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1daxc/respect_jack_the_ripper_hanma_grappler_baki/

add_data(['Jack'],
'Jack',
False,
False,
[
    ['Hanma (Family|Bloodline)'], ['Jack ?\(Baki']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1daxc/respect_jack_the_ripper_hanma_grappler_baki/

########################################

id = get_rt_id(cur, 'Respect Mr. T (Anki Deck #1635663511)', 'https://redd.it/z1ppe2')
add_data(['Mr\.? T'],
'Mr. T',
False,
False,
[
    ['Anki Deck']
],
'Anki Deck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1ppe2/respect_mr_t_anki_deck_1635663511/

########################################

id = get_rt_id(cur, 'Respect Sega Shiro! (Go Sega 60th anniversary adverts)', 'https://redd.it/z1s00o')
add_data(['Sega Shiro'],
'Sega Shiro',
False,
True,
[
    ['advert(isement)s?']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1s00o/respect_sega_shiro_go_sega_60th_anniversary/

########################################

id = get_rt_id(cur, 'Respect Zala / Miss Doublefinger (One Piece)', 'https://redd.it/z1xkv9')
add_data(['M(is)?s\.? Doublefinger'],
'Miss Doublefinger',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1xkv9/respect_zala_miss_doublefinger_one_piece/

add_data(['Zala'],
'Zala',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1xkv9/respect_zala_miss_doublefinger_one_piece/

########################################

id = get_rt_id(cur, 'Respect Odin! (Fate)', 'https://redd.it/z1zw00')
add_data(['Odin'],
'Odin',
False,
False,
[
    ['Odin ?\(Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z1zw00/respect_odin_fate/

########################################

id = get_rt_id(cur, "Respect William! (The Inquisitor''s Tale: Or, The Three Magical Children and Their Holy Dog)", 'https://redd.it/z292x1')
add_data(['William'],
'William',
False,
False,
[
    ["Inquisitor\'\'?s Tale"]
],
"The Inquisitor''s Tale",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Crane (The Sting of Death)', 'https://redd.it/z29geo')
add_data(['Crane'],
'Crane',
False,
False,
[
    ['Sting of Death']
],
'The Sting of Death',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z29geo/respect_crane_the_sting_of_death/

########################################

id = get_rt_id(cur, 'Respect Rogu (American Dad!)', 'https://redd.it/z2plym')
add_data(['Rogu'],
'Rogu',
False,
False,
[
    ['American Dad']
],
'American Dad!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z2plym/respect_rogu_american_dad/

########################################

id = get_rt_id(cur, 'Respect Riful of the West and Dauf (Claymore)', 'https://redd.it/z33l41')
add_data(['Riful'],
'Riful',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z33l41/respect_riful_of_the_west_and_dauf_claymore/

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

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

update_respectthread(cur, 3306, 'Respect Piccolo (Dragon Ball [Manga])', 'https://redd.it/1dkpsye')
update_respectthread(cur, 293, 'Respect Team Evil! (Shaolin Soccer)', 'https://redd.it/1dlajov')
update_respectthread(cur, 13090, 'Respect Porky Minch (Mother Series)', 'https://redd.it/1dngz6i')
update_respectthread(cur, 2415, 'Respect Kenuichio Harada the Silver Samurai! (Marvel 616)', 'https://redd.it/1dn96gl')

########################################

add_data(['Garou'],
'Garou',
False,
False,
[
    ['World of Darkness']
],
'World of Darkness',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1dm39fu/average_spacemarine_vs_average_garou_warhammer/l9uhxoc/?context=3

########################################

id = get_rt_id(cur, 'Respect Almond! (Cucumber Quest)', 'https://redd.it/1dj8uto')
add_data(['Almond'],
'Almond',
False,
False,
[
    ['Cucumber Quest']
],
'Cucumber Quest',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dj8uto/respect_almond_cucumber_quest/

########################################

id = get_rt_id(cur, "Respect Misty''s Togepi (Pokemon Anime)", 'https://redd.it/1djlcuy')
add_data(['Togepi'],
'Togepi',
False,
True,
[
    ['Pok(e|é)m(o|a)n'], ['Misty']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1djlcuy/respect_mistys_togepi_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect Brock''s Steelix (Pokemon Anime)", 'https://redd.it/1dluuwu')
add_data(['Steelix'],
'Steelix',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dluuwu/respect_brocks_steelix_pokemon_anime/

add_data(['Onix'],
'Onix',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dluuwu/respect_brocks_steelix_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect Misty''s Politoed (Pokemon Anime)", 'https://redd.it/1dkbrh7')
add_data(['Politoed'],
'Politoed',
False,
True,
[
    ['Pok(e|é)m(o|a)n'], ['Misty']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Poliwhirl'],
'Poliwhirl',
False,
True,
[
    ['Pok(e|é)m(o|a)n'], ['Misty']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dkbrh7/respect_mistys_politoed_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Misty (Pokemon Anime)', 'https://redd.it/1dmnaxv')
add_data(['Misty'],
'Misty',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dmnaxv/respect_misty_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Swarm (Moonfall)', 'https://redd.it/1djqu2a')
add_data(['Swarm'],
'Swarm',
False,
False,
[
    ['Moonfall']
],
'Moonfall',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1djqu2a/respect_the_swarm_moonfall/

########################################

id = get_rt_id(cur, 'Respect the Moon! (Moonfall)', 'https://redd.it/1djqudj')
add_data(['Moon'],
'Moon',
False,
False,
[
    ['Moonfall']
],
'Moonfall',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1djqu2a/respect_the_swarm_moonfall/

########################################

id = get_rt_id(cur, 'Respect Merlin the Magician (Arthurian Mythology)', 'https://redd.it/1dkrd0i')
add_data(['Merlin'],
'Merlin',
False,
True,
[
    ['Arthurian'], ['King Arthur']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dkrd0i/respect_merlin_the_magician_arthurian_mythology/

add_data(['Merlin'],
'Merlin',
False,
False,
[
    ['\(Fate( Series)?\)']
],
'Fate',
'{14407}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tariq Isbili, the Grey Pilgrim (A Practical Guide to Evil)', 'https://redd.it/1dkxuud')
add_data(['Tariq Isbili'],
'Tariq Isbili',
False,
True,
[
    ['Practical Guide to Evil']
],
'A Practical Guide to Evil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dkxuud/respect_tariq_isbili_the_grey_pilgrim_a_practical/

########################################

id = get_rt_id(cur, "Respect Ryo Saeba! (Netflix''s City Hunter)", 'https://redd.it/1dl8eyu')
add_data(['Ryo Saeba'],
'Ryo Saeba',
False,
False,
[
    ['Netflix']
],
"Netflix''s City Hunter",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dl8eyu/respect_ryo_saeba_netflixs_city_hunter/


########################################

id = get_rt_id(cur, '[NSFW] Respect Bellezza! (Monster Wrestling: Interspecies Combat Girls)', 'https://redd.it/1dlmawb')
add_data(['Bellezza'],
'Bellezza',
True,
False,
[
    ['Monster Wrestling']
],
'Monster Wrestling: Interspecies Combat Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dlmawb/nsfw_respect_bellezza_monster_wrestling/

########################################

id = get_rt_id(cur, "Respect Blaze the Cat! (Archie''s Sonic the Hedgehog)", 'https://redd.it/1dln7k1')
add_data(['Blaze the Cat'],
'Blaze the Cat',
False,
False,
[
    ['Archie']
],
'Archie Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dln7k1/respect_blaze_the_cat_archies_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, 'Respect The Midnighter (DC, Post-Flashpoint)', 'https://redd.it/1dm9nbl')
add_data(['Midnighter'],
'Midnighter',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dm9nbl/respect_the_midnighter_dc_postflashpoint/

add_data(['Midnighter'],
'Midnighter',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dm9nbl/respect_the_midnighter_dc_postflashpoint/

add_data(['Midnighter'],
'Midnighter',
False,
False,
[
    ['Wildstorm']
],
'Wildstorm',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dm9nbl/respect_the_midnighter_dc_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect Daryl the Wendigo (B.P.R.D.)', 'https://redd.it/1dma5im')
add_data(['Daryl the Wendigo'],
'Daryl the Wendigo',
False,
True,
[
    ['B\.?P\.?R\.?D']
],
'B.P.R.D.',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dma5im/respect_daryl_the_wendigo_bprd/

add_data(['Daryl Tynon'],
'Daryl Tynon',
False,
False,
[
    ['B\.?P\.?R\.?D']
],
'B.P.R.D.',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dma5im/respect_daryl_the_wendigo_bprd/

########################################

id = get_rt_id(cur, 'Respect Genichi Sojo (Kagurabachi)', 'https://redd.it/1dnfzn1')
add_data(['Genichi Sojo'],
'Genichi Sojo',
False,
True,
[
    ['Kagurabachi']
],
'Kagurabachi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dnfzn1/respect_genichi_sojo_kagurabachi/

########################################

id = get_rt_id(cur, 'Respect Salsa (Mother 3)', 'https://redd.it/1dngp30')
add_data(['Salsa'],
'Salsa',
False,
False,
[
    ['Mother 3']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dngp30/respect_salsa_mother_3/

########################################

id = get_rt_id(cur, 'Respect Fassad (Mother 3)', 'https://redd.it/1dngrux')
add_data(['Fassad'],
'Fassad',
False,
False,
[
    ['Mother 3']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Masked Man (Mother 3)', 'https://redd.it/1dngsvx')
add_data(['Masked Man'],
'Masked Man',
False,
False,
[
    ['Mother 3']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Flint (Mother 3)', 'https://redd.it/1dnh39m')
add_data(['Flint'],
'Flint',
False,
False,
[
    ['Mother 3']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dnh39m/respect_flint_mother_3/

########################################

add_data(['Porky'],
'Porky',
False,
False,
[
    ['Porky Minch'], ['Mother']
],
'EarthBound',
'{13090}'
)
#


########################################

id = get_rt_id(cur, 'Respect Lucas, Kumatora, Duster, and Boney (Mother 3)', 'https://redd.it/1dnguqy')
add_data(['Duster'],
'Duster',
False,
False,
[
    ['Mother 3'], ['Earth(-| )?bound']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Boney'],
'Boney',
False,
False,
[
    ['Mother 3'], ['Earth(-| )?bound']
],
'EarthBound',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dnguqy/respect_lucas_kumatora_duster_and_boney_mother_3/

########################################

id = get_rt_id(cur, 'Respect Rikki Barnes (Marvel 616, Heroes Reborn)', 'https://redd.it/1dklf83')
add_data(['Rikki Barnes'],
'Rikki Barnes',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dklf83/respect_rikki_barnes_marvel_616_heroes_reborn/

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

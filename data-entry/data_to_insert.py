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

update_respectthread(cur, 13542, 'Respect Merasmus (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1p2isg3/respect_merasmus_team_fortress_2/')
update_respectthread(cur, 8111, 'Respect Darkseid (DC Animated Universe)', 'https://www.reddit.com/r/respectthreads/comments/1p4zvkg/respect_darkseid_dc_animated_universe/')
update_respectthread(cur, 4187, 'Respect Dawn (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/728jj0/respect_dawn_pokemon_anime/')

########################################

id = get_rt_id(cur, 'Respect Thundercracker (Transformers, IDW Comics [2005])', 'https://www.reddit.com/r/respectthreads/comments/1p2cb0l/respect_thundercracker_transformers_idw_comics/')
add_data(['Thundercracker'],
'Thundercracker',
False,
False,
[
    ['IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lancelot (Night at The Museum)', 'https://www.reddit.com/r/respectthreads/comments/1p2jp7l/respect_lancelot_night_at_the_museum/')
add_data(['Lancelot'],
'Lancelot',
False,
False,
[
    ['Night at The Museum']
],
'Night at The Museum',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Duncan the Tall! (A Song Of Ice And Fire)', 'https://www.reddit.com/r/respectthreads/comments/1p3azsv/respect_duncan_the_tall_a_song_of_ice_and_fire/')
add_data(['Duncan the Tall'],
'Duncan the Tall',
False,
True,
[
    ['Song Of Ice']
],
'A Song Of Ice And Fire',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Dawn''s Piplup (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1p4rd8e/respect_dawns_piplup_pokemon_anime/')
add_data(['Piplup'],
'Piplup',
False,
False,
[
    ['Dawn']
],
'Dawn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/6ra7ff/respect_piplup_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Lana Lang, Superwoman (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1p4yd6p/respect_lana_lang_superwoman_dc_comics/')
add_data(['Lana Lang'],
'Lana Lang',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lana Lang'],
'Lana Lang',
False,
True,
[
    ['DC Comics?']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Nox Eternis A.K.A The Shadow Plague (Plague Inc.)', 'https://www.reddit.com/r/respectthreads/comments/1p1pux0/respect_the_nox_eternis_aka_the_shadow_plague/')
add_data(['Nox Eternis'],
'Nox Eternis',
False,
True,
[
    ['Plague Inc']
],
'Plague Inc.',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Shadow Plague'],
'Shadow Plague',
False,
False,
[
    ['Plague Inc']
],
'Plague Inc.',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Aaron Tide (The Boxer)', 'https://www.reddit.com/r/respectthreads/comments/1p591yv/respect_aaron_tide_the_boxer/')
add_data(['Aaron Tide'],
'Aaron Tide',
False,
True,
[
    ['Boxer']
],
'The Boxer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yu (The Boxer)', 'https://www.reddit.com/r/respectthreads/comments/1p59ujx/respect_yu_the_boxer/')
add_data(['Yu'],
'Yu',
False,
False,
[
    ['Yu.*The Boxer'], ['Aaron Tide']
],
'The Boxer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Felix (Armor)', 'https://www.reddit.com/r/respectthreads/comments/1p5a33o/respect_felix_armor/')
add_data(['Felix'],
'Felix',
False,
False,
[
    ['Felix ?\(Armor\)']
],
'Armor',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Victor Crowley (Hatchet comics)', 'https://www.reddit.com/r/respectthreads/comments/1p5ior6/respect_victor_crowley_hatchet_comics/')
add_data(['Victor Crowley'],
'Victor Crowley',
False,
False,
[
    ['Hatchet', 'comics']
],
'Hatchet comics',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Wonder Woman (The New Adventures of Wonder Woman)', 'https://www.reddit.com/r/respectthreads/comments/1p5pad6/respect_wonder_woman_the_new_adventures_of_wonder/')
add_data(['Wonder ?Woman'],
'Wonder Woman',
False,
False,
[
    ['New Adventures of Wonder Woman']
],
'The New Adventures of Wonder Woman',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Buffy Summers! (Buffy the Vampire Slayer: The Animated Series)', 'https://www.reddit.com/r/respectthreads/comments/1p60kyi/respect_buffy_summers_buffy_the_vampire_slayer/')
add_data(['Buffy Summers'],
'Buffy Summers',
False,
False,
[
    ['Buffy the Vampire Slayer.*Animated Series']
],
'Buffy the Vampire Slayer: The Animated Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect James''s Carnivine (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1p78hvv/respect_jamess_carnivine_pokemon_anime/')
add_data(['Carnivine'],
'Carnivine',
False,
False,
[
    ['James']
],
'James',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Karre and Am (Star Wars: Visions - The Twins)', 'https://www.reddit.com/r/respectthreads/comments/1p6majq/respect_karre_and_am_star_wars_visions_the_twins/')
add_data(['Karre'],
'Karre',
False,
False,
[
    ['Star Wars', 'Visions']
],
'Star Wars: Visions',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Am'],
'Am',
False,
False,
[
    ['Star Wars', 'Visions|Karre']
],
'Star Wars: Visions',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/q5hnzz/who_is_the_strongest_star_wars_character_am/

########################################

id = get_rt_id(cur, 'Respect the Master of Puppets (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1p6sc8c/respect_the_master_of_puppets_fortnite/')
add_data(['Master of Puppets'],
'Master of Puppets',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Metallica! (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1p6sc92/respect_metallica_fortnite/')
add_data(['Metallica'],
'Metallica',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Red Duke! (Warhammer Fantasy)', 'https://www.reddit.com/r/respectthreads/comments/1p72fy4/respect_the_red_duke_warhammer_fantasy/')
add_data(['Red Duke'],
'Red Duke',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#

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

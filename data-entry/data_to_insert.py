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

update_respectthread(cur, 2018, 'Respect Ultron (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1pdxvz0/respect_ultron_marvel_comics_616/')

########################################

id = get_rt_id(cur, 'Respect Ben Grimm, the Thing (Marvel Comics, 616)', 'https://www.reddit.com/r/rangernumberx/comments/1f0a4p8/respect_ben_grimm_the_thing_marvel_comics_616/')
add_data(['The Thing'],
'The Thing',
False,
False,
[
    ['Marvel', 'Luke Cage'], ['Marvel Bricks?']
],
'616',
'{' + '{}, 2072,22166'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pd6m5g/vulkan_runs_a_marvel_brick_gauntlet_where_does_he/ns2rsvc/?context=3

add_data(['D-Man'],
'D-Man',
False,
False,
[
    ['Marvel', 'Luke Cage'], ['Marvel Bricks?']
],
'616',
'{2438}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pd6m5g/vulkan_runs_a_marvel_brick_gauntlet_where_does_he/ns2rsvc/?context=3

########################################

id = get_rt_id(cur, 'Respect the Ultron Drones (Marvel Comics, Earth-61112)', 'https://www.reddit.com/r/respectthreads/comments/1pdxvzh/respect_the_ultron_drones_marvel_comics_earth61112/')
add_data(['Ultron Drones'],
'Ultron Drones',
False,
False,
[
    ['61112']
],
'61112',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Zoey''s Glameow (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1pd4ytj/respect_zoeys_glameow_pokemon_anime/')
add_data(['Glameow'],
'Glameow',
False,
False,
[
    ['Zoey']
],
'Zoey',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zoey (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1pd4zbf/respect_zoey_pokemon_anime/')
add_data(['Zoey'],
'Zoey',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Multiversal Masters of Evil (Marvel Comics)', 'https://www.reddit.com/r/respectthreads/comments/1pd5ps8/respect_the_multiversal_masters_of_evil_marvel/')
add_data(['Masters of Evil'],
'Masters of Evil',
True,
False,
[
    ['Multivers(e|al)']
],
'Multiverse',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Multiversal Masters of Evil'],
'Multiversal Masters of Evil',
True,
True,
[
    ['Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://marvel.fandom.com/wiki/Masters_of_Evil_(Multiverse)

########################################

id = get_rt_id(cur, 'Respect the Bounty Hunter (High On Life)', 'https://www.reddit.com/r/respectthreads/comments/1pd5psk/respect_the_bounty_hunter_high_on_life/')
add_data(['Bounty Hunter'],
'Bounty Hunter',
False,
False,
[
    ['High On Life']
],
'High On Life',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Scavengers (Transformers IDW, 2005)', 'https://www.reddit.com/r/respectthreads/comments/1pd5pu4/respect_the_scavengers_transformers_idw_2005/')
add_data(['Scavengers'],
'Scavengers',
True,
False,
[
    ['Transformers', 'IDW']
],
'Transformers IDW',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Leslie(The Amazing World Of Gumball)', 'https://www.reddit.com/r/respectthreads/comments/1pdmzzg/respect_lesliethe_amazing_world_of_gumball/')
add_data(['Leslie'],
'Leslie',
False,
False,
[
    ['Gumball']
],
'The Amazing World Of Gumball',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mark Twelve (Marvel Comics, Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/1pdxw0l/respect_mark_twelve_marvel_comics_earth616/')
add_data(['Mark Twelve'],
'Mark Twelve',
False,
False,
[
    ['616'], ['Ultron']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kris Kalenov (The Winter Men)', 'https://www.reddit.com/r/respectthreads/comments/1pe223u/respect_kris_kalenov_the_winter_men/')
add_data(['Kris Kalenov'],
'Kris Kalenov',
False,
False,
[
    ['Winter Men']
],
'The Winter Men',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Hammer of the Revolution (The Winter Men)', 'https://www.reddit.com/r/respectthreads/comments/1pe24fp/respect_the_hammer_of_the_revolution_the_winter/')
add_data(['Hammer of the Revolution'],
'Hammer of the Revolution',
False,
False,
[
    ['Winter Men']
],
'The Winter Men',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect The 4''8 Heavy (Meet the 4''8 Heavy)", 'https://www.reddit.com/r/respectthreads/comments/1pehogd/respect_the_48_heavy_meet_the_48_heavy/')
add_data(["4''8 Heavy"],
"4''8 Heavy",
False,
False,
[
    ["The 4''8 Heavy"]
],
"Meet the 4''8 Heavy",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Isaac Lightbrad (LostMagic)', 'https://www.reddit.com/r/respectthreads/comments/1petnsj/respect_isaac_lightbrad_lostmagic/')
add_data(['Isaac Lightbrad'],
'Isaac Lightbrad',
False,
True,
[
    ['Lost ?Magic']
],
'LostMagic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Helena Kyle (Birds of Prey)', 'https://www.reddit.com/r/respectthreads/comments/1peto9g/respect_helena_kyle_birds_of_prey/')
add_data(['Helena Kyle'],
'Helena Kyle',
False,
False,
[
    ['Birds of Prey']
],
'Birds of Prey',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Harley Quinn (Birds of Prey)', 'https://www.reddit.com/r/respectthreads/comments/1petohq/respect_harley_quinn_birds_of_prey/')
add_data(['Harley Quinn?'],
'Harley Quinn',
False,
False,
[
    ['Birds of Prey']
],
'Birds of Prey',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lily (V/H/S/, Siren)', 'https://www.reddit.com/r/respectthreads/comments/1pewi75/respect_lily_vhs_siren/')
add_data(['Lily'],
'Lily',
False,
False,
[
    ['V/H/S/', 'Siren']
],
'V/H/S/',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Forrest''s Rhyperior (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1pez3c9/respect_forrests_rhyperior_pokemon_anime/')
add_data(['Rhyperior'],
'Rhyperior',
False,
False,
[
    ['Forrest']
],
'Forrest',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Team Rocket''s Sinnoh League Mecha (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1pez43p/respect_team_rockets_sinnoh_league_mecha_pokemon/')
add_data(['Sinnoh League Mecha'],
'Sinnoh League Mecha',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
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

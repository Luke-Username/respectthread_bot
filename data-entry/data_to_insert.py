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

update_respectthread(cur, 5473, 'Respect The Demoman (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1pbd37h/respect_the_demoman_team_fortress_2/')
update_respectthread(cur, 5481, 'Respect the Sniper (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1pbdjcm/respect_the_sniper_team_fortress_2/')
update_respectthread(cur, 211, 'Respect SpaceGodzilla (Godzilla Franchise, Heisei Continuity)', 'https://www.reddit.com/r/respectthreads/comments/1pbebj7/respect_spacegodzilla_godzilla_franchise_heisei/')
update_respectthread(cur, 1252, "Respect Alucard! (Netflix''s Castlevania)", 'https://www.reddit.com/r/respectthreads/comments/1pcm808/respect_alucard_netflixs_castlevania/')

########################################

add_data(['Saint Seiya'],
'Saint Seiya',
False,
False,
[
    ['Hades Chapter'], ['God Cloth']
],
'Saint Seiya',
'{4493}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pcnu4c/goku_ssj_blue_kaioken_x20_seiya_god_cloth_luffy/nrz1axg/?context=3

########################################

id = get_rt_id(cur, 'Respect the Looper! (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1pba8cr/respect_the_looper_fortnite/')
add_data(['Looper'],
'Looper',
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

id = get_rt_id(cur, 'Respect Golden Bat (Golden Bat, 1966)', 'https://www.reddit.com/r/respectthreads/comments/1pbc508/respect_golden_bat_golden_bat_1966/')
add_data(['Looper'],
'Looper',
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

id = get_rt_id(cur, 'Respect Golden Bat (Golden Bat, 1966)', 'https://www.reddit.com/r/respectthreads/comments/1pbc508/respect_golden_bat_golden_bat_1966/')
add_data(['Golden Bat'],
'Golden Bat',
False,
False,
[
    ['1966']
],
'1966',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect K (Robot Detective)', 'https://www.reddit.com/r/respectthreads/comments/1pbc51d/respect_k_robot_detective/')
add_data(['K'],
'K',
False,
False,
[
    ['Robot Detective']
],
'Robot Detective',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Mysterians (The Mysterians)', 'https://www.reddit.com/r/respectthreads/comments/1pbc522/respect_the_mysterians_the_mysterians/')
add_data(['Mysterians'],
'Mysterians',
True,
True,
[
    ['Mysterians ?\(The Mysterians']
],
'1957',
'{' + '{}'.format(id) + '}'
)
#
########################################

id = get_rt_id(cur, 'Respect The Flatwoods Monster, The Yeti (Abominable, 2006)', 'https://www.reddit.com/r/respectthreads/comments/1pbd47m/respect_the_flatwoods_monster_the_yeti_abominable/')
add_data(['Yeti'],
'Yeti',
False,
False,
[
    ['Abominable', '2006']
],
'Abominable, 2006',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Larry (Christmas Massacre)', 'https://www.reddit.com/r/respectthreads/comments/1pbfm84/respect_larry_christmas_massacre/')
add_data(['Larry'],
'Larry',
False,
False,
[
    ['Christmas Massacre']
],
'Christmas Massacre',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Erzsebet Bathory! (Castlevania Nocturne)', 'https://www.reddit.com/r/respectthreads/comments/1pbtt9b/respect_erzsebet_bathory_castlevania_nocturne/')
add_data(['(Elizabeth|Erzs(é|e)bet) (Bartley|B(a|á)thory)'],
'Elizabeth Bartley',
False,
False,
[
    ['Castlevania:? Nocturne']
],
'Castlevania: Nocturne',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Drolta Tzuentes! (Castlevania Nocturne)', 'https://www.reddit.com/r/respectthreads/comments/1pbtuzo/respect_drolta_tzuentes_castlevania_nocturne/')
add_data(['Drolta Tzuentes'],
'Drolta Tzuentes',
False,
False,
[
    ['Castlevania:? Nocturne']
],
'Castlevania: Nocturne',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Ori (Ori Series)', 'https://www.reddit.com/r/respectthreads/comments/1pc1bas/respect_ori_ori_series/')
add_data(['Ori'],
'Ori',
False,
False,
[
    ['Ori ?\(Ori\)'], ['Blind Forest'], ['Will of the Wisps'], ['Ori Series'], ['Cuphead']
],
'Ori Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/vp3hsz/cuphead_and_mugman_vs_ghost_of_hallownest_and_ori/

########################################

id = get_rt_id(cur, 'Respect Don Diego de la Vega, Zorro (Zorro, 1957)', 'https://www.reddit.com/r/respectthreads/comments/1pc5neb/respect_don_diego_de_la_vega_zorro_zorro_1957/')
add_data(['Zorro'],
'Zorro',
False,
False,
[
    ['1957']
],
'1957',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Team Galactic (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1pc97zu/respect_team_galactic_pokemon_anime/')
add_data(['Team Galactic'],
'Team Galactic',
True,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Streaky the Super-Cat (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1pc9wxo/respect_streaky_the_supercat_dc_comics/')
add_data(['Streaky the Super(-| )?cat'],
'Streaky the Supercat',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Streaky'],
'Streaky',
False,
False,
[
    ['Krypto', 'Dex(-?Starr)?|Superman']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/59g9dg/casual_see_them_fighting_like_cats_and_dogs/
#https://www.reddit.com/r/whowouldwin/comments/2g6xif/superman_and_streaky_the_supercat_vs_supergirl/


add_data(['Streaky the Super(-| )?cat'],
'Streaky the Supercat',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Streaky'],
'Streaky',
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

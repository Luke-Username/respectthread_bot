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

update_respectthread(cur, 7523, 'Respect Kalibak (DC Animated Universe)', 'https://www.reddit.com/r/respectthreads/comments/1p9cccu/respect_kalibak_dc_animated_universe/')

########################################

add_data(['Reze'],
'Reze',
False,
False,
[
    ['Bakugo', 'vs\.? Reze']
],
'Chainsaw Man',
'{15327}'
)
#https://www.reddit.com/r/whowouldwin/comments/1p83cgc/bakugo_vs_reze/

########################################

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
#


########################################

id = get_rt_id(cur, 'Respect Megatron (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1p9vis9/respect_megatron_marvel_616/')
add_data(['Megatron'],
'Megatron',
False,
False,
[
    ['Megatron ?\((Marvel )?616\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Samurai Destroyer (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1p9vioe/respect_the_samurai_destroyer_marvel_616/')
add_data(['Samurai Destroyer'],
'Samurai Destroyer',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect The Shogun Warriors (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1p9v91u/respect_the_shogun_warriors_marvel_616/')
add_data(['Shogun Warriors'],
'Shogun Warriors',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jay Waringcrane (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p858go/respect_jay_waringcrane_cleveland_quixotic/')
add_data(['Jay Waringcrane'],
'Jay Waringcrane',
False,
True,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Queen Mallory Tivania Coke (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p859xo/respect_queen_mallory_tivania_coke_cleveland/')
add_data(['Queen Mallory Tivania Coke'],
'Queen Mallory Tivania Coke',
False,
False,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Flanz-le-Flore (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p85aq7/respect_flanzleflore_cleveland_quixotic/')
add_data(['Flanz(-| )le)(-| )Flore'],
'Flanz-le-Flore',
False,
False,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lalum (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p85bau/respect_lalum_cleveland_quixotic/')
add_data(['Lalum'],
'Lalum',
False,
False,
[
    ['Cleveland Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Relics of Whitecrosse (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p85c2t/respect_the_relics_of_whitecrosse_cleveland/')
add_data(['Relics of Whitecrosse'],
'Relics of Whitecrosse',
True,
False,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Perfidia Bal Berith (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p8x2gv/respect_perfidia_bal_berith_cleveland_quixotic/')
add_data(['Perfidia Bal Berith'],
'Perfidia Bal Berith',
False,
True,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ubiquitous Bal Berith (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p8x7ua/respect_ubiquitous_bal_berith_cleveland_quixotic/')
add_data(['Ubiquitous Bal Berith'],
'Ubiquitous Bal Berith',
False,
False,
[
    ['Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kadeshah (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p8x93g/respect_kadeshah_cleveland_quixotic/')
add_data(['Kadeshah'],
'Kadeshah',
False,
False,
[
    ['Cleveland Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Seven Princes of Hell (Cleveland Quixotic)', 'https://www.reddit.com/r/respectthreads/comments/1p8xafa/respect_the_seven_princes_of_hell_cleveland/')
add_data(['Seven Princes of Hell'],
'Seven Princes of Hell',
True,
False,
[
    ['Cleveland Quixotic']
],
'Cleveland Quixotic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect El Patito Feo, Bird Cowboy (Mummy Joe)', 'https://www.reddit.com/r/respectthreads/comments/1p86lg0/respect_el_patito_feo_bird_cowboy_mummy_joe/')
add_data(['El Patito Feo'],
'El Patito Feo',
False,
False,
[
    ['Mummy Joe']
],
'Mummy Joe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jimmy Hedgeman! (Sonic: The Movie 1994)', 'https://www.reddit.com/r/respectthreads/comments/1p874l1/respect_jimmy_hedgeman_sonic_the_movie_1994/')
add_data(['Jimmy Hedgeman'],
'Jimmy Hedgeman',
False,
False,
[
    ['Sonic:? The Movie', '1994']
],
'Sonic: The Movie, 1994',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Skirk! (Genshin Impact)', 'https://www.reddit.com/r/respectthreads/comments/1p8c20v/respect_skirk_genshin_impact/')
add_data(['Skirk'],
'Skirk',
False,
False,
[
    ['Genshin']
],
'Genshin Impact',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gus Fring (Gus vs. Literally Everyone)', 'https://www.reddit.com/r/respectthreads/comments/1p8czdu/respect_gus_fring_gus_vs_literally_everyone/')
add_data(['Gus Fring'],
'Gus Fring',
False,
False,
[
    ['Gus vs\.? Literally Everyone']
],
'Gus vs. Literally Everyone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Paninya (FullMetal Alchemist Manga/Brotherhood)', 'https://www.reddit.com/r/respectthreads/comments/1p8n1b9/respect_paninya_fullmetal_alchemist/')
add_data(['Paninya'],
'Paninya',
False,
False,
[
    ['Full ?metal'], ['FMA:?B?']
],
'Fullmetal Alchemist',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Gold Toothed Doctor and Wrath Candidates(FullMetal Alchemist Manga/Brotherhood)', 'https://www.reddit.com/r/respectthreads/comments/1pai75i/respect_the_gold_toothed_doctor_and_wrath/')
add_data(['Gold(-| )Toothed Doctors'],
'Gold Toothed Doctor',
False,
False,
[
    ['Full ?metal'], ['FMA:?B?']
],
'Fullmetal Alchemist',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/3y849q/11_of_the_gold_toothed_doctors_fuhrer_candidates/

########################################

id = get_rt_id(cur, "Respect Jessie''s Yanmega (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1p8wfwu/respect_jessies_yanmega_pokemon_anime/')
add_data(['Yanma'],
'Yanma',
False,
False,
[
    ['Jessie']
],
'Jessie',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Yanmega'],
'Yanmega',
False,
False,
[
    ['Jessie']
],
'Jessie',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dex-Starr (DC Comics, Post Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1p9gla1/respect_dexstarr_dc_comics_post_flashpoint/')
add_data(['Dex(-| )?Starr'],
'Dex-Starr',
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

id = get_rt_id(cur, 'Respect Gotham and Gotham Girl! (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1p9s6fx/respect_gotham_and_gotham_girl_dc_comics/')
add_data(['Gotham and Gotham Girl'],
'Gotham and Gotham Girl',
True,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Gotham and Gotham Girl'],
'Gotham and Gotham Girl',
True,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}, 1512'.format(id) + '}'
)
#

add_data(['Gotham Girl'],
'Gotham Girl',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Gotham Girl'],
'Gotham Girl',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}, 1512'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Wakinyan, the Thunderer (Lakota/Dakota Mythology)', 'https://www.reddit.com/r/respectthreads/comments/1pa834e/respect_wakinyan_the_thunderer_lakotadakota/')
add_data(['Wakinyan'],
'Wakinyan',
False,
True,
[
    ['Mythology']
],
'Mythology',
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

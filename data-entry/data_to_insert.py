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

add_data(['Perc(y|eus) Jackson'],
'Percy Jackson',
False,
True,
[
    ['book']
],
'Percy Jackson',
'{5905,23655,23656}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pi418b/percy_jacksonbook_vs_percy_jacksonmovie_vs_percy/nt3b4d8/?context=3

########################################

id = get_rt_id(cur, 'Respect Donkey Kong (Donkey Kong Country)', 'https://www.reddit.com/r/respectthreads/comments/1pfop7l/respect_donkey_kong_donkey_kong_country/')
add_data(['Donkey Kong'],
'Donkey Kong',
False,
False,
[
    ['Donkey Kong Country.*show']
],
'Donkey Kong Country',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect King K. Rool (Donkey Kong Country)', 'https://www.reddit.com/r/respectthreads/comments/1pfosmr/respect_king_k_rool_donkey_kong_country/')
add_data(['King K\\.? ?Rool'],
'King K. Rool',
False,
False,
[
    ['Donkey Kong Country.*show']
],
'Donkey Kong Country',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Funky Kong (Donkey Kong Country)', 'https://www.reddit.com/r/respectthreads/comments/1pfosoe/respect_funky_kong_donkey_kong_country/')
add_data(['Funky Kong'],
'Funky Kong',
False,
False,
[
    ['Donkey Kong Country.*show']
],
'Donkey Kong Country',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Riri Hoshina (Magical Girl and Narco Wars)', 'https://www.reddit.com/r/respectthreads/comments/1pfs3k9/respect_riri_hoshina_magical_girl_and_narco_wars/')
add_data(['Riri Hoshina'],
'Riri Hoshina',
False,
False,
[
    ['Magical Girl|Narco Wars']
],
'Magical Girl and Narco Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Velvet Crowe (Tales of Berseria)', 'https://www.reddit.com/r/respectthreads/comments/1pgtc7c/respect_velvet_crowe_tales_of_berseria/')
add_data(['Velvet Crowe'],
'Velvet Crowe',
False,
True,
[
    ['Tales']
],
'Tales of Berseria',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Laphicet (Tales of Berseria)', 'https://www.reddit.com/r/respectthreads/comments/1pgtc8k/respect_laphicet_tales_of_berseria/')
add_data(['Laphicet'],
'Laphicet',
False,
False,
[
    ['Tales']
],
'Tales of Berseria',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Magilou (Tales of Berseria)', 'https://www.reddit.com/r/respectthreads/comments/1pgtcet/respect_magilou_tales_of_berseria/')
add_data(['Magilou'],
'Magilou',
False,
False,
[
    ['Tales']
],
'Tales of Berseria',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rokurou Rangetsu (Tales of Berseria)', 'https://www.reddit.com/r/respectthreads/comments/1pgtcfo/respect_rokurou_rangetsu_tales_of_berseria/')
add_data(['Rokurou Rangetsu'],
'Rokurou Rangetsu',
False,
True,
[
    ['Tales']
],
'Tales of Berseria',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Eleanor Hume (Tales of Berseria)', 'https://www.reddit.com/r/respectthreads/comments/1pgtcls/respect_eleanor_hume_tales_of_berseria/')
add_data(['Eleanor Hume'],
'Eleanor Hume',
False,
True,
[
    ['Tales']
],
'Tales of Berseria',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Beatrix Kiddo, the Bride (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1pgyald/respect_beatrix_kiddo_the_bride_fortnite/')
add_data(['Beatrix Kiddo'],
'Beatrix Kiddo',
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

id = get_rt_id(cur, 'Respect Kururu (Undead Unluck)', 'https://www.reddit.com/r/respectthreads/comments/1ph01gp/respect_kururu_undead_unluck/')
add_data(['Kururu'],
'Kururu',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kenny (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1phd7am/respect_kenny_pokemon_anime/')
add_data(['Kenny'],
'Kenny',
False,
False,
[
    ['Kenny.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ursula (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1phd7z5/respect_ursula_pokemon_anime/')
add_data(['Ursula'],
'Ursula',
False,
False,
[
    ['Ursula.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rohan (Mystic Knights of Tir Na Nog)', 'https://www.reddit.com/r/respectthreads/comments/1phe0x4/respect_rohan_mystic_knights_of_tir_na_nog/')
add_data(['Rohan'],
'Rohan',
False,
False,
[
    ['Mystic Knights of Tir Na Nog']
],
'Mystic Knights of Tir Na Nog',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Deidre (Mystic Knights of Tir Na Nog)', 'https://www.reddit.com/r/respectthreads/comments/1phe0xl/respect_deidre_mystic_knights_of_tir_na_nog/')
add_data(['Deidre'],
'Deidre',
False,
False,
[
    ['Mystic Knights of Tir Na Nog']
],
'Mystic Knights of Tir Na Nog',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Ivar (Mystic Knights of Tir Na Nog)', 'https://www.reddit.com/r/respectthreads/comments/1phe0yh/respect_ivar_mystic_knights_of_tir_na_nog/')
add_data(['Ivar'],
'Ivar',
False,
False,
[
    ['Mystic Knights of Tir Na Nog']
],
'Mystic Knights of Tir Na Nog',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Angus (Mystic Knights of Tir Na Nog)', 'https://www.reddit.com/r/respectthreads/comments/1phe0zc/respect_angus_mystic_knights_of_tir_na_nog/')
add_data(['Angus'],
'Angus',
False,
False,
[
    ['Mystic Knights of Tir Na Nog']
],
'Mystic Knights of Tir Na Nog',
'{' + '{}'.format(id) + '}'
)


########################################

id = get_rt_id(cur, 'Respect Garrett (Mystic Knights of Tir Na Nog)', 'https://www.reddit.com/r/respectthreads/comments/1phe102/respect_garrett_mystic_knights_of_tir_na_nog/')
add_data(['Garrett'],
'Garrett',
False,
False,
[
    ['Mystic Knights of Tir Na Nog']
],
'Mystic Knights of Tir Na Nog',
'{' + '{}'.format(id) + '}'
)

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

"""
# This script is used to enter new characters into the database when a respect thread is written of them.
# New respect threads are found at this link: https://www.reddit.com/r/respectthreads/new/
# An example of how to enter a new character is as follows.

id = get_rt_id(cur, 'Respect Dr. Evil (Austin Powers)', 'https://www.reddit.com/r/respectthreads/comments/1my1b8x/respect_dr_evil_austin_powers/')
add_data(['Dr\.? Evil'],
'Dr. Evil',
False,
False,
[
    ['Austin Powers']
],
'Austin Powers',
'{' + '{}'.format(id) + '}'
)
#

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
            # Turn the name into a string acceptable for PostgreSQL (no idea if this is correct. can't be bothered to do proper testing.)
            formatted_name_list.append(name.replace('\\', '\\\\'))
            #formatted_name_list.append(name)

    formatted_version_list = []
    for version in version_list:
        version_array_string = '{'
        for regex in version:
            if not is_valid_regex(regex):
                return
            else:
                # Note: Replacing \\ with \\\\ is needed so Postgres can pick up that a \ is supposed to be there
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

update_respectthread(cur, 4353, 'Respect Skyla (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1r0y97n/respect_skyla_pokemon_anime/')
update_respectthread(cur, 3521, 'Respect Neferpitou (Hunter x Hunter)', 'https://www.reddit.com/r/respectthreads/comments/1r2cm5k/respect_neferpitou_hunter_x_hunter/')
update_respectthread(cur, 159, 'Respect Laura/X-23 (Fox X-Men)', 'https://www.reddit.com/r/respectthreads/comments/1r3gl4e/respect_laurax23_fox_xmen/')

########################################

add_data(['Dabura'],
'Dabura',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1r14uq6/dabura_jjk_modulo_vs_the_primearchs_40k_one_on_one/o4mw6sa/?context=3

########################################

id = get_rt_id(cur, 'Respect the Wolf Chimeras (Fullmetal Alchemist: The Sacred Star of Milos)', 'https://www.reddit.com/r/respectthreads/comments/1r31uam/respect_the_wolf_chimeras_fullmetal_alchemist_the/')
add_data(['(Were)?wolf Chimeras?'],
'Wolf Chimeras',
False,
False,
[
    ['Full ?metal']
],
'Fullmetal Alchemist',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Sailor Moon & friends (Sailor Moon Abridged)', 'https://www.reddit.com/r/CasualRespectThreads/comments/1q6hkti/respect_sailor_moon_friends_sailor_moon_abridged/')
add_data(['Sailor Moon'],
'Sailor Moon',
False,
False,
[
    ['Abridged']
],
'Sailor Moon Abridged',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cheren (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1r3n1wf/respect_cheren_pokemon_anime/')
add_data(['Cheren'],
'Cheren',
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

id = get_rt_id(cur, 'Respect the Titan Speakerman (Skibidi Toilet)', 'https://www.reddit.com/r/respectthreads/comments/1r4c9dh/respect_the_titan_speakerman_skibidi_toilet/')
add_data(['Titan Speakerman'],
'Titan Speakerman',
False,
True,
[
    ['Skibidi Toilet']
],
'Skibidi Toilet',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Guadalupe Droin (World of Darkness)', 'https://www.reddit.com/r/respectthreads/comments/1r5yhsk/respect_guadalupe_droin_world_of_darkness/')
add_data(['Guadalupe Droin'],
'Guadalupe Droin',
False,
True,
[
    ['World of Darkness']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hayashizake Jinsuke (Tenkaichi)', 'https://www.reddit.com/r/respectthreads/comments/1r6k9mu/respect_hayashizake_jinsuke_tenkaichi/')
add_data(['Hayashizake Jinsuke'],
'Hayashizake Jinsuke',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hozoin Inshun (Tenkaichi)', 'https://www.reddit.com/r/respectthreads/comments/1r6k9ol/respect_hozoin_inshun_tenkaichi/')
add_data(['Hozoin Inshun'],
'Hozoin Inshun',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
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

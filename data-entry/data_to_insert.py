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

update_respectthread(cur, 1242, 'Respect Judy Hopps! (Zootopia)', 'https://www.reddit.com/r/respectthreads/comments/1qwehfu/respect_judy_hopps_zootopia/')

########################################

id = get_rt_id(cur, 'Respect Ectotron (Transformers/Ghostbusters)', 'https://www.reddit.com/r/respectthreads/comments/1quv43g/respect_ectotron_transformersghostbusters/')
add_data(['Ectotron'],
'Ectotron',
False,
False,
[
    ['Transformers', 'Ghostbusters']
],
'Transformers/Ghostbusters',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Hand (Talk to Me)', 'https://www.reddit.com/r/respectthreads/comments/1qwpgio/respect_the_hand_talk_to_me/')
add_data(['The Hand'],
'The Hand',
False,
False,
[
    ['Talk to Me']
],
'Talk to Me',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Jessie''s Seviper (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1qx0v58/respect_jessies_seviper_pokemon_anime/')
add_data(['Seviper'],
'Seviper',
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

id = get_rt_id(cur, 'Respect Elesa (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1qx2tkj/respect_elesa_pokemon_anime/')
add_data(['Elesa'],
'Elesa',
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

id = get_rt_id(cur, 'Respect Georgia (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1qzomue/respect_georgia_pokemon_anime/')
add_data(['Georgia'],
'Georgia',
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

id = get_rt_id(cur, 'Respect Marlon (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1r05ysk/respect_marlon_pokemon_anime/')
add_data(['Marlon'],
'Marlon',
False,
False,
[
    ['Marlon.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Swords of Justice (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1r03xwa/respect_the_swords_of_justice_pokemon_anime/')
add_data(['Swords of Justice'],
'Swords of Justice',
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

id = get_rt_id(cur, 'Respect Ingo and Emmet (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1qxe0tv/respect_ingo_and_emmet_pokemon_anime/')
add_data(['Ingo and Emmet'],
'Ingo and Emmet',
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

id = get_rt_id(cur, 'Respect Suckhead! (Vampire: the Masquerade - Bloodlines)', 'https://www.reddit.com/r/respectthreads/comments/1qxizve/respect_suckhead_vampire_the_masquerade_bloodlines/')
add_data(['Suckhead'],
'Suckhead',
False,
False,
[
    ['Vampire:? The Masquerade'], ['VTM']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Godzilla (IDW Comics, Kai-Sei Era)', 'https://www.reddit.com/r/respectthreads/comments/1qyx3oz/respect_godzilla_idw_comics_kaisei_era/')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['IDW', 'Kai-Sei']
],
'IDW Comics, Kai-Sei Era',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Charles, the Mighty Accelguard (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1qyfruk/respect_charles_the_mighty_accelguard_pokemon/')
add_data(['Charles'],
'Charles',
False,
False,
[
    ['Accelg(or|uard)']
],
'Accelguard',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Clay (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1qzabx1/respect_clay_pokemon_anime/')
add_data(['Clay'],
'Clay',
False,
False,
[
    ['Clay ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nibbles Maplestick (Zootopia)', 'https://www.reddit.com/r/respectthreads/comments/1qzavmo/respect_nibbles_maplestick_zootopia/')
add_data(['Nibbles Maplestick'],
'Nibbles Maplestick',
False,
False,
[
    ['Zootopia']
],
'Zootopia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Lynxleys (Zootopia)', 'https://www.reddit.com/r/respectthreads/comments/1qzaxbs/respect_the_lynxleys_zootopia/')
add_data(['Lynxleys'],
'Lynxleys',
False,
False,
[
    ['Zootopia']
],
'Zootopia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Gary De''Snake (Zootopia)", 'https://www.reddit.com/r/respectthreads/comments/1qzayad/respect_gary_desnake_zootopia/')
add_data(["Gary De''Snake"],
"Gary De''Snake",
False,
False,
[
    ['Zootopia']
],
'Zootopia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Homelander! (DC Comics)', 'https://www.reddit.com/r/respectthreads/comments/1qzey8j/respect_homelander_dc_comics/')
add_data(['Homelander'],
'Homelander',
False,
False,
[
    ['Homelander ?\(DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Michael Myers (Halloween 3D)', 'https://www.reddit.com/r/respectthreads/comments/1qzgihn/respect_michael_myers_halloween_3d/')
add_data(['Mich(ae|ea)l Me?y(er|re)s'],
'Michael Myers',
False,
False,
[
    ['Halloween 3D']
],
'Halloween 3D',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Sheriff (Vampire: the Masquerade - Bloodlines)', 'https://www.reddit.com/r/respectthreads/comments/1qzlnod/respect_the_sheriff_vampire_the_masquerade/')
add_data(['Sheriff'],
'Sheriff',
False,
False,
[
    ['Vampire:? The Masquerade']
],
'Vampire: The Masquerade',
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

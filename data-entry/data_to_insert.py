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

update_respectthread(cur, 7411, 'Respect Birdy Cephon Altera (Birdy The Mighty: Decode)', 'https://www.reddit.com/r/respectthreads/comments/1rksv8o/respect_birdy_cephon_altera_birdy_the_mighty/')

########################################

id = get_rt_id(cur, "Respect Jessie''s Frillish (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rktbfw/respect_jessies_frillish_pokemon_anime/')
add_data(['Frillish'],
'Frillish',
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

id = get_rt_id(cur, 'Respect Striker Berserker (Pacific Rim)', 'https://www.reddit.com/r/respectthreads/comments/1rl2ipg/respect_striker_berserker_pacific_rim/')
add_data(['Striker Berserker'],
'Striker Berserker',
False,
True,
[
    ['Pacific Rim']
],
'Pacific Rim',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marco Mardon/Weather Wizard (DC Comics, Post Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rl8v4v/respect_marco_mardonweather_wizard_dc_comics_post/')
add_data(['Weather Wizard'],
'Weather Wizard',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Weather Wizard'],
'Weather Wizard',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}, 1605'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Frank Stone (The Casting of Frank Stone)', 'https://www.reddit.com/r/respectthreads/comments/1rlhyo7/respect_frank_stone_the_casting_of_frank_stone/')
add_data(['Frank Stone'],
'Frank Stone',
False,
False,
[
    ['Casting of Frank Stone']
],
'The Casting of Frank Stone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Twin-Tailed Beast (Path of the Twin-Tailed Beast)', 'https://www.reddit.com/r/respectthreads/comments/1rm0gt8/respect_the_twintailed_beast_path_of_the/')
add_data(['Twin(-| )Tailed Beast'],
'Twin-Tailed Beast',
False,
False,
[
    ['Path of the Twin(-| )Tailed Beast']
],
'Path of the Twin-Tailed Beast',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Pestilence (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1rmbf2l/respect_the_pestilence_marvel_comics_616/')
add_data(['The Pestilence'],
'The Pestilence',
False,
False,
[
    ['The Pestilence ?\(616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bruno (Looney Tunes)', 'https://www.reddit.com/r/respectthreads/comments/1rmdees/respect_bruno_looney_tunes/')
add_data(['Bruno'],
'Bruno',
False,
False,
[
    ['Looney Tunes']
],
'Looney Tunes',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Jessie''s Woobat (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rmeioe/respect_jessies_woobat_pokemon_anime/')
add_data(['Woobat'],
'Woobat',
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

id = get_rt_id(cur, 'Respect Maru! (Jujutsu Kaisen Modulo)', 'https://www.reddit.com/r/respectthreads/comments/1rmgl9s/respect_maru_jujutsu_kaisen_modulo/')
add_data(['Maru'],
'Maru',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJKM?']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Yuka Okkotsu! (Jujutsu Kaisen Modulo)', 'https://www.reddit.com/r/respectthreads/comments/1rmj1uc/respect_yuka_okkotsu_jujutsu_kaisen_modulo/')
add_data(['Yuka Okkotsu'],
'Yuka Okkotsu',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJKM?']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tsurugi Okkotsu! (Jujutsu Kaisen Modulo)', 'https://www.reddit.com/r/respectthreads/comments/1rmj21k/respect_tsurugi_okkotsu_jujutsu_kaisen_modulo/')
add_data(['Tsurugi Okkotsu'],
'Tsurugi Okkotsu',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJKM?']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Mysterious Game(The Midnight Library)', 'https://www.reddit.com/r/respectthreads/comments/1rmzq68/respect_the_mysterious_gamethe_midnight_library/')
add_data(['Mysterious Game'],
'Mysterious Game',
False,
False,
[
    ['Midnight Library']
],
'The Midnight Library',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Tiger-Sized Cat (Zack D. Films)', 'https://www.reddit.com/r/respectthreads/comments/1rnrmv0/respect_the_tigersized_cat_zack_d_films/')
add_data(['Tiger(-| )Sized Cat'],
'Tiger-Sized Cat',
False,
False,
[
    ['Zack D\.? Films']
],
'Zack D. Films',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, '[NSFW] Respect the Weakest Gladiator, Mikagami Kouji! (Reincarnation Coliseum)', 'https://www.reddit.com/r/respectthreads/comments/1rnvjmp/nsfw_respect_the_weakest_gladiator_mikagami_kouji/')
add_data(['Kouji Mikagami|Mikagami Kouji'],
'Kouji Mikagami',
False,
False,
[
    ['Reincarnation Coliseum']
],
'Reincarnation Coliseum',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Getaway (Transformers, IDW Comics [2005])', 'https://www.reddit.com/r/respectthreads/comments/1ro0a40/respect_getaway_transformers_idw_comics_2005/')
add_data(['Getaway'],
'Getaway',
False,
False,
[
    ['Transformers', 'IDW']
],
'Transformers IDW',
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

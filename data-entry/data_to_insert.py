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

update_respectthread(cur, 17633, 'Respect Spider (Dreamwalker)', 'https://redd.it/u2dxuu')
update_respectthread(cur, 4064, 'Respect Charlotte Cracker (One Piece)', 'https://redd.it/u2hz7f')
update_respectthread(cur, 5784, 'Respect Sieg, Custodian of the Grail (Fate)', 'https://redd.it/u2ygcy')

########################################

add_data(['Spawn'],
'Spawn',
False,
False,
[
    ['Ghost Rider']
],
'Image Comics',
'{2638,2639}'
)
#https://www.reddit.com/r/whowouldwin/comments/u1yhp7/team_sorcerers_vs_team_hell/

########################################

add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['Punisher.*TV (show|version)']
],
'MCU',
'{1297}'
)
#https://www.reddit.com/r/whowouldwin/comments/u20epx/the_punisher_marvel_tv_show_20172019_vs_the/i4fm49z/?context=3

########################################

add_data(['Charles Xavier'],
'Charles Xavier',
False,
False,
[
    ['Charles Xavier.*movies?']
],
'FOX',
'{21408}'
)
#https://www.reddit.com/r/whowouldwin/comments/u246ou/charles_xavier_1st_movie_vs_quicksilver_mcu/

########################################

id = get_rt_id(cur, 'Respect Grookey (Pokemon Anime)', 'https://redd.it/u1xwwu')
add_data(['Grookey'],
'Grookey',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u1xwwu/respect_grookey_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Drasna (Pokemon Anime)', 'https://redd.it/u3hwf5')
add_data(['Drasna'],
'Drasna',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u3hwf5/respect_drasna_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Wiz (Konosuba Light Novel)', 'https://redd.it/u2aokw')
add_data(['Wiz'],
'Wiz',
False,
False,
[
    ['Konosuba']
],
'Konosuba',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2aokw/respect_wiz_konosuba_light_novel/

########################################

id = get_rt_id(cur, 'Respect Niklaus "Klaus" Mikaelson (The Vampire Diaries)', 'https://redd.it/u2cskt')
add_data(['Klaus'],
'Klaus',
False,
False,
[
    ['Vampire Diaries'], ['Mikaelson'], ['Originals']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2cskt/respect_niklaus_klaus_mikaelson_the_vampire/

add_data(['Niklaus'],
'Niklaus',
False,
True,
[
    ['Vampire Diaries'], ['Mikaelson'], ['Originals']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2cskt/respect_niklaus_klaus_mikaelson_the_vampire/

########################################

id = get_rt_id(cur, 'Respect Elijah Mikaelson (The Vampire Diaries)', 'https://redd.it/u2d1ff')
add_data(['Elijah'],
'Elijah',
False,
False,
[
    ['Vampire Diaries'], ['Mikaelson']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2d1ff/respect_elijah_mikaelson_the_vampire_diaries/

########################################

id = get_rt_id(cur, 'Respect Rebekah Mikaelson (The Vampire Diaries)', 'https://redd.it/u2d7zq')
add_data(['Rebekah'],
'Rebekah',
False,
True,
[
    ['Vampire Diaries'], ['Mikaelson'], ['Originals']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2d7zq/respect_rebekah_mikaelson_the_vampire_diaries/

########################################

id = get_rt_id(cur, 'Respect Mikael (The Vampire Diaries)', 'https://redd.it/u2de2d')
add_data(['Mikael'],
'Mikael',
False,
False,
[
    ['Vampire Diaries'], ['Mikaelson'], ['The Originals']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2de2d/respect_mikael_the_vampire_diaries/

########################################

id = get_rt_id(cur, 'Respect Marcel Gerard (The Vampire Diaries)', 'https://redd.it/u2dny6')
add_data(['Marcel'],
'Marcel',
False,
False,
[
    ['Vampire Diaries'], ['Mikaelsons?'], ['The Originals'],
    ['Marcel Gerard']
],
'The Vampire Diaries',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2dny6/respect_marcel_gerard_the_vampire_diaries/

########################################

id = get_rt_id(cur, "Respect Goh''s Inteleon (Pokemon Anime)", 'https://redd.it/u2otih')
add_data(['Inteleon'],
'Inteleon',
False,
False,
[
    ['Go(h|u)']
],
'Goh',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2otih/respect_gohs_inteleon_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect Jojo The Kissing Bandit (Avatar: The Last Airbender''s Official TCG)", 'https://redd.it/u2psvj')
add_data(['Jojo'],
'Jojo',
False,
False,
[
    ['Avatar', 'TCG|Card Game']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2psvj/respect_jojo_the_kissing_bandit_avatar_the_last/

########################################

id = get_rt_id(cur, 'Respect Siegfried, the Dragonslayer (Fate)', 'https://redd.it/u2v5nz')
add_data(['Siegfried'],
'Siegfried',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/u2v5nz/respect_siegfried_the_dragonslayer_fate/?context=3

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

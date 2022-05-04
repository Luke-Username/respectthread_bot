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

########################################

add_data(['Constantine'],
'John Constantine',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{1704}'
)
#https://www.reddit.com/r/whowouldwin/comments/uhk9ro/lex_luther_batman_and_john_constantine_vs_doctor/i76hlbx/?context=3

########################################

id = get_rt_id(cur, 'Red Skull (616) feat repository', 'https://redd.it/kuyb0k')
add_data(['Red Skulls?'],
'Red Skull',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/WhoWouldWinWorkshop/comments/kuyb0k/red_skull_616_feat_repository/

########################################

id = get_rt_id(cur, 'Respect Tintin (The Adventures of Tintin: The Secret of the Unicorn)', 'https://redd.it/ugo6sr')
add_data(['Tintin'],
'Tintin',
False,
False,
[
    ['Adventures of Tintin', 'Secret of.*Unicorn']
],
'The Adventures of Tintin: The Secret of the Unicorn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ugo6sr/respect_tintin_the_adventures_of_tintin_the/

########################################

id = get_rt_id(cur, 'Respect Captain Archibald Haddock (The Adventures of Tintin: The Secret of the Unicorn)', 'https://redd.it/ugo71w')
add_data(['(Captain|Archibald) Haddock'],
'Captain Haddock',
False,
False,
[
    ['Adventures of Tintin', 'Secret of.*Unicorn']
],
'The Adventures of Tintin: The Secret of the Unicorn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ugo71w/respect_captain_archibald_haddock_the_adventures/

########################################

id = get_rt_id(cur, 'Respect Revka Scyros III, Psycho-Man (Marvel, Earth-1610)', 'https://redd.it/ugq2sx')
add_data(['Psycho(-| )?Man'],
'Psycho-Man',
False,
False,
[
    ['1610']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ugq2sx/respect_revka_scyros_iii_psychoman_marvel/

########################################

id = get_rt_id(cur, 'Respect Hanami! (Jujutsu Kaisen)', 'https://redd.it/ugqxkv')
add_data(['Hanami'],
'Hanami',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ugqxkv/respect_hanami_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect: He-Man! (Pre-Crisis DC Comics)', 'https://redd.it/ugwrf3')
add_data(['He(-| )?Man'],
'He-Man',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ugwrf3/respect_heman_precrisis_dc_comics/

########################################

id = get_rt_id(cur, 'Respect King Elizabello II (One Piece)', 'https://redd.it/uh4uq7')
add_data(['Elizabello IIs?'],
'Elizabello II',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uh4uq7/respect_king_elizabello_ii_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Secret Society of Second-Born Royals (The Secret Society of Second-Born Royals)', 'https://redd.it/uhcj6v')
add_data(['Secret Society of Second(-| )Born Royals'],
'Secret Society of Second-Born Royals',
False,
True,
[
    ['Prince(ss)?']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uhcj6v/respect_the_secret_society_of_secondborn_royals/

########################################

id = get_rt_id(cur, 'Respect Optimus Prime! (Transformers: Shattered Glass)', 'https://redd.it/uhh0rh')
add_data(['Optimus Prime'],
'Optimus Prime',
False,
False,
[
    ['Shattered Glass']
],
'Transformers: Shattered Glass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uhh0rh/respect_optimus_prime_transformers_shattered_glass/

########################################

id = get_rt_id(cur, 'Respect Glory (Buffy the Vampire Slayer)', 'https://redd.it/uhpujz')
add_data(['Glory'],
'Glory',
False,
False,
[
    ['Buffy the Vampire Slayer'],['Buffyverse'], ['Buffy', 'Angel']
],
'Buffy the Vampire Slayer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uhpujz/respect_glory_buffy_the_vampire_slayer/

########################################

id = get_rt_id(cur, 'Respect Vaisravana (Xi Xing Ji)', 'https://redd.it/uhwu3y')
add_data(['Vaisravana'],
'Vaisravana',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uhwu3y/respect_vaisravana_xi_xing_ji/

########################################

add_data(['Kurono'],
'Kurono',
False,
False,
[
    ['Fire ?Force']
],
'Fire Force',
'{8237}'
)
#https://www.reddit.com/r/respectthreads/comments/uhxges/respect_yuchiro_kurono_fire_force_anime/

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

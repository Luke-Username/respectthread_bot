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

add_data(['Chaise Long'],
'Chaise Long',
False,
False,
[
    ['Simpsons']
],
'The Simpsons',
'{896}'
)
#https://www.reddit.com/r/whowouldwin/comments/16i3465/jason_voorhees_friday_the_13th_vs_chaise_long_the/k0hcjox/?context=3

########################################

add_data(['Toya Todoroki|Todoroki Toya'],
'Toya Todoroki',
False,
True,
[
    ['My Hero Academia'], ['\(My Hero\)'], ['(M|BN?)HA'], ['Boku no Hero']
],
'My Hero Academia',
'{17317}'
)
#https://www.reddit.com/r/whowouldwin/comments/16kl49f/kazuya_mishima_vs_toya_todoroki_tekken_vs_my_hero/k0wkv3t/?context=3

########################################

add_data(['Shadow'],
'Shadow',
False,
False,
[
    ['Sega']
],
'Sonic the Hedgehog',
'{5389}'
)
#https://www.reddit.com/r/whowouldwin/comments/16jvnkh/shadow_vs_vegeta_sega_vs_dragon_ball/k0s9sun/?context=3

########################################

add_data(['Black Manta'],
'Black Manta',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'],
    ['DC vs'], ['vs\.? DC\)']
],
'DC',
'{1488}'
)
#https://www.reddit.com/r/whowouldwin/comments/16jgp3j/boba_fett_vs_black_manta_star_wars_vs_dc/k0plicu/?context=3

########################################

add_data(['Gappy'],
'Gappy',
False,
False,
[
    ['Go Beyond'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3628}'
)
#https://www.reddit.com/r/whowouldwin/comments/16ht39b/ainz_ooal_gown_vs_16_jojo_characters/k0fkhht/?context=3

########################################

id = get_rt_id(cur, 'Respect Ultimate War Machine (Marvel, 1610)', 'https://redd.it/16hrmjy')
add_data(['Ultimates? War Machine'],
'Ultimate War Machine',
False,
True,
[
    ['1610']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16hrmjy/respect_ultimate_war_machine_marvel_1610/

########################################

id = get_rt_id(cur, 'Respect Bill Cipher. (Death Battle)', 'https://redd.it/16i06bl')
add_data(['Bill C(i|y)phers?'],
'Bill Cipher',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16i06bl/respect_bill_cipher_death_battle/

########################################

id = get_rt_id(cur, 'Respect Zathura (Zathura: A Space Adventure)', 'https://redd.it/16iit2v')
add_data(['Zathura'],
'Zathura',
False,
True,
[
    ['A Space Adventure']
],
'Zathura: A Space Adventure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16iit2v/respect_zathura_zathura_a_space_adventure/

########################################

id = get_rt_id(cur, '(Prototype) Respect Arthas Menethil, The Lich King [Warcraft Universe]', 'https://redd.it/92cebq')
add_data(['Lich King'],
'Lich King',
False,
False,
[
    ['Warcraft'], ['WOW']
],
'World of Warcraft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/16jozdr/darth_vader_vs_the_lich_king_star_wars_vs_warcraft/k0r46dp/?context=3

########################################

id = get_rt_id(cur, 'Respect Singularity (Marvel Comics)', 'https://redd.it/16jjqy4')
add_data(['Singularity'],
'Singularity',
False,
False,
[
    ['\(Marvel( Comics)?\)']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16jjqy4/respect_singularity_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect Shen Xorn (Marvel Comics)', 'https://redd.it/16kd14t')
add_data(['Xorn'],
'Xorn',
False,
False,
[
    ['Marvel'], ['X(-| )?Men']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16kd14t/respect_shen_xorn_marvel_comics/

add_data(['Shen Xorn'],
'Shen Xorn',
False,
True,
[
    ['Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16kd14t/respect_shen_xorn_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect the Hellrider (Judas Priest Song)', 'https://redd.it/16ki40f')
add_data(['Hellrider'],
'Hellrider',
False,
False,
[
    ['Judas Priest']
],
'Judas Priest',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16ki40f/respect_the_hellrider_judas_priest_song/

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

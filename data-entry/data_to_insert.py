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

update_respectthread(cur, 14491, 'Respect War (Darksiders)', 'https://www.reddit.com/r/respectthreads/comments/1pp0v9x/respect_war_darksiders/')

########################################

id = get_rt_id(cur, 'Respect Strife (Darksiders)', 'https://www.reddit.com/r/respectthreads/comments/1pp0vc6/respect_strife_darksiders/')
add_data(['Strife'],
'Strife',
False,
False,
[
    ['Darksiders']
],
'Darksiders',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zephyro (Honkai: Star Rail)', 'https://www.reddit.com/r/respectthreads/comments/1pn83ie/respect_zephyro_honkai_star_rail/')
add_data(['Zephyro'],
'Zephyro',
False,
False,
[
    ['Honkai']
],
'Honkai: Star Rail',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mil Muertes (Lucha Underground)', 'https://www.reddit.com/r/respectthreads/comments/1pnm5km/respect_mil_muertes_lucha_underground/')
add_data(['Mil Muertes'],
'Mil Muertes',
False,
True,
[
    ['Lucha Underground']
],
'Lucha Underground',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nick Russel, the Red Mystic Ranger (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po2dwe/respect_nick_russel_the_red_mystic_ranger_power/')
add_data(['Red Mystic Ranger'],
'Red Mystic Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Nick Russel'],
'Nick Russel',
False,
False,
[
    ['Power Rangers?'], ['Mystic Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Koragg / Leanbow, the Wolf Warrior (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po2e0z/respect_koragg_leanbow_the_wolf_warrior_power/')
add_data(['Koragg'],
'Koragg',
False,
False,
[
    ['Rangers?|Mystic Force|Knight Wolf']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Leanbow'],
'Leanbow',
False,
False,
[
    ['Power Rangers?|Mystic Rangers?|Mystic Force']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect the Titan Megazord (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po2e1h/respect_the_titan_megazord_power_rangers_mystic/')
add_data(['Titan Megazord'],
'Titan Megazord',
False,
True,
[
    ['Power Rangers?|Mystic Rangers?|Mystic Force']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Daggeron, the Solaris Knight (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po2e2a/respect_daggeron_the_solaris_knight_power_rangers/')
add_data(['Daggeron'],
'Daggeron',
False,
False,
[
    ['Rangers?|Mystic Force|Solaris Knight']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Chip Thorn, the Yellow Mystic Ranger (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po75p4/respect_chip_thorn_the_yellow_mystic_ranger_power/')
add_data(['Yellow Mystic Ranger'],
'Yellow Mystic Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Chip Thorn'],
'Chip Thorn',
False,
False,
[
    ['Power Rangers?'], ['Mystic Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Madison Rocca, the Blue Mystic Ranger (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po75qv/respect_madison_rocca_the_blue_mystic_ranger/')
add_data(['Blue Mystic Ranger'],
'Blue Mystic Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Madison Rocca'],
'Madison Rocca',
False,
False,
[
    ['Power Rangers?'], ['Mystic Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Vida Rocca, the Pink Mystic Ranger (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po75rt/respect_vida_rocca_the_pink_mystic_ranger_power/')
add_data(['Pink Mystic Ranger'],
'Pink Mystic Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Vida Rocca'],
'Vida Rocca',
False,
False,
[
    ['Power Rangers?'], ['Mystic Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Xander Bly, the Green Mystic Ranger (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po75t9/respect_xander_bly_the_green_mystic_ranger_power/')
add_data(['Green Mystic Ranger'],
'Green Mystic Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Xander Bly'],
'Xander Bly',
False,
False,
[
    ['Power Rangers?'], ['Mystic Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect the Manticore Megazord (Power Rangers Mystic Force)', 'https://www.reddit.com/r/respectthreads/comments/1po75ur/respect_the_manticore_megazord_power_rangers/')
add_data(['Manticore Megazord'],
'Manticore Megazord',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dick Grayson, Super Robin (DC Comics, New52/Rebirth)', 'https://www.reddit.com/r/respectthreads/comments/1po4k2s/respect_dick_grayson_super_robin_dc_comics/')
add_data(['Dick Grayson'],
'Dick Grayson',
False,
False,
[
    ['Super Robin']
],
'Super Robin',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tia! (Diamond Jack)', 'https://www.reddit.com/r/respectthreads/comments/1po902t/respect_tia_diamond_jack/')
add_data(['Tia'],
'Tia',
False,
False,
[
    ['Diamond Jack']
],
'Diamond Jack',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ms Green! (The Teacher from the Black Lagoon)', 'https://www.reddit.com/r/respectthreads/comments/1ppaizi/respect_ms_green_the_teacher_from_the_black_lagoon/')
add_data(['Mr?s\.? Green'],
'Mrs. Green',
False,
False,
[
    ['Teacher from the Black Lagoon']
],
'The Teacher from the Black Lagoon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cheetah (Justice League: Doom)', 'https://www.reddit.com/r/respectthreads/comments/1ppb0pk/respect_cheetah_justice_league_doom/')
add_data(['Cheetah'],
'Cheetah',
False,
False,
[
    ['Justice League:? Doom']
],
'Justice League: Doom',
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

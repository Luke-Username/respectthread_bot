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

update_respectthread(cur, 5434, 'Respect Rosalina (Super Mario)', 'https://www.reddit.com/r/respectthreads/comments/1ptrsxn/respect_rosalina_super_mario/')
update_respectthread(cur, 12403, 'Respect Merus (Dragon Ball Super)', 'https://www.reddit.com/r/respectthreads/comments/1pup8tr/respect_merus_dragon_ball_super/')
update_respectthread(cur, 5252, 'Respect Solid Snake (Metal Gear)', 'https://www.reddit.com/r/respectthreads/comments/1putrjj/respect_solid_snake_metal_gear/')
update_respectthread(cur, 5244, 'Respect Gray Fox (Metal Gear)', 'https://www.reddit.com/r/respectthreads/comments/1pv0vsy/respect_gray_fox_metal_gear/')

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['Batman.*Wolverine|Wolverine.*Batman', 'vs']
],
'616',
'{2391}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pv12bz/batman_vs_wolverine/nvst6np/?context=3

########################################

id = get_rt_id(cur, 'Respect Chance! (Forsaken)', 'https://www.reddit.com/r/respectthreads/comments/1ptmx3b/respect_chance_forsaken/')
add_data(['Chance'],
'Chance',
False,
False,
[
    ['Chance ?\(Forsaken\)']
],
'Forsaken',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dante the Great (V/H/S: Viral)', 'https://www.reddit.com/r/respectthreads/comments/1ptv5c5/respect_dante_the_great_vhs_viral/')
add_data(['Dante the Great'],
'Dante the Great',
False,
False,
[
    ['V/?H/?S:? Viral']
],
'V/H/S: Viral',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ality Mellowlink (Armor Hunter Mellowlink)', 'https://www.reddit.com/r/respectthreads/comments/1pu3u45/respect_ality_mellowlink_armor_hunter_mellowlink/')
add_data(['Ality Mellowlink'],
'Ality Mellowlink',
False,
True,
[
    ['Armor Hunter Mellowlink']
],
'Armor Hunter Mellowlink',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Joe 90! (Joe 90)', 'https://www.reddit.com/r/respectthreads/comments/1pu8ovj/respect_joe_90_joe_90/')
add_data(['Joe 90'],
'Joe 90',
False,
True,
[
    ['Joe 90 ?\(Joe 90']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pipo Snake (Mesal Gear Solid: Snake Escape)', 'https://www.reddit.com/r/respectthreads/comments/1pv0vti/respect_pipo_snake_mesal_gear_solid_snake_escape/')
add_data(['Pipo Snake'],
'Pipo Snake',
False,
False,
[
    ['Mesal Gear']
],
'Mesal Gear Solid: Snake Escape',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Road Runner (Looney Tunes)', 'https://www.reddit.com/r/respectthreads/comments/1pv21k3/respect_road_runner_looney_tunes/')
add_data(['Road Runner'],
'Road Runner',
False,
True,
[
    ['Looney Tunes']
],
'Looney Tunes',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Ghosts of Christmas (A Christmas Carol)', 'https://www.reddit.com/r/respectthreads/comments/1pvdik0/respect_the_ghosts_of_christmas_a_christmas_carol/')
add_data(['Ghosts'],
'Ghosts',
True,
False,
[
    ['A Christmas Carol']
],
'A Christmas Carol',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Ghosts? of Christmas'],
'Ghosts of Christmas',
True,
True,
[
    ['A Christmas Carol']
],
'A Christmas Carol',
'{' + '{}'.format(id) + '}'
)
#

add_data(['(Three|3) Ghosts'],
'Three Ghosts',
True,
False,
[
    ['Christmas']
],
'A Christmas Carol',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Christmas Trees (Treevenge)', 'https://www.reddit.com/r/respectthreads/comments/1pve0g8/respect_the_christmas_trees_treevenge/')
add_data(['Christmas Trees?'],
'Christmas Trees',
False,
False,
[
    ['Treevenge']
],
'Treevenge',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect ''Vulture'' Li Yao (Swallowed Star)", 'https://www.reddit.com/r/respectthreads/comments/1pvsf8a/respect_vulture_li_yao_swallowed_star/')
add_data(['Vulture'],
'Vulture',
False,
False,
[
    ['Swallowed Star']
],
'Swallowed Star',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Li Yao'],
'Li Yao',
False,
False,
[
    ['Swallowed Star']
],
'Swallowed Star',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Winged Lion (Delicious in Dungeon)', 'https://www.reddit.com/r/respectthreads/comments/1pvvrw7/respect_the_winged_lion_delicious_in_dungeon/')
add_data(['Winged Lion'],
'Winged Lion',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Laios, Marcille, Senshi, Izutsumi, and Chilchuck (Delicious in Dungeon)', 'https://www.reddit.com/r/respectthreads/comments/1pvvtda/respect_laios_marcille_senshi_izutsumi_and/')
add_data(["Laios's? Party"],
"Laios'' Party",
True,
True,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Laios'],
'Laios',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Marcille'],
'Marcille',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Senshi'],
'Senshi',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Izutsumi'],
'Izutsumi',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Chilchuck'],
'Chilchuck',
False,
False,
[
    ['Delicious in Dungeon'], ['Dungeon Meshi']
],
'Delicious in Dungeon',
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

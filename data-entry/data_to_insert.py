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

update_respectthread(cur, 4057, 'Respect Arlong the Saw (One Piece)', 'https://redd.it/sx4y6h')

########################################

add_data(['Prue Halliwell'],
'Prue Halliwell',
False,
True,
[
    ['Charmed']
],
'Charmed',
'{82}'
)
#https://www.reddit.com/r/whowouldwin/comments/sx7swb/magical_tv_show_battle_piper_halliwell_charmed_vs/hxqe2gw/?context=3

########################################

add_data(['Shredder'],
'Shredder',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?'], ['TMNT']
],
'TMNT',
'{9373, 20422, 981, 2673, 2677, 16443}'
)
#https://www.reddit.com/r/whowouldwin/comments/sxbshw/shredder_tmnt_vs_liu_kang_mk_in_2_different/hxr6v7d/?context=3

########################################

add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Van Helsing', '2004']
],
'Van Helsing, 2004',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/swtcui/mcu_spiderman_vs_dracula_van_helsing_2004/hxoreg0/?context=3

########################################

add_data(['Shrike'],
'Shrike',
False,
False,
[
    ['Hyperion']
],
'Hyperion Cantos',
'{5840}'
)
#https://www.reddit.com/r/whowouldwin/comments/swczq3/shrike_hyperion_vs_flash_villains/

########################################

id = get_rt_id(cur, 'Respect the Red King (Marvel, Earth-616)', 'https://redd.it/swo6pb')
add_data(['Red King'],
'Red King',
False,
False,
[
    ['616'], ['Angmo(-| )Asan']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/swo6pb/respect_the_red_king_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect Pleiades (Ple Ple Pleiades)', 'https://redd.it/swp5v3')
add_data(['Pleiades'],
'Pleiades',
False,
False,
[
    ['Ple Ple Pleiades']
],
'Ple Ple Pleiades',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/swp5v3/respect_pleiades_ple_ple_pleiades/

########################################

id = get_rt_id(cur, 'Respect The Zombie Hunting Cheerleader, Juliet Starling', 'https://redd.it/7mkms2')
add_data(['Juliet Starling'],
'Juliet Starling',
False,
True,
[
    ['Lollipop Chainsaw']
],
'Lollipop Chainsaw',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/7mkms2/respect_the_zombie_hunting_cheerleader_juliet/

add_data(['Juliet'],
'Juliet',
False,
False,
[
    ['Lollipop Chainsaw']
],
'Lollipop Chainsaw',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/7mkms2/respect_the_zombie_hunting_cheerleader_juliet/

########################################

id = get_rt_id(cur, 'Respect The Swoledier (Ceno0)', 'https://redd.it/swvnkc')
add_data(['Swoledier'],
'Swoledier',
False,
False,
[
    ['Ceno0']
],
'Ceno0',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/swvnkc/respect_the_swoledier_ceno0/

########################################

id = get_rt_id(cur, 'Respect Grovyle (Pokemon Mystery Dungeon)', 'https://redd.it/sx44w9')
add_data(['Grovyle'],
'Grovyle',
False,
False,
[
    ['Mystery Dungeon']
],
'Pokémon Mystery Dungeon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sx44w9/respect_grovyle_pokemon_mystery_dungeon/

########################################

id = get_rt_id(cur, 'Respect Dusknoir (Pokemon Mystery Dungeon)', 'https://redd.it/sx44yp')
add_data(['Dusknoir'],
'Dusknoir',
False,
False,
[
    ['Mystery Dungeon']
],
'Pokémon Mystery Dungeon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sx44yp/respect_dusknoir_pokemon_mystery_dungeon/

########################################

id = get_rt_id(cur, 'Respect "Flitting Sparrowkeet" Wong (Avatar: The Kyoshi Novels)', 'https://redd.it/sxbd1u')
add_data(['Wong'],
'Wong',
False,
False,
[
    ['Kyoshi Novels?']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxbd1u/respect_flitting_sparrowkeet_wong_avatar_the/

########################################

id = get_rt_id(cur, 'Respect Skateman (Pacific Comics)', 'https://redd.it/sxd6mh')
add_data(['Skateman'],
'Skateman',
False,
False,
[
    ['Kyoshi Novels?']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxd6mh/respect_skateman_pacific_comics/

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

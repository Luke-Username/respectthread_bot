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

update_respectthread(cur, 5347, 'Respect Naoto Shirogane (Persona 4)', 'https://redd.it/10rfm7e')

########################################

add_data(['Cap(tain)? Marvel'],
'Captain Marvel',
False,
False,
[
    ['Cap(tain)? Marvel ?\(DC( Comics)?\)']
],
'DC',
'{22688}'
)
#https://www.reddit.com/r/whowouldwin/comments/10qm3sa/full_on_captain_brawl/j6r0u1b/?context=3

########################################

id = get_rt_id(cur, 'Respect Uzu! (Tank Chair)', 'https://redd.it/10qbsp3')
add_data(['Uzu'],
'Uzu',
False,
False,
[
    ['Tank Chair']
],
'Tank Chair',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qbsp3/respect_uzu_tank_chair/

########################################

id = get_rt_id(cur, 'Respect the Nanobots (The Adventures of Jimmy Neutron, Boy Genius)', 'https://redd.it/10qd5ev')
add_data(['Nano ?bots'],
'Nanobots',
False,
False,
[
    ['Jimmy Neutron']
],
'Jimmy Neutron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qd5ev/respect_the_nanobots_the_adventures_of_jimmy/

########################################

id = get_rt_id(cur, 'Respect Jinx! (Arcane / League of Legends)', 'https://redd.it/10qm3w6')
add_data(['Jinx'],
'Jinx',
False,
False,
[
    ['Arcane'], ['League of Legends'], ['LoL (players?|lore)']
],
'League of Legends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qm3w6/respect_jinx_arcane_league_of_legends/

########################################

id = get_rt_id(cur, 'Respect Tank Girl! (Tank Girl)', 'https://redd.it/10qoisq')
add_data(['Tank Girl'],
'Tank Girl',
False,
True,
[
    ['Tank Girl ?\(Tank Girl']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qoisq/respect_tank_girl_tank_girl/

########################################

id = get_rt_id(cur, 'Respect Sharla (Xenoblade Chronicles)', 'https://redd.it/10qq0lz')
add_data(['Sharla'],
'Sharla',
False,
False,
[
    ['Xenoblade'], ['Shulk']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qq0lz/respect_sharla_xenoblade_chronicles/

########################################

id = get_rt_id(cur, 'Respect Mew (Pokemon: Lucario and the Mystery of Mew)', 'https://redd.it/10qqln4')
add_data(['Mew'],
'Mew',
False,
False,
[
    ['Lucario and the Mystery of Mew']
],
'Lucario and the Mystery of Mew',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jirachi (Pokemon Anime)', 'https://redd.it/10qqlpc')
add_data(['Jirachi'],
'Jirachi',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qqlpc/respect_jirachi_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Primal Dialga (Pokemon Mystery Dungeon)', 'https://redd.it/10qqlrd')
add_data(['Primal Dialga'],
'Primal Dialga',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qqlrd/respect_primal_dialga_pokemon_mystery_dungeon/

########################################

id = get_rt_id(cur, 'Respect Snowbird (Marvel Comics, Earth-616)', 'https://redd.it/10quy36')
add_data(['Snowbird'],
'Snowbird',
False,
False,
[
    ['Marvel Comics'], ['616'], ['Alpha Flight']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10quy36/respect_snowbird_marvel_comics_earth616/

########################################

id = get_rt_id(cur, 'Respect Sindr, Queen of Muspelheim! (Marvel 616)', 'https://redd.it/10qxdhe')
add_data(['Sindr'],
'Sindr',
False,
False,
[
    ['Marvel Comics'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qxdhe/respect_sindr_queen_of_muspelheim_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Purple Hayes, Nosferata (Marvel, 616)', 'https://redd.it/10qy0ir')
add_data(['Nosferata'],
'Nosferata',
False,
False,
[
    ['Marvel Comics'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qy0ir/respect_purple_hayes_nosferata_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Haumea! (Fire Force)', 'https://redd.it/10qx6gt')
add_data(['Haumea'],
'Haumea',
False,
False,
[
    ['Fire Force']
],
'Fire Force',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10qx6gt/respect_haumea_fire_force/

########################################

id = get_rt_id(cur, 'Respect Wario! (Xploshi)', 'https://redd.it/10r24cb')
add_data(['Wario'],
'Wario',
False,
False,
[
    ['Xploshi']
],
'Xploshi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10r24cb/respect_wario_xploshi/

########################################

id = get_rt_id(cur, 'Respect Frey Holland (Forspoken)', 'https://redd.it/10rmp9z')
add_data(['Frey Holland'],
'Frey Holland',
False,
True,
[
    ['Forspoken']
],
'Forspoken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10rmp9z/respect_frey_holland_forspoken/

########################################

id = get_rt_id(cur, 'Respect Steve Fox (Tekken)', 'https://redd.it/10rneys')
add_data(['Steve Fox'],
'Steve Fox',
False,
False,
[
    ['Tekken']
],
'Tekken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10rneys/respect_steve_fox_tekken/

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

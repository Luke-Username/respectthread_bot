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

update_respectthread(cur, 242, 'Respect Sam Wilson, Captain America (Marvel Cinematic Universe)', 'https://redd.it/1ku9apg')

########################################

add_data(['Tarzan'],
'Tarzan',
False,
False,
[
    ['Shrek']
],
'Disney',
'{14470}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ksj86u/tarzan_shrek_and_mannyice_age_vs_30_vikings_with/

########################################

add_data(['Turok'],
'Turok',
False,
False,
[
    ['Dinosaur Hunter'], ['Turok the Hunted']
],
'Valiant Comics',
'{25730}'
)
#

########################################

id = get_rt_id(cur, 'Respect Larce the Undying (Dreamwalker)', 'https://redd.it/1ks1gy8')
add_data(['Larce'],
'Larce',
False,
False,
[
    ['Dreamwalker'], ['Larce the Undying']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the All-New Venom (Marvel, Earth-616)', 'https://redd.it/1kscvnt')
add_data(['All(-| )New Venom'],
'All-New Venom',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/1kscvnt/respect_the_allnew_venom_marvel_earth616/

########################################

id = get_rt_id(cur, "Respect Hallows'' Eve (Marvel, Earth-616)", 'https://redd.it/1kv6s4g')
add_data(["Hallows'' Eve"],
"Hallows'' Eve",
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Elizabeth Tyne'],
'Elizabeth Tyne',
False,
False,
[
    ['616'], ['Marvel']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect: T''Challa, the Ultimate Black Panther (Marvel, 6160)", 'https://redd.it/1kud6dh')
add_data(['Ultimate Black Panther'],
'Ultimate Black Panther',
False,
True,
[
    ['6160']
],
'6160',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kud6dh/respect_tchalla_the_ultimate_black_panther_marvel/

########################################

id = get_rt_id(cur, 'Respect: Fleet Delmar, Karma (DC, Rebirth)', 'https://redd.it/1kvtd4d')
add_data(['Fleet Delmar'],
'Fleet Delmar',
False,
True,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)

add_data(['Fleet Delmar'],
'Fleet Delmar',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)


########################################

id = get_rt_id(cur, 'Respect Silver Sable and Black Cat (Silver & Black Unproduced Movie)', 'https://redd.it/1kt2rbh')
add_data(['Silver Sable'],
'Silver Sable',
False,
False,
[
    ['Silver (&||and) Black', 'unproduced']
],
'Silver & Black',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Black Cat'],
'Black Cat',
False,
False,
[
    ['Silver (&||and) Black', 'unproduced']
],
'Silver & Black',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect May''s Beautifly (Pokemon Anime)", 'https://redd.it/1ku8iie')
add_data(['Beautifly'],
'Beautifly',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ku8iie/respect_mays_beautifly_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect May''s Blaziken (Pokemon Anime)", 'https://redd.it/1kvfzwx')
add_data(['Blaziken'],
'Blaziken',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kvfzwx/respect_mays_blaziken_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Sun (Pokemon Adventures)', 'https://redd.it/1kubjqu')
add_data(['Sun'],
'Sun',
False,
False,
[
    ['Sun.*Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Moon (Pokemon Adventures)', 'https://redd.it/1kubjq6')
add_data(['Moon'],
'Moon',
False,
False,
[
    ['Moon.*Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Chrollo Lucifer, Boss of the Phantom Troupe (Hunter x Hunter)', 'https://redd.it/1kvajlm')
add_data(['Chrollo Lucifer'],
'Chrollo Lucifer',
False,
True,
[
    ['Hunter ?(x ?)?Hunter'], ['HxH']
],
'Hunter x Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kvajlm/respect_chrollo_lucifer_boss_of_the_phantom/

add_data(['Chrollo'],
'Chrollo',
False,
False,
[
    ['Hunter ?(x ?)?Hunter'], ['HxH']
],
'Hunter x Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kvajlm/respect_chrollo_lucifer_boss_of_the_phantom/

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

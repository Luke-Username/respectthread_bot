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

update_respectthread(cur, 1809, 'Respect Livewire (DC, Post Crisis)', 'https://redd.it/tz2gfd')
update_respectthread(cur, 6247, 'Respect Archer! (Fate)', 'https://redd.it/tz3j7e')

########################################

add_data(['Electro'],
'Electro',
False,
False,
[
    ['Electro ?\(Spider(-| )?Mans?\)']
],
'616',
'{2268}'
)
#https://www.reddit.com/r/whowouldwin/comments/tzncyv/eneru_one_piece_vs_electro_spiderman/

########################################

id = get_rt_id(cur, 'Respect Francine Frye, Electro (Marvel, 616)', 'https://redd.it/tz2gvy')
add_data(['Francine Frye'],
'Francine Frye',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tz2gfd/respect_livewire_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect Gax (Ben 10 [2016])', 'https://redd.it/tz6196')
add_data(['Gax'],
'Gax',
False,
False,
[
    ['Ben (10|Ten(nyson)?)'], ['(Omn|Ulti)itrix']
],
'Ben 10',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tz6196/respect_gax_ben_10_2016/

########################################

id = get_rt_id(cur, 'Respect Superman (Zimaut Animation)', 'https://redd.it/tzjf1m')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Zimaut']
],
'Zimaut Animation',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzjf1m/respect_superman_zimaut_animation/

########################################

id = get_rt_id(cur, "Respect Sirfetch''d (Pokemon Anime)", 'https://redd.it/tzt8yx')
add_data(["Farfetch''d"],
"Farfetch''d",
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzt8yx/respect_sirfetchd_pokemon_anime/

add_data(["Sirfetch''d"],
"Sirfetch''d",
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzt8yx/respect_sirfetchd_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Omni Man (Omni Man vs Class S/AniMatt)', 'https://redd.it/tzu96s')
add_data(['Omni(-| )?Man'],
'Omni-Man',
False,
False,
[
    ['AniMatt']
],
'AniMatt',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzu96s/respect_omni_man_omni_man_vs_class_sanimatt/

########################################

id = get_rt_id(cur, 'Respect Superman (DC Versus Marvel/Marvel Versus DC)', 'https://redd.it/tzufmq')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['DC Versus Marvel']
],
'DC Versus Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzufmq/respect_superman_dc_versus_marvelmarvel_versus_dc/

########################################

id = get_rt_id(cur, 'Respect the Smart Pants (The Adventures of Jimmy Neutron, Boy Genius)', 'https://redd.it/tzuufr')
add_data(['Pants'],
'Pants',
False,
False,
[
    ['Jimmy Neutron']
],
'Jimmy Neutron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzuufr/respect_the_smart_pants_the_adventures_of_jimmy/

########################################

id = get_rt_id(cur, "Respect Lee Everett (Telltale''s The Walking Dead Game)", 'https://redd.it/tzwf5d')
add_data(['Lee'],
'Lee',
False,
False,
[
    ['Wa(lk|kl)ing Dead'], ['TWD'], ['Everett']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tzwf5d/respect_lee_everett_telltales_the_walking_dead/

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

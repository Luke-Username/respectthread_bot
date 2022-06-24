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

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Thor ?\((Norse)? Mythology']
],
'Norse Mythology',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/vii4fz/zeus_greek_mythology_vs_thor_norse_mythology/idd57z5/?context=3

########################################

id = get_rt_id(cur, 'Respect John Constantine (DC/Vertigo - Pre-Flashpoint)', 'https://redd.it/9xp0fr')
add_data(['Constantine'],
'John Constantine',
False,
False,
[
    ['Vertigo'], ['Flashpoint']
],
'Vertigo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/vh9fcd/john_constantine_vertigo_vs_freddy_krueger/id5wu0n/?context=3

########################################

id = get_rt_id(cur, 'Respect Rorgg, King of the Spider Men (Marvel, 616)', 'https://redd.it/vhasp5')
add_data(['Rorgg'],
'Rorgg',
False,
False,
[
    ['616'], ['Marvel']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhasp5/respect_rorgg_king_of_the_spider_men_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Master Chief! (Halo - Silver Timeline)', 'https://redd.it/vhcsre')
add_data(['Mas?ter Chiefs?'],
'Master Chief',
False,
False,
[
    ['Silver Timeline']
],
'Silver Timeline',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhcsre/respect_master_chief_halo_silver_timeline/

########################################

id = get_rt_id(cur, 'Respect Miles Morales, Thor (Marvel, What If...?)', 'https://redd.it/vhe5od')
add_data(['Miles? Morales'],
'Miles Morales',
False,
False,
[
    ['Thor', 'What If']
],
'What if...?',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhe5od/respect_miles_morales_thor_marvel_what_if/

########################################

id = get_rt_id(cur, 'Respect Pieck Finger, the Cart Titan! (Attack on Titan [Anime])', 'https://redd.it/vhjb7d')
add_data(['Pieck Finger'],
'Pieck Finger',
False,
True,
[
    ['Attack on Titan'], ['Shingeki no Kyojin'], ['AOT'], ['SnK']
],
'Attack on Titan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhjb7d/respect_pieck_finger_the_cart_titan_attack_on/

add_data(['Cart Titan'],
'Cart Titan',
False,
True,
[
    ['Attack on Titan'], ['Shingeki no Kyojin'], ['AOT'], ['SnK']
],
'Attack on Titan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhjb7d/respect_pieck_finger_the_cart_titan_attack_on/

########################################

id = get_rt_id(cur, 'Respect the Allosaurus (Dino Crisis 2)', 'https://redd.it/vhybof')
add_data(['Allosaurus'],
'Allosaurus',
False,
False,
[
    ['Dino Crisis']
],
'Dino Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhybof/respect_the_allosaurus_dino_crisis_2/

########################################

id = get_rt_id(cur, 'Respect Spamton NEO (Deltarune)', 'https://redd.it/vhz1j4')
add_data(['Spamton'],
'Spamton',
False,
True,
[
    ['Deltarune'], ['Spamton NEO']
],
'Deltarune',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vhz1j4/respect_spamton_neo_deltarune/

########################################

id = get_rt_id(cur, 'Respect Bio-Broly (Dragon Ball Z, Movies)', 'https://redd.it/vi4x15')
add_data(['Bio(-| )Broly'],
'Bio-Broly',
False,
True,
[
    ['Dragon ?Ball']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vi4x15/respect_biobroly_dragon_ball_z_movies/

########################################

id = get_rt_id(cur, 'Respect Godbert Manderville! (Final Fantasy XIV)', 'https://redd.it/vi9iu2')
add_data(['Godbert'],
'Godbert',
False,
True,
[
    ['Manderville'], ['FFXIV'], ['Final Fantasy']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vi9iu2/respect_godbert_manderville_final_fantasy_xiv/

########################################

id = get_rt_id(cur, 'Respect The Art of Witchcraft (American Dad!)', 'https://redd.it/virl8z')
add_data(['Art of Witchcraft'],
'Art of Witchcraft',
False,
False,
[
    ['American Dad']
],
'American Dad!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/virl8z/respect_the_art_of_witchcraft_american_dad/

########################################

id = get_rt_id(cur, 'Respect Heisuke Mashimo (Sakamoto Days)', 'https://redd.it/vj1vys')
add_data(['Heisuke Mashimo'],
'Heisuke Mashimo',
False,
True,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vj1vys/respect_heisuke_mashimo_sakamoto_days/

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

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

update_respectthread(cur, 13308, 'Respect Wong (Marvel Cinematic Universe)', 'https://redd.it/15eazy4')
update_respectthread(cur, 3327, 'Respect Shizuo Heiwajima (Durarara!!)', 'https://redd.it/15fmwhr')

########################################

id = get_rt_id(cur, 'Respect Unnamed Pokemon Hunter (Pokemon Anime: Aim To Be A Pokemon Master)', 'https://redd.it/15dlqy2')
add_data(['Pok(e|é)m(o|a)n Hunter'],
'Pokémon',
False,
False,
[
    ['Aim To Be A Pokemon Master']
],
'Aim To Be A Pokemon Master',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15dlqy2/respect_unnamed_pokemon_hunter_pokemon_anime_aim/

########################################

id = get_rt_id(cur, 'Respect The Mask! (The Mask: Animated Series)', 'https://redd.it/15dxt8a')
add_data(['The Mask'],
'The Mask',
False,
False,
[
    ['Animated Series']
],
'Animated Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15dxt8a/respect_the_mask_the_mask_animated_series/

########################################

id = get_rt_id(cur, 'Respect Mikoto Kibitsu! (Peach Boy Riverside)', 'https://redd.it/15e60h7')
add_data(['Mikoto Kibitsu'],
'Mikoto Kibitsu',
False,
True,
[
    ['Peach Boy Riverside']
],
'Peach Boy Riverside',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15e60h7/respect_mikoto_kibitsu_peach_boy_riverside/

########################################

id = get_rt_id(cur, 'Respect Lily Chilman, the Jungle Fury Yellow Ranger! (Power Rangers Jungle Fury)', 'https://redd.it/15e9ojw')
add_data(['Lily Chilman'],
'Lily Chilman',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15e9ojw/respect_lily_chilman_the_jungle_fury_yellow/

add_data(['Yellow Ranger'],
'Yellow Ranger',
False,
False,
[
    ['Jungle Fury']
],
'Power Rangers Jungle Fury',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15e9ojw/respect_lily_chilman_the_jungle_fury_yellow/

########################################

id = get_rt_id(cur, "Respect Oroku Saki, the Green Ranger Shredder (Mighty Morphin'' Power Rangers/Teenage Mutant Ninja Turtles)", 'https://redd.it/15ec1mn')
add_data(['Green Ranger Shredder'],
'Green Ranger Shredder',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15ec1mn/respect_oroku_saki_the_green_ranger_shredder/

########################################

id = get_rt_id(cur, 'Respect Scott Wozniak (Scott The Woz)', 'https://redd.it/15eigps')
add_data(['Scott the Woz'],
'Scott the Woz',
False,
True,
[
    ['Scott The Woz vs']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15eigps/respect_scott_wozniak_scott_the_woz/

########################################

id = get_rt_id(cur, 'Respect Ana Helstrom (Helstrom)', 'https://redd.it/15eptny')
add_data(['Ana Helstrom'],
'Ana Helstrom',
False,
True,
[
    ['\(Helstrom\)'], ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15eptny/respect_ana_helstrom_helstrom/

########################################

id = get_rt_id(cur, 'Respect Arion, Lord of Atlantis (DC Pre-Flashpoint)', 'https://redd.it/15fe8gd')
add_data(['Arion'],
'Arion',
False,
False,
[
    ['Pre(-| )?Flashpoint']
],
'Pre-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15fe8gd/respect_arion_lord_of_atlantis_dc_preflashpoint/

add_data(['Arion'],
'Arion',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['Arion the Immortal', 'DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15fe8gd/respect_arion_lord_of_atlantis_dc_preflashpoint/

########################################

id = get_rt_id(cur, 'Respect Moses Magnum (Marvel 616)', 'https://redd.it/15fe8kz')
add_data(['Moses Magnum'],
'Moses Magnum',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15fe8kz/respect_moses_magnum_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Elphaba (Wicked: The Life and Times of the Wicked Witch of the West)', 'https://redd.it/15fe8il')
add_data(['Elphaba'],
'Elphaba',
False,
False,
[
    ['Life and Times of the Wicked Witch of the West']
],
'Wicked: The Life and Times of the Wicked Witch of the West',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Troll King (Troll)', 'https://redd.it/15fgdle')
add_data(['Troll King'],
'Troll King',
False,
False,
[
    ['\(Troll\)'], ['Netflix']
],
'Troll',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15fgdle/respect_the_troll_king_troll/

########################################

id = get_rt_id(cur, 'Respect Bad Mr. Frosty (ClayFighter)', 'https://redd.it/15fva7a')
add_data(['Bad Mr\.? Frosty'],
'Bad Mr. Frosty',
False,
True,
[
    ['ClayFighter']
],
'ClayFighter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15fva7a/respect_bad_mr_frosty_clayfighter/

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

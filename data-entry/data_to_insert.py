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

update_respectthread(cur, 13595, "Respect Queen Maeve (Amazon''s The Boys)", 'https://redd.it/wwjhel')

########################################

add_data(['Wolverines'],
'Wolverines',
False,
False,
[
    ['Hugh|Jackman'], ['FOX'], ['Foxverse'],
    ['X(-| )?Men (Movie|Film)s?'], ['X-?Men Cinematic Universe']
],
'FOX',
'{158}'
)
#https://www.reddit.com/r/whowouldwin/comments/wxi9wa/how_many_fox_wolverines_does_it_take_to_kill_mcu/

########################################

add_data(['Cracker'],
'Cracker',
False,
False,
[
    ['One Piece', 'Doflamingo']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/wx6bmr/one_piece_doflamingo_vs_cracker/ilp82vr/?context=3

add_data(['Cracker'],
'Cracker',
False,
False,
[
    ['Cracker ?\(One Piece']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/wx6bmr/one_piece_doflamingo_vs_cracker/ilp82vr/?context=3

########################################

id = get_rt_id(cur, 'Respect Molly Carpenter (The Dresden Files)', 'https://redd.it/ww6bd5')
add_data(['Molly'],
'Molly',
False,
False,
[
    ['Molly Carpenter'], ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ww6bd5/respect_molly_carpenter_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect the Ghost of Harry Dresden (The Dresden Files)', 'https://redd.it/wx1pj9')
add_data(['Ghost of Harry Dresden', "Harry Dresden''?s Ghost"],
'Ghost of Harry Dresden',
False,
True,
[
    ['Dresden( Files|verse)']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wx1pj9/respect_the_ghost_of_harry_dresden_the_dresden/

########################################

id = get_rt_id(cur, 'Respect Voolvif Monn (Star Wars Legends)', 'https://redd.it/ww9zwh')
add_data(['Voolvif Monn'],
'Voolvif Monn',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ww9zwh/respect_voolvif_monn_star_wars_legends/

########################################

id = get_rt_id(cur, 'Respect Molly McGee! (The Ghost and Molly McGee)', 'https://redd.it/wwcy1y')
add_data(['Molly McGee'],
'Molly McGee',
False,
True,
[
    ['Ghost']
],
'The Ghost and Molly McGee',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wwcy1y/respect_molly_mcgee_the_ghost_and_molly_mcgee/

########################################

id = get_rt_id(cur, 'Respect General Zod, Avruskin (DC, Post-Crisis)', 'https://redd.it/wwzdga')
add_data(['Zod'],
'General Zod',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wwzdga/respect_general_zod_avruskin_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Duplicate Vegeta (Dragon Ball Super - Anime)', 'https://redd.it/wx265m')
add_data(['Duplicate Vegeta'],
'Duplicate Vegeta',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wx265m/respect_duplicate_vegeta_dragon_ball_super_anime/

add_data(['Copy(-| )Vegeta'],
'Copy-Vegeta',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wx265m/respect_duplicate_vegeta_dragon_ball_super_anime/

########################################

id = get_rt_id(cur, 'Respect Leonard Snart, Captain Cold (DC Post-Crisis)', 'https://redd.it/wxakmd')
add_data(['Captain Cold'],
'Captain Cold',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wxakmd/respect_leonard_snart_captain_cold_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect: Casey Jones! (Teenage Mutant Ninja Turtles 1987)', 'https://redd.it/wxn6k5')
add_data(['Casey Jones'],
'Casey Jones',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '1987'], ['TMNT', '1987']
],
'TMNT 1987',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wxn6k5/respect_casey_jones_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Fordo (Star Wars Legends)', 'https://redd.it/wxr2vr')
add_data(['Fordo'],
'Fordo',
False,
False,
[
    ['S(tar )?Wars'], ['Captain Fordo'], ['ARC(77)?']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wxr2vr/respect_fordo_star_wars_legends/

########################################

id = get_rt_id(cur, 'Respect The Golden Turd (American Dad!)', 'https://redd.it/wy5757')
add_data(['Golden Turd'],
'Golden Turd',
False,
True,
[
    ['American Dad'], ["Roger''?s?"]
],
'American Dad!',
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

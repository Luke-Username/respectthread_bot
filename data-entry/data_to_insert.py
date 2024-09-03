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

id = get_rt_id(cur, "[NSFW] Respect Emperor Caligula! (David Lapham''s Caligula)", 'https://redd.it/1f6fpye')
add_data(['Caligula'],
'Caligula',
False,
False,
[
    ['David Lapham']
],
"David Lapham''s Caligula",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6fpye/nsfw_respect_emperor_caligula_david_laphams/

########################################

id = get_rt_id(cur, "[NSFW] Respect Verraxis! (David Lapham''s Caligula: Heart of Rome)", 'https://redd.it/1f6uqcv')
add_data(['Verraxis'],
'Verraxis',
False,
False,
[
    ['David Lapham']
],
"David Lapham''s Caligula",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6uqcv/nsfw_respect_verraxis_david_laphams_caligula/

########################################

id = get_rt_id(cur, 'Respect Percy de Rolo! (The Legend of Vox Machina)', 'https://redd.it/1f6gfk0')
add_data(['Perc(y|ival) de Rolo'],
'Percy de Rolo',
False,
True,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6gfk0/respect_percy_de_rolo_the_legend_of_vox_machina/

add_data(['Percival'],
'Percival',
False,
False,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6gfk0/respect_percy_de_rolo_the_legend_of_vox_machina/


add_data(['Percy'],
'Percy',
False,
False,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6gfk0/respect_percy_de_rolo_the_legend_of_vox_machina/

########################################

id = get_rt_id(cur, 'Respect Grog Strongjaw! (The Legend of Vox Machina)', 'https://redd.it/1f6l15w')
add_data(['Grog Strongjaw'],
'Grog Strongjaw',
False,
True,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Grog'],
'Grog',
False,
False,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pike Trickfoot! (The Legend of Vox Machina)', 'https://redd.it/1f7b0td')
add_data(['Pike Trickfoot'],
'Pike Trickfoot',
False,
True,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Pike'],
'Pike',
False,
False,
[
    ['Vox Machina'], ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Predators (Predator Hunting Grounds)', 'https://redd.it/1f6pbdk')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Predator:? Hunting Grounds']
],
'Predator: Hunting Grounds',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f6pbdk/respect_the_predators_predator_hunting_grounds/

########################################

id = get_rt_id(cur, 'Respect Wally (Pokemon Adventures)', 'https://redd.it/1f7axek')
add_data(['Wally'],
'Wally',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7axek/respect_wally_pokemon_adventures/

########################################

id = get_rt_id(cur, 'Respect Emerald (Pokemon Adventures)', 'https://redd.it/1f7axhc')
add_data(['Emerald'],
'Emerald',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7axhc/respect_emerald_pokemon_adventures/

########################################

id = get_rt_id(cur, 'Respect Diabolico (Power Rangers Lightspeed Rescue)', 'https://redd.it/1f7axg1')
add_data(['Diabolico'],
'Diabolico',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7axg1/respect_diabolico_power_rangers_lightspeed_rescue/

########################################

id = get_rt_id(cur, 'Respect the MetalBeast (Project: MetalBeast)', 'https://redd.it/1f7f8e4')
add_data(['MetalBeast'],
'MetalBeast',
False,
False,
[
    ['Project:? MetalBeast']
],
'Project: MetalBeast',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7f8e4/respect_the_metalbeast_project_metalbeast/

########################################

id = get_rt_id(cur, "Respect Fetch (Five Nights at Freddy''s: Fazbear Frights)", 'https://redd.it/1f7f8fm')
add_data(['Fetch'],
'Fetch',
False,
False,
[
    ['Five Nights at Fredd(ys?|ies)'], ['FNAF\d?']
],
'FNAF',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7f8fm/respect_fetch_five_nights_at_freddys_fazbear/

########################################

id = get_rt_id(cur, 'Shin Getter Robo (shin Getter Robo vs Neo Getter Robo OVA)', 'https://redd.it/1f7pi6b')
add_data(['Shin Getter Robo'],
'Shin Getter Robo',
False,
False,
[
    ['Neo Getter Robo']
],
'Shin Getter Robo vs Neo Getter Robo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1f7pi6b/shin_getter_robo_shin_getter_robo_vs_neo_getter/

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

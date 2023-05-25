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

add_data(['Dagger'],
'Dagger',
False,
False,
[
    ['Dagger ?\((Marvel)? 616\)']
],
'616',
'{2435}'
)
#https://www.reddit.com/r/whowouldwin/comments/11ttj8t/lady_nagantmha_vs_daggermarvel_616/jlfrxdn/?context=3

########################################

add_data(['Wallace West'],
'Wallace West',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{1591}'
)
#https://www.reddit.com/r/whowouldwin/comments/13rgal3/which_character_would_last_longest_in_the_naruto/jllat71/?context=3

########################################

id = get_rt_id(cur, 'Respect Marci Camp, Bulldozer (Marvel, Earth-616)', 'https://redd.it/13qrrry')
add_data(['Bulldozer'],
'Bulldozer',
False,
False,
[
    ['Bulldozer ?\((Marvel)? 616\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qr74j/respect_savitar_arrowverse/

add_data(['Marci Camp'],
'Marci Camp',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qr74j/respect_savitar_arrowverse/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 35: the Hydro Armor Mark III (Marvel, Earth-616)', 'https://redd.it/13rfkjr')
add_data(['Hydro Armor Mark III'],
'Hydro Armor Mark III',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13rfkjr/respect_iron_man_model_35_the_hydro_armor_mark/

########################################

add_data(['Apocalyps?e'],
'Apocalypse',
False,
False,
[
    ['Apocalyps?e vs|vs\.? Apocalyps?e', 'Marvel comics? versions?']
],
'616',
'{2392}'
)
#https://www.reddit.com/r/whowouldwin/comments/13oxqgy/dr_doom_vs_apocalypse/jl6mw4i/?context=3

########################################

id = get_rt_id(cur, 'Respect Dracula (Blade: Trinity)', 'https://redd.it/13o7llv')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Blade:? Trinity']
],
'Blade: Trinity',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13o7llv/respect_dracula_blade_trinity/

########################################

id = get_rt_id(cur, 'Respect Donkey Kong (The Super Mario Bros. Movie)', 'https://redd.it/13p3k6d')
add_data(['Donkey Kong'],
'Donkey Kong',
False,
False,
[
    ['Mario( Bros\\.?)? Movie']
],
'The Super Mario Bros. Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13p3k6d/respect_donkey_kong_the_super_mario_bros_movie/

########################################

id = get_rt_id(cur, 'Respect Mecha Shark! (Mega Shark vs Mecha Shark)', 'https://redd.it/13qa0zq')
add_data(['Mecha Shark'],
'Mecha Shark',
False,
False,
[
    ['Mega Shark vs Mecha Shark']
],
'Mega Shark vs Mecha Shark',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qa0zq/respect_mecha_shark_mega_shark_vs_mecha_shark/

########################################

id = get_rt_id(cur, 'Respect Rodney Casares (Ex-Heroes)', 'https://redd.it/13qbox6')
add_data(['Rodney Casares'],
'Rodney Casares',
False,
True,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qbox6/respect_rodney_casares_exheroes/

########################################

id = get_rt_id(cur, 'Respect Midknight (Ex-Heroes)', 'https://redd.it/13qcbq6')
add_data(['Midknight'],
'Midknight',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qcbq6/respect_midknight_exheroes/

########################################

id = get_rt_id(cur, 'Respect Banzai (Ex-Heroes)', 'https://redd.it/13qcqy3')
add_data(['Banzai'],
'Banzai',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qcqy3/respect_banzai_exheroes/

########################################

id = get_rt_id(cur, 'Respect Ethan James, the Blue Dino Ranger (Power Rangers Dino Thunder)', 'https://redd.it/13qjuzv')
add_data(['Ethan James'],
'Ethan James',
False,
False,
[
    ['Power Rangers?'], ['Dino Thunder']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qjuzv/respect_ethan_james_the_blue_dino_ranger_power/

add_data(['Ethan'],
'Ethan',
False,
False,
[
    ['Dino Thunder Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qjuzv/respect_ethan_james_the_blue_dino_ranger_power/

add_data(['Blue Dino Ranger'],
'Blue Dino Ranger',
False,
True,
[
    ['Dino Thunder Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qjuzv/respect_ethan_james_the_blue_dino_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Kira Ford, the Yellow Dino Ranger (Power Rangers Dino Thunder)', 'https://redd.it/13qjv18')
add_data(['Kira Ford'],
'Kira Ford',
False,
True,
[
    ['Power Rangers?'], ['Dino Thunder']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qjuzv/respect_ethan_james_the_blue_dino_ranger_power/

add_data(['Kira'],
'Kira',
False,
False,
[
    ['Dino Thunder Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qjuzv/respect_ethan_james_the_blue_dino_ranger_power/

add_data(['Yellow Dino Ranger'],
'Yellow Dino Ranger',
False,
True,
[
    ['Dino Thunder Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Savitar (Arrowverse)', 'https://redd.it/13qr74j')
add_data(['Savitar'],
'Savitar',
False,
False,
[
    ['(Fl)?arrow(-| )?verse'], ['(DC)?CW'], ['DC ?TV']
],
'CW Arrowverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qr74j/respect_savitar_arrowverse/

########################################

id = get_rt_id(cur, 'Respect Dick Grayson, Superwing! (DC Comics, New52/Rebirth)', 'https://redd.it/13qvz0g')
add_data(['Dick Grayson'],
'Dick Grayson',
False,
False,
[
    ['Superwing']
],
'Superwing',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13qvz0g/respect_dick_grayson_superwing_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Bruce Wayne, Super-Bat (DC, Post Crisis)', 'https://redd.it/13riig4')
add_data(['Bruce Wayne'],
'Bruce Wayne',
False,
False,
[
    ['Super-Bat']
],
'Super-Bat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13riig4/respect_bruce_wayne_superbat_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect Waylon Jones, the Killer Croc (DC Comics: Earth One)', 'https://redd.it/13rhxsm')
add_data(['Killer Croc'],
'Killer Croc',
False,
False,
[
    ['Earth One']
],
'Earth One',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13rhxsm/respect_waylon_jones_the_killer_croc_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Bob Lee Swagger! (Shooter [2007])', 'https://redd.it/13rh75n')
add_data(['Bob Lee Swagger'],
'Bob Lee Swagger',
False,
True,
[
    ['Shooter']
],
'Shooter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13rh75n/respect_bob_lee_swagger_shooter_2007/

########################################

id = get_rt_id(cur, 'Respect Woltekamui! (Ragna Crimson)', 'https://redd.it/13rn22n')
add_data(['Woltekamui'],
'Woltekamui',
False,
True,
[
    ['Ragna Crimson']
],
'Ragna Crimson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13rn22n/respect_woltekamui_ragna_crimson/

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

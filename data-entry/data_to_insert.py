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

update_respectthread(cur, 5821, 'Respect Harry Potter!', 'https://redd.it/3pwwx2')

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['Fox X(-| )?men']
],
'FOX',
'{158}'
)
#https://www.reddit.com/r/whowouldwin/comments/1el9bk7/who_would_win_at_arm_wrestling_chewbacca_or/lgq6bgv/?context=3

########################################

id = get_rt_id(cur, 'Respect Chad Lee, the Blue Lightspeed Ranger (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ei8wsc')
add_data(['Chad Lee'],
'Chad Lee',
False,
False,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ei8wsc/respect_chad_lee_the_blue_lightspeed_ranger_power/

add_data(['Blue Lightspeed Ranger'],
'Blue Lightspeed Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ei8wsc/respect_chad_lee_the_blue_lightspeed_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Kelsey Winslow, the Yellow Lightspeed Ranger (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ekono0')
add_data(['Kelsey Winslow'],
'Kelsey Winslow',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ei8wsc/respect_chad_lee_the_blue_lightspeed_ranger_power/

add_data(['Yellow Lightspeed Ranger'],
'Yellow Lightspeed Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ekono0/respect_kelsey_winslow_the_yellow_lightspeed/

########################################

id = get_rt_id(cur, 'Respect the Supertrain Megazord (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ej2gf2')
add_data(['Supertrain Megazord'],
'Supertrain Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ej2gf2/respect_the_supertrain_megazord_power_rangers/

########################################

id = get_rt_id(cur, 'Respect the Lightspeed Megazord (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ei8wv9')
add_data(['Lightspeed Megazord'],
'Lightspeed Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ei8wv9/respect_the_lightspeed_megazord_power_rangers/

########################################

id = get_rt_id(cur, 'Respect the Omega Megazord (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ekonpw')
add_data(['Omega Megazord'],
'Omega Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ekonpw/respect_the_omega_megazord_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Joel Rawlings, the Green Lightspeed Rescue (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ej2ge1')
add_data(['Joel Rawlings'],
'Joel Rawlings',
False,
False,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ei8wsc/respect_chad_lee_the_blue_lightspeed_ranger_power/

add_data(['Green Lightspeed Rescue'],
'Green Lightspeed Rescue',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ej2ge1/respect_joel_rawlings_the_green_lightspeed_rescue/

########################################

id = get_rt_id(cur, 'Respect Darts Grumer! (Bakuage Sentai BoonBoomger)', 'https://redd.it/1el966h')
add_data(['Darts Grumer'],
'Darts Grumer',
False,
True,
[
    ['Bakuage Sentai BoonBoomger']
],
'Bakuage Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1el966h/respect_darts_grumer_bakuage_sentai_boonboomger/

########################################

id = get_rt_id(cur, 'Respect Edwin (Klown Kamp Massacre)', 'https://redd.it/1eicmom')
add_data(['Edwin'],
'Edwin',
False,
False,
[
    ['Klown Kamp Massacre']
],
'Klown Kamp Massacre',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eicmom/respect_edwin_klown_kamp_massacre/

########################################

id = get_rt_id(cur, 'Respect SCP-409, Contagious Crystal (SCP Foundation)', 'https://redd.it/1eikq7c')
add_data(['SCP ?(-| )? ?409'],
'SCP-409',
False,
True,
[
    ['Contagious Crystal']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eikq7c/respect_scp409_contagious_crystal_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Jinora (The Legend of Korra)', 'https://redd.it/1eitxyu')
add_data(['Jinora'],
'Jinora',
False,
False,
[
    ['Korra'], ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eitxyu/respect_jinora_the_legend_of_korra/

########################################

id = get_rt_id(cur, 'Respect Arnold Wesker, the Ventriloquist (DC Comics, Post Crisis)', 'https://redd.it/1ej5x59')
add_data(['Arnold Wesker'],
'Arnold Wesker',
False,
False,
[
    ['DC'], ['Ventriloquist']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ej5x59/respect_arnold_wesker_the_ventriloquist_dc_comics/

add_data(['Arnold Wesker'],
'Arnold Wesker',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ej5x59/respect_arnold_wesker_the_ventriloquist_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Wade Eiling, The General (DC Post Crisis)', 'https://redd.it/1ek6g8l')
add_data(['Wade Eiling'],
'General Wade Eiling',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Wade Eiling'],
'General Wade Eiling',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Shaggy Man (DC Post Crisis)', 'https://redd.it/1ek6inb')
add_data(['Shaggy Man'],
'Shaggy Man',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['Doomsday'], ['Wonder Woman', 'Superman']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Shaggy Man'],
'Shaggy Man',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ek6inb/respect_the_shaggy_man_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect Luna Snow! (Marvel 616)', 'https://redd.it/1ejpz67')
add_data(['Luna Snow'],
'Luna Snow',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ejpz67/respect_luna_snow_marvel_616/

########################################

id = get_rt_id(cur, 'Respect S.C.A.T. (Night Trap)', 'https://redd.it/1ejvx9q')
add_data(['S\.C\.A\.T'],
'S.C.A.T.',
False,
False,
[
    ['Night Trap']
],
'Night Trap',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ejvx9q/respect_scat_night_trap/

########################################

id = get_rt_id(cur, 'Respect Ceroba Ketsukane! (Undertale Yellow)', 'https://redd.it/1ek0tr7')
add_data(['Ceroba Ketsukane'],
'Ceroba Ketsukane',
False,
True,
[
    ['Undertale Yellow']
],
'Undertale Yellow',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ek0tr7/respect_ceroba_ketsukane_undertale_yellow/

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

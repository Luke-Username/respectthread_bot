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

update_respectthread(cur, 14384, 'Respect Marisa (minusT Animations)', 'https://redd.it/ygge4b')
update_respectthread(cur, 14383, 'Respect Reimu (minusT Animations)', 'https://redd.it/ygge9k')
update_respectthread(cur, 3963, 'Respect Might Guy! (Naruto)', 'https://redd.it/yhf02s')
update_respectthread(cur, 6476, 'Respect Liliana Vess! (Magic: The Gathering)', 'https://redd.it/yhynb6')

########################################

add_data(['Pure Blood'],
'Pure Blood',
False,
False,
[
    ['One(-| )Punch Man'], ['OPM']
],
'One Punch Man',
'{4119}'
)
#

########################################

add_data(['Alucard'],
'Alucard',
False,
False,
[
    ['Seras']
],
'Hellsing',
'{3476}'
)
#https://www.reddit.com/r/whowouldwin/comments/yi610d/dio_vs_alucard_vs_muzanbut_with_a_twist/iuh8dfw/?context=3

########################################

add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Vampire:? The Masquerade'], ['VTM']
],
'Vampire: The Masquerade',
'{3476}'
)
#https://www.reddit.com/r/whowouldwin/comments/yi7ko7/whod_win_alucard_hellsing_vs_the_eldesttzimisce/iuhd4ln/?context=3

########################################

add_data(['Terraria Player'],
'Terrarian',
False,
True,
[
    ['default']
],
'Terraria',
'{5497}'
)
#https://www.reddit.com/r/whowouldwin/comments/yhm76m/the_dragonborn_vs_a_maxed_melee_terraria_player/

########################################

id = get_rt_id(cur, 'Respect Lord Morbius (Marvel Earth-37072)', 'https://redd.it/yggrw4')
add_data(['Lord Morbius'],
'Lord Morbius',
False,
True,
[
    ['37072']
],
'37072',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yggrw4/respect_lord_morbius_marvel_earth37072/

########################################

id = get_rt_id(cur, 'Respect The Creature Commandos (DC Pre-Crisis)', 'https://redd.it/ygxg0g')
add_data(['Creature Commandos'],
'Creature Commandos',
True,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ygxg0g/respect_the_creature_commandos_dc_precrisis/

add_data(['Creature Commandos'],
'Creature Commandos',
True,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ygxg0g/respect_the_creature_commandos_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Dark Carnage (Marvel, Earth-616)', 'https://redd.it/yhancm')
add_data(['Dark Carnage'],
'Dark Carnage',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yhancm/respect_dark_carnage_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect the Silence Priests (Doctor Who)', 'https://redd.it/yhewh3')
add_data(['Silence Priests?'],
'Silence Priests',
False,
False,
[
    ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yhewh3/respect_the_silence_priests_doctor_who/

########################################

id = get_rt_id(cur, 'Respect Consul of Omashu! (Avatar: The Legend of Aang Videogame)', 'https://redd.it/yhjsns')
add_data(['Consul'],
'Consul',
False,
False,
[
    ['Avatar'], ['A?TLA'], ['Air(-| )bender']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yhjsns/respect_consul_of_omashu_avatar_the_legend_of/

########################################

id = get_rt_id(cur, "Respect the Bride of Chucky, Tiffany Valentine! (Child''s Play)", 'https://redd.it/yhny4r')
add_data(['Tiffany Valentine'],
'Tiffany Valentine',
False,
True,
[
    ["Child''?s Play"]
],
"Child''s Play",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yhny4r/respect_the_bride_of_chucky_tiffany_valentine/

########################################

id = get_rt_id(cur, 'Respect Cindy Campbell (Scary Movie)', 'https://redd.it/yi5s6r')
add_data(['Cindy Campbell'],
'Cindy Campbell',
False,
True,
[
    ['Scary Movie']
],
'Scary Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yi5s6r/respect_cindy_campbell_scary_movie/

########################################

id = get_rt_id(cur, 'Respect Brenda Meeks', 'https://www.reddit.com/r/respectthreads/comments/yi5s6r/respect_cindy_campbell_scary_movie/iuh7efx/')
add_data(['Brenda Meeks'],
'Brenda Meeks',
False,
True,
[
    ['Scary Movie']
],
'Scary Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yi5s6r/respect_cindy_campbell_scary_movie/iuh7efx/

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

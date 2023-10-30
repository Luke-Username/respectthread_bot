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

update_respectthread(cur, 6020, "[Warhammer 40k] New respect thread for the C''tan", 'https://redd.it/17hw9hc')

########################################

id = get_rt_id(cur, 'Respect Officer Roger Mortis (Dead Heat)', 'https://redd.it/17hp0s2')
add_data(['Roger Mortis'],
'Roger Mortis',
False,
False,
[
    ['Dead Heat']
],
'Dead Heat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17hp0s2/respect_officer_roger_mortis_dead_heat/

########################################

id = get_rt_id(cur, 'Respect: Medusa! (Conan the Adventurer)', 'https://redd.it/17httlx')
add_data(['Medusa'],
'Medusa',
False,
False,
[
    ['Conan the Adventurer']
],
'Conan the Adventurer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17httlx/respect_medusa_conan_the_adventurer/

########################################

id = get_rt_id(cur, 'Respect Rouge the Bat (Speed Smackdown)', 'https://redd.it/17i3wjw')
add_data(['Ro(ug|gu)e the Bat'],
'Rouge the Bat',
False,
False,
[
    ['Speed Smackdown']
],
'Speed Smackdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17i3wjw/respect_rouge_the_bat_speed_smackdown/

########################################

id = get_rt_id(cur, 'Respect Catwoman (Speed Smackdown)', 'https://redd.it/17i3wlo')
add_data(['Cat(-| )?woman'],
'Catwoman',
False,
False,
[
    ['Speed Smackdown']
],
'Speed Smackdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17i3wlo/respect_catwoman_speed_smackdown/

########################################

id = get_rt_id(cur, 'Respect Mort (Discworld)', 'https://redd.it/17idzr1')
add_data(['Mort'],
'Mort',
False,
False,
[
    ['Discworld']
],
'Discworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17idzr1/respect_mort_discworld/

########################################

id = get_rt_id(cur, 'Respect The Red Death (Masque of the Red Death)', 'https://redd.it/17ietvq')
add_data(['Red Death'],
'Red Death',
False,
False,
[
    ['Masque of the Red Death']
],
'Masque of the Red Death',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ietvq/respect_the_red_death_masque_of_the_red_death/

########################################

id = get_rt_id(cur, 'Respect Chihiro Rokuhira (Kagurabachi)', 'https://redd.it/17ifba8')
add_data(['Chihiro Rokuhira'],
'Chihiro Rokuhira',
False,
True,
[
    ['Kagura ?bachi']
],
'Kagurabachi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ifba8/respect_chihiro_rokuhira_kagurabachi/

########################################

id = get_rt_id(cur, 'Respect Ruin! (Undead Unluck)', 'https://redd.it/17io55o')
add_data(['Ruin'],
'Ruin',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17io55o/respect_ruin_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Ruin! (Undead Unluck)', 'https://redd.it/17io55o')
add_data(['Ruin'],
'Ruin',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Super X (Godzilla Franchise, Heisei Continuity)', 'https://redd.it/17iuftr')
add_data(['Super X'],
'Super X',
False,
False,
[
    ['Heisei'], ['Godzilla']
],
'Godzilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17iuftr/respect_the_super_x_godzilla_franchise_heisei/

########################################

id = get_rt_id(cur, 'Respect Godzilla Junior (Godzilla Franchise, Heisei Continuity)', 'https://redd.it/17ivxb2')
add_data(['Godzilla Junior'],
'Godzilla Junior',
False,
True,
[
    ['Heisei']
],
'Godzilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ivxb2/respect_godzilla_junior_godzilla_franchise_heisei/

########################################

id = get_rt_id(cur, 'Respect The Golem (Der Golem)', 'https://redd.it/17j3ohm')
add_data(['Der Golem'],
'Der Golem',
False,
True,
[
    ['How He Came into the World']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17j3ohm/respect_the_golem_der_golem/

########################################

id = get_rt_id(cur, 'Respect IG-88 (Star Wars)', 'https://redd.it/17j6fse')
add_data(['IG(-| )88'],
'IG-88',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Damned Thing! (The Damned Thing)', 'https://redd.it/17j7ztd')
add_data(['The Damned Thing'],
'The Damned Thing',
False,
True,
[
    ['The Damned Thing ?\(The Damned Thing\)'], ['1893']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17j7ztd/respect_the_damned_thing_the_damned_thing/

########################################

id = get_rt_id(cur, 'Respect Garlic Jr! (Dragon Ball Z)', 'https://redd.it/17j9bfj')
add_data(['Garlic Jr'],
'Garlic Jr',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17j9bfj/respect_garlic_jr_dragon_ball_z/

########################################

id = get_rt_id(cur, 'Respect Red Ronin (Marvel Comics, Earth-616)', 'https://redd.it/17jkhhd')
add_data(['Red Ronin'],
'Red Ronin',
False,
False,
[
    ['616'], ['\(Marvel\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17jkhhd/respect_red_ronin_marvel_comics_earth616/

########################################

id = get_rt_id(cur, "Respect Golden Boy (Amazon''s The Boys: Gen V)", 'https://redd.it/17jlj76')
add_data(['Golden Boy'],
'Golden Boy',
False,
False,
[
    ['The Boys'], ['Gen V']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17jlj76/respect_golden_boy_amazons_the_boys_gen_v/

########################################

id = get_rt_id(cur, 'Respect the Lasser Glass! (Oculus)', 'https://redd.it/17jm3fa')
add_data(['Lasser Glass'],
'Lasser Glass',
False,
False,
[
    ['Oculus']
],
'Oculus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17jm3fa/respect_the_lasser_glass_oculus/

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

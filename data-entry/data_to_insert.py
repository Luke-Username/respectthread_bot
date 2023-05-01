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

update_respectthread(cur, 1493, 'Respect Batman (DC, Post-Flashpoint)', 'https://redd.it/1348ale')
update_respectthread(cur, 4433, 'Respect Sayaka Miki! (Puella Magi Madoka Magica)', 'https://redd.it/1349g95')
update_respectthread(cur, 4426, 'Respect Kyoko Sakura! (Puella Magi Madoka Magica)', 'https://redd.it/134bntd')
update_respectthread(cur, 110, 'Respect Max Dillon, Electro (The Amazing Spider-Man 2)', 'https://redd.it/134njd5')

########################################

id = get_rt_id(cur, 'Respect Lelouch vi Britannia! (Code Geass (Anime Timeline))', 'https://redd.it/133xio2')
add_data(['Lelouch'],
'Lelouch',
False,
True,
[
    ['Code Geass']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/133xio2/respect_lelouch_vi_britannia_code_geass_anime/

########################################

id = get_rt_id(cur, 'Respect Mipha (The Legend of Zelda: Breath of the Wild)', 'https://redd.it/1345259')
add_data(['Mipha'],
'Mipha',
False,
True,
[
    ['Zelda'], ['T?LOZ'],
    ['Breath of the Wild'], ['BOTW'], ['OOT'], ['princess(es)?'], ['Age of Calamity']
],
'Breath of the Wild',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1345259/respect_mipha_the_legend_of_zelda_breath_of_the/

########################################

id = get_rt_id(cur, 'Respect Daruk (The Legend of Zelda: Breath of the Wild)', 'https://redd.it/134528m')
add_data(['Daruk'],
'Daruk',
False,
True,
[
    ['Zelda'], ['T?LOZ'],
    ['Breath of the Wild'], ['BOTW'], ['Age of Calamity']
],
'Breath of the Wild',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134528m/respect_daruk_the_legend_of_zelda_breath_of_the/

########################################

id = get_rt_id(cur, 'Respect Revali (The Legend of Zelda: Breath of the Wild)', 'https://redd.it/13452bw')
add_data(['Revali'],
'Revali',
False,
True,
[
    ['Zelda'], ['T?LOZ'],
    ['Breath of the Wild'], ['BOTW'], ['Age of Calamity']
],
'Breath of the Wild',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13452bw/respect_revali_the_legend_of_zelda_breath_of_the/

########################################

id = get_rt_id(cur, 'Respect Urbosa (The Legend of Zelda: Breath of the Wild)', 'https://redd.it/13452jr')
add_data(['Urbosa'],
'Urbosa',
False,
True,
[
    ['Zelda'], ['T?LOZ'],
    ['Breath of the Wild'], ['BOTW'], ['Age of Calamity']
],
'Breath of the Wild',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13452jr/respect_urbosa_the_legend_of_zelda_breath_of_the/

########################################

id = get_rt_id(cur, 'Respect Weegee (Cartoon Fight Club)', 'https://redd.it/134bqqh')
add_data(['Weegee'],
'Weegee',
False,
False,
[
    ['Cartoon Fight Club']
],
'Cartoon Fight Club',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134bqqh/respect_weegee_cartoon_fight_club/

########################################

id = get_rt_id(cur, 'Respect Adam Park (Power Rangers)', 'https://redd.it/134i9wx')
add_data(['Adam Park'],
'Adam Park',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134i9wx/respect_adam_park_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Conner McKnight, the Red Dino Ranger (Power Rangers Dino Thunder)', 'https://redd.it/134i9zd')
add_data(['Conner McKnight'],
'Conner McKnight',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134i9zd/respect_conner_mcknight_the_red_dino_ranger_power/

add_data(['Red Dino Ranger'],
'Red Dino Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134i9zd/respect_conner_mcknight_the_red_dino_ranger_power/
########################################

id = get_rt_id(cur, 'Respect Utam (The Mighty Peking Man)', 'https://redd.it/134ia1l')
add_data(['Utam'],
'Utam',
False,
False,
[
    ['Mighty Peking Man']
],
'The Mighty Peking Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134ia1l/respect_utam_the_mighty_peking_man/

########################################

id = get_rt_id(cur, 'Respect Frank Drebin (The Naked Gun)', 'https://redd.it/134kasy')
add_data(['Frank Drebin'],
'Frank Drebin',
False,
True,
[
    ['Naked Gun']
],
'The Naked Gun',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/134kasy/respect_frank_drebin_the_naked_gun/

########################################

id = get_rt_id(cur, 'Respect Doshin the Love Giant (Doshin the Giant)', 'https://redd.it/13504d0')
add_data(['Doshin the( Love)? Giant'],
'Doshin the Love Giant',
False,
True,
[
    ['games?']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13504d0/respect_doshin_the_love_giant_doshin_the_giant/

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

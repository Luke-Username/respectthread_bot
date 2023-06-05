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

update_respectthread(cur, 21323, 'Respect Peacemaker (DC Post-Crisis)', 'https://redd.it/13yl067')
update_respectthread(cur, 2266, 'Respect Hobgoblin (Marvel 616)', 'https://redd.it/13yl07t')
update_respectthread(cur, 244, 'Respect Clint Barton, Hawkeye! (Marvel Cinematic Universe)', 'https://redd.it/13xvu4c')
update_respectthread(cur, 5430, 'Respect Luigi (Super Mario Bros.)', 'https://redd.it/1408n3p')

########################################

add_data(['Meta(-| )Cooler'],
'Meta-Cooler',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{20387}'
)
#https://www.reddit.com/r/whowouldwin/comments/13zm1ph/10_billion_metacoolers_vs_broly/jmrvom6/?context=3

########################################

id = get_rt_id(cur, 'Respect Alfred Pennyworth (DC Comics: Earth One)', 'https://redd.it/13yc220')
add_data(['Alfred Pennyworth'],
'Alfred Pennyworth',
False,
False,
[
    ['Earth One']
],
'Earth One',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13yc220/respect_alfred_pennyworth_dc_comics_earth_one/

########################################

id = get_rt_id(cur, 'Respect Tentionmaru! (Rock Hard Gladiators)', 'https://redd.it/13yc99u')
add_data(['Tentionmaru'],
'Tentionmaru',
False,
True,
[
    ['Rock Hard Gladiators'], ['RHG']
],
'RHG',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13yc99u/respect_tentionmaru_rock_hard_gladiators/

########################################

id = get_rt_id(cur, "Respect Spider-Man (Avengers: Earth''s Mightiest Heroes)", 'https://redd.it/13yc99u')
add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Avengers:? Earths? Mightiest Heroes'], ['Avengers:? Earth\'\'s Mightiest Heroes'], ['A(vengers)?: ?EMH'],
	["Earth''?s? Mightiest Heroes", 'Disney']
],
'Earth''s Mightiest Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ye7pc/respect_spiderman_avengers_earths_mightiest_heroes/

########################################

id = get_rt_id(cur, 'Respect Beast I, Goetia (Fate/Grand Order)', 'https://redd.it/13yfcnc')
add_data(['Goetia'],
'Goetia',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13yfcnc/respect_beast_i_goetia_fategrand_order/

########################################

id = get_rt_id(cur, 'Respect Godzilla! (Godzilla (Hanna-Barbera Cartoon))', 'https://redd.it/13yiuhy')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Hanna(-| )Barbera']
],
'Hanna-Barbera',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13yiuhy/respect_godzilla_godzilla_hannabarbera_cartoon/

########################################

id = get_rt_id(cur, 'Respect Payakan (Avatar)', 'https://redd.it/13ytnn5')
add_data(['Payakan'],
'Payakan',
False,
True,
[
    ['Avatar']
],
'Avatar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ytnn5/respect_payakan_avatar/

########################################

id = get_rt_id(cur, 'Respect Abominations! (Madness: Project Nexus)', 'https://redd.it/13ziiwm')
add_data(['Abominations'],
'Abominations',
False,
False,
[
    ['Madness Combat'], ['Project Nexus']
],
'Madness Combat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ziiwm/respect_abominations_madness_project_nexus/

########################################

id = get_rt_id(cur, 'Respect: Cato Sicarius (Warhammer 40k)', 'https://redd.it/13zwu80')
add_data(['Cato Sicarius'],
'Cato Sicarius',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13zwu80/respect_cato_sicarius_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Abdiel (Shin Megami Tensei V)', 'https://redd.it/140c4de')
add_data(['Abdiel'],
'Abdiel',
False,
False,
[
    ['S(hin)? ?M(egami)? ?T(ensei)?']
],
'Shin Megami Tensei',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/140c4de/respect_abdiel_shin_megami_tensei_v/

########################################

id = get_rt_id(cur, 'Respect Nahobino (Shin Megami Tensei V)', 'https://redd.it/140c960')
add_data(['Nahobino'],
'Nahobino',
False,
True,
[
    ['S(hin)? ?M(egami)? ?T(ensei)?']
],
'Shin Megami Tensei',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/140c960/respect_nahobino_shin_megami_tensei_v/

########################################

id = get_rt_id(cur, 'Respect Jennika (Teenage Mutant Ninja Turtles) [IDW Comics]', 'https://redd.it/140iark')
add_data(['Jennika'],
'Jennika',
False,
True,
[
    ['Teenaged? Mutant Ninja Turtles?', 'IDW'], ['TMNT', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/140iark/respect_jennika_teenage_mutant_ninja_turtles_idw/

########################################

id = get_rt_id(cur, "Respect Goldar (Mighty Morphin'' Power Rangers)", 'https://redd.it/13z9nw2')
add_data(['Goldar'],
'Goldar',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13z9nw2/respect_goldar_mighty_morphin_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Justin Stewart, the Blue Turbo Ranger (Power Rangers Turbo)', 'https://redd.it/141d084')
add_data(['Blue Turbo Ranger'],
'Blue Turbo Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/141d084/respect_justin_stewart_the_blue_turbo_ranger/

########################################

id = get_rt_id(cur, 'Respect The Spriggan, Yu Ominae (Spriggan, 2022)', 'https://redd.it/141ng7n')
add_data(['Yu Ominae'],
'Yu Ominae',
False,
True,
[
    ['Spriggan', '2022']
],
'Spriggan, 2022',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/141ng7n/respect_the_spriggan_yu_ominae_spriggan_2022/

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

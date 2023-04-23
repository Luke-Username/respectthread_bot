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

update_respectthread(cur, 6025, 'Respect: Kharn the Betrayer (Warhammer 40k)', 'https://redd.it/12q817t')
update_respectthread(cur, 1324, 'Respect Cinder Fall (RWBY)', 'https://redd.it/12qvfrf')
update_respectthread(cur, 100, 'Respect Tommy Oliver (Power Rangers)', 'https://redd.it/12ro2bo')
update_respectthread(cur, 15297, 'Respect Jason Lee Scott (Power Rangers)', 'https://redd.it/12w49oh')
update_respectthread(cur, 483, 'Respect King Kong, The Eighth Wonder of the World! (King Kong 2005)', 'https://redd.it/12sfa0q')
update_respectthread(cur, 2099, 'Respect Ghost Rider (Robbie Reyes) [616]', 'https://redd.it/12wa3zs')

########################################

add_data(['Barry All(e|a)n'],
'Barry Allen',
False,
False,
[
    ['Keaton'], ['ZSJL'], ['Snyder']
],
'DCEU',
'{21548}'
)
#https://www.reddit.com/r/respectthreads/comments/taz1sa/respect_the_flash_dceu/

add_data(['Flash'],
'Flash',
False,
False,
[
    ['Keaton'], ['ZSJL']
],
'DCEU',
'{21548}'
)
#https://www.reddit.com/r/respectthreads/comments/taz1sa/respect_the_flash_dceu/

########################################

id = get_rt_id(cur, 'Respect Sanford! (Madness Combat)', 'https://redd.it/12qm5n1')
add_data(['Sanford'],
'Sanford',
False,
False,
[
    ['Madness']
],
'Madness Combat',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yukihiko Higetsu, the End of Miracles! (Heir to the Stars: Adam Conquest)', 'https://redd.it/12qp7ht')
add_data(['Yukihiko Higetsu'],
'Yukihiko Higetsu',
False,
True,
[
    ['Suggs(verse)?'], ['Heir to the Stars']
],
'Suggsverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12qp7ht/respect_yukihiko_higetsu_the_end_of_miracles_heir/

########################################

id = get_rt_id(cur, 'Respect Bevis of Hampton (Bevis of Hampton)', 'https://redd.it/12qy8q7')
add_data(['Bevis of Hampton'],
'Bevis of Hampton',
False,
True,
[
    ['romance']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12qy8q7/respect_bevis_of_hampton_bevis_of_hampton/

########################################

id = get_rt_id(cur, 'Respect Suzaku Kururugi and the Lancelot! (Code Geass (Anime Timeline))', 'https://redd.it/12qyhj5')
add_data(['Suzaku'],
'Suzaku',
False,
False,
[
    ['Kururugi'], ['Lancelot']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12qyhj5/respect_suzaku_kururugi_and_the_lancelot_code/

########################################

id = get_rt_id(cur, 'Respect Porter Engle (Star Wars Canon)', 'https://redd.it/12r8h9j')
add_data(['Porter Engle'],
'Porter Engle',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12r8h9j/respect_porter_engle_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Gargoyle (Gargoyle of the Yoshinaga House)', 'https://redd.it/12ralmw')
add_data(['Gargoyle'],
'Gargoyle',
False,
False,
[
    ['Gargoyle of the Yoshinaga House']
],
'Gargoyle of the Yoshinaga House',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12ralmw/respect_gargoyle_gargoyle_of_the_yoshinaga_house/

########################################

id = get_rt_id(cur, 'Respect Rodrik “the Ruined” Forrester (Telltale’s Game of Thrones)', 'https://redd.it/12rg4zp')
add_data(['Rodrik'],
'Rodrik',
False,
False,
[
    ['Forrester'], ['Rodrik the Ruined'], ['Telltale']
],
"Telltale''s Game of Thrones",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12rg4zp/respect_rodrik_the_ruined_forrester_telltales/

########################################

id = get_rt_id(cur, 'Respect Billy Cranston, the Blue Ranger (Power Rangers)', 'https://redd.it/12sycpv')
add_data(['Billy Cranston'],
'Billy Cranston',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12sycpv/respect_billy_cranston_the_blue_ranger_power/

add_data(['Billy'],
'Billy',
False,
False,
[
    ['Power Rangers?'], ['Blue Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12sycpv/respect_billy_cranston_the_blue_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Kimberly Ann Hart, the Pink Ranger (Power Rangers)', 'https://redd.it/12tx6dx')
add_data(['Kimberly( Ann)? Hart'],
'Kimberly Ann Hart',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12tx6dx/respect_kimberly_ann_hart_the_pink_ranger_power/

add_data(['Kimberly'],
'Kimberly',
False,
False,
[
    ['Power Rangers?'], ['Pink Ranger']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12tx6dx/respect_kimberly_ann_hart_the_pink_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Trey of Triforia (Power Rangers Zeo)', 'https://redd.it/12v0jzi')
add_data(['Trey of Triforia'],
'Trey of Triforia',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12v0jzi/respect_trey_of_triforia_power_rangers_zeo/

########################################

id = get_rt_id(cur, 'Respect Joe Biden (The Stars and Strifes)', 'https://redd.it/12rszjy')
add_data(['Joe Biden'],
'Joe Biden',
False,
False,
[
    ['Stars and Strifes']
],
'The Stars and Strifes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12rszjy/respect_joe_biden_the_stars_and_strifes/

########################################

id = get_rt_id(cur, 'Respect Barack Obama (The Stars and Strifes)', 'https://redd.it/12rt1fp')
add_data(['Obama'],
'Obama',
False,
False,
[
    ['Stars and Strifes']
],
'The Stars and Strifes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12rt1fp/respect_barack_obama_the_stars_and_strifes/

########################################

id = get_rt_id(cur, 'Respect Donald Trump (The Stars and Strifes)', 'https://redd.it/12rt2o5')
add_data(['Donald Trump'],
'Donald Trump',
False,
False,
[
    ['Stars and Strifes']
],
'The Stars and Strifes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12rt2o5/respect_donald_trump_the_stars_and_strifes/

########################################

id = get_rt_id(cur, 'Respect Shaggy (The Stars and Strifes)', 'https://redd.it/12rt48a')
add_data(['Shaggy'],
'Shaggy',
False,
False,
[
    ['Stars and Strifes']
],
'The Stars and Strifes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12rt48a/respect_shaggy_the_stars_and_strifes/

########################################

id = get_rt_id(cur, 'Respect Lara Croft! (Tomb Raider (2018))', 'https://redd.it/12s3y7l')
add_data(['Lara Croft'],
'Lara Croft',
False,
False,
[
    ['2018']
],
'Tomb Raider, 2018',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12s3y7l/respect_lara_croft_tomb_raider_2018/

########################################

id = get_rt_id(cur, 'Respect Summer Atler! (The Candy Shop War)', 'https://redd.it/12sab8y')
add_data(['Summer Atler'],
'Summer Atler',
False,
True,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12sab8y/respect_summer_atler_the_candy_shop_war/

########################################

id = get_rt_id(cur, 'Respect: Talos Valcoran, the Soul Hunter (Warhammer 40k)', 'https://redd.it/12sjdyl')
add_data(['Talos Valcoran'],
'Talos Valcoran',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12sjdyl/respect_talos_valcoran_the_soul_hunter_warhammer/

########################################

id = get_rt_id(cur, 'Respect Lim Lau (Chili and the Chocolate Factory: Fudge Revelation)', 'https://redd.it/12sytpd')
add_data(['Lim Lau'],
'Lim Lau',
False,
False,
[
    ['Chili and the Chocolate Factory']
],
'Chili and the Chocolate Factory',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12sytpd/respect_lim_lau_chili_and_the_chocolate_factory/

########################################

id = get_rt_id(cur, 'Respect Dr. Vegapunk! (One Piece)', 'https://redd.it/12t7rl7')
add_data(['Vegapunk'],
'Vegapunk',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12t7rl7/respect_dr_vegapunk_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Intruder (The Mandela Catalogue)', 'https://redd.it/12unaay')
add_data(['The Intruder'],
'The Intruder',
False,
False,
[
    ['Mandela Catalogue']
],
'The Mandela Catalogue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12unaay/respect_the_intruder_the_mandela_catalogue/

########################################

id = get_rt_id(cur, 'Respect Freedom (Monument Mythos)', 'https://redd.it/12v49kl')
add_data(['Freedom'],
'Freedom',
False,
False,
[
    ['Monument Mythos'], ['Nixonverse']
],
'The Monument Mythos',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12v49kl/respect_freedom_monument_mythos/

########################################

id = get_rt_id(cur, 'Respect The Last Son Of Alcatraz. (Monument Mythos)', 'https://redd.it/12whrxc')
add_data(['Last Son'],
'Last Son',
False,
False,
[
    ['Monument Mythos'], ['Nixonverse'],
    ['Alcatraz']
],
'The Monument Mythos',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12whrxc/respect_the_last_son_of_alcatraz_monument_mythos/

########################################

id = get_rt_id(cur, 'Respect the D-Day Knight (Monument Mythos)', 'https://redd.it/12w5jul')
add_data(['D(-| )Day Knight'],
'D-Day Knight',
False,
True,
[
    ['Monument Mythos'], ['Nixonverse']
],
'The Monument Mythos',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12w5jul/respect_the_dday_knight_monument_mythos/

########################################

id = get_rt_id(cur, 'Respect Richard Nixon/The Moon God (Monument Mythos)', 'https://redd.it/12wna1g')
add_data(['Nixon'],
'Nixon',
False,
False,
[
    ['Monument Mythos'], ['Nixonverse']
],
'The Monument Mythos',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12wna1g/respect_richard_nixonthe_moon_god_monument_mythos/

########################################

id = get_rt_id(cur, 'Respect the Air Force One Angel (Monument Mythos)', 'https://redd.it/12vj08u')
add_data(['Air Force One Angel'],
'Air Force One Angel',
False,
True,
[
    ['Monument Mythos'], ['Nixonverse']
],
'The Monument Mythos',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12vj08u/respect_the_air_force_one_angel_monument_mythos/

########################################

id = get_rt_id(cur, 'Respect Entity Zero (Creepypasta)', 'https://redd.it/12vf3iz')
add_data(['Entity Zero'],
'Entity Zero',
False,
False,
[
    ['Creepypasta']
],
'Creepypasta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12vf3iz/respect_entity_zero_creepypasta/

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

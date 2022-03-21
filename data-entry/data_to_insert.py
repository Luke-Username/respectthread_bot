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

update_respectthread(cur, 5382, 'Respect Sly Cooper (Sly Cooper)', 'https://redd.it/thtq1p')
update_respectthread(cur, 5377, 'Respect Bentley (Sly Cooper)', 'https://redd.it/tio46a')
update_respectthread(cur, 5381, 'Respect Murray (Sly Cooper)', 'https://redd.it/tio5l9')
update_respectthread(cur, 17514, "Respect Afiko The Betrayer (Avatar: The Last Airbender''s Official TCG)", 'https://redd.it/tikeo1')
update_respectthread(cur, 3543, "Respect Rudol von Stroheim (Jojo''s Bizarre Adventure)", 'https://redd.it/tiuj5c')

########################################

add_data(['Madoka Magica'],
'Madoka Magica',
False,
False,
[
    ['Goddess']
],
'',
'{4428}'
)
#https://www.reddit.com/r/whowouldwin/comments/thnmjn/would_madoka_magica_goddess_form_win_to_giorno/i1cffyv/?context=3

########################################

add_data(['Iron(-| )?Man'],
'Iron Man',
False,
False,
[
    ['RDJ'], ['Downey']
],
'MCU',
'{247}'
)
#https://www.reddit.com/r/whowouldwin/comments/tihl6n/andrew_garfield_spiderman_vs_rdj_ironman/

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['MCU'], ['Marvel Cinematic Universe']
],
'FOX',
'{158}'
)
#https://www.reddit.com/r/whowouldwin/comments/thzvyx/wolverine_deadpool_and_black_noir_vs_the_black/i1bbwqd/?context=3

########################################

id = get_rt_id(cur, 'Respect Victor Von Doom (Marvel, Earth-14412)', 'https://redd.it/thvuyb')
add_data(['Doom Supreme'],
'Doom Supreme',
False,
True,
[
    ['14412']
],
'14412',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/thvuyb/respect_victor_von_doom_marvel_earth14412/

add_data(['Victor Von Doom'],
'Doctor Doom',
False,
False,
[
    ['14412']
],
'14412',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/thvuyb/respect_victor_von_doom_marvel_earth14412/

########################################

id = get_rt_id(cur, 'Respect Victor Von Doom (Marvel, Earth-14412)', 'https://redd.it/thvuyb')
add_data(['Old Woman Laura'],
'Old Woman Laura',
False,
True,
[
    ['18366']
],
'18366',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/thw1zb/respect_old_woman_laura_marvel_earth18366/

########################################

id = get_rt_id(cur, 'Respect Miyamoto Usagi II (Space Usagi)', 'https://redd.it/thywec')
add_data(['Miyamoto Usagi'],
'Miyamoto Usagi',
False,
False,
[
    ['Space Usagi']
],
'Space Usagi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/thywec/respect_miyamoto_usagi_ii_space_usagi/

########################################

id = get_rt_id(cur, 'Respect the Fallen One (Marvel, Thanos Wins)', 'https://redd.it/ti10ci')
add_data(['Fallen One'],
'Fallen One',
False,
False,
[
    ['Thanos Wins'], ['Norrin'], ['Silver Surfer']
],
'Thanos Wins',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Ozai''s Governor of Omashu (ATLA: The Burning Earth)", 'https://redd.it/ti11kz')
add_data(['Governor'],
'Governor',
False,
False,
[
    ['Avatar|A?TLA', 'Burning Earth']
],
'A:TLA - The Burning Earth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ti11kz/respect_ozais_governor_of_omashu_atla_the_burning/

########################################

id = get_rt_id(cur, 'Respect Nite Owl II (Watchmen, 2009 film)', 'https://redd.it/ti15tb')
add_data(['Nite Owl'],
'Nite Owl',
False,
False,
[
    ['Watchmen', '2009'], ['Watchmen (movie|film)s?'], ['movie|film', 'Rorsc?hach'], ['(movie|film) Nite Owl']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ti15tb/respect_nite_owl_ii_watchmen_2009_film/

########################################

id = get_rt_id(cur, 'Respect Little Mac and the WVBA Boxers! (Nintendo Comics System)', 'https://redd.it/ti881d')
add_data(['Little Mac'],
'Little Mac',
False,
False,
[
    ['Nintendo Comics System']
],
'Nintendo Comics System',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ti881d/respect_little_mac_and_the_wvba_boxers_nintendo/

########################################

id = get_rt_id(cur, 'Respect Cammy! (Udon Comics Street Fighter)', 'https://redd.it/tiba9l')
add_data(['Cammy'],
'Cammy',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tiba9l/respect_cammy_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Kaela Mensha Khaine (Warhammer 40k)', 'https://redd.it/tiiu86')
add_data(['Khaine'],
'Khaine',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tiiu86/respect_kaela_mensha_khaine_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Dr. Manhattan (Watchmen, 2009)', 'https://redd.it/tiktva')
add_data(['(Doctor|Dr\.?) Manhattan'],
'Doctor Manhattan',
False,
False,
[
    ['2009'], ['Manhattan ?\(Movie']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tiktva/respect_dr_manhattan_watchmen_2009/

########################################

id = get_rt_id(cur, 'Respect Dabura, The King of the Demon Realm (Dragon Ball Manga)', 'https://redd.it/timkfi')
add_data(['Dabura'],
'Dabura',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)?']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/timkfi/respect_dabura_the_king_of_the_demon_realm_dragon/

########################################

id = get_rt_id(cur, 'Respect Mario (Mario Warfare)', 'https://redd.it/tioohz')
add_data(['Mario'],
'Mario',
False,
False,
[
    ['Mario Warfare']
],
'Mario Warfare',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tioohz/respect_mario_mario_warfare/

########################################

id = get_rt_id(cur, 'Respect Waluigi (Mario Warfare)', 'https://redd.it/tiop69')
add_data(['Waluigi'],
'Waluigi',
False,
False,
[
    ['Mario Warfare']
],
'Mario Warfare',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tiop69/respect_waluigi_mario_warfare/

########################################

id = get_rt_id(cur, 'Respect Ash Ketchum and Pikachu (Mario Warfare)', 'https://redd.it/tioq6o')
add_data(['Pikachu'],
'Pikachu',
False,
False,
[
    ['Mario Warfare']
],
'Mario Warfare',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tioq6o/respect_ash_ketchum_and_pikachu_mario_warfare/


########################################

id = get_rt_id(cur, 'Respect Leonardo (Teenage Mutant Ninja Turtles) [Image Comics]', 'https://redd.it/tip0mx')
add_data(['Leonardo'],
'Leonardo',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', 'Image Comics'], ['TMNT', 'Image Comics']
],
'TMNT, Image Comics',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Raphael (Teenage Mutant Ninja Turtles) [Image Comics]', 'https://redd.it/tip0nx')
add_data(['Raphael'],
'Raphael',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', 'Image Comics'], ['TMNT', 'Image Comics']
],
'TMNT, Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tip0nx/respect_raphael_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Donatello (Teenage Mutant Ninja Turtles) [Image Comics]', 'https://redd.it/tip0p9')
add_data(['Donatello'],
'Donatello',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', 'Image Comics'], ['TMNT', 'Image Comics']
],
'TMNT, Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tip0p9/respect_donatello_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Michelangelo (Teenage Mutant Ninja Turtles) [Image Comics]', 'https://redd.it/tip0qj')
add_data(['Michelangelo'],
'Michelangelo',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', 'Image Comics'], ['TMNT', 'Image Comics']
],
'TMNT, Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tip0qj/respect_michelangelo_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect The C.I.A Avatar Program (American Dad!)', 'https://redd.it/tiq1nq')
add_data(['C\.I\.A\.? Avatar'],
'C.I.A Avatar',
False,
False,
[
    ['American Dad']
],
'American Dad!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tiq1nq/respect_the_cia_avatar_program_american_dad/

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

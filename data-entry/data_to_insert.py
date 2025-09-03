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

update_respectthread(cur, 216, 'Respect Liz Sherman (Hellboy 2004-2008 films)', 'https://www.reddit.com/r/respectthreads/comments/1n4pbzp/respect_liz_sherman_hellboy_20042008_films/')
update_respectthread(cur, 580, 'Respect The Graboids! (Tremors)', 'https://www.reddit.com/r/respectthreads/comments/1n4s4rp/respect_the_graboids_tremors/')

########################################

add_data(['Ash'],
'Ash',
False,
False,
[
    ['Ash from.*Evil Dead']
],
'Evil Dead',
'{425}'
)
#https://www.reddit.com/r/whowouldwin/comments/1n6qux2/dante_from_dmc_games_ash_from_ash_vs_evil_dead/nc1yujs/?context=3

########################################

add_data(['Spawn'],
'Spawn',
False,
False,
[
    ['Al Simm?ons']
],
'Image Comics',
'{2638,2639}'
)
#https://www.reddit.com/r/whowouldwin/comments/1n6qux2/dante_from_dmc_games_ash_from_ash_vs_evil_dead/nc1yujs/?context=3

########################################

id = get_rt_id(cur, 'Respect Sweet Tooth (Twisted Metal TV Series)', 'https://www.reddit.com/r/respectthreads/comments/1n38tju/respect_sweet_tooth_twisted_metal_tv_series/')
add_data(['Sweet Tooth'],
'Sweet Tooth',
False,
False,
[
    ['Twisted Metal (TV Series|Show)']
],
'Twisted Metal TV Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shade Darby (Gone)', 'https://www.reddit.com/r/respectthreads/comments/1n3lpp3/respect_shade_darby_gone/')
add_data(['Shade Darby'],
'Shade Darby',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hajime Igarashi (Shinewbi)', 'https://www.reddit.com/r/respectthreads/comments/1n43zbx/respect_hajime_igarashi_shinewbi/')
add_data(['Hajime Igarashi'],
'Hajime Igarashi',
False,
False,
[
    ['Shinewbi']
],
'Shinewbi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rio Mikazuki (Shinewbi)', 'https://www.reddit.com/r/respectthreads/comments/1n43zjp/respect_rio_mikazuki_shinewbi/')
add_data(['Rio Mikazuki'],
'Rio Mikazuki',
False,
False,
[
    ['Shinewbi']
],
'Shinewbi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Che Heart (Ordeal)', 'https://www.reddit.com/r/respectthreads/comments/1n4mhsp/respect_che_heart_ordeal/')
add_data(['Che Heart'],
'Che Heart',
False,
True,
[
    ['Ordeal']
],
'Ordeal',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bjorn Grimmson (Ordeal)', 'https://www.reddit.com/r/respectthreads/comments/1n4v88y/respect_bjorn_grimmson_ordeal/')
add_data(['Bjorn Grimmson'],
'Bjorn Grimmson',
False,
True,
[
    ['Ordeal']
],
'Ordeal',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Masato Mishima/Gryllus Worm (Kamen Rider Kabuto)', 'https://www.reddit.com/r/respectthreads/comments/1n5etzs/respect_masato_mishimagryllus_worm_kamen_rider/')
add_data(['Masato Mishima'],
'Masato Mishima',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Gryllus Worm'],
'Gryllus Worm',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Brent Halligan (Mystery of the Druids)', 'https://www.reddit.com/r/respectthreads/comments/1n5nand/respect_brent_halligan_mystery_of_the_druids/')
add_data(['Brent Halligan'],
'Brent Halligan',
False,
True,
[
    ['Mystery of the Druids']
],
'The Mystery of the Druids',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Martians (The War of the Worlds, Original 1938 Radio Drama)', 'https://www.reddit.com/r/respectthreads/comments/1n5wa2k/respect_the_martians_the_war_of_the_worlds/')
add_data(['Martians'],
'Martians',
False,
False,
[
    ['War of the Worlds', 'Radio (Drama|Broadcast)'],
    ['War of the Worlds', '1938', 'Radio'],
],
'War of the Worlds Radio Drama',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Boba Fett (Star Wars: 1313)', 'https://www.reddit.com/r/respectthreads/comments/1n5y4ga/respect_boba_fett_star_wars_1313/')
add_data(['Boba Fett'],
'Boba Fett',
False,
False,
[
    ['Star Wars:? 1313']
],
'Star Wars: 1313',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Darth Malak (Star Wars)', 'https://www.reddit.com/r/respectthreads/comments/1n6j800/respect_darth_malak_star_wars/')
add_data(['Darth Malak'],
'Darth Malak',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1n6j800/respect_darth_malak_star_wars/

########################################

id = get_rt_id(cur, 'Respect Archangel Michael, the Great Prince of Israel (Abrahamic Religions)', 'https://www.reddit.com/r/respectthreads/comments/1n66cte/respect_archangel_michael_the_great_prince_of/')
add_data(['Archangel Michael'],
'Archangel Michael',
False,
True,
[
    ['Bible|Biblical|Christianity|Abrahamic']
],
'Bible',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Michael'],
'Michael',
False,
False,
[
    ['Archangel', 'Bible|Biblical|Christianity|Abrahamic'], ['(Arch)?Angels?', 'Gabriel|Raphael|Uriel'],
    ['Michael \(?the Archangel']
],
'Bible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/13l2unb/about_bible_supernatural_beings/
#https://www.reddit.com/r/whowouldwin/comments/1bcy01w/mythology_earth_vs_the_elder_scrolls_verse/
#https://www.reddit.com/r/whowouldwin/comments/2r54ay/the_4_archangels_michael_gabriel_raphael_and/
#https://www.reddit.com/r/whowouldwin/comments/18cxeno/michael_the_archangel_vs_v1_ultrakill/
#https://www.reddit.com/r/whowouldwin/comments/1dm0i4u/homelander_the_boys_vs_michael_the_archangel/
#https://www.reddit.com/r/whowouldwin/comments/2gmo6a/michael_the_archangel_supernatural_versus_fully/

########################################

id = get_rt_id(cur, 'Respect Dionysius, the wise old man (Old School RuneScape)', 'https://www.reddit.com/r/respectthreads/comments/1n70lgq/respect_dionysius_the_wise_old_man_old_school/')
add_data(['Dionysius'],
'Dionysius',
False,
False,
[
    ['RuneScape']
],
'RuneScape',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Wise Old Man'],
'Wise Old Man',
False,
False,
[
    ['RuneScape']
],
'RuneScape',
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

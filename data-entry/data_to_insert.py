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

add_data(['Luz'],
'Luz',
False,
False,
[
    ['Hexside']
],
'The Owl House',
'{20975}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/

########################################

add_data(['Amity'],
'Amity',
False,
False,
[
    ['Hexside']
],
'The Owl House',
'{20614}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/

########################################

add_data(['Amity'],
'Amity',
False,
False,
[
    ['Hexside']
],
'The Owl House',
'{20614}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/

########################################

add_data(['Anne'],
'Anne',
False,
False,
[
    ['Calamity Trio']
],
'Amphibia',
'{22017}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/
########################################

add_data(['Sasha'],
'Sasha',
False,
False,
[
    ['Calamity Trio']
],
'Amphibia',
'{22017}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/

########################################

id = get_rt_id(cur, 'Respect Marcy Wu! (Amphibia)', 'https://redd.it/uwnmmh')
add_data(['Marcy'],
'Marcy',
False,
False,
[
    ['Calamity Trio']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzqiei/the_calamity_trio_vs_the_hexside_5_luz_willow/

########################################

add_data(['Virgil'],
'Virgil',
False,
False,
[
    ['Devil May Cry'], ['DMC\d?'], ['Dante']
],
'Devil May Cry',
'{5048}'
)
#https://www.reddit.com/r/whowouldwin/comments/v0dcet/the_following_characters_play_monopoly/

########################################

add_data(['Metal Bat'],
'Metal Bat',
False,
False,
[
    ['Puri Puri Prisoner'], ['S(-| )class'], ['Tatsumaki']
],
'One Punch Man',
'{4107}'
)
#https://www.reddit.com/r/whowouldwin/comments/uzt83y/invincible_runs_a_s_class_hero_gauntlet/iad29ag/?context=3

########################################

id = get_rt_id(cur, 'Respect Tiaane (Chaotic)', 'https://redd.it/uyyc2g')
add_data(['Tiaane'],
'Tiaane',
False,
True,
[
    ['Chaotic']
],
'Chaotic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uyyc2g/respect_tiaane_chaotic/

########################################

id = get_rt_id(cur, 'Respect The Middleman (The Middleman) [Comics]', 'https://redd.it/uz1fxr')
add_data(['The Middleman'],
'The Middleman',
False,
False,
[
    ['The Middleman ?\((The Middleman|Comics?)']
],
'Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uz1fxr/respect_the_middleman_the_middleman_comics/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Cartoon Hooligans)', 'https://redd.it/uzglcd')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Cartoon ?Hooligans']
],
'CartoonHooligans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzglcd/respect_godzilla_cartoon_hooligans/

########################################

id = get_rt_id(cur, 'Respect Kong (Cartoon Hooligans)', 'https://redd.it/uzqsue')
add_data(['Kong'],
'Kong',
False,
False,
[
    ['Cartoon ?Hooligans']
],
'CartoonHooligans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzqsue/respect_kong_cartoon_hooligans/

########################################

id = get_rt_id(cur, 'Respect Thor (Death Battle!)', 'https://redd.it/uzqe92')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzqe92/respect_thor_death_battle/

########################################

id = get_rt_id(cur, 'Respect Cassandra Nova (Marvel Comics, 616)', 'https://redd.it/v09g23')
add_data(['Cassandra Nova'],
'Cassandra Nova',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v09g23/respect_cassandra_nova_marvel_comics_616/

########################################

id = get_rt_id(cur, 'Respect Ultimate Morbius (Marvel, 1610)', 'https://redd.it/uzrcw9')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['1610'], ['Ultimates'], ['Ultimate Morbius']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzrcw9/respect_ultimate_morbius_marvel_1610/

########################################

id = get_rt_id(cur, 'Respect Zombie Morbius (Marvel, Earth-2149)', 'https://redd.it/uztgrv')
add_data(['Zombie Morbius'],
'Zombie Morbius',
False,
True,
[
    ['2149']
],
'2149',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uztgrv/respect_zombie_morbius_marvel_earth2149/

########################################

id = get_rt_id(cur, 'Respect Dr. Michael Morbius (Ultimate Spider-Man cartoon/Earth-12041)', 'https://redd.it/v0ex5l')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['Ultimate Spider(-| )?Man'], ['12041']
],
'12041',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0ex5l/respect_dr_michael_morbius_ultimate_spiderman/

########################################

id = get_rt_id(cur, 'Respect Michael Morbius (Marvel Animated Universe / Earth-92131)', 'https://redd.it/v0jtre')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['Marvel Animated Universe'], ['92131']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0jtre/respect_michael_morbius_marvel_animated_universe/

########################################

id = get_rt_id(cur, 'Respect the Bat Devil (Chainsaw Man)', 'https://redd.it/uzrxp1')
add_data(['Bat Devil'],
'Bat Devil',
False,
False,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzrxp1/respect_the_bat_devil_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Warp Darkmatter (Buzz Lightyear of Star Command)', 'https://redd.it/uzs3a9')
add_data(['Warp Darkmatter'],
'Warp Darkmatter',
False,
False,
[
    ['Buzz Lightyear']
],
'Buzz Lightyear of Star Command',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzs3a9/respect_warp_darkmatter_buzz_lightyear_of_star/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Marvel Zombies vs. The Army of Darkness)', 'https://redd.it/uzukmx')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Marvel Zombies']
],
'Marvel Zombies',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uzukmx/respect_ash_williams_marvel_zombies_vs_the_army/

########################################

id = get_rt_id(cur, 'Respect Stella Vermillion, (Rakudai Kishi No Calvary)', 'https://redd.it/v01f99')
add_data(['Stella Vermillion'],
'Stella Vermillion',
False,
True,
[
    ['Chivalry of a Failed Knight'], ['Rakudai']
],
'Chivalry of a Failed Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v01f99/respect_stella_vermillion_rakudai_kishi_no_calvary/

########################################

id = get_rt_id(cur, "Respect Javier \"Javi\" Garcia (Telltale''s The Walking Dead Game)", 'https://redd.it/v01os4')
add_data(['Javi'],
'Javi',
False,
False,
[
    ['Wa(lk|kl)ing Dead']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v01os4/respect_javier_javi_garcia_telltales_the_walking/

########################################

id = get_rt_id(cur, 'Respect Cadre (DC Post Flashpoint)', 'https://redd.it/v0anl1')
add_data(['Cadre'],
'Cadre',
False,
False,
[
    ['(Post(-| ))?Flash(-| )?point']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0anl1/respect_cadre_dc_post_flashpoint/

########################################

id = get_rt_id(cur, 'Respect The Most Interesting Man In The World (Dos Equis)', 'https://redd.it/v0j2zv')
add_data(["Most Interesting Man in the World|World''?s Most Interesting Man"],
'Most Interesting Man in the World',
False,
True,
[
    ['Beer'], ['Dos Equis']
],
'Dos Equis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0j2zv/respect_the_most_interesting_man_in_the_world_dos/

########################################

id = get_rt_id(cur, 'Respect the Red Court of Vampires (The Dresden Files)', 'https://redd.it/v0h937')
add_data(['Red Court of Vampires'],
'Red Court of Vampires',
True,
True,
[
    ['Dresden Files']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0h937/respect_the_red_court_of_vampires_the_dresden/

add_data(['Red Court'],
'Red Court',
True,
False,
[
    ['Dresden Files']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v0h937/respect_the_red_court_of_vampires_the_dresden/

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

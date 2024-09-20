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

update_respectthread(cur, 4462, 'Respect The Wandering Samurai, Kenshin Himura (Rurouni Kenshin) [Manga]', 'https://redd.it/1fl5usn')

########################################

add_data(['Custodian'],
'Custodian',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{23647}'
)
#https://www.reddit.com/r/whowouldwin/comments/1fkxhz1/emperors_guard_battle_20_imperial_guards_star/

########################################

add_data(['Moria'],
'Moria',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{4044}'
)
#https://www.reddit.com/r/whowouldwin/comments/1fl3nov/whos_zombie_army_would_win_in_a_three_way_battle/lo04j0d/?context=3

########################################

id = get_rt_id(cur, 'Respect Mizore Shirayuki! (Rosario + Vampire)', 'https://redd.it/1fjrx3m')
add_data(['Mizore'],
'Mizore',
False,
False,
[
    ['Mizore Shirayuki'], ['Rosario']
],
'Rosario + Vampire',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fjrx3m/respect_mizore_shirayuki_rosario_vampire/

########################################

id = get_rt_id(cur, 'Respect Doctor Psycho (Harley Quinn)', 'https://redd.it/1fjylti')
add_data(['Doctor Psycho'],
'Doctor Psycho',
False,
False,
[
    ['Doctor Psycho ?\(Harley Quinn\)']
],
'Harley Quinn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fjylti/respect_doctor_psycho_harley_quinn/

########################################

id = get_rt_id(cur, 'Respect Doctor Demonicus (Marvel, 616)', 'https://redd.it/1fk10n3')
add_data(['Doctor Demonicus'],
'Doctor Demonicus',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fk10n3/respect_doctor_demonicus_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Son Goku! (Sonic vs Goku) [Webcomic]', 'https://redd.it/1fk3620')
add_data(['Goku'],
'Goku',
False,
False,
[
    ['Sonic vs\.? Goku.*Webcomic']
],
'Sonic vs Goku Webcomic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Sonic the Hedgehog! (Sonic vs Goku) [Webcomic]', 'https://redd.it/1fk37ab')
add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Sonic vs\.? Goku.*Webcomic']
],
'Sonic vs Goku Webcomic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fk37ab/respect_sonic_the_hedgehog_sonic_vs_goku_webcomic/

########################################

id = get_rt_id(cur, 'Respect Rex (Dogs of War)', 'https://redd.it/1fk70lj')
add_data(['Rex'],
'Rex',
False,
False,
[
    ['Dogs of War']
],
'Dogs of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fk70lj/respect_rex_dogs_of_war/

########################################

id = get_rt_id(cur, 'Respect the Dragon (Dra+Koi)', 'https://redd.it/1fkklks')
add_data(['Dragon'],
'Dragon',
False,
False,
[
    ['Dra+Koi']
],
'Dra+Koi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fkklks/respect_the_dragon_drakoi/

########################################

id = get_rt_id(cur, 'Respect the Dragon Slayer (Dra+Koi)', 'https://redd.it/1fkklly')
add_data(['Dragon Slayer'],
'Dragon Slayer',
False,
False,
[
    ['Dra+Koi']
],
'Dra+Koi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fkklly/respect_the_dragon_slayer_drakoi/

########################################

id = get_rt_id(cur, 'Respect Otogiri, the Soul Sucking Orian (Dark Gathering)', 'https://redd.it/1fkl6sz')
add_data(['Otogiri'],
'Otogiri',
False,
False,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fkl6sz/respect_otogiri_the_soul_sucking_orian_dark/

########################################

id = get_rt_id(cur, 'Respect Julian (Centuria)', 'https://redd.it/1fkro02')
add_data(['Julian'],
'Julian',
False,
False,
[
    ['Centuria']
],
'Centuria',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fkro02/respect_julian_centuria/

########################################

id = get_rt_id(cur, 'Respect Richter Belmont! (Castlevania Nocturne)', 'https://redd.it/1fkvnei')
add_data(['Richter Belmont'],
'Richter Belmont',
False,
False,
[
    ['Nocturne']
],
'Castlevania Nocturne',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fkvnei/respect_richter_belmont_castlevania_nocturne/

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

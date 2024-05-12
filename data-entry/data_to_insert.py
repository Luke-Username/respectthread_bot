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

add_data(['Gojo'],
'Gojo',
False,
False,
[
    ['Sukuna']
],
'Jujutsu Kaisen',
'{14809}'
)
#https://www.reddit.com/r/whowouldwin/comments/1cq9j2q/whos_winning_this_team_1_zoro_megumi_sukuna_gohan/l3q6qql/?context=3

########################################

add_data(['Blitzø'],
'Blitzø',
False,
True,
[
    ['Helluva Boss']
],
'Helluva Boss',
'{23869}'
)
#https://www.reddit.com/r/whowouldwin/comments/1cq9j2q/whos_winning_this_team_1_zoro_megumi_sukuna_gohan/l3q6qql/?context=3

########################################

id = get_rt_id(cur, 'Respect Aggron (Pokemon Anime)', 'https://redd.it/1cn4ew8')
add_data(['Aggron'],
'Aggron',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cn4ew8/respect_aggron_pokemon_anime/
########################################

id = get_rt_id(cur, 'Respect Deoxys (Pokemon Anime)', 'https://redd.it/1cnu9jy')
add_data(['Deoxys'],
'Deoxys',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cn4ew8/respect_aggron_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Edward Carnby (Alone in the Dark)', 'https://redd.it/1cnxmv0')
id2 = get_rt_id(cur, 'Respect Edward Carnby (Alone in the Dark: The New Nightmare)', 'https://redd.it/1cn60r1')
id3 = get_rt_id(cur, 'Respect Edward Carnby (Alone in the Dark, film series)', 'https://redd.it/1cn60u1')
id4 = get_rt_id(cur, 'Respect Edward Carnby (Alone in the Dark, 2024 Remake)', 'https://redd.it/1cn60pq')
add_data(['Edward Carnby'],
'Edward Carnby',
False,
True,
[
    ['Alone in the Dark']
],
'Alone in the Dark',
'{' + '{}, {}, {}, {}'.format(id, id2, id3, id4) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cn60pq/respect_edward_carnby_alone_in_the_dark_2024/

########################################

id = get_rt_id(cur, 'Respect Tatiana! (Undead Unluck)', 'https://redd.it/1cn74pi')
add_data(['Tatiana'],
'Tatiana',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cn74pi/respect_tatiana_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Top! (Undead Unluck)', 'https://redd.it/1copvd0')
add_data(['Top'],
'Top',
False,
False,
[
    ['Undead Unluck'], ['Top Bull Sparx']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1copvd0/respect_top_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Isshin! (Undead Unluck)', 'https://redd.it/1coq0c1')
add_data(['Isshin'],
'Isshin',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1coq0c1/respect_isshin_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect The Predators (AVP: Rage War Trilogy)', 'https://redd.it/1cnn0aj')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Rage War Trilogy']
],
'Rage War Trilogy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cnn0aj/respect_the_predators_avp_rage_war_trilogy/

########################################

id = get_rt_id(cur, "Respect Prince Phillip (Disney''s Sleeping Beauty)", 'https://redd.it/1cnrl9i')
add_data(['Prince Phillip'],
'Prince Phillip',
False,
False,
[
    ['Sleeping Beauty']
],
"Disney''s Sleeping Beauty",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cnrl9i/respect_prince_phillip_disneys_sleeping_beauty/

########################################

id = get_rt_id(cur, "Respect M''Baku, Man-Ape (Marvel, 616)", 'https://redd.it/1co5c4f')
add_data(["M''Baku"],
"M''Baku",
False,
True,
[
    ['616'], ['Man-Ape', 'Comics?']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1co5c4f/respect_mbaku_manape_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Phineas Mason, the Tinkerer (Marvel Comics, 616)', 'https://redd.it/1cqfjzd')
add_data(['Tinkerer'],
'Tinkerer',
False,
False,
[
    ['Tinkerer ?\(Marvel\)'], ['Tinkerer ?\(616\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cqfjzd/respect_phineas_mason_the_tinkerer_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect Timber Wolf (DC, Pre-Flashpoint)', 'https://redd.it/1cok0q8')
add_data(['Timber Wolf'],
'Timber Wolf',
False,
False,
[
    ['Pre(-| )?Flashpoint']
],
'Pre-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cok0q8/respect_timber_wolf_dc_preflashpoint/

########################################

id = get_rt_id(cur, 'Respect Rena Rouge (Miraculous Ladybug)', 'https://redd.it/1cp4fvf')
add_data(['Rena Rouge'],
'Rena Rouge',
False,
True,
[
    ['Miraculous']
],
'Miraculous Ladybug',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cp4fvf/respect_rena_rouge_miraculous_ladybug/

########################################

id = get_rt_id(cur, 'Respect Sakuya Izayoi (minusT Animations)', 'https://redd.it/1cph52z')
add_data(['Sakuya( Izayoi)?'],
'Sakuya Izayoi',
False,
False,
[
    ['minusT']
],
'minusT',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cph52z/respect_sakuya_izayoi_minust_animations/

########################################

id = get_rt_id(cur, 'Respect Youmu Konpaku (minusT Animations)', 'https://redd.it/1cph53s')
add_data(['Youmu Konpaku'],
'Youmu Konpaku',
False,
False,
[
    ['minusT']
],
'minusT',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cph53s/respect_youmu_konpaku_minust_animations/

########################################

id = get_rt_id(cur, 'Respect Beverly Sutphin (Serial Mom)', 'https://redd.it/1cqaqzd')
add_data(['Beverly Sutphin'],
'Beverly Sutphin',
False,
True,
[
    ['Serial Mom']
],
'Serial Mom',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1cqaqzd/respect_beverly_sutphin_serial_mom/

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

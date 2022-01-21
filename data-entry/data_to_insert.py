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

update_respectthread(cur, 2343, 'Respect Archangel (Marvel, 616)', 'https://redd.it/dmom6e')
update_respectthread(cur, 2489, 'Respect Maxwell Markham, The Grizzly (Marvel-616)', 'https://redd.it/s95n7e')
update_respectthread(cur, 16395, 'Respect Arashiyama Jurota, "The Gentle King" (Kengan Omega)', 'https://redd.it/s9hnvx')

########################################

add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['51914'], ['Golden Spongecake']
],
'51914',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/s9ed27/golden_spongecake_spiderman_vs_superman/htm9rgc/?context=3

########################################

id = get_rt_id(cur, 'Respect John F. Walker! (Marvel Cinematic Universe)', 'https://redd.it/mwz5vm')
add_data(['John Walker'],
'John Walker',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/mwz5vm/respect_john_f_walker_marvel_cinematic_universe/
#https://www.reddit.com/r/whowouldwin/comments/s9h2pn/super_soldier_grandpa/htmo3ls/?context=3

########################################

id = get_rt_id(cur, 'Respect Crimson (Dreamwalker)', 'https://redd.it/s9em60')
add_data(['Crimson'],
'Crimson',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9em60/respect_crimson_dreamwalker/

########################################

id = get_rt_id(cur, 'Respect Katsumi Orochi (Baki)', 'https://redd.it/s9fcw8')
add_data(['Katsumi Orochi'],
'Katsumi Orochi',
False,
True,
[
    ['Baki']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9fcw8/respect_katsumi_orochi_baki/

########################################

id = get_rt_id(cur, 'Respect Colonel Avery Hull (The Bionic Man) (Dynamite Comics)!', 'https://redd.it/s9fji0')
add_data(['Colonel Avery Hull'],
'Colonel Avery Hull',
False,
False,
[
    ['Bionic Man'], ['Dynamite']
],
'Bionic Man, Dynamite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bigfoot (Bionic Man) (Dynamite Comics)!', 'https://redd.it/s9frxl')
add_data(['Bigfoot'],
'Bigfoot',
False,
False,
[
    ['Bionic Man']
],
'Bionic Man, Dynamite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9frxl/respect_bigfoot_bionic_man_dynamite_comics/

########################################

id = get_rt_id(cur, 'Respect Trench (The Bionic Man vs The Bionic Woman) (Dynamite Comics)!', 'https://redd.it/s9g0vh')
add_data(['Trench'],
'Trench',
False,
False,
[
    ['Bionic Man']
],
'Bionic Man, Dynamite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9g0vh/respect_trench_the_bionic_man_vs_the_bionic_woman/

########################################

id = get_rt_id(cur, 'Respect Bebop & Rocksteady (Teenage Mutant Ninja Turtles) [IDW Comics]', 'https://redd.it/s9ie4d')
add_data(['Bebop'],
'Bebop',
False,
False,
[
    ['Rocksteady', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9ie4d/respect_bebop_rocksteady_teenage_mutant_ninja/

add_data(['Rocksteady'],
'Rocksteady',
False,
False,
[
    ['Bebop', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9ie4d/respect_bebop_rocksteady_teenage_mutant_ninja/

########################################

id = get_rt_id(cur, 'Respect King Mordred (Fate/Paradox Reincarnator)', 'https://redd.it/s9jly4')
add_data(['Mordred'],
'Mordred',
False,
False,
[
    ['Paradox Reincarnator']
],
'Fate/Paradox Reincarnator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9jly4/respect_king_mordred_fateparadox_reincarnator/

########################################

id = get_rt_id(cur, "Respect Shinji''s Servants (Fate/Paradox Reincarnator)", 'https://redd.it/s9jmbc')
add_data(['Medea'],
'Medea',
False,
False,
[
    ['Paradox Reincarnator']
],
'Fate/Paradox Reincarnator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9jmbc/respect_shinjis_servants_fateparadox_reincarnator/

add_data(['Shuten(-| )D(ō|o)u?ji'],
'Shuten-Dōji',
False,
False,
[
    ['Paradox Reincarnator']
],
'Fate/Paradox Reincarnator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9jmbc/respect_shinjis_servants_fateparadox_reincarnator/

add_data(['Shinji Makiri'],
'Shinji Makiri',
False,
False,
[
    ['Paradox Reincarnator']
],
'Fate/Paradox Reincarnator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/s9jmbc/respect_shinjis_servants_fateparadox_reincarnator/

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

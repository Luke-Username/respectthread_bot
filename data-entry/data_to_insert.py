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

id = get_rt_id(cur, 'Respect Yayoi Hozuki (Dark Gathering)', 'https://redd.it/1ftncw1')
add_data(['Yayoi Hozuki'],
'Yayoi Hozuki',
False,
True,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ftncw1/respect_yayoi_hozuki_dark_gathering/

########################################

id = get_rt_id(cur, 'Respect Jonathan Teatime (Discworld)', 'https://redd.it/1ftq9xi')
add_data(['Jonathan Teatime'],
'Jonathan Teatime',
False,
True,
[
    ['Discworld']
],
'Discworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ftq9xi/respect_jonathan_teatime_discworld/

add_data(['Mr\.? Teatime'],
'Mr. Teatime',
False,
True,
[
    ['Discworld']
],
'Discworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ftq9xi/respect_jonathan_teatime_discworld/

########################################

id = get_rt_id(cur, 'Respect The Demon Spawn (Ash vs. Evil Dead)', 'https://redd.it/1ftxr8r')
add_data(['Demon Spawn'],
'Demon Spawn',
False,
False,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ftxr8r/respect_the_demon_spawn_ash_vs_evil_dead/

########################################

id = get_rt_id(cur, 'Respect the Possessed Delta (Ash vs Evil Dead)', 'https://redd.it/1fuiwe2')
add_data(['Possessed Delta'],
'Possessed Delta',
False,
True,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fuiwe2/respect_the_possessed_delta_ash_vs_evil_dead/

########################################

id = get_rt_id(cur, 'Respect Miwa (Jujutsu Kaisen)', 'https://redd.it/1fujjb0')
add_data(['Miwa'],
'Miwa',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Kobeni']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fujjb0/respect_miwa_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Mechamaru! (Jujutsu Kaisen)', 'https://redd.it/1fujjip')
add_data(['Mechamaru'],
'Mechamaru',
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fujjip/respect_mechamaru_jujutsu_kaisen/

add_data(['Kokichi Muta'],
'Kokichi Muta',
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fujjip/respect_mechamaru_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Uraume, the Frozen Star! (Jujutsu Kaisen)', 'https://redd.it/1ful3u1')
add_data(['Uraume'],
'Uraume',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ful3u1/respect_uraume_the_frozen_star_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Hakari! (Jujutsu Kaisen)', 'https://redd.it/1ful44b')
add_data(['Hakari'],
'Hakari',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Kinji Hakari']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ful44b/respect_hakari_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Higuruma! (Jujutsu Kaisen)', 'https://redd.it/1fuww2w')
add_data(['Higuruma'],
'Higuruma',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Hiromi Higuruma']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fuww2w/respect_higuruma_jujutsu_kaisen/


########################################

id = get_rt_id(cur, 'Respect Takaba! (Jujutsu Kaisen)', 'https://redd.it/1fuww3o')
add_data(['Takaba'],
'Takaba',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Fumihiko Takaba']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fuww3o/respect_takaba_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Cliff Steele, The Robotman (DC)', 'https://redd.it/1futcx3')
add_data(['Robotman'],
'Robotman',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['Doom Patrol'], ['Cliff(ord)? Steele']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1futcx3/respect_cliff_steele_the_robotman_dc/

########################################

id = get_rt_id(cur, 'Respect Alexandria (Worm)', 'https://redd.it/1fuzjxy')
add_data(['Alexandria'],
'Alexandria',
False,
False,
[
    ['Worm']
],
'Worm',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fuzjxy/respect_alexandria_worm/

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

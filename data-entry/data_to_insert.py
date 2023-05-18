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

add_data(['Jonathan'],
'Jonathan',
False,
False,
[
    ['Dio Brando']
],
"Jojo''s Bizarre Adventure",
'{3533}'
)
#https://www.reddit.com/r/whowouldwin/comments/13knl1w/who_is_the_better_sun_breathing_sword_wielding/jkleyyt/?context=3

########################################

add_data(['Dr\. Reid'],
'Dr. Reid',
False,
False,
[
    ['Vampyr']
],
'Vampyr',
'{17351}'
)
#https://www.reddit.com/r/whowouldwin/comments/13kh2la/dr_reid_vampyr_vs_morgan_yu_prey/jkkbo6y/?context=3

########################################

add_data(['Shere?( |-)Khan'],
'Shere Khan',
False,
True,
[
    ['1894']
],
'1894',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Barry Burke, AKA Zzzap (Ex-Heroes)', 'https://redd.it/13ig9sn')
add_data(['Zzzap'],
'Zzzap',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ig9sn/respect_barry_burke_aka_zzzap_exheroes/

add_data(['Barry Burke'],
'Barry Burke',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ig9sn/respect_barry_burke_aka_zzzap_exheroes/

########################################

id = get_rt_id(cur, 'Respect Stealth! (Ex-Heroes)', 'https://redd.it/13jtzfo')
add_data(['Stealth'],
'Stealth',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Cerberus Battle System (Ex-Heroes)', 'https://redd.it/13imguu')
add_data(['Cerberus Battle System'],
'Cerberus Battle System',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13imguu/respect_the_cerberus_battle_system_exheroes/

########################################

id = get_rt_id(cur, 'Respect Pluton (Halo Legends)', 'https://redd.it/13ijjw6')
add_data(['Pluton'],
'Pluton',
False,
False,
[
    ['Halo']
],
'Halo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13ijjw6/respect_pluton_halo_legends/

########################################

id = get_rt_id(cur, 'Respect The Madden 08 Cyborg (Scott The Woz)', 'https://redd.it/13iqnyi')
add_data(['Madden 08 Cyborg'],
'Madden 08 Cyborg',
False,
True,
[
    ['Scott The Woz']
],
'Scott The Woz',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13iqnyi/respect_the_madden_08_cyborg_scott_the_woz/

########################################

id = get_rt_id(cur, 'Respect M3GAN (M3GAN)', 'https://redd.it/13j7s20')
add_data(['M3GAN'],
'M3GAN',
False,
True,
[
    ['M3GAN \(M3GAN\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13j7s20/respect_m3gan_m3gan/

########################################

id = get_rt_id(cur, 'Respect Superman Beyond! (DCAU, Earth-12)', 'https://redd.it/13kmxnk')
add_data(['Superman Beyond'],
'Superman Beyond',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13kmxnk/respect_superman_beyond_dcau_earth12/

########################################

id = get_rt_id(cur, "Respect Jafar (Disney''s 2019 Aladdin)", 'https://redd.it/13kojm3')
add_data(['Jafar'],
'Jafar',
False,
False,
[
    ['2019']
],
'Aladdin, 2019',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Themberchaud (Dungeons & Dragons: Honor Among Thieves)', 'https://redd.it/13k4011')
add_data(['Themberchaud'],
'Themberchaud',
False,
False,
[
    ['Honor Among Thieves'], ['Dungeons (&|and) Dragons', 'movie|film'], ['D ?(&|n) ?D', 'movie|film']
],
'Dungeons & Dragons: Honor Among Thieves',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13k4011/respect_themberchaud_dungeons_dragons_honor_among/

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

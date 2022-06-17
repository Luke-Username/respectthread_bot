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

update_respectthread(cur, 644, 'Respect Toph Beifong (Avatar: The Last Airbender)', 'https://redd.it/vc590y')
update_respectthread(cur, 22104, 'Respect Erynis the Implacable One (The One Who Eats Monsters)', 'https://redd.it/vccf9c')
update_respectthread(cur, 1321, 'Respect Blake Belladonna! (RWBY)', 'https://redd.it/vdaan9')

########################################

add_data(['The Ring'],
'The Ring',
False,
False,
[
    ['Lord of the Rings'], ['T?LOTR']
],
'Lord of the Rings',
'{5863}'
)
#https://www.reddit.com/r/whowouldwin/comments/vct230/dr_doom_marvel_vs_the_ring_the_lord_of_the_rings/

########################################

id = get_rt_id(cur, 'Respect Tigra (The Avengers: United They Stand)', 'https://redd.it/vbt96i')
add_data(['Tigra'],
'Tigra',
False,
False,
[
    ['Avengers:? United They Stand']
],
'The Avengers: United They Stand',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vbt96i/respect_tigra_the_avengers_united_they_stand/

########################################

id = get_rt_id(cur, 'Respect General Mung! (Avatar: The Last Airbender)', 'https://redd.it/vcgln7')
add_data(['Mung'],
'Mung',
False,
False,
[
    ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vcgln7/respect_general_mung_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'Respect Bedman (Guilty Gear)', 'https://redd.it/vcw15p')
add_data(['Bedman'],
'Bedman',
False,
False,
[
    ['Guilty Gear']
],
'Guilty Gear',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vcw15p/respect_bedman_guilty_gear/

########################################

id = get_rt_id(cur, 'Respect The Dirty Bubble! (Spongebob Squarepants)', 'https://redd.it/vcy30v')
add_data(['Dirty Bubble'],
'Dirty Bubble',
False,
True,
[
    ['SpongeBob']
],
'SpongeBob',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vcy30v/respect_the_dirty_bubble_spongebob_squarepants/

########################################

id = get_rt_id(cur, 'Respect Yakon (Dragon Ball Z)', 'https://redd.it/vd1q4w')
add_data(['Yakon'],
'Yakon',
False,
False,
[
    ['Dragon ?Ball'], ['DB(Z|S)?'], ['Babidis?'], ['Frieza']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vd1q4w/respect_yakon_dragon_ball_z/

########################################

id = get_rt_id(cur, 'Respect the Curator (Amphibia)', 'https://redd.it/vd6dk4')
add_data(['Curator'],
'Curator',
False,
False,
[
    ['Amphibia'], ['Curator Ponds']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vd6dk4/respect_the_curator_amphibia/

add_data(['Mr\.? ?Ponds'],
'Mr. Ponds',
False,
False,
[
    ['Amphibia'], ['Curator']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vd6dk4/respect_the_curator_amphibia/

########################################

id = get_rt_id(cur, 'Respect Juggernaut! (X-Men 1992)', 'https://redd.it/vdez20')
add_data(['Curator'],
'Curator',
False,
False,
[
    ['X(-| )?Men', '1992']
],
'X-Men, 1992',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vdez20/respect_juggernaut_xmen_1992/

########################################

id = get_rt_id(cur, 'Knights of Ren Respect Thread', 'https://comicvine.gamespot.com/profile/thevivas/blog/knights-of-ren-respect-thread/156909/')
add_data(['Knights of Ren'],
'Knights of Ren',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/vdlhp4/reva_vs_the_knights_of_ren_star_wars/ickst6f/?context=3

########################################

id = get_rt_id(cur, 'Respect the Lostbelt Olympians! (Fate)', 'https://redd.it/ve6epn')
add_data(['Lostbelt Olympians'],
'Lostbelt Olympians',
True,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ve6epn/respect_the_lostbelt_olympians_fate/

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

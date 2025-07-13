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

update_respectthread(cur, 25154, 'Respect Sienna Shaw (Terrifier)', 'https://redd.it/1lwx0cx')

########################################

add_data(['Rumi'],
'Rumi',
False,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{26193}'
)
#

add_data(['Mira'],
'Mira',
False,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{26193}'
)
#

add_data(['Zoey'],
'Zoey',
False,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{26193}'
)
#

add_data(['HUNTRiX'],
'HUNTRiX',
True,
False,
[
    ['KPop Demon Hunters']
],
'KPop Demon Hunters',
'{26193}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hugh de Clairvaux! (Dark Ages Vampire)', 'https://redd.it/1lum3v2')
add_data(['Hugh de Clairvaux'],
'Hugh de Clairvaux',
False,
False,
[
    ['Dark Ages:? Vampire'], ['Vampire:? The Masquerade'], ['Vampire:? The Dark Ages']
],
'Vampire: The Masquerade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lum3v2/respect_hugh_de_clairvaux_dark_ages_vampire/
#https://whitewolf.fandom.com/wiki/Dark_Ages:_Vampire

########################################

id = get_rt_id(cur, 'Respect Miss Eglantine Prince (Bedknobs and Broomsticks)', 'https://redd.it/1luq3iv')
add_data(['Miss Eglantine Prin?ce'],
'Miss Eglantine Prince',
False,
True,
[
    ['Bedknobs (and|&) Broomsticks']
],
'Bedknobs and Broomsticks',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Eglantine Prin?ce'],
'Eglantine Prince',
False,
False,
[
    ['Bedknobs (and|&) Broomsticks']
],
'Bedknobs and Broomsticks',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect November Ajax (Pacific Rim)', 'https://redd.it/1luwjav')
add_data(['November Ajax'],
'November Ajax',
False,
False,
[
    ['Pacific Rims?']
],
'Pacific Rim',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Jean-Paul Valley, Azrael! (DC, Post-Flashpoint)', 'https://redd.it/1lv4ddv')
add_data(['Jean(-| )Paul Valley'],
'Jean-Paul Valley',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Jean(-| )Paul Valley'],
'Jean-Paul Valley',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['DC Comics'], ['Azrael']
],
'DC',
'{' + '{}, 1527'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lv4ddv/respect_jeanpaul_valley_azrael_dc_postflashpoint/

add_data(['Jean(-| )Paul Valley'],
'Jean-Paul Valley',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{1527}'
)
#

add_data(['Michael Lane'],
'Michael Lane',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{1528}'
)
#

add_data(['Michael Lane'],
'Michael Lane',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['DC Comics'], ['Azrael']
],
'DC',
'{1528}'
)
#

add_data(['Azrael'],
'Azrael',
False,
False,
[
    ['Azrael ?\(DC( Comics)?\)']
],
'DC',
'{' + '{}, 1527, 1528'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Plungerman (Skibidi Toilet)', 'https://redd.it/1lvbcym')
add_data(['Plungerman'],
'Plungerman',
False,
False,
[
    ['Skibidi Toilet']
],
'Skibidi Toilet',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lvbcym/respect_plungerman_skibidi_toilet/

########################################

id = get_rt_id(cur, 'Respect the Titan Cameraman (Skibidi Toilet)', 'https://redd.it/1lwshlx')
add_data(['Titan Cameraman'],
'Titan Cameraman',
False,
True,
[
    ['Skibidi Toilet']
],
'Skibidi Toilet',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lwshlx/respect_the_titan_cameraman_skibidi_toilet/

########################################

id = get_rt_id(cur, 'Respect Knife Missiles and smaller missile types (Culture Series)', 'https://redd.it/1lww5s9')
add_data(['Knife Missiles?'],
'Knife Missiles',
False,
False,
[
    ['Culture']
],
'Culture series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lww5s9/respect_knife_missiles_and_smaller_missile_types/

########################################

id = get_rt_id(cur, 'Respect Yusuke Onodera, Kamen Rider Kuuga (Kamen Rider Decade)', 'https://redd.it/1lvjj4c')
add_data(['Yusuke Onodera'],
'Yusuke Onodera',
False,
True,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yaotsu, God of Indignia! (VERSUS)', 'https://redd.it/1lvk74c')
add_data(['Yaotsu'],
'Yaotsu',
False,
False,
[
    ['VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Daikokuzan the Mega-Kaiju! (VERSUS)', 'https://redd.it/1lvkzaw')
add_data(['Daikokuzan'],
'Daikokuzan',
False,
False,
[
    ['VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lvkzaw/respect_daikokuzan_the_megakaiju_versus/

########################################

id = get_rt_id(cur, 'Respect Ginbak (VERSUS)', 'https://redd.it/1lvsj03')
add_data(['Ginbak'],
'Ginbak',
False,
False,
[
    ['VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Moa that Fought Superman (DC, Pre-Crisis)', 'https://redd.it/1lvrybl')
add_data(['Moa that Fought Superman'],
'Moa that Fought Superman',
False,
True,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lvrybl/respect_the_moa_that_fought_superman_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect the Arkham Knight! (DC Comics [Post-Flashpoint])', 'https://redd.it/1lx4g82')
add_data(['Arkham Knight'],
'Arkham Knight',
False,
False,
[
    ['Arkham Knight ?\((Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Astrid Arkham'],
'Astrid Arkham',
False,
False,
[
    ['((Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Joanna Dark (Canceled Perfect Dark reboot)', 'https://redd.it/1lx9fxr')
add_data(['Joanna Dark'],
'Joanna Dark',
False,
False,
[
    ['Canceled Perfect Dark reboot']
],
'Canceled Perfect Dark reboot',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Richard Benson, The Avenger (Dynamite Comics)', 'https://redd.it/1lxd7yb')
add_data(['Richard Benson'],
'Richard Benson',
False,
False,
[
    ['Dynamite']
],
'Dynamite Entertainment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lxd7yb/respect_richard_benson_the_avenger_dynamite_comics/

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

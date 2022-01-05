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

update_respectthread(cur, 5787, 'Respect Sir Lancelot, the Knight of the Lake! (Fate)', 'https://redd.it/rtbfov')

########################################

add_data(['Serv(a|e)nts'],
'Servants',
True,
False,
[
    ['Fate(/| )Zero']
],
'Fate/Zero',
'{20234, 20236, 20235, 21175, 5787}'
)
#https://www.reddit.com/r/whowouldwin/comments/rwamjn/the_seven_sevants_fatezero_vs_the_akatsuki_naruto/hrampee/?context=3

########################################

add_data(['Akatsuki'],
'Akatsuki',
True,
False,
[
    ['Naruto']
],
'Naruto',
'{3964, 3967, 3960, 3950, 3959, 3972, 3942, 3948, 3956}'
)
#https://www.reddit.com/r/whowouldwin/comments/rwamjn/the_seven_sevants_fatezero_vs_the_akatsuki_naruto/

########################################

add_data(['Bonesaw'],
'Bonesaw',
False,
False,
[
    ['Slaughterhouse 9']
],
'Worm',
'{6060}'
)
#https://www.reddit.com/r/whowouldwin/comments/rw71nq/phantom_troupe_vs_slaughterhouse_9/hr9yv47/?context=3

########################################

add_data(['New Goblin'],
'New Goblin',
False,
False,
[
    ['Amazing Spider((-| )Man)? 2']
],
'The Amazing Spider-Man',
'{}'
)
#

add_data(['Green Goblin'],
'Green Goblin',
False,
False,
[
    ['No Way Home'], ['NWH']
],
'MCU',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/rw4uvq/new_goblin_and_goblin_amazing_spider_2_vs_green/hr9idpl/?context=3

########################################

id = get_rt_id(cur, 'Respect the Prince of Lan Ling! (Fate)', 'https://redd.it/rvidm1')
add_data(['Prince of Lan Ling'],
'Prince of Lan Ling',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rvidm1/respect_the_prince_of_lan_ling_fate/

########################################

id = get_rt_id(cur, 'Respect William Tell! (Fate)', 'https://redd.it/rviwgc')
add_data(['William Tell'],
'William Tell',
False,
False,
[
    ['Fate', 'Archer', 'Class'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rviwgc/respect_william_tell_fate/

########################################

id = get_rt_id(cur, 'Respect Nitocris, the Avatar of the Sky! (Fate)', 'https://redd.it/rw85o1')
add_data(['Nitocris'],
'Nitocris',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rw85o1/respect_nitocris_the_avatar_of_the_sky_fate/

########################################

id = get_rt_id(cur, 'Respect The Three Eyed Deva General (Xi Xing Ji)', 'https://redd.it/rvwfcy')
add_data(['Three(-| )Eyed Deva General'],
'Three Eyed Deva General',
False,
True,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rahu (Xi Xing Ji)', 'https://redd.it/rw82br')
add_data(['Rahu'],
'Rahu',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rw82br/respect_rahu_xi_xing_ji/

########################################

id = get_rt_id(cur, 'Respect Mr. Pain (Marvel, 616)', 'https://redd.it/rwbdoj')
add_data(['(Mister|Mr\.?) Pain'],
'Mister Pain',
False,
False,
[
    ['(Mister|Mr\.?) Pain ?\(616'], ['Vince', 'Dio']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwbdoj/respect_mr_pain_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Underworld (Marvel, 616)', 'https://redd.it/rwc7yf')
add_data(['Underworld'],
'Underworld',
False,
False,
[
    ['Underworld Pain ?\(616'], ['Jack Dio']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rwc7yf/respect_underworld_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Healer Atuat! (Avatar: Shadow of Kyoshi)', 'https://redd.it/rvjjaa')
add_data(['Atuat'],
'Atuat',
False,
False,
[
    ['Avatar'], ['Kyoshi'], ['Bend(er|ing)']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lex Luthor, Apex Predator! (DC Post Rebirth)', 'https://redd.it/rvwd4f')
add_data(['Luthor'],
'Luthor',
False,
False,
[
    ['Apex']
],
'Apex Predator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rvwd4f/respect_lex_luthor_apex_predator_dc_post_rebirth/

########################################

id = get_rt_id(cur, 'Respect Harvey Dent, the Superman (DC Comics, Earth-9)', 'https://redd.it/rvxuio')
add_data(['Harvey Dent'],
'Harvey Dent',
False,
False,
[
    ['Earth-9']
],
'Earth-9',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rvxuio/respect_harvey_dent_the_superman_dc_comics_earth9/

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

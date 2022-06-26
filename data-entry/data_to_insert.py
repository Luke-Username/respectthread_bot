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

update_respectthread(cur, 5550, 'Respect Part of Me/Badeline (Celeste)', 'https://redd.it/vl35l5')
update_respectthread(cur, 5734, "Respect Clementine (Telltale''s The Walking Dead Game)", 'https://redd.it/vlcqxt')

########################################

add_data(['Composite Superman'],
'Composite Superman',
False,
False,
[
    ['Amalgamax'], ['Xan']
],
'Pre-Crisis',
'{1797}'
)
#https://www.reddit.com/r/whowouldwin/comments/vkvqb3/which_characters_without_reality/idrm8w1/?context=3

########################################

add_data(['Kai'],
'Kai',
False,
False,
[
    ['Po', 'Panda']
],
'Kung Fu Panda',
'{1142}'
)
#

########################################

id = get_rt_id(cur, 'Respect Your Car (Is Your Car Safe From Supermaneuverable Air-Defense Fighter Aircraft?)', 'https://redd.it/vjypef')
add_data(['Car'],
'Car',
False,
False,
[
    ['Is Your Car Safe.*Aircraft?']
],
'Is Your Car Safe From Supermaneuverable Air-Defense Fighter Aircraft?',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vjypef/respect_your_car_is_your_car_safe_from/

########################################

id = get_rt_id(cur, 'Respect Outlaw! (Marvel 616)', 'https://redd.it/vk2x6t')
add_data(['Inez Temple'],
'Inez Temple',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vk2x6t/respect_outlaw_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Anya Forger! (Spy x Family)', 'https://redd.it/vk5d4h')
add_data(['Anya Forger'],
'Anya Forger',
False,
True,
[
    ['Spy x Family']
],
'Spy x Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vk5d4h/respect_anya_forger_spy_x_family/

########################################

id = get_rt_id(cur, 'Respect Bond! (Spy x Family)', 'https://redd.it/vkdx11')
add_data(['Bond Forger'],
'Bond Forger',
False,
True,
[
    ['Spy x Family']
],
'Spy x Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkdx11/respect_bond_spy_x_family/

add_data(['Bond'],
'Bond',
False,
False,
[
    ['Spy x Family']
],
'Spy x Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkdx11/respect_bond_spy_x_family/

########################################

id = get_rt_id(cur, 'Respect Loid Forger, Agent Twilight! (Spy x Family)', 'https://redd.it/vkl4pl')
add_data(['Loid Forger'],
'Loid Forger',
False,
True,
[
    ['Spy x Family']
],
'Spy x Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkdx11/respect_bond_spy_x_family/

add_data(['Loid'],
'Loid',
False,
False,
[
    ['Spy x Family']
],
'Spy x Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkl4pl/respect_loid_forger_agent_twilight_spy_x_family/

########################################

id = get_rt_id(cur, 'Respect Pikkon (Dragon Ball Z)', 'https://redd.it/vki1w1')
add_data(['Pikkon'],
'Pikkon',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)?']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vki1w1/respect_pikkon_dragon_ball_z/

########################################

id = get_rt_id(cur, 'Respect the Spinosaurus (Jurassic Park 3 in One Minute)', 'https://redd.it/vkkphj')
add_data(['Spinosaurus'],
'Spinosaurus',
False,
False,
[
    ['Jurassic Park 3 in One Minute']
],
'Jurassic Park 3 in One Minute',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkkphj/respect_the_spinosaurus_jurassic_park_3_in_one/

########################################

id = get_rt_id(cur, 'Respect the Giganotosaurus (Dino Crisis 2)', 'https://redd.it/vkn6q0')
add_data(['Giganotosaurus'],
'Giganotosaurus',
False,
False,
[
    ['Dino Crisis']
],
'Dino Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vkn6q0/respect_the_giganotosaurus_dino_crisis_2/

########################################

id = get_rt_id(cur, 'Respect Isaiah Mustafa (Old Spice)', 'https://redd.it/vktz8r')
add_data(['Isaiah Mustafa'],
'Isaiah Mustafa',
False,
True,
[
    ['Old Spice']
],
'Old Spice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vktz8r/respect_isaiah_mustafa_old_spice/

########################################

add_data(['Badeline'],
'Badeline',
False,
True,
[
    ['Celeste']
],
'Celeste',
'{5550}'
)
#https://www.reddit.com/r/respectthreads/comments/vl35l5/respect_part_of_mebadeline_celeste/

########################################

id = get_rt_id(cur, 'Respect Madeline (Celeste)', 'https://redd.it/vl35o3')
add_data(['Madeline'],
'Madeline',
False,
True,
[
    ['Celeste']
],
'Celeste',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vl35o3/respect_madeline_celeste/

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

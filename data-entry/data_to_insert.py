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

update_respectthread(cur, 1943, "Respect Mulan Kato (Kevin Smith''s Green Hornet)", 'https://redd.it/196ok59')
update_respectthread(cur, 1942, "Respect Hayashi Kato (Kevin Smith''s Green Hornet)", 'https://redd.it/196olbc')
update_respectthread(cur, 1940, "Respect Britt Reid Jr., The New Green Hornet (Kevin Smith''s Green Hornet)", 'https://redd.it/196omqx')
update_respectthread(cur, 1944, "Respect Redhand, The Last Red Hand Assassin (Kevin Smith''s Green Hornet)", 'https://redd.it/196oynv')
update_respectthread(cur, 1939, "Respect Hirohito Juuma, The Black Hornet (Kevin Smith''s Green Hornet)", 'https://redd.it/196p2t4')
update_respectthread(cur, 1941, "The Hornet Family''s Vehicles (Kevin Smith''s Green Hornet)", 'https://redd.it/196p58m')

########################################

add_data(['Yujiro'],
'Yujiro',
False,
True,
[
    ['Yujiro vs'], ['vs\.? Yujiro']
],
'Baki',
'{3452}'
)
#https://www.reddit.com/r/whowouldwin/comments/195l025/yujiro_vs_heihachi_vs_akuma/khng4o2/?context=3

########################################

add_data(['Geto'],
'Geto',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{23195}'
)
#https://www.reddit.com/r/whowouldwin/comments/195l025/yujiro_vs_heihachi_vs_akuma/khng4o2/?context=3

########################################

id = get_rt_id(cur, 'Respect Renfield (Renfield)', 'https://redd.it/195s50s')
add_data(['Renfield'],
'Renfield',
False,
False,
[
    ['Renfield'], ['2023']
],
'2023',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dracula (Renfield)', 'https://redd.it/195s5bq')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Renfield', '2023']
],
'Renfield, 2023',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/195s5bq/respect_dracula_renfield/

########################################

id = get_rt_id(cur, 'Respect the Unnamed Knight (The Elder Scrolls Online: High Isle Launch Cinematic)', 'https://redd.it/195zo49')
add_data(['Unnamed Knight'],
'Unnamed Knight',
False,
False,
[
    ['Elder Scrolls? Online']
],
'Elder Scrolls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/195zo49/respect_the_unnamed_knight_the_elder_scrolls/

########################################

id = get_rt_id(cur, 'Respect Hades! (Greek Mythology)', 'https://redd.it/1962ad3')
add_data(['Hades'],
'Hades',
False,
False,
[
    ['Greek myth?(olog(y|ical))?'], ['\(Mythology\)']
],
'Greek Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1962ad3/respect_hades_greek_mythology/

########################################

id = get_rt_id(cur, 'Respect Dragonflyman (The Wrong Earth)', 'https://redd.it/196h2m3')
add_data(['Dragonflyman'],
'Dragonflyman',
False,
True,
[
    ['Wrong Earth']
],
'The Wrong Earth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/196h3wz/respect_dragonfly_the_wrong_earth/

########################################

id = get_rt_id(cur, 'Respect Future Gohan (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/196m9kw')
add_data(['Future Gohan'],
'Future Gohan',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/196m9kw/respect_future_gohan_hyourinjutsu_dragon_ball/

########################################

id = get_rt_id(cur, "Respect Britt Reid Sr., The First Green Hornet (Kevin Smith''s Green Hornet)", 'https://redd.it/196ow3z')
add_data(['Britt Reid Sr'],
'Britt Reid Sr.',
False,
False,
[
    ['Green Hornet'], ['Kevin Smith']
],
'Green Hornet',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/196ow3z/respect_britt_reid_sr_the_first_green_hornet/

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

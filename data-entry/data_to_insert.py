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

update_respectthread(cur, 5905, 'Respect Percy Jackson (Percy Jackson & the Olympians) Updated Version', 'https://redd.it/1kwtha1')
update_respectthread(cur, 4880, 'Respect Kumada (Oyaji)', 'https://redd.it/1kxmd68')

########################################

id = get_rt_id(cur, 'Respect Spider Jerusalem (Transmetropolitan)', 'https://redd.it/1kvv8gb')
add_data(['Spider Jerusalem'],
'Spider Jerusalem',
False,
True,
[
    ['Transmetropolitan']
],
'Transmetropolitan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kvv8gb/respect_spider_jerusalem_transmetropolitan/

########################################

id = get_rt_id(cur, 'Respect The Mummy (Lot No. 249)', 'https://redd.it/1kvxsy1')
add_data(['Mummy'],
'Mummy',
False,
False,
[
    ['Lot No\.? 249']
],
'Lot No. 249',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gingy (Shrek Tie-In Games)', 'https://redd.it/1kw08nd')
add_data(['Gingy'],
'Gingy',
False,
False,
[
    ['Shrek( Tie(-| )In)? Games']
],
'Shrek Tie-In Games',
'{' + '{}'.format(id) + '}'
)
#

########################################

########################################

id = get_rt_id(cur, "Respect May''s Skitty (Pokemon Anime)", 'https://redd.it/1kw8o94')
add_data(['Skitty'],
'Skitty',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kw8o94/respect_mays_skitty_pokemon_anime/


########################################

id = get_rt_id(cur, "Respect May''s Munchlax (Pokemon Anime)", 'https://redd.it/1kwzwp6')
add_data(['Munchlax'],
'Munchlax',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kwzwp6/respect_mays_munchlax_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect May''s Glaceon (Pokemon Anime)", 'https://redd.it/1kxpo73')
add_data(['Glaceon'],
'Glaceon',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Invader (The Day the Earth Blew Up)', 'https://redd.it/1kwnpql')
add_data(['Invader'],
'Invader',
False,
False,
[
    ['Day the Earth Blew Up']
],
'The Day the Earth Blew Up',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jeff the Land Shark (Marvel 616)', 'https://redd.it/1kwro1d')
add_data(['Jeff the Land Shark'],
'Jeff the Land Shark',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect "Bill Rizer" and Genbei "Jaguar" Yagyu (Contra)', 'https://redd.it/1kwro3t')
add_data(['Jaguar'],
'Jaguar',
False,
False,
[
    ['Contra']
],
'Contra',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Little Pete (Gone)', 'https://redd.it/1kx4see')
add_data(['Little Pete'],
'Little Pete',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "You probably shouldn''t respect Not Important! (Hatred)", 'https://redd.it/1kx74il')
add_data(['Not Important'],
'Not Important',
False,
False,
[
    ['Hatred']
],
'Hatred',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kx74il/you_probably_shouldnt_respect_not_important_hatred/


########################################

id = get_rt_id(cur, "Respect Popeye (Genndy''s Cancelled Popeye Movie)", 'https://redd.it/1kxvpgi')
add_data(['Popeye'],
'Popeye',
False,
False,
[
    ['Genndy|Tartakovsky', 'Cancelled']
],
"Genndy''s Cancelled Popeye Movie",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kxvpgi/respect_popeye_genndys_cancelled_popeye_movie/

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

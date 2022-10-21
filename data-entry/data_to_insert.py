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

update_respectthread(cur, 578, 'Respect Agent Bishop (Teenage Mutant Ninja Turtles 2003)', 'https://redd.it/y92i5r')

########################################

add_data(['Utrom Shredder'],
'Utrom Shredder',
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{981}'
)
#

add_data(["Ch(''|’)rell"],
"Ch''rell",
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{981}'
)
#

########################################

add_data(['Utrom Shredder'],
'Utrom Shredder',
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{981}'
)
#

########################################

id = get_rt_id(cur, 'Respect Oroku Saki, the Tengu Shredder (Teenage Mutant Ninja Turtles 2003)', 'https://redd.it/y87ctn')
add_data(['Tengu Shredder'],
'Tengu Shredder',
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y7ullw/respect_the_box_assassin_the_box_assassin/

add_data(['Oroku Saki'],
'Oroku Saki',
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y7ullw/respect_the_box_assassin_the_box_assassin/

########################################

id = get_rt_id(cur, 'Respect Cyber Shredder (Teenage Mutant Ninja Turtles 2003)', 'https://redd.it/y87cvv')
add_data(['Cyber Shredder'],
'Cyber Shredder',
False,
True,
[
    ['2003'], ['Teenaged? Mutant Ninja Turtles?'], ['TMNT']
],
'TMNT 2003',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cyber Shredder (Teenage Mutant Ninja Turtles 2003)', 'https://redd.it/y87cvv')
add_data(['Miyamoto Usagi|Usagi Miyamoto'],
'Miyamoto Usagi',
False,
False,
[
    ['2003']
],
'TMNT 2003',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Leslie Vernon (Behind the Mask: The Legend of Leslie Vernon)', 'https://redd.it/y80rk0')
add_data(['Leslie Vernon'],
'Leslie Vernon',
False,
True,
[
    ['Behind the Mask']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y80rk0/respect_leslie_vernon_behind_the_mask_the_legend/

########################################

id = get_rt_id(cur, 'Respect The Babylon Rogues! (Sonic the Hedgehog (IDW Comics))', 'https://redd.it/y8apmt')
add_data(['Babylon Rogues'],
'Babylon Rogues',
True,
False,
[
    ['IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y8apmt/respect_the_babylon_rogues_sonic_the_hedgehog_idw/

########################################

id = get_rt_id(cur, 'Respect Mimic! (Sonic the Hedgehog (IDW Comics)', 'https://redd.it/y8arr4')
add_data(['Mimic'],
'Mimic',
False,
False,
[
    ['Sonic', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y8arr4/respect_mimic_sonic_the_hedgehog_idw_comics/

########################################

id = get_rt_id(cur, 'Respect Dr. Starline (Sonic the Hedgehog (IDW Comics))', 'https://redd.it/y8i90n')
add_data(['D(octo)?r\.? Starline'],
'Doctor Starline',
False,
True,
[
    ['Sonic', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y8i90n/respect_dr_starline_sonic_the_hedgehog_idw_comics/

########################################

id = get_rt_id(cur, 'Respect Kitsunami "Kit" the Fennec! (Sonic the Hedgehog (IDW Comics))', 'https://redd.it/y97k7n')
add_data(['Kitsunami'],
'Kitsunami',
False,
True,
[
    ['Sonic', 'IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y97k7n/respect_kitsunami_kit_the_fennec_sonic_the/

########################################

id = get_rt_id(cur, 'Respect Surge the Tenrec! (Sonic the Hedgehog (IDW Comics))', 'https://redd.it/y97kxe')
add_data(['Surge'],
'Surge',
False,
False,
[
    ['Sonic', 'IDW'], ['Surge the Tenrec']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y97kxe/respect_surge_the_tenrec_sonic_the_hedgehog_idw/

########################################

id = get_rt_id(cur, 'Respect The Powerpuff Girls Z (Powerpuff Girls Z)', 'https://redd.it/y9et4m')
add_data(['Power ?puff Girls Z'],
'Powerpuff Girls Z',
True,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Ring of Brass (Critical Role)', 'https://redd.it/y9h5re')
add_data(['Ring of Brass'],
'Ring of Brass',
True,
False,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(['Nydas Okiro'],
'Nydas Okiro',
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(["Patia Por''co"],
"Patia Por''co",
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(['Zerxus Ilerez'],
'Zerxus Ilerez',
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(['Loquatius Seelie'],
'Loquatius Seelie',
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(['Laerryn Coramar(-| )Seelie'],
'Laerryn Coramar-Seelie',
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

add_data(['Cerrit Agrupnin'],
'Cerrit Agrupnin',
False,
True,
[
    ['Critical Role']
],
'Critical Role',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9h5re/respect_the_ring_of_brass_critical_role/

########################################

id = get_rt_id(cur, 'Respect Wanda Maximoff, the Scarlet Witch (Death Battle)', 'https://redd.it/y9huk6')
add_data(['Wanda Maximoff'],
'Wanda Maximoff',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9huk6/respect_wanda_maximoff_the_scarlet_witch_death/

########################################

id = get_rt_id(cur, 'Respect Zatanna Zatara (Death Battle)', 'https://redd.it/y9hv6r')
add_data(['Zatanna'],
'Zatanna',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y9hv6r/respect_zatanna_zatara_death_battle/

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

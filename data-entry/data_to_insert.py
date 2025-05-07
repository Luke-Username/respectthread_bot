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

update_respectthread(cur, 2176, 'Respect Iron Man Model 42: the Black and Gold Armor (Marvel, Earth-616)', 'https://redd.it/1kepboi')

########################################

add_data(['Terminator'],
'Terminator',
False,
False,
[
    ['Doomslayer', 'or Terminator']
],
'',
'{329,330,331,332}'
)
#https://www.reddit.com/r/whowouldwin/comments/1kd6i68/who_would_win_the_doomslayer_or_terminator/

########################################

id = get_rt_id(cur, 'Respect Sougo Tokiwa, Kamen Rider Zi-O (Kamen Rider Zi-O)', 'https://redd.it/1kcfv0q')
add_data(['Kamen Rider Zi-O'],
'Kamen Rider Zi-O',
False,
True,
[
    ['Sougo Tokiwa']
],
'',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Kamen Rider'],
'Kamen Rider',
False,
False,
[
    ['Zi-O']
],
'Zi-O',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kcfv0q/respect_sougo_tokiwa_kamen_rider_zio_kamen_rider/

add_data(['Sougo Tokiwa'],
'Sougo Tokiwa',
False,
True,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Sougo'],
'Sougo',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Ohma Zi-O (Kamen Rider Zi-O)', 'https://redd.it/1kcfx9t')
add_data(['Ohma Zi-?O'],
'Ohma Zi-O',
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

id = get_rt_id(cur, 'Respect Princess Arzette (Arzette: The Jewel of Faramore)', 'https://redd.it/1kd0tmy')
add_data(['Princess Arzette'],
'Princess Arzette',
False,
True,
[
    ['Jewel of Faramore']
],
'Arzette: The Jewel of Faramore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kd0tmy/respect_princess_arzette_arzette_the_jewel_of/

########################################

id = get_rt_id(cur, 'Respect Darth Nihilus (Star Wars)', 'https://redd.it/1kd46wg')
add_data(['Darth Nihilus'],
'Darth Nihilus',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kd46wg/respect_darth_nihilus_star_wars/

########################################

id = get_rt_id(cur, 'Respect Thorn Harvestar! (BONE)', 'https://redd.it/1kdd69x')
add_data(['Thorn Harvestar'],
'Thorn Harvestar',
False,
True,
[
    ['BONE']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Lord of Locusts! (BONE)', 'https://redd.it/1kdiiro')
add_data(['Lord of Locusts'],
'Lord of Locusts',
False,
False,
[
    ['BONE']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Bone Cousins! (BONE)', 'https://redd.it/1kdcod6')
add_data(['Bone Cousins'],
'Bone Cousins',
True,
False,
[
    ['\(BONE\)']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kdcod6/respect_the_bone_cousins_bone/


add_data(['Fone Bone'],
'Fone Bone',
False,
True,
[
    ['BONE']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kdcod6/respect_the_bone_cousins_bone/


add_data(['Phoney Bone'],
'Phoney Bone',
False,
True,
[
    ['BONE']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kdcod6/respect_the_bone_cousins_bone/

add_data(['Smiley Bone'],
'Smiley Bone',
False,
True,
[
    ['BONE']
],
'BONE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kdcod6/respect_the_bone_cousins_bone/

########################################

id = get_rt_id(cur, 'Respect Frank Castle (Punisher Kills the Marvel Universe)', 'https://redd.it/1kdskmx')
add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['Punisher Kills the Marvel Universe']
],
'Punisher Kills the Marvel Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Blindside (Marvel Comics, Earth 616)', 'https://redd.it/1kel7ei')
add_data(['Blindside'],
'Blindside',
False,
False,
[
    ['Blindside ?\(616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

########################################

id = get_rt_id(cur, 'Respect Samson (Fate/Samurai Remnant)', 'https://redd.it/1ke3wv8')
add_data(['Samson'],
'Samson',
False,
False,
[
    ['Samson.*\(Fate\)'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yui Shousetsu (Fate/Samurai Remnant)', 'https://redd.it/1kehds4')
add_data(['Yui Sh(ō|o)u?setsu'],
'Yui Shōsetsu',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kehds4/respect_yui_shousetsu_fatesamurai_remnant/

########################################

id = get_rt_id(cur, 'Respect Vincent Vu, Abaddon (Gone)', 'https://redd.it/1kemgjr')
add_data(['Abaddon'],
'Abaddon',
False,
False,
[
    ['Abaddon ?\(Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Vincent Vu'],
'Vincent Vu',
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

id = get_rt_id(cur, 'Respect Wallace (Pokemon Anime)', 'https://redd.it/1kfaqzz')
add_data(['Wallace'],
'Wallace',
False,
False,
[
    ['Pok(e|é)m(o|a)n', 'Champions?']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Team Aqua (Pokemon Anime)', 'https://redd.it/1kfbgjr')
add_data(['Team Aqua'],
'Team Aqua',
True,
False,
[
    ['Pok(e|é)m(o|a)n'], ['Team Magma'], ['Kyogre']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tate and Liza (Pokemon Anime)', 'https://redd.it/1kfqgjr')
add_data(['Tate and Liza'],
'Tate and Liza',
True,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Drake of the Hoenn Elite 4 (Pokemon Anime)', 'https://redd.it/1kgimo9')
add_data(['Drake'],
'Drake',
False,
False,
[
    ['Pok(e|é)m(o|a)n', '(Hoenn|Elite Four)']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

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

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

update_respectthread(cur, 1026, 'Respect Roger the Alien (American Dad!)', 'https://redd.it/yva4kt')

########################################

id = get_rt_id(cur, 'Respect the Black Cat Guardian! (Fablehaven)', 'https://redd.it/yu0s43')
add_data(['Black Cat Guardian'],
'Black Cat Guardian',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu0s43/respect_the_black_cat_guardian_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Olloch the Glutton! (Fablehaven)', 'https://redd.it/yvhu2z')
add_data(['Olloch'],
'Olloch',
False,
True,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yvhu2z/respect_olloch_the_glutton_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Patton Burgess! (Fablehaven)', 'https://redd.it/yvvvie')
add_data(['Patton Burgess'],
'Patton Burgess',
False,
True,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yvvvie/respect_patton_burgess_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Bracken! (Fablehaven)', 'https://redd.it/yu0ug6')
add_data(['Bracken'],
'Bracken',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu0ug6/respect_bracken_fablehaven/

########################################

id = get_rt_id(cur, 'Respect the Gray Assassin! (Fablehaven)', 'https://redd.it/yu0vtk')
add_data(['Gray Assassin'],
'Gray Assassin',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu0vtk/respect_the_gray_assassin_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Mirav! (Fablehaven)', 'https://redd.it/yu0yzz')
add_data(['Mirav'],
'Mirav',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu0yzz/respect_mirav_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Mendigo! (Fablehaven)', 'https://redd.it/yu12q3')
add_data(['Mendigo'],
'Mendigo',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hugo! (Fablehaven)', 'https://redd.it/yu4jyw')
add_data(['Hugo'],
'Hugo',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu4jyw/respect_hugo_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Ephira! (Fablehaven)', 'https://redd.it/yu10ws')
add_data(['Ephira'],
'Ephira',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu10ws/respect_ephira_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Tanu! (Fablehaven)', 'https://redd.it/yuxwof')
add_data(['Tanu'],
'Tanu',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yuxwof/respect_tanu_fablehaven/

########################################

id = get_rt_id(cur, 'Respect Ryland, the Somber Knight! (Fablehaven)', 'https://redd.it/yuxy1r')
add_data(['Ryland'],
'Ryland',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yuxy1r/respect_ryland_the_somber_knight_fablehaven/

########################################

id = get_rt_id(cur, "Respect Leon''s Rillaboom (Pokemon Anime)", 'https://redd.it/yv9xyn')
add_data(['Rillaboom'],
'Rillaboom',
False,
False,
[
    ['Leons?']
],
'Leon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yv9xyn/respect_leons_rillaboom_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect Leon''s Dragapult (Pokemon Anime)", 'https://redd.it/yv9y9f')
add_data(['Dragapult'],
'Dragapult',
False,
False,
[
    ['Leons?']
],
'Leon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yv9y9f/respect_leons_dragapult_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Babadook (The Babadook)', 'https://redd.it/yudczk')
add_data(['Babadook'],
'Babadook',
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yudczk/respect_the_babadook_the_babadook/

########################################

id = get_rt_id(cur, 'Respect "God-Eye" Galatea (Claymore)', 'https://redd.it/yufcp1')
add_data(['Galatea'],
'Galatea',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yufcp1/respect_godeye_galatea_claymore/

########################################

id = get_rt_id(cur, 'Respect SCP-162, Ball of Sharp (SCP Foundation)', 'https://redd.it/yuffty')
add_data(['SCP ?(-| )? ?162'],
'SCP-162',
False,
False,
[
    ['Ball of Sharp']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lady Liadrin (Hearthstone)', 'https://redd.it/yulm4l')
add_data(['Lady Liadrin'],
'Lady Liadrin',
False,
False,
[
    ['Hearthstone']
],
'Hearthstone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yulm4l/respect_lady_liadrin_hearthstone/

########################################

id = get_rt_id(cur, 'Respect Arthas Menethil, the Lich King (Hearthstone)', 'https://redd.it/yulupk')
add_data(['Arthas Menethil'],
'Arthas Menethil',
False,
False,
[
    ['Hearthstone']
],
'Hearthstone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yulupk/respect_arthas_menethil_the_lich_king_hearthstone/

########################################

id = get_rt_id(cur, 'Respect Kainé (NieR Replicant ver.1.22474487139...)', 'https://redd.it/yvn6l1')
add_data(['Kain(é|e)'],
'Kainé',
False,
False,
[
    ['Nier']
],
'NieR Replicant',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yvn6l1/respect_kain%C3%A9_nier_replicant_ver122474487139/

########################################

id = get_rt_id(cur, 'Respect Tropic Woods (Kirby and the Forgotten Land)', 'https://redd.it/ywakht')
add_data(['Tropic Woods'],
'Tropic Woods',
False,
True,
[
    ['Kirby']
],
'Kirby',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ywakht/respect_tropic_woods_kirby_and_the_forgotten_land/

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

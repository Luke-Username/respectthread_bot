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

update_respectthread(cur, 197, 'Respect Mechagodzilla (Godzilla Franchise, Showa Continuity)', 'https://redd.it/1g9gvub')

########################################

add_data(['Scare ?crow'],
'Scarecrow',
False,
False,
[
    ['Batman', 'Scar(es?|ing']
],
'DC',
'{1557,1558}'
)
#https://www.reddit.com/r/whowouldwin/comments/1g9t8tw/who_can_become_the_next_pumpkin_king/lt8kvnm/?context=3

########################################

id = get_rt_id(cur, 'Respect Sakamaki Deido (Souboutei Must Be Destroyed)', 'https://redd.it/1g9o92u')
add_data(['(Sakamaki Deido|Deido Sakamaki)'],
'Sakamaki Deido',
False,
True,
[
    ['S(ō|o)u? ?b(ō|o)u? ?tei']
],
'Sōbōtei Must Be Destroyed',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g9qmae/respect_souboutei_souboutei_must_be_destroyed/

########################################

id = get_rt_id(cur, 'Respect Souboutei! (Souboutei Must Be Destroyed)', 'https://redd.it/1g9qmae')
add_data(['S(ō|o)u? ?b(ō|o)u? ?tei'],
'Sōbōtei',
False,
True,
[
    ['S(ō|o)u? ?b(ō|o)u? ?tei Must Be Destroyed'], ['Kowasubeshi']
],
'Sōbōtei Must Be Destroyed',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g9qmae/respect_souboutei_souboutei_must_be_destroyed/

########################################

id = get_rt_id(cur, 'Respect Prince (AVP2)', 'https://redd.it/1g9pljc')
add_data(['Prince'],
'Prince',
False,
False,
[
    ['Aliens versus Predator 2'], ['AVP2']
],
'Aliens versus Predator 2',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g9pljc/respect_prince_avp2/

########################################

id = get_rt_id(cur, 'Respect The Deep Ones (H.P. Lovecraft)', 'https://redd.it/1gb2zbu')
add_data(['The Deep Ones'],
'The Deep Ones',
False,
False,
[
    ['Lovecraft']
],
'Lovecraft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gb2zbu/respect_the_deep_ones_hp_lovecraft/

########################################

id = get_rt_id(cur, 'Respect Doc Savage, the Man of Bronze! (DC Comics, First Wave)', 'https://redd.it/1gb36rv')
add_data(['Doc Savage'],
'Doc Savage',
False,
False,
[
    ['First Wave']
],
'First Wave',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gb36rv/respect_doc_savage_the_man_of_bronze_dc_comics/
#https://dc.fandom.com/wiki/First_Wave

########################################

id = get_rt_id(cur, 'Respect the Necronomicon (RetroRealms: Ash vs Evil Dead)', 'https://redd.it/1gbdk21')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['RetroRealms']
],
'RetroRealms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gbdk21/respect_the_necronomicon_retrorealms_ash_vs_evil/

########################################

id = get_rt_id(cur, 'Respect Electric Guitar Grumer! (Bakuage Sentai BoonBoomger)', 'https://redd.it/1gb3kgn')
add_data(['Electric Guitar Grumer'],
'Electric Guitar Grumer',
False,
True,
[
    ['Bakuage Sentai BoonBoomger']
],
'Bakuage Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gb3kgn/respect_electric_guitar_grumer_bakuage_sentai/

########################################

id = get_rt_id(cur, 'Respect Berserker! (Fate/Lost Einherjar)', 'https://redd.it/1gbxxt4')
add_data(['Ragnar Lodbrok'],
'Ragnar Lodbrok',
False,
False,
[
    ['Fate'], ['Lost Einherjar']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gbxxt4/respect_berserker_fatelost_einherjar/

########################################

id = get_rt_id(cur, "Respect Spooky (Spooky''s Jump Scare Mansion)", 'https://redd.it/1gc6k1n')
add_data(['Spooky'],
'Spooky',
False,
False,
[
    ["Spooky''?s Jump Scare Mansion"]
],
"Spooky''s Jump Scare Mansion",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1gc6k1n/respect_spooky_spookys_jump_scare_mansion/

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

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

update_respectthread(cur, 6264, 'Respect Featherine Augustus Aurora, the Witch of Theater! (Umineko: When They Cry [Manga])', 'https://redd.it/1heszwg')

########################################

add_data(['Featherine'],
'Featherine',
False,
True,
[
    ['Umineko']
],
'Umineko',
'{6264}'
)
#https://www.reddit.com/r/respectthreads/comments/1heszwg/respect_featherine_augustus_aurora_the_witch_of/

########################################

add_data(['Power'],
'Power',
False,
False,
[
    ['CSM']
],
'Chainsaw Man',
'{15966}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hdsh7z/power_csm_vs_jinx_arcane_vs_azula_atla/

########################################

id = get_rt_id(cur, 'Respect the Skull Merchant (Dead by Daylight)', 'https://redd.it/1hddbk8')
add_data(['Skull Merchant'],
'Skull Merchant',
False,
True,
[
    ['Dead by Daylight']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Grey (Snowpiercer)', 'https://redd.it/1hddfde')
add_data(['Grey'],
'Grey',
False,
False,
[
    ['Snowpiercer']
],
'Snowpiercer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hddfde/respect_grey_snowpiercer/

########################################

id = get_rt_id(cur, 'Respect the Barillian Bugs (Power Rangers in Space)', 'https://redd.it/1hdhppt')
add_data(['Barillian Bugs?'],
'Barillian Bugs',
False,
True,
[
    ['Power Rangers in Space']
],
'Power Rangers in Space',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hdhppt/respect_the_barillian_bugs_power_rangers_in_space/

########################################

add_data(['Jack Frost'],
'Jack Frost',
False,
False,
[
    ['Jack Frost.*Killer Snowman']
],
'The Mutant Killer Snowman',
'{13084}'
)
#https://www.reddit.com/r/whowouldwin/comments/1heujyw/the_gingerdead_man_vs_jack_frost_the_killer/m26ka8f/?context=3

########################################

add_data(['Momo'],
'Momo',
False,
False,
[
    ['Dandadan']
],
'Dandadan',
'{22080}'
)
#https://www.reddit.com/r/whowouldwin/comments/1heut1v/dandadan_team_vs_jujutsu_kaisen_team/m26fo7w/?context=3

########################################

add_data(['Aira'],
'Aira',
False,
False,
[
    ['Dandadan']
],
'Dandadan',
'{22079}'
)
#

########################################

id = get_rt_id(cur, 'Respect Link (The Legend of Zelda: Count of the Black Shadows)', 'https://redd.it/1he4kq0')
add_data(['Link'],
'Link',
False,
False,
[
    ['Count of the Black Shadows']
],
'Count of the Black Shadows',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Erlang Shen (Chinese Mythology)', 'https://redd.it/1henxw6')
add_data(['Erlang Shen'],
'Erlang Shen',
False,
True,
[
    ['myth?(ical|olog(y|ical))?']
],
'Chinese Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1henxw6/respect_erlang_shen_chinese_mythology/

add_data(['Erlang Shen'],
'Erlang Shen',
False,
False,
[
    ['Black Myth:? Wukong']
],
'Black Myth: Wukong',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/1henxw6/respect_erlang_shen_chinese_mythology/

########################################

id = get_rt_id(cur, 'Respect Kya (Kya: Dark Lineage)', 'https://redd.it/1her9fo')
add_data(['Kya'],
'Kya',
False,
False,
[
    ['Dark Lineage']
],
'Kya: Dark Lineage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1her9fo/respect_kya_kya_dark_lineage/

########################################

id = get_rt_id(cur, 'Respect the Carnivores Triassic Gojirasaurus (M e d i c b a g)', 'https://redd.it/1hf2mgo')
add_data(['Carnivores Triassic Gojirasaurus'],
'Carnivores Triassic Gojirasaurus',
False,
False,
[
    ['M e d i c b a g']
],
'M e d i c b a g',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hf2mgo/respect_the_carnivores_triassic_gojirasaurus_m_e/

########################################

id = get_rt_id(cur, 'Respect Entity 94, "The Tour Guide" (The Backrooms, Fandom)', 'https://redd.it/1hfb6qj')
add_data(['Entity 94'],
'Entity 94',
False,
False,
[
    ['The Backrooms']
],
'The Backrooms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hfb6qj/respect_entity_94_the_tour_guide_the_backrooms/

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

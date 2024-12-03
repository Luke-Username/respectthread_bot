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

add_data(['Reed Richards'],
'Reed Richards',
False,
False,
[
    ['1610.*Reed Richards']
],
'1610',
'{2537}'
)
#https://www.reddit.com/r/whowouldwin/comments/1h4kpnw/ultimate_earth_fight/m03uk0r/?context=3

########################################

id = get_rt_id(cur, 'Respect Megatron (Transformers One)', 'https://redd.it/1h45mjx')
add_data(['Megatron'],
'Megatron',
False,
False,
[
    ['Transformers One']
],
'Transformers One',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h45mjx/respect_megatron_transformers_one/

########################################

id = get_rt_id(cur, 'Respect Garth One-Eye (Magic: The Gathering)', 'https://redd.it/1h461jc')
add_data(['Garth One-Eye'],
'Garth One-Eye',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h461jc/respect_garth_oneeye_magic_the_gathering/

########################################

id = get_rt_id(cur, "Respect Carl ''CJ'' Johnson (Grand Theft Auto: San Andreas)", 'https://redd.it/1h4un12')
add_data(['CJ'],
'CJ',
False,
False,
[
    ['Grand Theft Auto'], ['GTA', 'San Andreas'], ['GTA:? SA'], ['CJ ?\[GTA\]'], ['CJ ?\(GTA\)']
],
'GTA',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Carl Johnson'],
'Carl Johnson',
False,
False,
[
    ['Grand Theft Auto'], ['GTA']
],
'GTA',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect the Sheena (Manifold Series)', 'https://redd.it/1h4vnh6')
add_data(['Sheena'],
'Sheena',
False,
False,
[
    ['Manifold']
],
'Manifold Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h4vnh6/respect_the_sheena_manifold_series/

########################################

id = get_rt_id(cur, 'Respect the Crackers (Manifold Series)', 'https://redd.it/1h5nvc0')
add_data(['Crackers'],
'Crackers',
False,
False,
[
    ['Manifold']
],
'Manifold Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bill Rizer (Contra)', 'https://redd.it/1h4yntk')
add_data(['Bill Rizer'],
'Bill Rizer',
False,
True,
[
    ['Contra']
],
'Contra',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h4yntk/respect_bill_rizer_contra/

########################################

id = get_rt_id(cur, "Respect the Wasp (The Avengers: Earth''s Mightiest Heroes)", 'https://redd.it/1h51xx0')
add_data(['Wasp'],
'Wasp',
False,
False,
[
    ['Avengers:? Earths? Mightiest Heroes'], ['Avengers:? Earth\'\'s Mightiest Heroes'], ['A(vengers)?: ?EMH'],
	["Earth''?s? Mightiest Heroes", 'Disney']
],
'Earth''s Mightiest Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h51xx0/respect_the_wasp_the_avengers_earths_mightiest/

########################################

id = get_rt_id(cur, 'Respect Venom (Insomniac Spider-Man/Earth-1048)', 'https://redd.it/1h5o930')
add_data(['Venom'],
'Venom',
False,
False,
[
    ['Insomniac(verse)?s?'], ['Spider(-| )?Man', 'PS4'], ['1048']
],
'Insomniac''s Spider-Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h5o930/respect_venom_insomniac_spidermanearth1048/

########################################

id = get_rt_id(cur, 'Respect Gosling 0186, aka Brightbill (The Wild Robot (Film))', 'https://redd.it/1h5l1u1')
add_data(['Brightbill'],
'Brightbill',
False,
False,
[
    ['Wild Robot']
],
'The Wild Robot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h5l1u1/respect_gosling_0186_aka_brightbill_the_wild/

########################################

id = get_rt_id(cur, 'Respect Astro Bot (Astro Bot)', 'https://redd.it/1h5nydn')
add_data(['Astro Bots?'],
'Astro Bot',
False,
True,
[
    ['Play ?Station'], ['Sony'], ['PS(\d)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h5nydn/respect_astro_bot_astro_bot/

########################################

id = get_rt_id(cur, 'Respect Gosling 0186, aka Brightbill (The Wild Robot (Film))', 'https://redd.it/1h5l1u1')
add_data(['Brightbill'],
'Brightbill',
False,
False,
[
    ["Hunter''?s Planet"]
],
"Aliens vs. Predator: Hunter''s Planet",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h5y0ly/respect_the_predators_avp_hunters_planet/

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

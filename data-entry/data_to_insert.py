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

add_data(['Lambdadelta'],
'Lambdadelta',
False,
True,
[
    ['Umineko'], ['Bernkastel'], ['Certainty']
],
'Umineko',
'{25691}'
)
#https://www.reddit.com/r/respectthreads/comments/1hv70e4/respect_lambdadelta_the_witch_of_certainty/
#https://www.reddit.com/r/whowouldwin/comments/1ippunh/bernkastel_vs_raven/

########################################

add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Genos'], ['One(-| )Punch Man'], ['OPM']
],
'One Punch Man',
'{4114}'
)
#https://www.reddit.com/r/whowouldwin/comments/1is6rdz/genos_and_sonic_vs_marineford/mde5h17/?context=3

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['Spider(-| )?Mans?'], ['Black Panther']
],
'616',
'{2391}'
)
#https://www.reddit.com/r/whowouldwin/comments/1is36t7/joe_biden_vs_donald_trump_vs_barack_obama/mddf3z4/?context=3

########################################

add_data(['Black ?Panther'],
'Black Panther',
False,
False,
[
    ['Spider(-| )?Mans?'], ['Wolverine']
],
'616',
'{2019}'
)
#https://www.reddit.com/r/whowouldwin/comments/1is36t7/joe_biden_vs_donald_trump_vs_barack_obama/mddf3z4/?context=3


########################################

add_data(['Kyrie Ushiromiya'],
'Kyrie Ushiromiya',
False,
True,
[
    ['Umineko']
],
'Umineko',
'{6266}'
)
#

add_data(['Maria Ushiromiya'],
'Maria Ushiromiya',
False,
True,
[
    ['Umineko']
],
'Umineko',
'{6266}'
)
#

add_data(['Ange Ushiromiya'],
'Ange Ushiromiya',
False,
True,
[
    ['Umineko']
],
'Umineko',
'{6266}'
)
#

########################################

id = get_rt_id(cur, 'Respect DA MEKLORD (Warhammer 40k)', 'https://redd.it/1iq94va')
add_data(['Da Meklord'],
'Da Meklord',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iq94va/respect_da_meklord_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect the Ashen Combine (Marvel Comics)', 'https://redd.it/1iqu7ju')
add_data(['Ashen Combine'],
'Ashen Combine',
True,
True,
[
    ['Marvel'], ['2023']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 64: the Crop Top Armor (Marvel, Earth-616)', 'https://redd.it/1ir54s0')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Crop Top Armor'], ['Model 64']
],
'Crop Top Armor',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ir54s0/respect_iron_man_model_64_the_crop_top_armor/

########################################

id = get_rt_id(cur, 'Respect Tigra (Marvel Mangaverse)', 'https://redd.it/1ir7y9g')
add_data(['Tigra'],
'Tigra',
False,
False,
[
    ['Mangaverse'], ['2301']
],
'Marvel Mangaverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ir7y9g/respect_tigra_marvel_mangaverse/

########################################

id = get_rt_id(cur, 'Respect Dao, Master of all Ninja Warriors (How to become a Teenage Ninja)', 'https://redd.it/1irakcl')
add_data(['Dao'],
'Dao',
False,
False,
[
    ['How to become a Teenage Ninja']
],
'How to become a Teenage Ninja',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Moana''s crewmen (Moana 2)", 'https://redd.it/1iqw001')
add_data(["Moana''s crew(men)?"],
"Moana''s crew",
True,
True,
[
    ['Moana 2']
],
'Moana',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iqw001/respect_moanas_crewmen_moana_2/

########################################

id = get_rt_id(cur, 'Respect Shogun X (Fortnite)', 'https://redd.it/1is55z1')
add_data(['Shogun X'],
'Shogun X',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1is55z1/respect_shogun_x_fortnite/

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

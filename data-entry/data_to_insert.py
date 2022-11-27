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

update_respectthread(cur, 4086, 'Respect Shanks! (One Piece)', 'https://redd.it/z5nv65')
update_respectthread(cur, 22535, 'Respect: Perturabo (Warhammer 40k)', 'https://redd.it/z5pdrd')

########################################

add_data(['Land ?lords'],
'Landlords',
False,
False,
[
    ['Kung Fu Hustle']
],
'Kung Fu Hustle',
'{228}'
)
#https://www.reddit.com/r/whowouldwin/comments/z57xip/the_landlords_from_king_fu_hustle_versus_captain/

########################################

id = get_rt_id(cur, 'Respect The Onmyo Bureau (Ayashimon)', 'https://redd.it/z4ni5s')
add_data(['Onmyo Bureau'],
'Onmyo Bureau',
False,
True,
[
    ['Ayashimon']
],
'Ayashimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z4ni5s/respect_the_onmyo_bureau_ayashimon/

########################################

id = get_rt_id(cur, 'Respect: Kalel Kent, aka Superman 2020 (Pre-Crisis DC Comics)', 'https://redd.it/z4rmhz')
add_data(['Kalel Kent'],
'Kalel Kent',
False,
True,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z4rmhz/respect_kalel_kent_aka_superman_2020_precrisis_dc/

########################################

id = get_rt_id(cur, 'Respect: Jorel Kent, aka Superman II (Pre-Crisis Earth 2020)', 'https://redd.it/z4sf3f')
add_data(['Jorel Kent'],
'Jorel Kent',
False,
True,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z4sf3f/respect_jorel_kent_aka_superman_ii_precrisis/

########################################

id = get_rt_id(cur, 'Respect King William (...And I Show You How Deep The Rabbit Hole Goes)', 'https://redd.it/z4xis2')
add_data(['King William'],
'King William',
False,
False,
[
    ['And I Show You How Deep The Rabbit Hole Goes']
],
'...And I Show You How Deep The Rabbit Hole Goes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z4xis2/respect_king_william_and_i_show_you_how_deep_the/

########################################

id = get_rt_id(cur, 'Respect Evan McCulloch, Mirror Master (DC Post-Crisis)', 'https://redd.it/z5andl')
add_data(['Mirror Master'],
'Mirror Master',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z5andl/respect_evan_mcculloch_mirror_master_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect: Clark Kent, Superman I (Pre-Crisis Earth 2020)', 'https://redd.it/z6bm20')
add_data(['Super(-| )?man I'],
'Superman I',
False,
False,
[
    ['Earth(-| )2020']
],
'Earth 2020',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z6bm20/respect_clark_kent_superman_i_precrisis_earth_2020/

########################################

id = get_rt_id(cur, 'Respect Spider-Nor-Man (Marvel, Earth-44145)', 'https://redd.it/z5ikb0')
add_data(['Spider(-| )Nor(-| )Man'],
'Spider-Nor-Man',
False,
True,
[
    ['44145']
],
'44145',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z5ikb0/respect_spidernorman_marvel_earth44145/

########################################

id = get_rt_id(cur, 'Respect Helen (Claymore)', 'https://redd.it/z5bb9q')
add_data(['Helen'],
'Helen',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z5bb9q/respect_helen_claymore/

########################################

id = get_rt_id(cur, 'Respect Daisuke Kambe (The Millionaire Detective Balance: Unlimited)', 'https://redd.it/z5anfl')
add_data(['Daisuke Kambe'],
'Daisuke Kambe',
False,
True,
[
    ['Millionaire Detective']
],
'The Millionaire Detective Balance: Unlimited',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z5anfl/respect_daisuke_kambe_the_millionaire_detective/

########################################

id = get_rt_id(cur, 'Respect Jewelry Bonney! (One Piece)', 'https://redd.it/z5nxho')
add_data(['Jewelry Bonney'],
'Jewelry Bonney',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z5nxho/respect_jewelry_bonney_one_piece/

########################################

id = get_rt_id(cur, 'Respect Steven Stone (Pokemon Anime)', 'https://redd.it/z61caz')
add_data(['Steven Stone'],
'Steven Stone',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z61caz/respect_steven_stone_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect The Sabertooth Swordsman (Sabertooth Swordsman)', 'https://redd.it/z66beg')
add_data(['Sabertooth Swordsman'],
'Sabertooth Swordsman',
False,
True,
[
    ['Sabertooth Swordsman ?\(Sabertooth Swordsman']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z66beg/respect_the_sabertooth_swordsman_sabertooth/ 

########################################

id = get_rt_id(cur, 'Respect: Rogal Dorn (Warhammer 40k)', 'https://redd.it/z6afhi')
add_data(['Rogal Dorn'],
'Rogal Dorn',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/z6afhi/respect_rogal_dorn_warhammer_40k/

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

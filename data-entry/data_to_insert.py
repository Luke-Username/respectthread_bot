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

add_data(['Unohana'],
'Unohana',
False,
False,
[
    ['Bleach']
],
'Bleach',
'{3159}'
)
#https://www.reddit.com/r/whowouldwin/comments/14zgh2s/aquakingdom_hearts_vs_unohanableach/

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['20th Century Fox'], ['FOX Wolverine']
],
'FOX',
'{158}'
)
#https://www.reddit.com/r/whowouldwin/comments/150i5qr/wolverine_marvelxmen_runs_the_gauntlet_of/js39yvg/?context=3

########################################

id = get_rt_id(cur, 'Respect Abyss (DC Comics, Rebirth)', 'https://redd.it/14yb03l')
add_data(['Abyss'],
'Abyss',
False,
False,
[
    ['DC', 'Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14yb03l/respect_abyss_dc_comics_rebirth/

########################################

id = get_rt_id(cur, 'Respect Jim Gordon, Batman (DC Comics, Post Flashpoint)', 'https://redd.it/14zfzq7')
add_data(['Jim Gordon'],
'Jim Gordon',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14zfzq7/respect_jim_gordon_batman_dc_comics_post/

########################################

id = get_rt_id(cur, 'Respect Peter Palmer, The Amazing Spiderman! (Marvel, 616 Beta)', 'https://redd.it/14zuogg')
add_data(['Peter Palmer'],
'Peter Palmer',
False,
False,
[
    ['616', 'Beta']
],
'616 Beta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14zuogg/respect_peter_palmer_the_amazing_spiderman_marvel/

########################################

id = get_rt_id(cur, 'Respect Bloodwork (Arrowverse)', 'https://redd.it/150bf2m')
add_data(['Bloodwork'],
'Bloodwork',
False,
False,
[
    ['(Fl)?arrow(-| )?verse'], ['(DC)?CW'], ['DC ?TV']
],
'CW Arrowverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/150bf2m/respect_bloodwork_arrowverse/

########################################

id = get_rt_id(cur, 'Respect Rusty the Boy Robot (Big Guy and Rusty the Boy Robot [Comic])', 'https://redd.it/14ynanq')
add_data(['Rusty the Boy Robot'],
'Rusty the Boy Robot',
False,
True,
[
    ['Big Guy and Rusty']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ynanq/respect_rusty_the_boy_robot_big_guy_and_rusty_the/

########################################

id = get_rt_id(cur, 'Respect Yuzun (Dragon Ball Super - Manga)', 'https://redd.it/14z5xj0')
add_data(['Yuzun'],
'Yuzun',
False,
False,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yorozu! (Jujutsu Kaisen)', 'https://redd.it/14zk9ur')
add_data(['Yorozu'],
'Yorozu',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14zk9ur/respect_yorozu_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Lily Tora-Asi (Star Wars Canon)', 'https://redd.it/150l13l')
add_data(['Lily Tora(-| )Asi'],
'Lily Tora-Asi',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/150l13l/respect_lily_toraasi_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Lily Tora-Asi (Star Wars Canon)', 'https://redd.it/150l13l')
add_data(['Pet Shop'],
'Pet Shop',
False,
False,
[
    ['I Get Stronger the More I Eat']
],
'I Get Stronger the More I Eat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/150lsm6/respect_mr_kim_pet_shop_i_get_stronger_the_more_i/

add_data(['Mr\.? Kim'],
'Mr. Kim',
False,
False,
[
    ['I Get Stronger the More I Eat']
],
'I Get Stronger the More I Eat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/150lsm6/respect_mr_kim_pet_shop_i_get_stronger_the_more_i/

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

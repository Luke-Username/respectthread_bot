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

update_respectthread(cur, 553, 'Respect the Sharktopi (Sharktopus)', 'https://redd.it/10wgrmi')

########################################

add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['whatever a spider can']
],
'1967',
'{23059}'
)
#https://www.reddit.com/r/whowouldwin/comments/10v8cw1/featured_character_spiderman_67/j7fx3vx/?context=3

########################################

id = get_rt_id(cur, 'Respect Mr. Zsasz (DC Comics, Post Crisis)', 'https://redd.it/10udlrd')
add_data(['Zsasz'],
'Zsasz',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10udlrd/respect_mr_zsasz_dc_comics_post_crisis/

add_data(['Zsasz'],
'Zsasz',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10udlrd/respect_mr_zsasz_dc_comics_post_crisis/

add_data(['Zsasz'],
'Zsasz',
False,
False,
[
    ['Gotham version'], ['Gotham', 'tv Series']
],
'Gotham',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10udlrd/respect_mr_zsasz_dc_comics_post_crisis/

########################################

id = get_rt_id(cur, 'Respect The Thanapod (LOVE DEATH + ROBOTS)', 'https://redd.it/10uf5ya')
add_data(['Thanapod'],
'Thanapod',
False,
True,
[
    ['Love','Death','Robots']
],
'Love, Death, & Robots',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10uf5ya/respect_the_thanapod_love_death_robots/

########################################

id = get_rt_id(cur, 'Respect Morbius (Spider-man 3 PS3/Wii game (Marvel Earth-96283))', 'https://redd.it/10ujb9c')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['Spider(-| )?Mans? 3','PS3|Wii']
],
'96283',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10ujb9c/respect_morbius_spiderman_3_ps3wii_game_marvel/

########################################

id = get_rt_id(cur, 'Respect Coco (Crash Bandicoot)', 'https://redd.it/10vgaoz')
add_data(['Coco'],
'Coco',
False,
False,
[
    ['Crash Bandicoot']
],
'Crash Bandicoot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10vgaoz/respect_coco_crash_bandicoot/

########################################

id = get_rt_id(cur, 'Respect Uka Uka (Crash Bandicoot)', 'https://redd.it/10weeuy')
add_data(['Uka Uka'],
'Uka Uka',
False,
False,
[
    ['Crash Bandicoot']
],
'Crash Bandicoot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10weeuy/respect_uka_uka_crash_bandicoot/

########################################

id = get_rt_id(cur, 'Respect Sphinx! (Sphinx and the Cursed Mummy)', 'https://redd.it/10vkk3t')
add_data(['Sphinx'],
'Sphinx',
False,
False,
[
    ['Sphinx and the Cursed Mummy']
],
'Sphinx and the Cursed Mummy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10vkk3t/respect_sphinx_sphinx_and_the_cursed_mummy/

########################################

id = get_rt_id(cur, 'Respect Tutankhamen, the Cursed Mummy! (Sphinx and the Cursed Mummy)', 'https://redd.it/10vkl63')
add_data(['Tutankham(u|e)n'],
'Tutankhamun',
False,
False,
[
    ['Sphinx and the Cursed Mummy']
],
'Sphinx and the Cursed Mummy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10vkl63/respect_tutankhamen_the_cursed_mummy_sphinx_and/

########################################

id = get_rt_id(cur, 'Respect The Death Dealer! (Death Dealer)', 'https://redd.it/10vmt9f')
add_data(['Death Dealer'],
'Death Dealer',
False,
False,
[
    ['Death Dealer ?\(Death Dealer']
],
'Death Dealer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10vmt9f/respect_the_death_dealer_death_dealer/

########################################

id = get_rt_id(cur, 'Respect the Keeper (The Evil Within)', 'https://redd.it/10w2eg2')
add_data(['Keeper'],
'Keeper',
False,
False,
[
    ['Evil Within']
],
'The Evil Within',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10w2eg2/respect_the_keeper_the_evil_within/

########################################

id = get_rt_id(cur, 'Respect Mac Gargan, Virus (Marvel, 616)', 'https://redd.it/10w3t7i')
add_data(['Mac Gargan'],
'Mac Gargan',
False,
False,
[
    ['Virus']
],
'Virus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10w3t7i/respect_mac_gargan_virus_marvel_616/
 
########################################

id = get_rt_id(cur, 'Respect The God of Chaos, Aesir (Bayonetta)', 'https://redd.it/10w6r7e')
add_data(['Aesir'],
'Aesir',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10w6r7e/respect_the_god_of_chaos_aesir_bayonetta/

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

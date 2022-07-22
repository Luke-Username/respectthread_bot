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

update_respectthread(cur, 13269, 'Respect Puck (Re:Zero, Anime)', 'https://redd.it/w3lxm0')

########################################

add_data(['Mega ?man'],
'Megaman',
False,
False,
[
    ['Battle Network']
],
'MegaMan NT Warrior',
'{4854}'
)
#https://www.reddit.com/r/whowouldwin/comments/w4h0yz/lan_and_megamanexe_vs_xana_megaman_battle_network/ih2hvwv/?context=3

########################################

add_data(['Adam'],
'Adam',
False,
False,
[
    ['Adam ?\(ROR']
],
'Shuumatsu no Valkyrie',
'{4539}'
)
#https://www.reddit.com/r/whowouldwin/comments/w3ypzc/adamror_vs_garou/igz0ng6/?context=3

########################################

add_data(['Hyperion'],
'Hyperion',
False,
False,
[
    ['Superman']
],
'Marvel',
'{2163,2164,2165,2166}'
)
#https://www.reddit.com/r/whowouldwin/comments/w4p0le/free_for_all_superman_vs_omni_man_vs_hyperion_vs/ih38t86/?context=3

########################################

add_data(['Bec Noir'],
'Bec Noir',
False,
True,
[
    ['Homestuck']
],
'Homestuck',
'{2876}'
)
#https://www.reddit.com/r/whowouldwin/comments/w48w8h/vsbattles_tier_2_thunderdome/ih0ncmw/?context=3

########################################

add_data(['Chaos 0'],
'Chaos 0',
False,
False,
[
    ['Sonic']
],
'Sonic the Hedgehog',
'{8577}'
)
#https://www.reddit.com/r/whowouldwin/comments/w48w8h/vsbattles_tier_2_thunderdome/ih0ncmw/?context=3

########################################

add_data(['Toothless'],
'Toothless',
False,
False,
[
    ['Toothless vs', 'fly']
],
'How to Train Your Dragon',
'{6572}'
)
#https://www.reddit.com/r/whowouldwin/comments/w3q3r2/toothless_vs_aang/igxkvps/?context=3

########################################

id = get_rt_id(cur, "Respect Kim''Dael, The Blood Moon Huntress (The Dragon Prince)", 'https://redd.it/w3ajj3')
add_data(["Kim''Dael"],
"Kim''Dael",
False,
False,
[
    ['Dragon Prince']
],
'The Dragon Prince',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3ajj3/respect_kimdael_the_blood_moon_huntress_the/

########################################

id = get_rt_id(cur, 'Respect Finn the Superhuman (Adventure Time [Comics])', 'https://redd.it/w3mm2q')
add_data(['Finn the Superhuman'],
'Finn the Superhuman',
False,
False,
[
    ['Adventure Time', 'Comics']
],
'Adventure Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3mm2q/respect_finn_the_superhuman_adventure_time_comics/

########################################

id = get_rt_id(cur, 'Respect Roxie! (Five Kingdoms)', 'https://redd.it/w3njzw')
add_data(['Roxie'],
'Roxie',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3njzw/respect_roxie_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Sidekick! (Five Kingdoms)', 'https://redd.it/w3y3je')
add_data(['Sidekick'],
'Sidekick',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3y3je/respect_sidekick_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Bowser (Brothers in Arms)', 'https://redd.it/w3psn6')
add_data(['Bowser'],
'Bowser',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3psn6/respect_bowser_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Samus (Brothers in Arms)', 'https://redd.it/w3q1v7')
add_data(['Samus'],
'Samus Aran',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3q1v7/respect_samus_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Pedro (One Piece)', 'https://redd.it/w4685i')
add_data(['Pedro'],
'Pedro',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w4685i/respect_pedro_one_piece/

########################################

id = get_rt_id(cur, "Respect Kin''emon (One Piece)", 'https://redd.it/w3ta3s')
add_data(["Kin''emon"],
"Kin''emon",
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3ta3s/respect_kinemon_one_piece/

add_data(["Kinemon"],
"Kinemon",
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3ta3s/respect_kinemon_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Leanansidhe (The Dresden Files)', 'https://redd.it/w3v448')
add_data(['Leanansidhe'],
'Leanansidhe',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w3v448/respect_the_leanansidhe_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Biggy (FIGHTERS)', 'https://redd.it/w4id89')
add_data(['Biggy'],
'Biggy',
False,
False,
[
    ['Biggy ?\(FIGHTERS\)']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w4id89/respect_biggy_fighters/

########################################

id = get_rt_id(cur, 'Respect Kamala Khan! (Marvel Cinematic Universe)', 'https://redd.it/w4uxof')
add_data(['Kh?amala Khan'],
'Kamala Khan',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w4uxof/respect_kamala_khan_marvel_cinematic_universe/

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

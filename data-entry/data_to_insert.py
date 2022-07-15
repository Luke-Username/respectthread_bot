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

update_respectthread(cur, 8143, 'Respect Narushima Koga, The Fist Eye! (Kengan Omega)', 'https://redd.it/vyg6u5')

########################################

id = get_rt_id(cur, 'Respect Kushala, the Spirit Rider (Marvel, 616)', 'https://redd.it/vxoohy')
add_data(['Kushala'],
'Kushala',
False,
False,
[
    ['616'], ['Spirit Rider'], ['Marvel']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vxoohy/respect_kushala_the_spirit_rider_marvel_616/

########################################

id = get_rt_id(cur, 'Respect America Chavez (Marvel Cinematic Universe)', 'https://redd.it/vyudsa')
add_data(['America Chavez'],
'America Chavez',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU'], ['Doctor Strange 2']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vyudsa/respect_america_chavez_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Strength of a River in His Shoulders (The Dresden Files)', 'https://redd.it/vxtba3')
add_data(['Strength of a River in His Shoulders'],
'Strength of a River in His Shoulders',
False,
True,
[
    ['Dresden']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vxtba3/respect_strength_of_a_river_in_his_shoulders_the/

########################################

id = get_rt_id(cur, 'Respect Warden Carlos Ramirez (The Dresden Files)', 'https://redd.it/vyan2m')
add_data(['Carlos Ramirez'],
'Carlos Ramirez',
False,
False,
[
    ['Dresden'], ['Warden']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vyan2m/respect_warden_carlos_ramirez_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect the Blackstaff, Ebenezer McCoy (The Dresden Files)', 'https://redd.it/vz17w4')
add_data(['Ebenez(a|e)r McCoy'],
'Ebenezar McCoy',
False,
True,
[
    ['Dresden']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vz17w4/respect_the_blackstaff_ebenezer_mccoy_the_dresden/

########################################

id = get_rt_id(cur, 'Respect Ivy, the Archive (The Dresden Files)', 'https://redd.it/vz4sft')
add_data(['Ivy'],
'Ivy',
False,
False,
[
    ['Dresden Files'], ['The Archive']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vz4sft/respect_ivy_the_archive_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Sha Wujing (Xi Xing Ji)', 'https://redd.it/vy0ndl')
add_data(['Sha Wujing'],
'Sha Wujing',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vy0ndl/respect_sha_wujing_xi_xing_ji/

########################################

id = get_rt_id(cur, 'Respect Sun Wukong (Xi Xing Ji)', 'https://redd.it/vyu5bj')
add_data(['Sun Wu ?Kong'],
'Sun Wukong',
False,
False,
[
    ['Xi Xing Ji']
],
'Xi Xing Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vyu5bj/respect_sun_wukong_xi_xing_ji/

########################################

id = get_rt_id(cur, 'Respect Echidna, the Witch of Greed (Re:Zero, Anime)', 'https://redd.it/vy2tpy')
add_data(['Echidna'],
'Echidna',
False,
False,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vy2tpy/respect_echidna_the_witch_of_greed_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Satella, the Witch of Envy (Re:Zero, Anime)', 'https://redd.it/vyvdhe')
add_data(['Satella'],
'Satella',
False,
True,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vyvdhe/respect_satella_the_witch_of_envy_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Izou (One Piece)', 'https://redd.it/vye1hx')
add_data(['Izou'],
'Izou',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vye1hx/respect_izou_one_piece/

add_data(['Izo'],
'Izo',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vye1hx/respect_izou_one_piece/

########################################

id = get_rt_id(cur, 'Respect Skye Ryland! (Five Kingdoms)', 'https://redd.it/vyey72')
add_data(['Skye Ryland'],
'Skye Ryland',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vyey72/respect_skye_ryland_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect SCP-2241 (SCP Foundation)', 'https://redd.it/vzioby')
add_data(['SCP ?(-| )? ?2241'],
'SCP-2241',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vzioby/respect_scp2241_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Eleven (Stranger Things)', 'https://redd.it/vzst6f')
add_data(['Eleven'],
'Eleven',
False,
False,
[
    ['Stranger Things']
],
'Stranger Things',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vzst6f/respect_eleven_stranger_things/

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

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

add_data(['Predator'],
'Predator',
False,
False,
[
    ['Spider(-| )?Man']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/txs88j/a_newbie_predator_vs_spiderman_on_his_1st_day/

########################################

id = get_rt_id(cur, 'Respect Hank Rutherford Hill! (King of the Hill)', 'https://redd.it/tx8xiw')
add_data(['Hank Hill'],
'Hank Hill',
False,
True,
[
    ['King of the Hill']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xiw/respect_hank_rutherford_hill_king_of_the_hill/

########################################

id = get_rt_id(cur, 'Respect Peggy Hill! (King of the Hill)', 'https://redd.it/tx8xo9')
add_data(['Peggy Hill'],
'Peggy Hill',
False,
True,
[
    ['King of the Hill']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xo9/respect_peggy_hill_king_of_the_hill/

########################################

id = get_rt_id(cur, 'Respect Bobby Hill! (King of the Hill)', 'https://redd.it/tx8xtj')
add_data(['Bobby Hill'],
'Bobby Hill',
False,
True,
[
    ['King of the Hill']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xtj/respect_bobby_hill_king_of_the_hill/

add_data(['Bobby'],
'Bobby',
False,
False,
[
    ['King of the Hill'], ['Hank|Peggy', 'Hill']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xtj/respect_bobby_hill_king_of_the_hill/

########################################

id = get_rt_id(cur, 'Respect Dale Gribble! (King of the Hill!)', 'https://redd.it/tx8xzo')
add_data(['Dale Gribble'],
'Dale Gribble',
False,
True,
[
    ['King of the Hill']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xzo/respect_dale_gribble_king_of_the_hill/

add_data(['Dale'],
'Dale',
False,
False,
[
    ['King of the Hill'], ['Hank', 'Hill'], ['pocket sand']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8xzo/respect_dale_gribble_king_of_the_hill/

########################################

id = get_rt_id(cur, 'Respect Sergeant William Fontaine de la Tour Dauterive (King of the Hill)', 'https://redd.it/tx8y5z')
add_data(['Bill Dauterive'],
'Bill Dauterive',
False,
True,
[
    ['King of the Hill'], ['KOTH']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8y5z/respect_sergeant_william_fontaine_de_la_tour/

add_data(['Bill'],
'Bill',
False,
False,
[
    ['King of the Hill'], ['KOTH']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8y5z/respect_sergeant_william_fontaine_de_la_tour/

########################################

id = get_rt_id(cur, 'Respect Luanne Platter! (King of the Hill)', 'https://redd.it/tx8y9w')
add_data(['Luanna Platter'],
'Luanna Platter',
False,
True,
[
    ['King of the Hill'], ['KOTH']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8y9w/respect_luanne_platter_king_of_the_hill/

########################################

id = get_rt_id(cur, 'Respect Kahn and Minh Souphanousinphone! (King of the Hill)', 'https://redd.it/tx8yiy')
add_data(['K(ah|ha)ns?'],
'Kahn',
False,
False,
[
    ['King of the Hill'], ['KOTH'], ['Souphanousinphone']
],
'King of the Hill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tx8yiy/respect_kahn_and_minh_souphanousinphone_king_of/

########################################

id = get_rt_id(cur, 'Respect Nora Fries, Mrs. Freeze (DC, Rebirth)', 'https://redd.it/tyeu1x')
add_data(['Nora Fries'],
'Nora Fries',
False,
False,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tyeu1x/respect_nora_fries_mrs_freeze_dc_rebirth/

add_data(['Nora Fries'],
'Nora Fries',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tyeu1x/respect_nora_fries_mrs_freeze_dc_rebirth/


########################################

id = get_rt_id(cur, 'Respect Lewis Padgett, Microwave Man (DC Pre-Crisis)', 'https://redd.it/txo3ml')
add_data(['Microwave(-| )Man'],
'Microwave Man',
False,
True,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/txo3ml/respect_lewis_padgett_microwave_man_dc_precrisis/

add_data(['Microwave(-| )Man'],
'Microwave Man',
False,
True,
[
    ['DC'], ['Padgett']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/txo3ml/respect_lewis_padgett_microwave_man_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Rudo! (Gachiakuta)', 'https://redd.it/ty5bbj')
add_data(['Rudo'],
'Rudo',
False,
False,
[
    ['Gachiakuta']
],
'Gachiakuta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ty5bbj/respect_rudo_gachiakuta/

########################################

id = get_rt_id(cur, 'Respect Souichirou Kuzuki! (Fate)', 'https://redd.it/tyhzlg')
add_data(['Sou?ichirou? Kuzuki|Kuzuki Sou?ichirou?'],
'Souichirou Kuzuki',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tyhzlg/respect_souichirou_kuzuki_fate/

########################################

id = get_rt_id(cur, 'Respect the Amazon Warriors (DCEU)', 'https://redd.it/tymjqi')
add_data(['Amazons'],
'Amazons',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tymjqi/respect_the_amazon_warriors_dceu/

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

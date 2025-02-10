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

update_respectthread(cur, 3573, "Respect Vanilla Ice (Jojo''s Bizarre Adventure)", 'https://redd.it/1ik8oow')
update_respectthread(cur, 5397, 'Respect Crimson Viper! (Street Fighter)', 'https://redd.it/1ikn4w6')

########################################

add_data(['Bill'],
'Bill',
False,
False,
[
    ['King of the Hill'], ['Hank Hill']
],
'King of the Hill',
'{21734}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ilu3o1/hank_hill_and_dale_vs_bill_and_boomhauer/mc0vfbm/?context=3

add_data(['Bill Dauterive'],
'Bill Dauterive',
False,
True,
[
    ['King of the Hill'], ['Hank Hill']
],
'King of the Hill',
'{21734}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ilu3o1/hank_hill_and_dale_vs_bill_and_boomhauer/mc0vfbm/?context=3

########################################

id = get_rt_id(cur, "Respect Nukesaku (Jojo''s Bizarre Adventure)", 'https://redd.it/1ikl3r0')
add_data(['Nukesaku'],
'Nukesaku',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ikl3r0/respect_nukesaku_jojos_bizarre_adventure/

########################################

id = get_rt_id(cur, 'Respect Able (Character Scramble) (Season 17)', 'https://redd.it/1ikt46a')
add_data(['Able'],
'Able',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ikt46a/respect_able_character_scramble_season_17/

########################################

id = get_rt_id(cur, 'Respect Lucam (Pokemon ReBurst)', 'https://redd.it/1il5fqx')
add_data(['Lucam'],
'Lucam',
False,
False,
[
    ['(Pok(e|é)m(o|a)n)|monsters) ReBurst']
],
'Pocket Monsters RéBURST',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Migs Mayfeld (Star Wars Canon)', 'https://redd.it/1il7fzy')
add_data(['Migs Mayfeld'],
'Migs Mayfeld',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1il7fzy/respect_migs_mayfeld_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Jack of Hearts (Marvel Comics, Earth-616)', 'https://redd.it/1ilkl23')
add_data(['Jack of Hearts'],
'Jack of Hearts',
False,
False,
[
    ['616'], ['Marvel']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ilkl23/respect_jack_of_hearts_marvel_comics_earth616/


########################################

id = get_rt_id(cur, "Respect Cole Rainsford (Cabela''s Dangerous Hunts 2011)", 'https://redd.it/1ilwf8d')
add_data(['Cole Rainsford'],
'Cole Rainsford',
False,
False,
[
    ["Dangerous Hunts"]
],
"Cabela''s Dangerous Hunts",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ilwf8d/respect_cole_rainsford_cabelas_dangerous_hunts/

########################################

id = get_rt_id(cur, 'Respect Boothill (Honkai: Star Rail)', 'https://redd.it/1im6p2u')
add_data(['Boothill'],
'Boothill',
False,
False,
[
    ['Honkai']
],
'Honkai: Star Rail',
'{' + '{}'.format(id) + '}'
)
#

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

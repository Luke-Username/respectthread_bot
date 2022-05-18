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

add_data(['The Thing'],
'The Thing',
False,
False,
[
    ['2005.*2007']
],
'Fantastic Four Movies',
'{8573}'
)
#https://www.reddit.com/r/whowouldwin/comments/ur1nh0/the_thing_20052004_vs_korg_mcu/i8ugpqj/?context=3

########################################

add_data(['Jean Gr(e|a)y'],
'Jean Grey',
False,
False,
[
    ['X(-| )?Men ?:( The)? ?Last Stand'], ['\(Last Stand\)']
],
'FOX',
'{14882}'
)
#https://www.reddit.com/r/whowouldwin/comments/urunr2/the_phoenix_xmen_last_stand_vs_scarlett_witch/i92yvpe/?context=3

########################################

add_data(['The Mods'],
'The Mods',
False,
False,
[
    ['Star Wars']
],
'Star Wars',
'{21385}'
)
#https://www.reddit.com/r/whowouldwin/comments/usbkxx/rey_skywalker_vs_bobba_fetts_gang_star_wars/i92cvq7/?context=3

########################################

id = get_rt_id(cur, 'Respect Kamen Rider Century (Kamen Rider Beyond Generations)!', 'https://redd.it/ura7ye')
add_data(['Kamen Rider Century'],
'Kamen Rider Century',
False,
True,
[
    ['Beyond Generations']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ura7ye/respect_kamen_rider_century_kamen_rider_beyond/

########################################

id = get_rt_id(cur, 'Respect Godzilla (IDW Comics Anthologies)', 'https://redd.it/urqlt7')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Godzilla: Rivals'], ['Godzilla:? Legends']
],
'IDW Anthologies',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/urqlt7/respect_godzilla_idw_comics_anthologies/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla: Gangsters and Goliaths)', 'https://redd.it/urvxvz')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Gangsters and Goliaths']
],
'Gangsters and Goliaths',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/urvxvz/respect_godzilla_godzilla_gangsters_and_goliaths/

########################################

id = get_rt_id(cur, 'Respect Billy Hatcher (Billy Hatcher and the Giant Egg)', 'https://redd.it/urt3y5')
add_data(['Billy Hatcher'],
'Billy Hatcher',
False,
True,
[
    ['Giant Egg']
],
'Billy Hatcher and the Giant Egg',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/urt3y5/respect_billy_hatcher_billy_hatcher_and_the_giant/

########################################

id = get_rt_id(cur, 'Respect Princess Lana (Captain N: The Game Master)', 'https://redd.it/urw7aw')
add_data(['Princess Lana'],
'Princess Lana',
False,
False,
[
    ['Captain N']
],
'Captain N: The Game Master',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/urw7aw/respect_princess_lana_captain_n_the_game_master/

########################################

id = get_rt_id(cur, 'Respect Prince Mamuwalde (Blacula)', 'https://redd.it/us28da')
add_data(['Blacula'],
'Blacula',
False,
True,
[
    ['Mamuwalde']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/us28da/respect_prince_mamuwalde_blacula/

########################################

id = get_rt_id(cur, 'Respect Peter Parker, Spider-Man (Spider-Man Unlimited)', 'https://redd.it/us9v3e')
add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Spider(-| )?Man Unlimited']
],
'Spider-Man Unlimited',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/us9v3e/respect_peter_parker_spiderman_spiderman_unlimited/

########################################

id = get_rt_id(cur, 'Respect Arthur Nagan, Gorilla-Man (Marvel, 616)', 'https://redd.it/usc1a8')
add_data(['Gorilla(-| )Man'],
'Gorilla-Man',
False,
False,
[
    ['Arthur Nagan']
],
'Arthur Nagan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/usc1a8/respect_arthur_nagan_gorillaman_marvel_616/

########################################

id = get_rt_id(cur, "Respect Dola''s Gang (Laputa: Castle in the Sky)", 'https://redd.it/ushj2b')
add_data(['Dola'],
'Dola',
False,
False,
[
    ['Castle in the Sky']
],
'Castle in the Sky',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ushj2b/respect_dolas_gang_laputa_castle_in_the_sky/

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

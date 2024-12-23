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

add_data(['Shocker'],
'Shocker',
False,
False,
[
    ['Shocker vs', 'Doc Ock']
],
'616',
'{2276}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hkap3l/shocker_vs_doc_ock/

########################################

add_data(['Cassandra Nova'],
'Cassandra Nova',
False,
False,
[
    ['Movie versions']
],
'MCU',
'{25393}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hiihes/darth_vader_vs_cassandra_nova/

########################################

add_data(['Solider Boy'],
'Solider Boy',
False,
False,
[
    ['The Boys']
],
'The Boys',
'{22191}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hip552/solider_boy_the_boys_vs_adam_smasher_cyberpunk/

########################################

id = get_rt_id(cur, 'Respect Zoe Laveau (Marvel 616)', 'https://redd.it/1hidmkm')
add_data(['Zoe Laveau'],
'Zoe Laveau',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Optimus Primal (Transformers: Rise of the Beasts)', 'https://redd.it/1hidhm6')
add_data(['Optimus Primal'],
'Optimus Primal',
False,
False,
[
    ['Rise of the Beasts']
],
'Transformers: Rise of the Beasts',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hidhm6/respect_optimus_primal_transformers_rise_of_the/

########################################

id = get_rt_id(cur, "Respect Jega ''Rdomnai (Halo)", 'https://redd.it/1hidb17')
add_data(["Jega ''?Rdomnai"],
"Jega ''Rdomnai",
False,
True,
[
    ['Halo']
],
'Halo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hidb17/respect_jega_rdomnai_halo/

########################################

id = get_rt_id(cur, 'Respect the Zergling! (Starcraft)', 'https://redd.it/1hiq963')
add_data(['Zerglings?'],
'Zergling',
False,
True,
[
    ['Star ?Craft']
],
'StarCraft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hiq963/respect_the_zergling_starcraft/

add_data(['Zergs?'],
'Zerg',
False,
False,
[
    ['Star ?Craft'], ['Overmind|hivemind'], ['The Zerg'], ['Tyranids?'], ['Zerg (Swarm|Rush)'], ['Legacy of the Void'], ['LotV']
],
'StarCraft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hiq963/respect_the_zergling_starcraft/

########################################

id = get_rt_id(cur, 'Respect the Rabid Grannies (Rabid Grannies)', 'https://redd.it/1hiuvct')
add_data(['Rabid Grannies'],
'Rabid Grannies',
False,
True,
[
    ['Remington']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hiuvct/respect_the_rabid_grannies_rabid_grannies/

########################################

id = get_rt_id(cur, 'Respect Slime (Loop Hero)', 'https://redd.it/1hj6p42')
add_data(['Slime'],
'Slime',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

add_data(['Slimes'],
'Slimes',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

########################################

id = get_rt_id(cur, 'Respect Ratwolf (Loop Hero)', 'https://redd.it/1hj6s05')
add_data(['Ratwolf'],
'Ratwolf',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

add_data(['Ratwolves'],
'Ratwolves',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Skeletons (Loop Hero)', 'https://redd.it/1hj74ze')
add_data(['Skeleton'],
'Skeleton',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

add_data(['Skeletons'],
'Skeletons',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Mimic (Loop Hero)', 'https://redd.it/1hj7ga6')
add_data(['Mimic'],
'Mimic',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

add_data(['Mimics'],
'Mimics',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Common Enemies (Loop Hero)', 'https://redd.it/1hj7hre')
add_data(['Common Enemies'],
'Common Enemies',
True,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hj6p42/respect_slime_loop_hero/

########################################

id = get_rt_id(cur, 'Respect Spider (Loop Hero)', 'https://redd.it/1hjvlnh')
add_data(['Spider'],
'Spider',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Spiders'],
'Spiders',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Blood Clot (Loop Hero)', 'https://redd.it/1hjvnow')
add_data(['Blood Clot'],
'Blood Clot',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Blood Clots'],
'Blood Clots',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Vampires (Loop Hero)', 'https://redd.it/1hjvvvp')
add_data(['Vampire'],
'Vampire',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Vampires'],
'Vampires',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#



########################################

id = get_rt_id(cur, 'Respect Watchers (Loop Hero)', 'https://redd.it/1hjw0qq')
add_data(['Watcher'],
'Watcher',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Watchers'],
'Watchers',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tome (Loop Hero)', 'https://redd.it/1hjw4ip')
add_data(['Tome'],
'Tome',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tomes'],
'Tomes',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Goblins (Loop Hero)', 'https://redd.it/1hklcvd')
add_data(['Goblin'],
'Goblin',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Goblins'],
'Goblins',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bandit (Loop Hero)', 'https://redd.it/1hkliwc')
add_data(['Bandit'],
'Bandit',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Bandits'],
'Bandits',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Harpy (Loop Hero)', 'https://redd.it/1hklmev')
add_data(['Harpy'],
'Harpy',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Harpies'],
'Harpies',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gargoyle (Loop Hero)', 'https://redd.it/1hklpet')
add_data(['Gargoyle'],
'Gargoyle',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Gargoyles'],
'Gargoyles',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hklpet/respect_gargoyle_loop_hero/

########################################

id = get_rt_id(cur, 'Respect Living Armor (Loop Hero)', 'https://redd.it/1hklyak')
add_data(['Living Armou?r'],
'Living Armor',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Loona! (Helluva Boss)', 'https://redd.it/1hkjbth')
add_data(['Loona'],
'Loona',
False,
False,
[
    ['Helluva Boss']
],
'Helluva Boss',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hkjbth/respect_loona_helluva_boss/

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

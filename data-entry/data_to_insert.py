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

update_respectthread(cur, 23243, 'Respect Denzel Crocker! (The Fairly OddParents)', 'https://www.reddit.com/r/respectthreads/comments/10hvsus/respect_denzel_crocker_the_fairly_oddparents/')
update_respectthread(cur, 7632, 'Respect Superman (DC Rebirth)', 'https://www.reddit.com/r/respectthreads/comments/aga7wr/respect_superman_dc_rebirth/')
update_respectthread(cur, 1761, 'Respect Superman (New 52)', 'https://www.reddit.com/r/respectthreads/comments/bq7jfu/respect_superman_new_52/')
update_respectthread(cur, 1756, 'Respect Superman (Post-Crisis)', 'https://www.reddit.com/r/respectthreads/comments/ljsibk/respect_superman_postcrisis/')
update_respectthread(cur, 5905, 'Respect Percy Jackson (Percy Jackson & the Olympians) Updated Version', 'https://www.reddit.com/r/respectthreads/comments/1kwtha1/respect_percy_jackson_percy_jackson_the_olympians/')
update_respectthread(cur, 24979, 'Respect Fang Runin (The Poppy War Trilogy)', 'https://www.reddit.com/r/respectthreads/comments/1d48r79/respect_fang_runin_the_poppy_war_trilogy/')
update_respectthread(cur, 792, 'Respect Bill Cipher (Gravity Falls)', 'https://www.reddit.com/r/respectthreads/comments/4qr9b8/respect_bill_cipher_gravity_falls/')
update_respectthread(cur, 5258, 'Respect the Metroids (Metroid)', 'https://www.reddit.com/r/respectthreads/comments/mvr1z4/respect_the_metroids_metroid/')
update_respectthread(cur, 5256, 'Respect Samus Aran (Metroid)', 'https://www.reddit.com/r/respectthreads/comments/n2g4us/respect_samus_aran_metroid/')
update_respectthread(cur, 25014, 'Batman Mega Respect Thread Hub', 'https://www.reddit.com/r/BatmanMegaRT/comments/859osl/batman_mega_respect_thread_hub/')
update_respectthread(cur, 1493, 'Respect Batman (DC, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1348ale/respect_batman_dc_postflashpoint/')
update_respectthread(cur, 1494, 'Respect Batman (Bruce Wayne) (DC - Post Crisis)', 'https://www.reddit.com/r/respectthreads/comments/85eb91/respect_batman_bruce_wayne_dc_post_crisis/')
update_respectthread(cur, 1077, 'Respect Marinette Dupain-Cheng, the Miraculous Ladybug! (Miraculous: Tales of Ladybug & Cat Noir)', 'https://www.reddit.com/r/respectthreads/comments/rt49u2/respect_marinette_dupaincheng_the_miraculous/')
update_respectthread(cur, 2223, 'Respect Frank Castle, the Punisher! (Marvel: Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/5hsrop/respect_frank_castle_the_punisher_marvel_earth616/')
update_respectthread(cur, 5094, 'Respect Kratos (God of War)', 'https://www.reddit.com/r/respectthreads/comments/1d7ifkc/respect_kratos_god_of_war/')
update_respectthread(cur, 26078, 'Respect Kratos, the Ghost of Sparta! (God of War [Greek Era])', 'https://www.reddit.com/r/respectthreads/comments/1ksq4up/respect_kratos_the_ghost_of_sparta_god_of_war/')
update_respectthread(cur, 263, 'Respect Thanos (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/k7uesx/respect_thanos_marvel_cinematic_universe/')
update_respectthread(cur, 264, 'Respect Thor Odinson (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/xguqef/respect_thor_odinson_marvel_cinematic_universe/')
update_respectthread(cur, 5093, 'Respect The Gods of Olympus (God of War series)', 'https://www.reddit.com/r/respectthreads/comments/4bzopl/respect_the_gods_of_olympus_god_of_war_series/')
update_respectthread(cur, 5483, 'Respect The Team Fortress Mercenaries (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/82yd3z/respect_the_team_fortress_mercenaries_team/')


########################################

id = get_rt_id(cur, 'Respect Jonesy! (Fortnite Battle Royale)', 'https://www.reddit.com/r/respectthreads/comments/1m0zit1/respect_jonesy_fortnite_battle_royale/')
add_data(['Jonesy'],
'Jonesy',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m0zit1/respect_jonesy_fortnite_battle_royale/

########################################

id = get_rt_id(cur, 'Respect Deathstroke (DC Comics Earth 3)', 'https://www.reddit.com/r/respectthreads/comments/1m1llur/respect_deathstroke_dc_comics_earth_3/')
add_data(['Death(-| )?stroke'],
'Deathstroke',
False,
False,
[
    ['Death(-| )?stroke.*Earth 3']
],
'Earth 3',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m1llur/respect_deathstroke_dc_comics_earth_3/

########################################

id = get_rt_id(cur, 'Respect: Cassandra Cain: Batgirl & Shazam! (DCeased, DC Comics)', 'https://www.reddit.com/r/respectthreads/comments/1m1q9rm/respect_cassandra_cain_batgirl_shazam_dceased_dc/')
add_data(['Cassandra Cain'],
'Cassandra Cain',
False,
False,
[
    ['DCeased']
],
'DCeased',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Knifehead (Pacific Rim)', 'https://www.reddit.com/r/respectthreads/comments/1m1pt5n/respect_knifehead_pacific_rim/')
add_data(['Knifehead'],
'Knifehead',
False,
False,
[
    ['Pacific Rim']
],
'Pacific Rim',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m1pt5n/respect_knifehead_pacific_rim/

########################################

id = get_rt_id(cur, 'Respect the Yeti (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1m1x4pl/respect_the_yeti_team_fortress_2/')
add_data(['Yeti'],
'Yeti',
False,
False,
[
    ['TF2'], ['Team Fortress']
],
'TF2',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Predators (Marvels Predator VS Spider-Man)', 'https://www.reddit.com/r/respectthreads/comments/1m1xv2k/respect_the_predators_marvels_predator_vs/')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Predator Vs\.? Spider-Man']
],
'Predator Vs. Spider-Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

add_data(['Shere?( |-)Khan'],
'Shere Khan',
False,
False,
[
    ['Talespin']
],
'Talespin',
'{}'
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

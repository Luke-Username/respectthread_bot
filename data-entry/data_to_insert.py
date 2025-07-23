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

update_respectthread(cur, 13282, 'Respect Kid Goku (Dragon Ball Manga)', 'https://www.reddit.com/r/respectthreads/comments/inf0pf/respect_kid_goku_dragon_ball_manga/')
update_respectthread(cur, 9352, 'Respect Krillin (Dragon Ball)', 'https://www.reddit.com/r/respectthreads/comments/g2sz8l/respect_krillin_dragon_ball/')
update_respectthread(cur, 17671, 'Respect Mark Grayson, Invincible! (Invincible)', 'https://www.reddit.com/r/respectthreads/comments/pdkigv/respect_mark_grayson_invincible_invincible/')
update_respectthread(cur, 14434, 'Respect Shere Khan (The Jungle Book - 1967)', 'https://www.reddit.com/r/respectthreads/comments/k5tiwb/respect_shere_khan_the_jungle_book_1967/')
update_respectthread(cur, 16826, 'Respect The Spartans (300) [Movie]', 'https://www.reddit.com/r/respectthreads/comments/nje8s4/respect_the_spartans_300_movie/')
update_respectthread(cur, 25816, 'Respect Te Fiti, the Goddess of Life (Moana)', 'https://www.reddit.com/r/respectthreads/comments/1izdfvy/respect_te_fiti_the_goddess_of_life_moana/')
update_respectthread(cur, 230, 'Respect Emil Blonsky, the Abomination (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/1m3mf6f/respect_emil_blonsky_the_abomination_marvel/')
update_respectthread(cur, 1342, 'Respect Pyrrha Nikos (RWBY)', 'https://www.reddit.com/r/respectthreads/comments/1m455tk/respect_pyrrha_nikos_rwby/')


########################################

add_data(['Te Ka'],
'Te Ka',
False,
False,
[
    ['Moana']
],
'Moana',
'{25816}'
)
#https://www.reddit.com/r/respectthreads/comments/d2kwip/respect_sully_monsters_inc/

########################################

id = get_rt_id(cur, 'Respect Ultraman (Marvel Comics)', 'https://www.reddit.com/r/respectthreads/comments/1m2r6mm/respect_ultraman_marvel_comics/')
add_data(['Ultraman'],
'Ultraman',
False,
False,
[
    ['Ultraman ?\(Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ultraman Nexus (Ultraman Nexus)', 'https://www.reddit.com/r/respectthreads/comments/1m2xa8v/respect_ultraman_nexus_ultraman_nexus/')
add_data(['Ultraman Nexus'],
'Ultraman Nexus',
False,
True,
[
    ['Ultraman Nexus ?\(Ultraman Nexus']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Spartacus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1m3gjt9/respect_spartacus_dinosaur_king/')
add_data(['Spartacus'],
'Spartacus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Vlad Von Carstein! (Warhammer Fantasy, The Old World)', 'https://www.reddit.com/r/respectthreads/comments/1m42aur/respect_vlad_von_carstein_warhammer_fantasy_the/')
add_data(['Vlad Von Carstein'],
'Vlad Von Carstein',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m42aur/respect_vlad_von_carstein_warhammer_fantasy_the/

########################################

id = get_rt_id(cur, 'Respect Kai (The Legend of Korra)', 'https://www.reddit.com/r/respectthreads/comments/1m46isk/respect_kai_the_legend_of_korra/')
add_data(['Kai'],
'Kai',
False,
False,
[
    ['Kai ?\((The )?Legend of Korra']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Demiurge Mottom, Blood Flower Imperiatrix of the Gates of Fire! (Kill Six Billion Demons)', 'https://www.reddit.com/r/respectthreads/comments/1m53sw6/respect_demiurge_mottom_blood_flower_imperiatrix/')
add_data(['Mottom'],
'Mottom',
False,
False,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Demiurge Gog-Agog, Queen of Worms! (Kill Six Billion Demons)', 'https://www.reddit.com/r/respectthreads/comments/1m5m8b3/respect_demiurge_gogagog_queen_of_worms_kill_six/')
add_data(['Gog(-| )Agog'],
'Gog-Agog',
False,
False,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect 82 White Chain! (Kill Six Billion Demons)', 'https://www.reddit.com/r/respectthreads/comments/1m5bd12/respect_82_white_chain_kill_six_billion_demons/')
add_data(['82 White Chain'],
'82 White Chain',
False,
True,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#

add_data(['White Chain'],
'White Chain',
False,
False,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Natsume Tsutsumi/Kuwagata Ohger (No.1 Sentai Gozyuger)', 'https://www.reddit.com/r/respectthreads/comments/1m58dwt/natsume_tsutsumikuwagata_ohger_no1_sentai_gozyuger/')
add_data(['Kuwagata Ohger'],
'Kuwagata Ohger',
False,
False,
[
    ['Sentai Gozyuger']
],
'No.1 Sentai Gozyuger',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Natsume Tsutsumi'],
'Natsume Tsutsumi',
False,
False,
[
    ['Sentai Gozyuger']
],
'No.1 Sentai Gozyuger',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tuco Salamanca (Breaking Bad and Better Call Saul)', 'https://www.reddit.com/r/respectthreads/comments/1m68ipi/respect_tuco_salamanca_breaking_bad_and_better/')
add_data(['Tuco Salamanca'],
'Tuco Salamanca',
False,
True,
[
    ['Breaking Bad']
],
'Breaking Bad',
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

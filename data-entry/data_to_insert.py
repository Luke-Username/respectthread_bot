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

id = get_rt_id(cur, 'Respect The Predators (AVP Ultimate Prey)', 'https://redd.it/1biyma7')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Ultimate Prey']
],
'Aliens vs. Predators: Ultimate Prey',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1biyma7/respect_the_predators_avp_ultimate_prey/

########################################

id = get_rt_id(cur, 'Respect the Predator (Marvel Comics Vs. Predator Variant Covers)', 'https://redd.it/1bkh47u')
add_data(['Predator'],
'Predator',
False,
False,
[
    ['Marvel', 'Variant Covers']
],
'Marvel Variant Covers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkh47u/respect_the_predator_marvel_comics_vs_predator/

########################################

id = get_rt_id(cur, 'Respect the Gollywomp (Predator: Strange Roux) [Dark Horse Comics]', 'https://redd.it/1bkidoi')
add_data(['Gollywomp'],
'Gollywomp',
False,
False,
[
    ['Predator']
],
'Predator: Strange Roux',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkidoi/respect_the_gollywomp_predator_strange_roux_dark/

########################################

id = get_rt_id(cur, 'Respect Gagagigo (Yu-Gi-Oh! Trading Card Game)', 'https://redd.it/1bj2ovr')
add_data(['Gagagigo'],
'Gagagigo',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bj2ovr/respect_gagagigo_yugioh_trading_card_game/

########################################

id = get_rt_id(cur, 'Respect God (Yu-Gi-Oh! Trading Card Game)', 'https://redd.it/1bkgmtz')
add_data(['God'],
'God',
False,
False,
[
    ['God ?\(Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Menat (Street Fighter)', 'https://redd.it/1bjo2su')
add_data(['Menat'],
'Menat',
False,
False,
[
    ['Street Fighter']
],
'Street Fighter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bjo2su/respect_menat_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Soujiki Grumer!(Bakuage Sentai BoonBoomger)', 'https://redd.it/1bk5oy8')
add_data(['Soujiki Grumer'],
'Soujiki Grumer',
False,
True,
[
    ['Bakuage Sentai BoonBoomger']
],
'Bakuage Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bk5oy8/respect_soujiki_grumerbakuage_sentai_boonboomger/

########################################

id = get_rt_id(cur, 'Respect Spawner (Ward)', 'https://redd.it/1bkgv3b')
add_data(['Spawner'],
'Spawner',
False,
False,
[
    ['Ward']
],
'Ward',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkgv3b/respect_spawner_ward/

########################################

id = get_rt_id(cur, 'Respect Brute Giant Panda (Killing Bites)', 'https://redd.it/1bkhoq6')
add_data(['Brute Giant Panda'],
'Brute Giant Panda',
False,
False,
[
    ['Killing Bites']
],
'Killing Bites',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkhoq6/respect_brute_giant_panda_killing_bites/

########################################

id = get_rt_id(cur, 'Respect Gudrun and her Kong (Kong of Skull Island) [BOOM! Studios]', 'https://redd.it/1bkk5zu')
add_data(['Gudrun'],
'Gudrun',
False,
False,
[
    ['Kong of Skull Island']
],
'Kong of Skull Island',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkk5zu/respect_gudrun_and_her_kong_kong_of_skull_island/

########################################

id = get_rt_id(cur, 'Respect Big Baby (DC, Earth 8)', 'https://redd.it/1bkkw9t')
add_data(['Big Baby'],
'Big Baby',
False,
False,
[
    ['DC', 'Earth 8']
],
'Earth 8',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bkkw9t/respect_big_baby_dc_earth_8/

########################################

id = get_rt_id(cur, 'Respect Mister Sinister! (DC Comics)', 'https://redd.it/1bn5vc1')
add_data(['(Mister|Mr\.?) Sinister'],
'Mister Sinister',
False,
False,
[
    ['Mister Sinister ?\(DC( Comics)?\)']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bn5vc1/respect_mister_sinister_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Charles Deckard (Legendary)', 'https://redd.it/1blq5xt')
add_data(['Charles Deckard'],
'Charles Deckard',
False,
True,
[
    ['Legendary']
],
'Legendary',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1blq5xt/respect_charles_deckard_legendary/

########################################

id = get_rt_id(cur, "Respect ''Thonius Slyte'' (Warhammer 40k)", 'https://redd.it/1bl8ifk')
add_data(['Thonius Slyte'],
'Thonius Slyte',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bl8ifk/respect_thonius_slyte_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Cidolfus Orlandeau "Thunder God Cid" (Final Fantasy Tactics)', 'https://redd.it/1blujc6')
add_data(['Cidolfus Orlandeau'],
'Cidolfus Orlandeau',
False,
True,
[
    ['Final Fantasy']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1blujc6/respect_cidolfus_orlandeau_thunder_god_cid_final/

add_data(['Thunder God Cid'],
'Thunder God Cid',
False,
True,
[
    ['Final Fantasy']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1blujc6/respect_cidolfus_orlandeau_thunder_god_cid_final/

########################################

id = get_rt_id(cur, 'Respect Great Mazinger (Great Mazinger) [Anime]', 'https://redd.it/1bluqi1')
add_data(['Great Mazinger'],
'Great Mazinger',
False,
True,
[
    ['Great Mazinger ?\(Great Mazinger\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bluqi1/respect_great_mazinger_great_mazinger_anime/

########################################

id = get_rt_id(cur, 'Respect Grendizer (UFO Robot Grendizer) [Anime]', 'https://redd.it/1bmp74d')
add_data(['Grendizer'],
'Grendizer',
False,
True,
[
    ['UFO Robot Grendizer']
],
'UFO Robot Grendizer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bmp74d/respect_grendizer_ufo_robot_grendizer_anime/


########################################

id = get_rt_id(cur, 'Respect Gojirasaurus quayi (Prehistoric Tournament Battle)', 'https://redd.it/1bmvuxp')
add_data(['Gojirasaurus quayi'],
'Gojirasaurus quayi',
False,
False,
[
    ['Prehistoric Tournament Battle']
],
'Prehistoric Tournament Battle',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bmvuxp/respect_gojirasaurus_quayi_prehistoric_tournament/


########################################

id = get_rt_id(cur, 'Respect Thanos simonattoi (Prehistoric Tournament Battle)', 'https://redd.it/1bmvv1b')
add_data(['Thanos simonattoi'],
'Thanos simonattoi',
False,
False,
[
    ['Prehistoric Tournament Battle']
],
'Prehistoric Tournament Battle',
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

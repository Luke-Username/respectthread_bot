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

add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['Supermans?.*Regime', 'games?']
],
'Injustice',
'{7575}'
)
#https://www.reddit.com/r/whowouldwin/comments/y1r3sn/omniman_comics_vs_supermans_regime/iryyudj/?context=3

add_data(['Shazam'],
'Shazam',
False,
False,
[
    ['Supermans?.*Regime', 'games?']
],
'Injustice',
'{7574}'
)
#https://www.reddit.com/r/whowouldwin/comments/y1sco1/whos_the_weakest_character_who_could_make_it/irz7s1c/?context=3

add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Supermans?.*Regime', 'games?']
],
'Injustice',
'{7685}'
)
#https://www.reddit.com/r/whowouldwin/comments/y1sco1/whos_the_weakest_character_who_could_make_it/irz7s1c/?context=3

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Toaru', 'Almighty Thor']
],
'Toaru Majutsu no Index',
'{15253}'
)
#

########################################

id = get_rt_id(cur, 'Respect Captain Marvel (DC Post-Crisis)', 'https://redd.it/3iwq7x')
add_data(['Shazam'],
'Shazam',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{1653, ' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/3iwq7x/respect_captain_marvel_dc_postcrisis/

########################################

add_data(['Madoka'],
'Madoka',
False,
False,
[
    ['Goddess Madoka']
],
'Madoka Magica',
'{4428}'
)
#

########################################

add_data(['Rorsc?har?ch'],
'Rorschach',
False,
False,
[
    ['C(o|ó)mics']
],
'Watchmen',
'{1838}'
)
#https://www.reddit.com/r/whowouldwin/comments/y28ym3/next_batman/

########################################

id = get_rt_id(cur, 'Respect the Columbian Mammoth (Primeval)', 'https://redd.it/y1rhrm')
add_data(['Columbian Mammoth'],
'Columbian Mammoth',
False,
False,
[
    ['Primeval']
],
'Primeval',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y1rhrm/respect_the_columbian_mammoth_primeval/

########################################

id = get_rt_id(cur, 'Respect the Camouflage Beast (Primeval)', 'https://redd.it/y2dnio')
add_data(['Camouflage Beast'],
'Camouflage Beast',
False,
True,
[
    ['Primeval']
],
'Primeval',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y2dnio/respect_the_camouflage_beast_primeval/

########################################

id = get_rt_id(cur, 'Respect The Future Predators (Primeval)', 'https://redd.it/y2ms20')
add_data(['Future Predators?'],
'Future Predators',
False,
True,
[
    ['Primeval']
],
'Primeval',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y2ms20/respect_the_future_predators_primeval/

########################################

id = get_rt_id(cur, 'Respect the Tree Creepers (Primeval)', 'https://redd.it/y31h1z')
add_data(['Tree Creepers?'],
'Tree Creepers',
False,
False,
[
    ['Primeval']
],
'Primeval',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y31h1z/respect_the_tree_creepers_primeval/

########################################

id = get_rt_id(cur, 'Respect Nathan Graves (Castlevania: Circle of the Moon)', 'https://redd.it/y22kyz')
add_data(['Nathan Graves'],
'Nathan Graves',
False,
True,
[
    ['Castle(-| )?vania']
],
'Castlevania',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y22kyz/respect_nathan_graves_castlevania_circle_of_the/

########################################

id = get_rt_id(cur, 'Respect Rampage (Transformers: Beast Wars)', 'https://redd.it/y2kch2')
add_data(['Rampage'],
'Rampage',
False,
False,
[
    ['Transformers', 'Beast Wars']
],
'Transformers: Beast Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y2kch2/respect_rampage_transformers_beast_wars/

########################################

id = get_rt_id(cur, 'Respect Funta (Powerpuff Girls Z)', 'https://redd.it/y2oych')
add_data(['Funta'],
'Funta',
False,
False,
[
    ['Power ?puff Girls Z']
],
'Powerpuff Girls Z',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y2oych/respect_funta_powerpuff_girls_z/

########################################

id = get_rt_id(cur, 'Respect Kyo Sohma! (Fruits Basket, 2019 Anime)', 'https://redd.it/y2vzjp')
add_data(['Kyo Sohma'],
'Kyo Sohma',
False,
True,
[
    ['Fruits Basket']
],
'Fruits Basket',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gabriel May (Malignant)', 'https://redd.it/y2zh9q')
add_data(['Gabriel'],
'Gabriel',
False,
False,
[
    ['Malignant']
],
'Malignant',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y2zh9q/respect_gabriel_may_malignant/

########################################

id = get_rt_id(cur, 'Respect SCP-7987, "The Irate Gamer" (SCP Foundation)', 'https://redd.it/y3daef')
add_data(['SCP ?(-| )? ?7987'],
'SCP-7987',
False,
True,
[
    ['Irate Gamer']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y3daef/respect_scp7987_the_irate_gamer_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect SCP-5175, DEATH KNIFE (SCP Foundation)', 'https://redd.it/y49fsp')
add_data(['SCP ?(-| )? ?5175'],
'SCP-5175',
False,
True,
[
    ['DEATH KNIFE']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y49fsp/respect_scp5175_death_knife_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Darkyloseid (DC Comics)', 'https://redd.it/y3hyp6')
add_data(['Darkyloseid'],
'Darkyloseid',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y3hyp6/respect_darkyloseid_dc_comics/

########################################

id = get_rt_id(cur, 'Respect The Jurassic League (DC Comics)', 'https://redd.it/y3hzsm')
add_data(['Jurassic League'],
'Jurassic League',
True,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y3hzsm/respect_the_jurassic_league_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Douglas Bullet (One Piece)', 'https://redd.it/y2wlyw')
add_data(['Douglas Bullet'],
'Douglas Bullet',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Robot Rudy (ChalkZone)', 'https://redd.it/y40bse')
add_data(['Robot Rudy'],
'Robot Rudy',
False,
False,
[
    ['Chalk ?Zone']
],
'ChalkZone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Moleculo, The Molecular Man (Saturday Night Live)', 'https://redd.it/y4449a')
add_data(['Moleculo'],
'Moleculo',
False,
False,
[
    ['Molecular Man'], ['Saturday Night Live'], ['SNL']
],
'Saturday Night Live',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/y4449a/respect_moleculo_the_molecular_man_saturday_night/

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

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

update_respectthread(cur, 2053, 'Respect Wilson Fisk, the Kingpin (Marvel Comics, Earth 616)', 'https://redd.it/1bbmc1h')

########################################

add_data(['Fire Lord'],
'Fire Lord',
False,
False,
[
    ['Herald'], ['Galactus']
],
'616',
'{2082}'
)
#https://www.reddit.com/r/whowouldwin/comments/1b95syh/natsu_dragneel_vs_14_fire_users/kttnvqz/?context=3

########################################

add_data(['Loki'],
'Loki',
False,
False,
[
    ['Warframe']
],
'Warframe',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1baxht0/what_is_the_weakest_warframe_that_can_still_beat/ku749lz/?context=3

add_data(['Lavos'],
'Lavos',
False,
False,
[
    ['Warframe']
],
'Warframe',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1baxht0/what_is_the_weakest_warframe_that_can_still_beat/ku749lz/?context=3

########################################

id = get_rt_id(cur, 'Respect Queen Anna of Arendelle (Frozen)', 'https://redd.it/1b667wx')
add_data(['Anna'],
'Anna',
False,
False,
[
    ['\(Frozen\)']
],
'Frozen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1b9o5iy/anna_frozen_vs_moana_moana/ktwx87u/?context=3

########################################

add_data(['The Juggernaut'],
'The Juggernaut',
False,
False,
[
    ['republic juggernaut']
],
'Republic',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1bc2fb0/an_atat_vs_a_republic_juggernaut/kuczesf/?context=3

########################################

add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Incredible Hulk', '2008']
],
'MCU',
'{236}'
)
#https://www.reddit.com/r/whowouldwin/comments/1bc54od/saxton_hale_vs_basic_hulk_incredible_hulk_2008/kudi45v/?context=3

########################################

id = get_rt_id(cur, 'Respect Solomon Grundy! (DC Comics, Post-Crisis)', 'https://redd.it/1b92m7s')
add_data(['Solomon Grundy'],
'Solomon Grundy',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1b92m7s/respect_solomon_grundy_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Shinegreymon ! (digimon Savers)', 'https://redd.it/1b93021')
add_data(['ShineGreymon'],
'ShineGreymon',
False,
False,
[
    ['Digimon']
],
'Digimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1b93021/respect_shinegreymon_digimon_savers/


########################################

id = get_rt_id(cur, 'Respect The Predators (AVP Rift War)', 'https://redd.it/1b9do6z')
add_data(['Predator'],
'Predator',
False,
False,
[
    ['Rift War']
],
'Aliens vs. Predators: Rift War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1b9do6z/respect_the_predators_avp_rift_war/

add_data(['Predators'],
'Predators',
False,
False,
[
    ['Rift War']
],
'Aliens vs. Predators: Rift War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1b9do6z/respect_the_predators_avp_rift_war/

########################################

id = get_rt_id(cur, 'Respect Karr Nuq Sin! (Star Wars Canon)', 'https://redd.it/1b9g4iq')
add_data(['Karr Nuq Sin'],
'Karr Nuq Sin',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1b9g4iq/respect_karr_nuq_sin_star_wars_canon/

########################################

########################################

id = get_rt_id(cur, 'Respect Bumblebee (Transformers Movie Reboot Universe)', 'https://redd.it/1baya6s')
add_data(['Bumblebee'],
'Bumblebee',
False,
False,
[
    ['Rise of the Beasts']
],
'Rise of the Beasts',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1baya6s/respect_bumblebee_transformers_movie_reboot/

########################################

id = get_rt_id(cur, 'Respect Rodin, the Infinite One (Bayonetta)', 'https://redd.it/1bb9bfl')
add_data(['Rodin'],
'Rodin',
False,
False,
[
    ['Bayonetta']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bb9bfl/respect_rodin_the_infinite_one_bayonetta/

########################################

id = get_rt_id(cur, 'Respect Failsafe! (DC Comics)', 'https://redd.it/1bbbxnt')
add_data(['Failsafe'],
'Failsafe',
False,
False,
[
    ['Failsafe ?\(DC\)'], ['Failsafe vs', 'Batman']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bbbxnt/respect_failsafe_dc_comics/

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

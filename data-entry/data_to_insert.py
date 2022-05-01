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

add_data(['Eggman'],
'Eggman',
False,
False,
[
    ['Jim Carreys?']
],
'Sonic the Hedgehog (2020 Film)',
'{8608}'
)
#https://www.reddit.com/r/whowouldwin/comments/ufj1td/jim_carreys_eggman_vs_jim_carreys_riddler_in_chess/

add_data(['Robotnik'],
'Robotnik',
False,
False,
[
    ['Jim Carreys?']
],
'Sonic the Hedgehog (2020 Film)',
'{8608}'
)
#https://www.reddit.com/r/whowouldwin/comments/ufj1td/jim_carreys_eggman_vs_jim_carreys_riddler_in_chess/

add_data(['Riddler'],
'Riddler',
False,
False,
[
    ['Jim Carreys?']
],
'Batman Forever',
'{16039}'
)
#https://www.reddit.com/r/whowouldwin/comments/ufj1td/jim_carreys_eggman_vs_jim_carreys_riddler_in_chess/

########################################

add_data(['Loki'],
'Loki',
False,
False,
[
    ['The Mask']
],
'The Mask',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/ufttnj/kars_vs_loki_jojos_bizarre_adventure_vs_the_mask/i6vomcb/?context=3

########################################

add_data(['Megatron'],
'Megatron',
False,
False,
[
    ['Revenge of the Fallen']
],
'Transformers Films',
'{338}'
)
#https://www.reddit.com/r/whowouldwin/comments/uf93mm/megatron_vs_bumblebee/i6s1ha4/?context=3

add_data(['Bumblebee'],
'Bumblebee',
False,
False,
[
    ['Revenge of the Fallen']
],
'Transformers Films',
'{16016}'
)
#https://www.reddit.com/r/whowouldwin/comments/uf93mm/megatron_vs_bumblebee/i6s1ha4/?context=3

########################################

id = get_rt_id(cur, 'Respect Princess Daisy! (Mario & Sonic at the Olympic Games)', 'https://redd.it/uf921n')
add_data(['Princess Daisy'],
'Princess Daisy',
False,
False,
[
    ['Olympic Games']
],
'Mario & Sonic at the Olympic Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uf921n/respect_princess_daisy_mario_sonic_at_the_olympic/

########################################

id = get_rt_id(cur, 'RESPECT Deathstroke (DCYou)', 'https://redd.it/agpiz2')
add_data(['Death(-| )?stroke'],
'Deathstroke',
False,
False,
[
    ['Post(-| )?Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '1577, {}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/ufv8dp/deathstroke_dc_vs_akame_akame_ga_kill/i6vw7pk/?context=3

########################################

id = get_rt_id(cur, 'Respect Avicebron, the Golem Master (Fate)', 'https://redd.it/ufib3p')
add_data(['Avicebron'],
'Avicebron',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ufib3p/respect_avicebron_the_golem_master_fate/

########################################

id = get_rt_id(cur, 'Respect Karolina Dean (Runaways/Marvel Cinematic Universe)', 'https://redd.it/ufmuuo')
add_data(['Karolina Dean'],
'Karolina Dean',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU'],
    ['Runaways']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ufmuuo/respect_karolina_dean_runawaysmarvel_cinematic/

########################################

id = get_rt_id(cur, 'Respect Myaxx (Ben 10 Classic)', 'https://redd.it/ufr0ql')
add_data(['Myaxx'],
'Myaxx',
False,
True,
[
    ['Ben (10|Ten(nyson)?)'], ['(Omn|Ulti)itrix']
],
'Ben 10',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ufr0ql/respect_myaxx_ben_10_classic/

########################################

id = get_rt_id(cur, 'Respect Saxton Hale (Character Scramble) (Season 15)', 'https://redd.it/ufvt2q')
add_data(['Saxton Hale'],
'Saxton Hale',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ufvt2q/respect_saxton_hale_character_scramble_season_15/

########################################

id = get_rt_id(cur, 'Respect Bugsnax (Bugsnax)', 'https://redd.it/ufwhrn')
add_data(['Bugsnax'],
'Bugsnax',
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ufwhrn/respect_bugsnax_bugsnax/

########################################

id = get_rt_id(cur, 'Respect The Numan Athletes (Numan Athlethics)', 'https://redd.it/ug1k5f')
add_data(['Numan Athletes'],
'Numan Athletes',
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ug1k5f/respect_the_numan_athletes_numan_athlethics/

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

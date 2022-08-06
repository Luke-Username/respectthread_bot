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

add_data(['Ghost ?Rider'],
'Ghost Rider',
False,
False,
[
    ['Ghost ?Rider ?\(Movies\)']
],
'Movies',
'{}'
)

########################################

add_data(['The Flash'],
'The Flash',
False,
False,
[
    ['can The Flash']
],
'DC',
'{1582,1583,1590,1589}'
)
#https://www.reddit.com/r/whowouldwin/comments/wg73vp/can_the_flash_speedrun_super_mario_odyssey/iixxvz9/?context=3

########################################

id = get_rt_id(cur, 'Respect Irene Rapona (Gorgeous Irene)', 'https://redd.it/wdv49b')
add_data(['Irene'],
'Irene',
False,
False,
[
    ['Gorgeous Irene'], ['Irene Rapona']
],
'Gorgeous Irene',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wdv49b/respect_irene_rapona_gorgeous_irene/

########################################

id = get_rt_id(cur, 'Respect Jinyu! (FLCL: Progressive)', 'https://redd.it/wdw7lq')
add_data(['Jinyu'],
'Jinyu',
False,
False,
[
    ['FLCL'], ['Fooly Cooly']
],
'FLCL',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect King the Wildfire (One Piece)', 'https://redd.it/wdzzji')
add_data(['King'],
'King',
False,
False,
[
    ['King ?\(One ?Piece?'], ['King the Wildfire']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wdzzji/respect_king_the_wildfire_one_piece/

########################################

id = get_rt_id(cur, 'Respect Captain Grime! (Amphibia)', 'https://redd.it/we26cu')
add_data(['Captain Grime'],
'Captain Grime',
False,
True,
[
    ['Amphibia']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/we26cu/respect_captain_grime_amphibia/

########################################

id = get_rt_id(cur, 'Respect the Blight! (Dead by Daylight)', 'https://redd.it/we720j')
add_data(['Talbot Grimes'],
'Talbot Grimes',
False,
True,
[
    ['Dead by Daylight'], ['DBD']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/we720j/respect_the_blight_dead_by_daylight/

add_data(['The Blight'],
'The Blight',
False,
False,
[
    ['Dead by Daylight'], ['DBD']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/we720j/respect_the_blight_dead_by_daylight/

########################################

id = get_rt_id(cur, 'Respect the Deathslinger! (Dead by Daylight)', 'https://redd.it/wgd57y')
add_data(['Deathslinger'],
'Deathslinger',
False,
True,
[
    ['Dead by Daylight'], ['DBD']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wgd57y/respect_the_deathslinger_dead_by_daylight/

########################################

id = get_rt_id(cur, 'Respect the Anti-Life Equation Infection! (DCeased)', 'https://redd.it/weeeex')
add_data(['Anti(-| )?Life Equation'],
'Anti-Life Equation',
False,
False,
[
    ['DCeased'], ['Anti(-| )?Life Equation Infection'], ['Zombies']
],
'DCeased',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/weeeex/respect_the_antilife_equation_infection_dceased/

########################################

id = get_rt_id(cur, 'Respect Lady Spellbinder (DC, Post Crisis)', 'https://redd.it/weerqb')
add_data(['Lady Spellbinder'],
'Lady Spellbinder',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/weerqb/respect_lady_spellbinder_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect Wild Dog! (Time Crisis)', 'https://redd.it/weq4c7')
add_data(['Wild Dog'],
'Wild Dog',
False,
False,
[
    ['Time Crisis']
],
'Time Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/weq4c7/respect_wild_dog_time_crisis/

########################################

id = get_rt_id(cur, 'Respect Lauper (Gorgeous Irene)', 'https://redd.it/wevcu8')
add_data(['Lauper'],
'Lauper',
False,
False,
[
    ['Gorgeous Irene']
],
'Gorgeous Irene',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wevcu8/respect_lauper_gorgeous_irene/

########################################

id = get_rt_id(cur, 'Respect This Unnamed Female Assassin (Gorgeous Irene)', 'https://redd.it/wevd8e')
add_data(['Female Assassin'],
'Female Assassin',
False,
False,
[
    ['Gorgeous Irene']
],
'Gorgeous Irene',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wevd8e/respect_this_unnamed_female_assassin_gorgeous/

########################################

id = get_rt_id(cur, 'Respect the Deadly Mantis (The Deadly Mantis)', 'https://redd.it/wexhf3')
add_data(['Deadly Mantis'],
'Deadly Mantis',
False,
True,
[
    ['1957']
],
'1957',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wexhf3/respect_the_deadly_mantis_the_deadly_mantis/

########################################

id = get_rt_id(cur, 'Respect Demonreach (The Dresden Files)', 'https://redd.it/wfh8d8')
add_data(['Demonreach'],
'Demonreach',
False,
True,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wfh8d8/respect_demonreach_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Doomsday! (Superman: Doomsday)', 'https://redd.it/wg3sbx')
add_data(['Doomsday'],
'Doomsday',
False,
False,
[
    ['Doomsday.*Superman ?: ?Doomsday']
],
'Superman: Doomsday',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wg3sbx/respect_doomsday_superman_doomsday/

########################################

id = get_rt_id(cur, 'Respect Superman! (Superman: Doomsday)', 'https://redd.it/wg79o7')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Super(-| )?man.*Superman ?: ?Doomsday']
],
'Superman: Doomsday',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wg79o7/respect_superman_superman_doomsday/

########################################

id = get_rt_id(cur, 'Respect Prophet Elisha (Holy Bible)', 'https://redd.it/wgg3ft')
add_data(['Elisha'],
'Elisha',
False,
False,
[
    ['Bible'], ['Prophe']
],
'Bible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wgg3ft/respect_prophet_elisha_holy_bible/

########################################

id = get_rt_id(cur, 'Respect Avatar Yangchen (Avatar: The Last Airbender)', 'https://redd.it/wgzuv7')
add_data(['Yangchen'],
'Yangchen',
False,
True,
[
    ['Avatar'], ['A?TLA'], ['Air(-| )bender']
],
'Avatar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wgzuv7/respect_avatar_yangchen_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'Respect Judge Dredd! (2000AD)', 'https://redd.it/wh8x07')
add_data(['Dredd'],
'Judge Dredd',
False,
False,
[
    ['2000 ?AD']
],
'2000 AD',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wh8x07/respect_judge_dredd_2000ad/

########################################

id = get_rt_id(cur, 'Respect The Collector (The Owl House)', 'https://redd.it/whnxaf')
add_data(['Collector'],
'Collector',
False,
False,
[
    ['Owl House']
],
'The Owl House',
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

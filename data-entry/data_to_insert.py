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

update_respectthread(cur, 20590, 'Respect the Death Angels (A Quiet Place)', 'https://www.reddit.com/r/respectthreads/comments/1oa0f6e/respect_the_death_angels_a_quiet_place/')
update_respectthread(cur, 4124, '[NSFW] Respect Panty and Stocking Anarchy (Panty & Stocking with Garterbelt)', 'https://www.reddit.com/r/respectthreads/comments/1oacnrc/nsfw_respect_panty_and_stocking_anarchy_panty/')
update_respectthread(cur, 4125, '[NSFW] Respect Scanty and Kneesocks Daemon (Panty & Stocking with Garterbelt)', 'https://www.reddit.com/r/respectthreads/comments/1oacovq/nsfw_respect_scanty_and_kneesocks_daemon_panty/')

########################################

id = get_rt_id(cur, '[NSFW] Respect Polyester and Polyurethane (Panty & Stocking with Garterbelt)', 'https://www.reddit.com/r/respectthreads/comments/1oacp3p/nsfw_respect_polyester_and_polyurethane_panty/')
add_data(['Polyester (and|&) Polyurethane'],
'Polyester and Polyurethane',
True,
False,
[
    ['Panty (&|and) Stocking']
],
'Panty & Stocking',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Yautja (DEATH BATTLE!)', 'https://www.reddit.com/r/respectthreads/comments/1o513l0/respect_the_yautja_death_battle/')
add_data(['Yautja'],
'Yautja',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect the Yautja (DEATH BATTLE!)', 'https://www.reddit.com/r/respectthreads/comments/1o513l0/respect_the_yautja_death_battle/')
add_data(['Yautja'],
'Yautja',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Lanier College Killer (Final Exam)', 'https://www.reddit.com/r/respectthreads/comments/1o5o440/respect_the_lanier_college_killer_final_exam/')
add_data(['Lanier College Killer'],
'Lanier College Killer',
False,
False,
[
    ['Final Exam']
],
'Final Exam',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dean Timothy Foley (Pieces)', 'https://www.reddit.com/r/respectthreads/comments/1o5oj9o/respect_dean_timothy_foley_pieces/')
add_data(['Dean Timothy Foley'],
'Dean Timothy Foley',
False,
False,
[
    ['Pieces']
],
'Pieces',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-7416 (SCP Foundation)', 'https://www.reddit.com/r/respectthreads/comments/1o68du5/respect_scp7416_scp_foundation/')
add_data(['SCP ?(-| )? ?7416'],
'SCP-7416',
False,
False,
[
    ['LAWBERT']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ghostface (Call of Duty)', 'https://www.reddit.com/r/respectthreads/comments/1o79k6s/respect_ghostface_call_of_duty/')
add_data(['Ghostface'],
'Ghostface',
False,
False,
[
    ['Call of Duty']
],
'Call of Duty',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Hulk (Hulk vs Thor)', 'https://www.reddit.com/r/respectthreads/comments/1o7jy79/respect_the_hulk_hulk_vs_thor/')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Hulk ?\(Hulk vs Thor\)']
],
'Hulk vs Thor',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Shadow (Amnesia)', 'https://www.reddit.com/r/respectthreads/comments/1o7lw8c/respect_the_shadow_amnesia/')
add_data(['Shadow'],
'Shadow',
False,
False,
[
    ['Amnesia', 'Dark Descent|Machine For Pigs|Rebirth']
],
'Amnesia',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Peacemaker! (DCU)', 'https://www.reddit.com/r/respectthreads/comments/1o7n5xm/respect_peacemaker_dcu/')
add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['DCU']
],
'DCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Please don''t respect Captain Triumph (DCU)", 'https://www.reddit.com/r/respectthreads/comments/1o84ert/please_dont_respect_captain_triumph_dcu/')
add_data(['Captain Triumph'],
'Captain Triumph',
False,
False,
[
    ['DCU']
],
'DCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Peacemaker! (Peacemaker Presents: The Vigilante/Eagly Double-Feature)', 'https://www.reddit.com/r/respectthreads/comments/1o7rm9n/respect_peacemaker_peacemaker_presents_the/')
add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['Peacemaker Presents', 'Vigilante', 'Double(-| )Feature']
],
'Peacemaker Presents: The Vigilante/Eagly Double Feature!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Hulk (Next Avengers: Heroes of Tomorrow)', 'https://www.reddit.com/r/respectthreads/comments/1o7nrgj/respect_the_hulk_next_avengers_heroes_of_tomorrow/')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Next Avengers', 'Heroes of Tomorrow']
],
'Next Avengers: Heroes of Tomorrow',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nova Prime (Transformers, IDW Comics [2005])', 'https://www.reddit.com/r/respectthreads/comments/1o7pa90/respect_nova_prime_transformers_idw_comics_2005/')
add_data(['Nova Prime'],
'Nova Prime',
False,
False,
[
    ['IDW']
],
'IDW',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Maxwell Carpenter! (World of Darkness)', 'https://www.reddit.com/r/respectthreads/comments/1o8k4c7/respect_maxwell_carpenter_world_of_darkness/')
add_data(['Maxwell Carpenter'],
'Maxwell Carpenter',
False,
False,
[
    ['World of Darkness']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zaybi (VERSUS)', 'https://www.reddit.com/r/respectthreads/comments/1oahb2j/respect_zaybi_versus/')
add_data(['Zaybi'],
'Zaybi',
False,
False,
[
    ['VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hallow (VERSUS)', 'https://www.reddit.com/r/respectthreads/comments/1oagzgg/respect_hallow_versus/')
add_data(['Hallow'],
'Hallow',
False,
False,
[
    ['Hallow ?\(VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Superman (At Earth''s End)", 'https://www.reddit.com/r/respectthreads/comments/1o916a6/respect_superman_at_earths_end/')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ["At Earth''s End"]
],
"At Earth''s End",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Weird Yellow Smiling Thing, WYST! (Pillar Chase 2)', 'https://www.reddit.com/r/respectthreads/comments/1oabh4i/respect_the_weird_yellow_smiling_thing_wyst/')
add_data(['Weird Yellow Smiling Thing'],
'Weird Yellow Smiling Thing',
False,
True,
[
    ['Pillar Chase']
],
'Pillar Chase',
'{' + '{}'.format(id) + '}'
)
#

add_data(['W\.?Y\.?S\.?T'],
'WYST',
False,
False,
[
    ['Pillar Chase']
],
'Pillar Chase',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Forsaken Survivors! (Forsaken, Roblox)', 'https://www.reddit.com/r/respectthreads/comments/1oad7f0/respect_the_forsaken_survivors_forsaken_roblox/')
add_data(['Forsaken Survivors'],
'Forsaken Survivors',
True,
False,
[
    ['Roblox'], ['\(Forsaken\)']
],
'Roblox',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1l6rhp8/1x1x1x1_1x1_forsaken_enters_the_mcu_what_is_the/

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

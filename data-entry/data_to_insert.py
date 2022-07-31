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

add_data(['Future Kevin Levin'],
'Future Kevin Levin',
False,
True,
[
    ['Ben (10|Ten(nyson)?)']
],
'Ben 10',
'{6547}'
)
#

########################################

id = get_rt_id(cur, 'Respect Asa Mitaka, the War Devil! (Chainsaw Man)', 'https://redd.it/wbhdw5')
add_data(['Asa Mitaka'],
'Asa Mitaka',
False,
True,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbhdw5/respect_asa_mitaka_the_war_devil_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Spock (Star Trek [Reboot Films])', 'https://redd.it/wbk4nx')
add_data(['Spock'],
'Spock',
False,
False,
[
    ['Reboot'], ['2009'], ['Into Darkness']
],
'Star Trek Reboot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbk4nx/respect_spock_star_trek_reboot_films/

########################################

id = get_rt_id(cur, 'Respect Nathaniel Richards, Rama-Tut (Marvel, 616)', 'https://redd.it/wbn2jn')
add_data(['Rama(-| )Tut'],
'Rama-Tut',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbn2jn/respect_nathaniel_richards_ramatut_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Malenia, Blade of Miquella (Elden Ring)', 'https://redd.it/wbnah2')
add_data(['Malenia'],
'Malenia',
False,
False,
[
    ['Elden Ring'], ['Miquella']
],
'Elden Ring',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbnah2/respect_malenia_blade_of_miquella_elden_ring/

########################################

id = get_rt_id(cur, "Respect Who''s-Who (One Piece)", 'https://redd.it/wbnbjj')
add_data(["Who''?s-Who"],
"Who''s-Who",
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbnbjj/respect_whoswho_one_piece/

########################################

id = get_rt_id(cur, 'Respect Deirdre Beaubeirdra! (Everything Everywhere All At Once)', 'https://redd.it/wbpq7o')
add_data(['Deirdre Beaubeirdra'],
'Deirdre Beaubeirdra',
False,
True,
[
    ['Everything Everywhere All At Once']
],
'Everything Everywhere All At Once',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbpq7o/respect_deirdre_beaubeirdra_everything_everywhere/

########################################

id = get_rt_id(cur, 'Respect Jobu Tupaki! (Everything Everywhere All At Once)', 'https://redd.it/wbptzy')
add_data(['Jobu Tupaki'],
'Jobu Tupaki',
False,
True,
[
    ['Everything Everywhere All At Once']
],
'Everything Everywhere All At Once',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbptzy/respect_jobu_tupaki_everything_everywhere_all_at/

########################################

id = get_rt_id(cur, 'Respect Waymond Wang! (Everything Everywhere All At Once)', 'https://redd.it/wc4gsz')
add_data(['Waymond Wang'],
'Waymond Wang',
False,
True,
[
    ['Everything Everywhere All At Once']
],
'Everything Everywhere All At Once',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wc4gsz/respect_waymond_wang_everything_everywhere_all_at/

########################################

id = get_rt_id(cur, 'Respect Evelyn Wang! (Everything Everywhere All At Once)', 'https://redd.it/wc4ogy')
add_data(['Evelyn Wang'],
'Evelyn Wang',
False,
False,
[
    ['Everything Everywhere All At Once']
],
'Everything Everywhere All At Once',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wc4ogy/respect_evelyn_wang_everything_everywhere_all_at/

########################################

id = get_rt_id(cur, 'Respect the Giant Crocodile (Resident Evil) [Netflix]', 'https://redd.it/wbq9n0')
add_data(['Crocodile'],
'Crocodile',
False,
False,
[
    ['Resident Evil', 'Netflix']
],
'Resident Evil Netflix',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bert Wesker (Resident Evil) [Netflix]', 'https://redd.it/wbr06a')
add_data(['Bert Wesker'],
'Bert Wesker',
False,
False,
[
    ['Resident Evil', 'Netflix']
],
'Resident Evil Netflix',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbr06a/respect_bert_wesker_resident_evil_netflix/

########################################

id = get_rt_id(cur, 'Respect Marcus Holloway (Watch_Dogs 2)', 'https://redd.it/wbyvtc')
add_data(['Marcus Holloway'],
'Marcus Holloway',
False,
True,
[
    ['Watch(_| )?Dogs_?2?']
],
'Watch_Dogs',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wbyvtc/respect_marcus_holloway_watch_dogs_2/

########################################

id = get_rt_id(cur, 'Respect Ryu (DEATH BATTLE!)', 'https://redd.it/wcdqd9')
add_data(['Ryu'],
'Ryu',
False,
False,
[
    ['DEATH BATTLE!']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wcdqd9/respect_ryu_death_battle/

########################################

id = get_rt_id(cur, 'Respect Fenghuang (Kung Fu Panda: Legends of Awesomeness)', 'https://redd.it/wc6ms2')
add_data(['Fenghuang'],
'Fenghuang',
False,
False,
[
    ['Kung(-| )?Fu Panda']
],
'Kung Fu Panda',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wc6ms2/respect_fenghuang_kung_fu_panda_legends_of/

########################################

id = get_rt_id(cur, 'Respect the Mummy Lobster (Two Best Friends Funtime Adventures)', 'https://redd.it/wcexa7')
add_data(['Mummy Lobster'],
'Mummy Lobster',
False,
False,
[
    ['Two Best Friends']
],
'Two Best Friends Funtime Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wcexa7/respect_the_mummy_lobster_two_best_friends/

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

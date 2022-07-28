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

update_respectthread(cur, 13268, 'Respect Emilia (Re:Zero, Anime)', 'https://redd.it/w8jdfv')
update_respectthread(cur, 13267, 'Respect Subaru Natsuki (Re:Zero, Anime)', 'https://redd.it/w9ecps')

########################################

add_data(['Creature from the Black Lagoon'],
'Creature from the Black Lagoon',
False,
True,
[
    ['Universal']
],
'',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/w9dkqg/dracula_vs_the_mummy_vs_frankensteins_monster_vs/ihueh65/?context=3

########################################

add_data(['Hiccup'],
'Hiccup',
False,
False,
[
    ['dragon', 'rider']
],
'How to Train Your Dragon',
'{6572}'
)
#https://www.reddit.com/r/whowouldwin/comments/w8ngrh/claude_von_riegan_vs_hiccup/ihq9wjp/?context=3

########################################

id = get_rt_id(cur, 'Respect Jasmine, DekaYellow (Tokusou Sentai Dekaranger)', 'https://redd.it/w8kuyk')
add_data(['DekaYellow'],
'DekaYellow',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w8kuyk/respect_jasmine_dekayellow_tokusou_sentai/

########################################

id = get_rt_id(cur, 'Respect Umeko, DekaPink (Tokusou Sentai Dekaranger)', 'https://redd.it/w8kvon')
add_data(['DekaPink'],
'DekaPink',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w8kvon/respect_umeko_dekapink_tokusou_sentai_dekaranger/

########################################

id = get_rt_id(cur, 'Respect Tetsu, DekaBreak (Tokusou Sentai Dekaranger)', 'https://redd.it/w9bfoa')
add_data(['DekaBreak'],
'DekaBreak',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9bfoa/respect_tetsu_dekabreak_tokusou_sentai_dekaranger/

########################################

id = get_rt_id(cur, 'Respect Doggie Kruger, DekaMaster (Tokusou Sentai Dekaranger)', 'https://redd.it/w9bgg4')
add_data(['DekaMaster'],
'DekaMaster',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9bgg4/respect_doggie_kruger_dekamaster_tokusou_sentai/

########################################

id = get_rt_id(cur, 'Respect Lord Guan Yu, the God of War (Romance of the Three Kingdoms)', 'https://redd.it/w8rzsk')
add_data(['Guan Yu'],
'Guan Yu',
False,
True,
[
    ['Romance of the (Three|3) Kingdoms'], ['Chinese Myth(ology)?']
],
'Romance of the Three Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w8rzsk/respect_lord_guan_yu_the_god_of_war_romance_of/

########################################

id = get_rt_id(cur, 'Respect the RX-78-01 Prototype Gundam (Mobile Suit Gundam: The Origin)', 'https://redd.it/w8woth')
add_data(['RX(-| )78(-| )01'],
'RX-78-01',
False,
True,
[
    ['Gundam']
],
'Gundam',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w8woth/respect_the_rx7801_prototype_gundam_mobile_suit/

########################################

id = get_rt_id(cur, 'Respect Majin Buu (Dragon Ball Multiverse)', 'https://redd.it/w9c55o')
add_data(['Buu'],
'Buu',
False,
False,
[
    ['Dragon Ball Multiverse']
],
'Dragon Ball Multiverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9c55o/respect_majin_buu_dragon_ball_multiverse/

########################################

id = get_rt_id(cur, "Respect Innistrad''s Werewolves! (Magic: The Gathering)", 'https://redd.it/w9g4fj')
add_data(["Innistrad''?s? Werewolves"],
"Innistrad''s Werewolves",
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9g4fj/respect_innistrads_werewolves_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Andy! (Undead Unluck)', 'https://redd.it/w9lbie')
add_data(['Andy'],
'Andy',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9lbie/respect_andy_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect the Knights of the Blackened Denarius (The Dresden Files)', 'https://redd.it/w9q1lw')
add_data(['Blackened Denarius'],
'Blackened Denarius',
False,
True,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9q1lw/respect_the_knights_of_the_blackened_denarius_the/

add_data(['Nicodemus Archleone'],
'Nicodemus Archleone',
False,
True,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9q1lw/respect_the_knights_of_the_blackened_denarius_the/

add_data(['Polonius Lartessa'],
'Polonius Lartessa',
False,
True,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9q1lw/respect_the_knights_of_the_blackened_denarius_the/

add_data(['Deirdre'],
'Deirdre',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9q1lw/respect_the_knights_of_the_blackened_denarius_the/

add_data(['Urisel'],
'Urisel',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w9q1lw/respect_the_knights_of_the_blackened_denarius_the/

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

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

update_respectthread(cur, 425, 'Respect Ash Williams (The Evil Dead Trilogy)', 'https://redd.it/1g51ig9')

########################################

add_data(['Po'],
'Po',
False,
False,
[
    ['Dragon Warrior']
],
'Kung Fu Panda',
'{1150}'
)
#https://www.reddit.com/r/whowouldwin/comments/1g2za7o/regular_sonic_vs_po_the_dragon_warrior/lrryulm/?context=3

########################################

id = get_rt_id(cur, 'Respect The Naturom Demonto (Evil Dead Rise)', 'https://redd.it/1g25fn0')
add_data(['Naturom Demonto'],
'Naturom Demonto',
False,
True,
[
    ['Evil Dead Rise']
],
'Evil Dead Rise',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g25fn0/respect_the_naturom_demonto_evil_dead_rise/

########################################

id = get_rt_id(cur, 'Respect the Deadites! (Dynamite Entertainment)', 'https://redd.it/1g53tvm')
add_data(['Deadites?'],
'Deadites',
False,
False,
[
    ['Dynamite Entertainment']
],
'Dynamite Entertainment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g53tvm/respect_the_deadites_dynamite_entertainment/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Evil Dead 2, Space Goat Publishing)', 'https://redd.it/1g3hkwy')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Evil Dead', 'Space Goat']
],
'Space Goat Productions',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g3hkwy/respect_ash_williams_evil_dead_2_space_goat/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Dark Horse Comics)', 'https://redd.it/1g4a0mh')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Dark(-| )?Horse']
],
'Dark Horse Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g4a0mh/respect_ash_williams_dark_horse_comics/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Evil Dead, video game composite)', 'https://redd.it/1g4n39s')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Evil Dead', '(video)?games?']
],
'Evil Dead Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g4n39s/respect_ash_williams_evil_dead_video_game/

########################################

id = get_rt_id(cur, 'Respect the Necronomicon (Evil Dead, video game composite)', 'https://redd.it/1g4ns9b')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['Evil Dead', '(video)?games?']
],
'Evil Dead Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g4ns9b/respect_the_necronomicon_evil_dead_video_game/


########################################

id = get_rt_id(cur, 'Respect Necronomicon Ex Mortis! (Dynamite Entertainment)', 'https://redd.it/1g4ajbx')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['Dynamite Entertainment']
],
'Dynamite Entertainment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g4ajbx/respect_necronomicon_ex_mortis_dynamite/

########################################

id = get_rt_id(cur, 'Respect the Necronomicon (Dark Horse Comics)', 'https://redd.it/1g4a0pi')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['Dark(-| )?Horse']
],
'Dark Horse Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g4a0pi/respect_the_necronomicon_dark_horse_comics/

########################################

id = get_rt_id(cur, "Respect Jessie''s Arbok (Pokemon Anime)", 'https://redd.it/1g27zli')
add_data(['Arbok'],
'Arbok',
False,
False,
[
    ['Jessies?']
],
'Jessie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g27zli/respect_jessies_arbok_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Kiva (VERSUS)', 'https://redd.it/1g29o3a')
add_data(['Kiva'],
'Kiva',
False,
False,
[
    ['VERSUS']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g29o3a/respect_kiva_versus/

########################################

id = get_rt_id(cur, 'Respect SCP-427, Lovecraftian Locket (SCP Foundation)', 'https://redd.it/1g2ggv2')
add_data(['SCP ?(-| )? ?427'],
'SCP-427',
False,
True,
[
    ['Lovecraftian Locket']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g2ggv2/respect_scp427_lovecraftian_locket_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Silent Hills (P.T.)', 'https://redd.it/1g2s6m0')
add_data(['Silent Hills?'],
'Silent Hill',
False,
False,
[
    ['P\.?T\.?']
],
'P.T.',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g2s6m0/respect_silent_hills_pt/

########################################

id = get_rt_id(cur, 'Respect The Unnamed Predator (AVP 1999/2000)', 'https://redd.it/1g2uoxz')
add_data(['Predator'],
'Predator',
False,
False,
[
    ['Aliens Versus Predator', '1999'], ['AVP', '1999']
],
'Aliens Versus Predator, 1999',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g2uoxz/respect_the_unnamed_predator_avp_19992000/


########################################

id = get_rt_id(cur, 'Respect the Children of Loki! (Norse Mythology)', 'https://redd.it/1g446hw')
add_data(['Children of Loki'],
'Children of Loki',
True,
False,
[
    ['myth?(ical|olog(y|ical))'], ['Four Horsemen of the Apocalypse'], ['Norse Myth']
],
'Norse Mythology',
'{' + '{}'.format(id) + '}'
)
#

add_data(['J(ö|o)rmungandr'],
'Jörmungandr',
False,
True,
[
    ['myth?(ical|olog(y|ical))'], ['Norse (Myth|Serpent|God|Pantheon)'], ['The World Snake'], ["Loki''s boys"]
],
'Norse Mythology',
'{' + '{}'.format(id) + '}'
)
#

add_data(['J(ö|o)rmungandr'],
'Jörmungandr',
False,
False,
[
    ['God of War'], ['G\.?O\.?W\.? ?(Ragnarok|Versions?)'], ['Atreus']
],
'God of War',
'{}'
)
#


add_data(['J(ö|o)rmungandr'],
'Jörmungandr',
False,
False,
[
    ['Worm']
],
'Worm',
'{}'
)
#


add_data(['Hel'],
'Hel',
False,
False,
[
    ['myth?(ical|olog(y|ical))'], ['Norse (Myth|Serpent|God(dess)?|Pantheon)'], ["Loki''s boys"]
],
'Norse Mythology',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect King Shark (Harley Quinn)', 'https://redd.it/1g5bw08')
add_data(['King Shark'],
'King Shark',
False,
False,
[
    ['King Shark ?\(Harley Quinn']
],
'Harley Quinn',
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

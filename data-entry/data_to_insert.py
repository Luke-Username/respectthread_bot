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
'{"Monsters,? Inc"}'
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

def add_data(name_list, default_name, is_team, is_default, version_list, displayed_version_name, rt_id_array):
    # Check if the names are valid regular expressions
    for name in name_list:    
        try:
            re.compile(name)
        except re.error:
            print("WARNING: {} is not a valid regular expression!".format(name))
            return

    name_lists.append(name_list)
    default_names.append(default_name)
    is_team_list.append(is_team)
    is_default_list.append(is_default)
    version_lists.append(version_list)
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

update_respectthread(cur, 6170, 'Respect Sun Wukong, The Great Sage Equal to Heaven! (Chinese Mythology)', 'https://redd.it/rdpmv4')

########################################

id = get_rt_id(cur, 'Respect Suzuka Gozen, the JK Saber! (Fate)', 'https://redd.it/rcjfjd')
add_data(['Suzuka Gozen'],
'Suzuka Gozen',
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rcjfjd/respect_suzuka_gozen_the_jk_saber_fate/

########################################

id = get_rt_id(cur, 'Respect Rockslide! (Marvel 616)', 'https://redd.it/rcryw4')
add_data(['Rockslide'],
'Rockslide',
False,
False,
[
'{"616"}',
'{"X(-| )?Men"}',
'{"Santo"}'
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rcryw4/respect_rockslide_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Anole! (Marvel 616)', 'https://redd.it/rcrywo')
add_data(['Anole'],
'Anole',
False,
False,
[
'{"616"}', '{"Marvel"}',
'{"X(-| )?Men"}',
'{"Victor"}'
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rcrywo/respect_anole_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Tarene, Thor Girl (Marvel, 616)', 'https://redd.it/rd918l')
add_data(['Thor Girl'],
'Thor Girl',
False,
True,
[
'{"616"}', '{"Marvel"}'
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rd918l/respect_tarene_thor_girl_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Gorr, the God Butcher (Marvel Comics)', 'https://redd.it/rdfbg9')
add_data(['Gorr'],
'Gorr',
False,
True,
[
'{"616"}', '{"Marvel"}'
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdfbg9/respect_gorr_the_god_butcher_marvel_comics/

add_data(['Gorr the God Butcher'],
'Gorr the God Butcher',
False,
True,
[
'{"616"}', '{"Marvel"}'
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdfbg9/respect_gorr_the_god_butcher_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect SCP-517-ARC, A Demon Born From War (SCP Foundation)', 'https://redd.it/rdkvpf')
add_data(['SCP(-| )?517(-| )?ARC'],
'SCP-517-ARC',
False,
True,
[
'{"Foundation"}'
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdkvpf/respect_scp517arc_a_demon_born_from_war_scp/

########################################

id = get_rt_id(cur, 'Respect Kosho Shinogi (Baki)', 'https://redd.it/rdduqz')
add_data(['K(ō|o)u?sh(ō|o)u? Shinogi'],
'Kōushō Shinogi',
False,
True,
[
'{"Baki"}'
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdduqz/respect_kosho_shinogi_baki/

########################################

id = get_rt_id(cur, "Respect Aa'une, the Oligarch (Chaotic)", 'https://redd.it/rdll7n')
add_data(["Aa''une"],
"Aa''une",
False,
True,
[
'{"Chaotic"}'
],
'Chaotic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdll7n/respect_aaune_the_oligarch_chaotic/

########################################

add_data(["Sun Wu ?Kong"],
"Sun Wukong",
False,
True,
[
'{"Journey to the West"}', '{"JTTW"}',
'{"Chinese"}',
'{"myth?(ical|olog(y|ical))?"}',
'{"buddha(hood)?"}'
],
'',
'{6170}'
)
#https://www.reddit.com/r/respectthreads/comments/rdpmv4/respect_sun_wukong_the_great_sage_equal_to_heaven/

########################################

id = get_rt_id(cur, 'Respect Frisk Dreemurr {Inseparable}', 'https://redd.it/rdymjg')
add_data(["Frisk"],
"Frisk",
False,
False,
[
'{"Inseparable"}'
],
'Inseparable',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdymjg/respect_frisk_dreemurr_inseparable/

########################################

id = get_rt_id(cur, 'Respect Asriel Dreemurr (Inseparable)', 'https://redd.it/rdymwx')
add_data(["Asriel"],
"Asriel",
False,
False,
[
'{"Inseparable"}'
],
'Inseparable',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/rdymwx/respect_asriel_dreemurr_inseparable/

########################################

id = get_rt_id(cur, 'Respect Toneri Ōtsutsuki! (Naruto)', 'https://redd.it/re0goh')
add_data(['Toneri'],
'Toneri',
False,
True,
[
'{"Naruto"}'
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/re0goh/respect_toneri_%C5%8Dtsutsuki_naruto/

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

con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

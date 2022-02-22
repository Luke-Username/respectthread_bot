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

update_respectthread(cur, 8209, 'Respect Neil Clarke! (Absolutely Anything)', 'https://redd.it/sysjhf')

########################################

add_data(['Storm'],
'Storm',
False,
False,
[
    ['vs\.? Storm', 'Johnny Storm'], ['vs\.? Storm', 'Hulk']
],
'616',
'{2386}'
)
#https://www.reddit.com/r/whowouldwin/comments/sxo8hd/she_hulk_vs_wonder_woman_vs_terminator_x_vs_storm/hxtdglm/?context=3

########################################

add_data(['Terminator X'],
'Terminator X',
False,
True,
[
    ['Terminatrix']
],
'',
'{328}'
)
#https://www.reddit.com/r/whowouldwin/comments/sxo8hd/she_hulk_vs_wonder_woman_vs_terminator_x_vs_storm/hxtdglm/?context=3

########################################

id = get_rt_id(cur, 'Respect Drake! (Beyonders)', 'https://redd.it/sxw86a')
add_data(['Drake'],
'Drake',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw86a/respect_drake_beyonders/

########################################

id = get_rt_id(cur, 'Respect Torivors! (Beyonders)', 'https://redd.it/sxw87m')
add_data(['Torivors?'],
'Torivors',
False,
True,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw87m/respect_torivors_beyonders/

########################################

id = get_rt_id(cur, 'Respect Jason Walker! (Beyonders)', 'https://redd.it/sxw89h')
add_data(['Jason Walker'],
'Jason Walker',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw89h/respect_jason_walker_beyonders/

########################################

id = get_rt_id(cur, 'Respect Ferrin! (Beyonders)', 'https://redd.it/sxw8bc')
add_data(['Ferrin'],
'Ferrin',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw8bc/respect_ferrin_beyonders/

########################################

id = get_rt_id(cur, 'Respect the Wanderer! (Beyonders)', 'https://redd.it/sxw8cx')
add_data(['Wanderer'],
'Wanderer',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw8cx/respect_the_wanderer_beyonders/

########################################

id = get_rt_id(cur, 'Respect Corinne! (Beyonders)', 'https://redd.it/sxw8fr')
add_data(['Corinne'],
'Corinne',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw8fr/respect_corinne_beyonders/

########################################

id = get_rt_id(cur, 'Respect Jasher! (Beyonders)', 'https://redd.it/sxw8h0')
add_data(['Jasher'],
'Jasher',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw8h0/respect_jasher_beyonders/

########################################

id = get_rt_id(cur, 'Respect Galloran! (Beyonders)', 'https://redd.it/sxw8ik')
add_data(['Galloran'],
'Galloran',
False,
True,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sxw8ik/respect_galloran_beyonders/

########################################

id = get_rt_id(cur, 'Respect Tark! (Beyonders)', 'https://redd.it/sy3wc2')
add_data(['Tark'],
'Tark',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy3wc2/respect_tark_beyonders/

########################################

id = get_rt_id(cur, 'Respect Maldor! (Beyonders)', 'https://redd.it/sy3xia')
add_data(['Maldor'],
'Maldor',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy3xia/respect_maldor_beyonders/

########################################

id = get_rt_id(cur, 'Respect Nedwin! (Beyonders)', 'https://redd.it/sy4ovf')
add_data(['Nedwin'],
'Nedwin',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy4ovf/respect_nedwin_beyonders/

########################################

id = get_rt_id(cur, 'Respect Aram! (Beyonders)', 'https://redd.it/sy8qpr')
add_data(['Aram'],
'Aram',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy8qpr/respect_aram_beyonders/

########################################

id = get_rt_id(cur, 'Respect Drinlings! (Beyonders)', 'https://redd.it/sy8ri8')
add_data(['Drinlings?'],
'Drinlings',
False,
True,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy8ri8/respect_drinlings_beyonders/

########################################

id = get_rt_id(cur, 'Respect the Maumet! (Beyonders)', 'https://redd.it/sy8sia')
add_data(['Maumet'],
'Maumet',
False,
False,
[
    ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy8sia/respect_the_maumet_beyonders/

########################################

id = get_rt_id(cur, 'Respect Rintrah (Marvel 616)', 'https://redd.it/sy5fdi')
add_data(['Rintrah'],
'Rintrah',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sy5fdi/respect_rintrah_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Garfiel Tinsel (Re:Zero, Anime)', 'https://redd.it/syp9qk')
add_data(['Garfiel Tinsel'],
'Garfiel Tinsel',
False,
True,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/syp9qk/respect_garfiel_tinsel_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Mochizuki Chiyome! (Fate)', 'https://redd.it/sypadx')
add_data(['Mochizuki Chiyome'],
'Mochizuki Chiyome',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/sypadx/respect_mochizuki_chiyome_fate/

########################################

id = get_rt_id(cur, 'Respect Frank Castle, the Punisher (2004 film)', 'https://redd.it/syqz67')
add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['Punisher.*2004|2004.*Punisher'], ['Thomas Jane']
],
'2004',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/syqz67/respect_frank_castle_the_punisher_2004_film/

########################################

id = get_rt_id(cur, 'Respect Captain Thunder (DC Pre-Crisis Earth-276)', 'https://redd.it/syvnra')
add_data(['Willie Fawcett'],
'Willie Fawcett',
False,
True,
[
    ['276']
],
'Earth-276',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/syvnra/respect_captain_thunder_dc_precrisis_earth276/

add_data(['Captain Thunder'],
'Captain Thunder',
False,
False,
[
    ['276']
],
'Earth-276',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/syvnra/respect_captain_thunder_dc_precrisis_earth276/

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

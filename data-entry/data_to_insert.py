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

id = get_rt_id(cur, 'Respect Uttamatomakkin! (Pocahontas)', 'https://redd.it/1jztax9')
add_data(['Uttamatomakkin'],
'Uttamatomakkin',
False,
False,
[
    ['Pocahontas']
],
'Pocahontas',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jztax9/respect_uttamatomakkin_pocahontas/

########################################

id = get_rt_id(cur, 'Respect John Rolfe! (Pocahontas)', 'https://redd.it/1jztcz7')
add_data(['John Rolfe'],
'John Rolfe',
False,
False,
[
    ['Pocahontas']
],
'Pocahontas',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jztax9/respect_uttamatomakkin_pocahontas/

########################################

id = get_rt_id(cur, 'Respect Pocahontas! (Pocahontas)', 'https://redd.it/1jztiyj')
add_data(['Pocahontas'],
'Pocahontas',
False,
False,
[
    ['Disneys?'], ['Mulan']
],
'Disney',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jztiyj/respect_pocahontas_pocahontas/

########################################

id = get_rt_id(cur, 'Respect Captain John Smith! (Pocahontas)', 'https://redd.it/1jztpzb')
add_data(['John Smith'],
'John Smith',
False,
False,
[
    ['Pocahontas']
],
'Pocahontas',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect C00lkidd! (Forsaken)', 'https://redd.it/1k0hjke')
add_data(['C00lkidd'],
'C00lkidd',
False,
True,
[
    ['Forsaken']
],
'Forsaken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k0hjke/respect_c00lkidd_forsaken/

########################################

id = get_rt_id(cur, 'Respect Darth Sion (Star Wars)', 'https://redd.it/1k0xdfv')
add_data(['Darth Sion'],
'Darth Sion',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Koga Saburo (Fate/Samurai Remnant)', 'https://redd.it/1k1jywv')
add_data(['K(ō|o)ga Sabur(ō|o)'],
'Kōga Saburō',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hieda-no-Are (Fate/Samurai Remnant)', 'https://redd.it/1k2f6n2')
add_data(['Hieda(-| )no(-| )Are'],
'Hieda-no-Are',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Luck (Dreamwalker)', 'https://redd.it/1k1slla')
add_data(['Luck'],
'Luck',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k1slla/respect_luck_dreamwalker/

########################################

id = get_rt_id(cur, 'Respect Bai Xing Ye, the White Emperor! (Ze Tian Ji/Way of Choices)', 'https://redd.it/1k1szab')
add_data(['Bai Xing Ye'],
'Bai Xing Ye',
False,
False,
[
    ['Way of Choices'], ['Ze Tian Ji']
],
'Ze Tian Ji',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k1szab/respect_bai_xing_ye_the_white_emperor_ze_tian/

########################################

id = get_rt_id(cur, 'Respect Tsukasa Kadoya, Kamen Rider Decade (Kamen Rider Decade)', 'https://redd.it/1k2g514')
add_data(['Kamen Rider Decade'],
'Kamen Rider Decade',
False,
True,
[
    ['Tsukasa Kadoya']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k2g514/respect_tsukasa_kadoya_kamen_rider_decade_kamen/

########################################

id = get_rt_id(cur, 'Respect Lucita De Aragon! (Vampire: the Masquerade)', 'https://redd.it/1k1sl8u')
add_data(['Lucita De Aragon'],
'Lucita De Aragon',
False,
True,
[
    ['Vampire:? The Masquerade'], ['VTM']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k1sl8u/respect_lucita_de_aragon_vampire_the_masquerade/

add_data(['Lucita'],
'Lucita',
False,
False,
[
    ['Vampire:? The Masquerade'], ['VTM']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k1sl8u/respect_lucita_de_aragon_vampire_the_masquerade/

########################################

id = get_rt_id(cur, 'Respect Despair of The Endless (DC Comics, The Sandman)', 'https://redd.it/1k2phab')
add_data(['Despair of The Endless'],
'Despair of The Endless',
False,
True,
[
    ['DC'], ['Sandman']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k2phab/respect_despair_of_the_endless_dc_comics_the/

add_data(['Despair'],
'Despair',
False,
False,
[
    ['of The Endless']
],
'The Sandman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k2phab/respect_despair_of_the_endless_dc_comics_the/

########################################

id = get_rt_id(cur, "Respect Stark (Frieren: Beyond Journey''s End)", 'https://redd.it/1k33yt5')
add_data(['Stark'],
'Stark',
False,
False,
[
    ['Frieren']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k33yt5/respect_stark_frieren_beyond_journeys_end/

########################################

id = get_rt_id(cur, "Respect Fern (Frieren: Beyond Journey''s End)", 'https://redd.it/1k3kb9q')
add_data(['Fern'],
'Fern',
False,
False,
[
    ['Frieren']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pico! (Newgrounds)', 'https://redd.it/1k36d6w')
add_data(['Pico'],
'Pico',
False,
False,
[
    ['Newgrounds?'], ["Pico''?s? School"], ['FNF'], ['Friday Night Funkin'], ['Pico Series']
],
'Newgrounds',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k36d6w/respect_pico_newgrounds/

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

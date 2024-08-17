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

update_respectthread(cur, 6189, 'Respect Thor, The Thunderer (Neil Gaiman''s Norse Mythology)', 'https://redd.it/1etnbui')
update_respectthread(cur, 2456, 'Respect: Moon Knight (Marvel, 616) - [Classic]', 'https://redd.it/1ets8w2')

########################################

add_data(['Dead(-| )?pool'],
'Deadpool',
False,
False,
[
    ['Deadpool 2013']
],
'2013',
'{24967}'
)
#https://www.reddit.com/r/respectthread_bot/comments/1eu544y/deadpool_deadpool_2013/lihwkui/?context=3

########################################

id = get_rt_id(cur, 'Respect Maxie (Pokemon Adventures)', 'https://redd.it/1eqoyas')
add_data(['Maxie'],
'Maxie',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eqoyas/respect_maxie_pokemon_adventures/

########################################

id = get_rt_id(cur, 'Respect Tyler Blu Gunderson (Rio)', 'https://redd.it/1er37kl')
add_data(['Blu'],
'Blu',
False,
False,
[
    ['Rio']
],
'Rio',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1er37kl/respect_tyler_blu_gunderson_rio/

########################################

id = get_rt_id(cur, 'Respect Moxxie and Millie! (Helluva Boss)', 'https://redd.it/1er4r1l')
add_data(['Millie'],
'Millie',
False,
False,
[
    ['Helluva Boss'], ['Blitz(ø|o)']
],
'Helluva Boss',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1er4r1l/respect_moxxie_and_millie_helluva_boss/

add_data(['Moxxie'],
'Moxxie',
False,
False,
[
    ['Helluva Boss'], ['Blitz(ø|o)']
],
'Helluva Boss',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1er4r1l/respect_moxxie_and_millie_helluva_boss/


add_data(['Moxxie,?( and)? Millie|Millie,?( and)? Moxxie'],
'Moxxie and Millie',
True,
True,
[
    ['Helluva Boss'], ['Blitz(ø|o)']
],
'Helluva Boss',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1er4r1l/respect_moxxie_and_millie_helluva_boss/

########################################

id = get_rt_id(cur, 'Respect Livyjira! (Ultraman Arc)', 'https://redd.it/1esjs5u')
add_data(['Livyjira'],
'Livyjira',
False,
True,
[
    ['Ultraman']
],
'Ultraman Arc',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1esjs5u/respect_livyjira_ultraman_arc/

########################################

id1 = get_rt_id(cur, 'Respect Hank, The Ranger! (Dungeons & Dragons [TV series])', 'https://redd.it/1err5yk')
add_data(['Hank'],
'Hank',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Ranger'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Ranger']
],
'Dungeons & Dragons',
'{' + '{}'.format(id1) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err5yk/respect_hank_the_ranger_dungeons_dragons_tv_series/

########################################

id2 = get_rt_id(cur, 'Respect Diana, The Acrobat! (Dungeons & Dragons [TV series])', 'https://redd.it/1err65e')
add_data(['Diana'],
'Diana',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Acrobat'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Acrobat']
],
'Dungeons & Dragons',
'{' + '{}'.format(id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err65e/respect_diana_the_acrobat_dungeons_dragons_tv/

########################################

id3 = get_rt_id(cur, 'Respect Presto, The Magician! (Dungeons & Dragons [TV series])', 'https://redd.it/1err6kr')
add_data(['Presto'],
'Presto',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Magician'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Magician']
],
'Dungeons & Dragons',
'{' + '{}'.format(id3) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err6kr/respect_presto_the_magician_dungeons_dragons_tv/

########################################

id4 = get_rt_id(cur, 'Respect Eric, The Cavalier! (Dungeons & Dragons [TV series])', 'https://redd.it/1err6t6')
add_data(['Presto'],
'Presto',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Cavalier'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Cavalier']
],
'Dungeons & Dragons',
'{' + '{}'.format(id4) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err6t6/respect_eric_the_cavalier_dungeons_dragons_tv/

########################################

id5 = get_rt_id(cur, 'Respect Bobby, The Barbarian! (Dungeons & Dragons [TV series])', 'https://redd.it/1err7a7')
add_data(['Bobby'],
'Bobby',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Barbarian'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Barbarian']
],
'Dungeons & Dragons',
'{' + '{}'.format(id5) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err7a7/respect_bobby_the_barbarian_dungeons_dragons_tv/

########################################

id6 = get_rt_id(cur, 'Respect Sheila, The Thief! (Dungeons & Dragons [TV series])', 'https://redd.it/1err7ua')
add_data(['Sheila'],
'Sheila',
False,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)|The Thief'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)|The Thief']
],
'Dungeons & Dragons',
'{' + '{}'.format(id6) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1err7ua/respect_sheila_the_thief_dungeons_dragons_tv/

########################################

id7 = get_rt_id(cur, 'Respect The Heroes! (Dungeons & Dragons [TV series])', 'https://redd.it/1erra0u')
add_data(['The Heroes'],
'The Heroes',
True,
False,
[
    ['Dungeons (&|and) Dragons', 'Cartoon|TV Series|198(3|0s)'], ['D ?(&|n) ?D', 'Cartoon|TV Series|198(3|0s)']
],
'Dungeons & Dragons',
'{' + '{}, {}, {}, {}, {}, {}, {}'.format(id7, id1, id2, id3, id4, id5, id6) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1erra0u/respect_the_heroes_dungeons_dragons_tv_series/

########################################

id = get_rt_id(cur, 'Respect Venger, The Force of Evil! (Dungeons & Dragons [TV series])', 'https://redd.it/1errksh')
add_data(['Venger'],
'Venger',
False,
False,
[
    ['Dungeons (&|and) Dragons'], ['D ?(&|n) ?D'], ['The Force of Evil']
],
'Dungeons & Dragons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1errksh/respect_venger_the_force_of_evil_dungeons_dragons/

########################################

id = get_rt_id(cur, 'Respect: Cassandra Cain, Batgirl! (DC Pre-Flashpoint)', 'https://redd.it/1es1c2t')
add_data(['Cassandra Cain'],
'Cassandra Cain',
False,
False,
[
    ['Pre(-| )?Flashpoint']
],
'Pre-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Cassandra Cain'],
'Cassandra Cain',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}, 1503, 1502'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1es1c2t/respect_cassandra_cain_batgirl_dc_preflashpoint/


########################################

id = get_rt_id(cur, 'Respect Stantler (Pokemon Anime)', 'https://redd.it/1esuly5')
add_data(['Stantler'],
'Stantler',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1esuly5/respect_stantler_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Elements (Elemental)', 'https://redd.it/1etm546')
add_data(['The Elements'],
'The Elements',
True,
False,
[
    ['The Elements ?\(Elemental\)']
],
'Elemental',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1etm546/respect_the_elements_elemental/

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

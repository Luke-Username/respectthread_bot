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

update_respectthread(cur, 13121, 'Respect Ophiuchus the emperor, A.K.A GODFIELD (Lumpy Touch)', 'https://redd.it/11dfb1l')

########################################

add_data(['Godfield'],
'Godfield',
False,
True,
[
    ['Lumpy Touch']
],
'Lumpy Touch',
'{13121}'
)
#

add_data(['Ophiuchus the emperor'],
'Ophiuchus the emperor',
False,
False,
[
    ['Lumpy Touch']
],
'Lumpy Touch',
'{13121}'
)
#

########################################

add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['Time Lords?']
],
'Doctor Who',
'{14419,23159,22631,23115,40,15401,23253}'
)
#https://www.reddit.com/r/whowouldwin/comments/11c4av8/batman_has_to_come_up_with_a_contingency_plan_for/ja2n6vn/?context=3

########################################

id = get_rt_id(cur, "Respect Nagao Kagetora, Echigo''s God of War (Fate)", 'https://redd.it/11c2g2m')
add_data(['Nagao Kagetora'],
'Nagao Kagetora',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11c2g2m/respect_nagao_kagetora_echigos_god_of_war_fate/

########################################

id = get_rt_id(cur, 'Respect Pidge (Voltron Force)', 'https://redd.it/11c7j6u')
add_data(['Pidge'],
'Pidge',
False,
False,
[
    ['Voltron Force']
],
'Voltron Force',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11c7j6u/respect_pidge_voltron_force/

########################################

id = get_rt_id(cur, 'Respect Ghiblib the Christmas Demon (Royalty Free Christmas Songs)', 'https://redd.it/11cgy7z')
add_data(['Ghiblib the Christmas Demon'],
'Ghiblib the Christmas Demon',
False,
True,
[
    ['Royalty Free Christmas Songs'], ['Jacksfilms']
],
'Royalty Free Christmas Songs',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Winslow Schott, the Toyman (DC Comics, Post Crisis)', 'https://redd.it/11cl4iz')
add_data(['Toyman'],
'Toyman',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl4iz/respect_winslow_schott_the_toyman_dc_comics_post/

add_data(['Toyman'],
'Toyman',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'],
    ['Toyman vs'], ['vs\.? Toyman'], ['Superman', 'DC'],
    ['Superman', 'Batman'], ['Superman', 'rogues? gallery'],
    ["Superman''?s? Villains"], ['Prep']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl4iz/respect_winslow_schott_the_toyman_dc_comics_post/

########################################

id = get_rt_id(cur, 'Respect Leonardo (Teenage Mutant Ninja Turtles) [Mirage Comics]', 'https://redd.it/11cl67q')
add_data(['Leonardo'],
'Leonardo',
False,
False,
[
    ['Mirage (Comics|Studios)']
],
'Mirage Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl67q/respect_leonardo_teenage_mutant_ninja_turtles/

########################################

id1 = get_rt_id(cur, 'Respect Raphael (Teenage Mutant Ninja Turtles) [Mirage Comics]', 'https://redd.it/11cl69j')
add_data(['Raphael'],
'Raphael',
False,
False,
[
    ['Mirage (Comics|Studios)']
],
'Mirage Comics',
'{' + '{}'.format(id1) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl69j/respect_raphael_teenage_mutant_ninja_turtles/

########################################

id2 = get_rt_id(cur, 'Respect Donatello (Teenage Mutant Ninja Turtles) [Mirage Comics]', 'https://redd.it/11cl6bk')
add_data(['Donatello'],
'Donatello',
False,
False,
[
    ['Mirage (Comics|Studios)']
],
'Mirage Comics',
'{' + '{}'.format(id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl6bk/respect_donatello_teenage_mutant_ninja_turtles/

########################################

id3 = get_rt_id(cur, 'Respect Michelangelo (Teenage Mutant Ninja Turtles) [Mirage Comics]', 'https://redd.it/11cl6dp')
add_data(['Michelangelo'],
'Michelangelo',
False,
False,
[
    ['Mirage (Comics|Studios)']
],
'Mirage Comics',
'{' + '{}'.format(id3) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cl6dp/respect_michelangelo_teenage_mutant_ninja_turtles/

########################################

add_data(['Ninja Turtles?'],
'Teenage Mutant Ninja Turtles',
True,
False,
[
    ['Mirage']
],
'Mirage Comics',
'{' + '{}, {}, {}, {}'.format(id, id1, id2, id3) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Koraidon and Miraidon (Pokemon Games)', 'https://redd.it/11cohk6')
add_data(['Koraidon'],
'Koraidon',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cohk6/respect_koraidon_and_miraidon_pokemon_games/

add_data(['Miraidon'],
'Miraidon',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cohk6/respect_koraidon_and_miraidon_pokemon_games/

########################################

id = get_rt_id(cur, 'Respect Rogue (X-Men: The Animated Series)', 'https://redd.it/11cvycx')
add_data(['Rogue'],
'Rogue',
False,
False,
[
    ['X(-| )?Men:? The Animated Series'], ['X(-| )?Men', '1992']
],
'X-Men, 1992',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cvycx/respect_rogue_xmen_the_animated_series/

########################################

id = get_rt_id(cur, 'Respect the Seal of Orichalcos (Yu-Gi-Oh!)', 'https://redd.it/11cwlkn')
add_data(['Seal of Orichalcos'],
'Seal of Orichalcos',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cwlkn/respect_the_seal_of_orichalcos_yugioh/

########################################

id = get_rt_id(cur, 'Respect the Legendary Dragons (Yu-Gi-Oh!)', 'https://redd.it/11cwlrb')
add_data(['Legendary Dragons'],
'Legendary Dragons',
True,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cwlrb/respect_the_legendary_dragons_yugioh/

add_data(['Timaeus'],
'Timaeus',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh'], ['Yugis?']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11cwlrb/respect_the_legendary_dragons_yugioh/

########################################

id = get_rt_id(cur, 'Respect Luka Redgrave (Bayonetta)', 'https://redd.it/11d2r94')
add_data(['Luka'],
'Luka',
False,
False,
[
    ['Bayonetta'], ['Luka Redgrave']
],
'Bayonetta',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11d2r94/respect_luka_redgrave_bayonetta/

########################################

id = get_rt_id(cur, 'Respect SCP-343, "God" (SCP Foundation)', 'https://redd.it/11dcoax')
add_data(['SCP ?(-| )? ?343'],
'SCP ?(-| )? ?343',
False,
True,
[
    ['God']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11dcoax/respect_scp343_god_scp_foundation/

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

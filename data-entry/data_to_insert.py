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

id = get_rt_id(cur, 'Respect Lucy MacLean (Fallout [TV Series])', 'https://redd.it/1ee6drs')
add_data(['Lucy MacLean'],
'Lucy MacLean',
False,
True,
[
    ['Fallout']
],
'Fallout',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ee6drs/respect_lucy_maclean_fallout_tv_series/

########################################

id = get_rt_id(cur, 'Respect the Psycho Sisters, Sena Riku and Sena Riko! (STAR: Strike It Rich)', 'https://redd.it/1een0mh')
add_data(['Psycho Sisters'],
'Psycho Sisters',
True,
False,
[
    ['STAR:? Strike It Rich']
],
'STAR: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1een0mh/respect_the_psycho_sisters_sena_riku_and_sena/

########################################

id = get_rt_id(cur, 'Respect: The Midnight Mission! (Marvel, 616)', 'https://redd.it/1efc5b3')
add_data(['Midnight Mission'],
'Midnight Mission',
True,
False,
[
    ['616'], ['Moon Knight']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Black (Pokémon Adventures)', 'https://redd.it/1efefe6')
add_data(['Black'],
'Black',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1efefe6/respect_black_pok%C3%A9mon_adventures/

########################################

id = get_rt_id(cur, 'Respect White (Pokémon Adventures)', 'https://redd.it/1egaaed')
add_data(['White'],
'White',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1egaaed/respect_white_pok%C3%A9mon_adventures/

########################################

id = get_rt_id(cur, 'Respect N (Pokémon Adventures)', 'https://redd.it/1eh3o71')
add_data(['N'],
'N',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eh3o71/respect_n_pok%C3%A9mon_adventures/

########################################

id = get_rt_id(cur, 'Respect Archie (Pokemon Adventures)', 'https://redd.it/1ehe6un')
add_data(['Archie'],
'Archie',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ehe6un/respect_archie_pokemon_adventures/

########################################

add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Mario and Sonic'], ['Mario', 'Olympic Games']
],
'Sonic the Hedgehog',
'{8276,8277}'
)
#https://www.reddit.com/r/whowouldwin/comments/1egcm6c/every_mario_and_sonic_character_all_participates/

########################################

add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['Rick Sanchez']
],
'Doctor Who',
'{14419,24653,23159,22631,23115,40,15401,23253,24571}'
)
#https://www.reddit.com/r/whowouldwin/comments/1egl6o3/how_would_rick_sanchez_deal_with_these_really/lfsv3az/?context=3

########################################

id = get_rt_id(cur, 'Respect Po Bidau Tiara, The Po Bidau Princess! (Tower of God)', 'https://redd.it/1eg1j1s')
add_data(['Po Bidau Tiara'],
'Po Bidau Tiara',
False,
True,
[
    ['Tower of God']
],
'Tower of God',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eg1j1s/respect_po_bidau_tiara_the_po_bidau_princess/

########################################

id = get_rt_id(cur, 'Respect "Boss-Boss" Kalyaan (Avatar: The Yangchen Novels)', 'https://redd.it/1egmf1t')
add_data(['Kalyaan'],
'Kalyaan',
False,
False,
[
    ['Yangchen'], ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1egmf1t/respect_bossboss_kalyaan_avatar_the_yangchen/

########################################

id = get_rt_id(cur, 'Respect Keerat (Slaxx)', 'https://redd.it/1egoi5t')
add_data(['Keerat'],
'Keerat',
False,
False,
[
    ['Slaxx']
],
'Slaxx',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1egoi5t/respect_keerat_slaxx/

########################################

id = get_rt_id(cur, 'Respect Meta Knight (Kirby: Right Back at Ya!)', 'https://redd.it/1egr26f')
add_data(['Meta Knight'],
'Meta Knight',
False,
False,
[
    ['Right Back at Ya']
],
'Kirby: Right Back at Ya!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1egr26f/respect_meta_knight_kirby_right_back_at_ya/

########################################

id = get_rt_id(cur, 'Respect Monogelos/Digelos! (Ultraman Arc)', 'https://redd.it/1eh19h3')
add_data(['Monogelos'],
'Monogelos',
False,
False,
[
    ['Ultraman']
],
'Ultraman Arc',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eh19h3/respect_monogelosdigelos_ultraman_arc/

add_data(['Digelos'],
'Digelos',
False,
False,
[
    ['Ultraman']
],
'Ultraman Arc',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eh19h3/respect_monogelosdigelos_ultraman_arc/

########################################

id = get_rt_id(cur, 'Respect Carter Grayson, the Red Lightspeed Ranger (Power Rangers Lightspeed Rescue)', 'https://redd.it/1ehe48o')
add_data(['Carter Grayson'],
'Carter Grayson',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Red Lightspeed Ranger'],
'Red Lightspeed Ranger',
False,
True,
[
    ['Power Rangers']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ehe48o/respect_carter_grayson_the_red_lightspeed_ranger/

########################################

id = get_rt_id(cur, 'Respect Mr. No Legs (Mr. No Legs)', 'https://redd.it/1ehe4wf')
add_data(['Mr\.? No Legs'],
'Mr. No Legs',
False,
True,
[
    ['Mr. No Legs ?\(Mr. No Legs\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ehe4wf/respect_mr_no_legs_mr_no_legs/

########################################

id = get_rt_id(cur, 'Respect The Knight (Dead By Daylight)', 'https://redd.it/1eher12')
add_data(['Knight'],
'Knight',
False,
False,
[
    ['Dead By Daylight']
],
'Dead By Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eher12/respect_the_knight_dead_by_daylight/

########################################

id = get_rt_id(cur, 'Respect Chuck D. Head (Decap Attack)', 'https://redd.it/1ehjylz')
add_data(['Chuck D\.? Head'],
'Chuck D. Head',
False,
True,
[
    ['Decap Attack']
],
'Decap Attack',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ehjylz/respect_chuck_d_head_decap_attack/

########################################

id = get_rt_id(cur, 'Respect The Reaver/Soul Reaver (Legacy of Kain)', 'https://redd.it/1ehmrba')
add_data(['Soul Reaver'],
'Soul Reaver',
False,
True,
[
    ['Legacy of Kain']
],
'Legacy of Kain',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ehmrba/respect_the_reaversoul_reaver_legacy_of_kain/

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

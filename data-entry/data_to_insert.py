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

update_respectthread(cur, 6268, 'Respect the Ultimate Ones! (TYPE-MOON / Nasuverse)', 'https://redd.it/115lh06')
update_respectthread(cur, 6023, 'Respect: The God Emperor of Mankind (40k)', 'https://redd.it/118h4ht')

########################################

add_data(['Cell'],
'Cell',
False,
False,
[
    ['Perfect', 'Androids?']
],
'Dragon Ball',
'{3277}'
)
#https://www.reddit.com/r/whowouldwin/comments/115bwur/roasting_challenge_cell_roasts_the_narutoverse/


########################################

add_data(['Wuxian'],
'Wuxian',
False,
False,
[
    ['Legend of Hei']
],
'The Legend of Luo Xiaohei',
'{22710}'
)
#

########################################

add_data(['Teen Titans'],
'Teen Titans',
False,
False,
[
    ['Teen Titans \(.*animation.*\)']
],
'Teen Titans',
'{977}'
)
#https://www.reddit.com/r/respectthreads/comments/9bajhs/respect_the_teen_titans_teen_titans/

########################################

add_data(['Hercules'],
'Hercules',
False,
False,
[
    ['Shuumatsu no Valkyrie'], ['Record of Ragnarok']
],
'Shuumatsu no Valkyrie',
'{9367}'
)
#

########################################

add_data(['Ultimate Ones'],
'Ultimate Ones',
False,
False,
[
    ['TYPE(-| )?MOON'], ['Nasu(-| )?verse'], ['Fate']
],
'Nasuverse',
'{6268}'
)
#https://www.reddit.com/r/respectthreads/comments/115lh06/respect_the_ultimate_ones_typemoon_nasuverse/

########################################

id = get_rt_id(cur, 'Respect the Japanese Special Defense Force! (Gate, Anime)', 'https://redd.it/114ueoq')
add_data(['Japanese Special Defense Force'],
'Japanese Special Defense Force',
False,
False,
[
    ['Gate']
],
'Gate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/114ueoq/respect_the_japanese_special_defense_force_gate/

########################################

id = get_rt_id(cur, "Respect Raiden Tame''emon (Shuumatsu no Valkyrie/Record of Ragnarok)", 'https://redd.it/1152cvz')
add_data(["Raiden Tame''?emon"],
'Raiden Tameemon',
False,
False,
[
    ['Shuumatsu no Valkyrie'], ['Record of Ragnarok']
],
'Shuumatsu no Valkyrie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1152cvz/respect_raiden_tameemon_shuumatsu_no/

########################################

id = get_rt_id(cur, 'Respect Cavendish/Hakuba (One Piece)', 'https://redd.it/1157doe')
add_data(['Cavendish'],
'Cavendish',
False,
False,
[
    ['Hakuba'], ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1157doe/respect_cavendishhakuba_one_piece/

########################################

id = get_rt_id(cur, 'Respect Miyoi Okunoda (Touhou)', 'https://redd.it/115fcoj')
add_data(['Miyoi Okunoda'],
'Miyoi Okunoda',
False,
False,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/115fcoj/respect_miyoi_okunoda_touhou/

########################################

id = get_rt_id(cur, 'Respect the Teenage Mutant Ninja Turtles (Mutant Turtles: Superman Legend)', 'https://redd.it/115itdf')
add_data(['TMNT'],
'Teenage Mutant Ninja Turtles',
False,
False,
[
    ['Mutant Turtles:? Superman Legend']
],
'Mutant Turtles: Superman Legend',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/115itdf/respect_the_teenage_mutant_ninja_turtles_mutant/

########################################

id = get_rt_id(cur, 'Respect Shredder (Mutant Turtles: Superman Legend)', 'https://redd.it/115itof')
add_data(['Shredder'],
'Shredder',
False,
False,
[
    ['Mutant Turtles:? Superman Legend']
],
'Mutant Turtles: Superman Legend',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/115itof/respect_shredder_mutant_turtles_superman_legend/

########################################

id = get_rt_id(cur, 'Respect Missy! (Doctor Who)', 'https://redd.it/115l0h1')
add_data(['Missy'],
'Missy',
False,
False,
[
    ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/115l0h1/respect_missy_doctor_who/

########################################

id = get_rt_id(cur, 'Respect Yelena Belova (Marvel Comics, Earth-616)', 'https://redd.it/117c4y4')
add_data(['Yelena Belova'],
'Yelena Belova',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/117c4y4/respect_yelena_belova_marvel_comics_earth616/

########################################

id = get_rt_id(cur, 'Respect Yelena Belova (Marvel Cinematic Universe)', 'https://redd.it/117ckm6')
add_data(['Yelena Belova'],
'Yelena Belova',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/117ckm6/respect_yelena_belova_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 54: the Marvelbuster (Marvel, Earth-616)', 'https://redd.it/116rlrg')
add_data(['Danversbuster'],
'Danversbuster',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/116rlrg/respect_iron_man_model_54_the_marvelbuster_marvel/

add_data(['Marvelbuster'],
'Marvelbuster',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/116rlrg/respect_iron_man_model_54_the_marvelbuster_marvel/

########################################

id = get_rt_id(cur, 'Respect Piccolo! (Dragon Ball Z Abridged)', 'https://redd.it/116j6wu')
add_data(['Piccolo'],
'Piccolo',
False,
False,
[
    ['Team ?Four ?Star'], ['TFSA?'], ['DBZ:? ?A'], ['Abridged'], ['D(ragon)? ?B(all)? ?Z:? Abridged']
],
'TeamFourStar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/116j6wu/respect_piccolo_dragon_ball_z_abridged/

########################################

id = get_rt_id(cur, 'Respect "Big" Jack Horner (Puss in Boots: The Last Wish)', 'https://redd.it/116tl6u')
add_data(['Jack Horner'],
'Jack Horner',
False,
False,
[
    ['Puss i?n Boots'], ['The Last Wish']
],
'Puss in Boots',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/116tl6u/respect_big_jack_horner_puss_in_boots_the_last/

########################################

id = get_rt_id(cur, 'Respect Loki, the God of Mischief! (LEGO Marvel)', 'https://redd.it/117hhxy')
add_data(['Loki'],
'Loki',
False,
False,
[
    ['LEGO Marvel']
],
'LEGO Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/117hhxy/respect_loki_the_god_of_mischief_lego_marvel/

########################################

id = get_rt_id(cur, 'Respect Sansfield (Bad Monday Simulator)', 'https://redd.it/117myie')
add_data(['Sansfield'],
'Sansfield',
False,
True,
[
    ['Bad Monday Simulator']
],
'Bad Monday Simulator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/117myie/respect_sansfield_bad_monday_simulator/

########################################

id = get_rt_id(cur, 'Respect Nermal (Bad Monday Simulator)', 'https://redd.it/117np0o')
add_data(['Nermal'],
'Nermal',
False,
False,
[
    ['Bad Monday Simulator']
],
'Bad Monday Simulator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/117np0o/respect_nermal_bad_monday_simulator/

########################################

id = get_rt_id(cur, 'Respect ORT! (TYPE-MOON / Nasuverse)', 'https://redd.it/1184x21')
add_data(['ORT'],
'ORT',
False,
False,
[
    ['TYPE(-| )?MOON'], ['Nasu(-| )?verse']
],
'Nasuverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1184x21/respect_ort_typemoon_nasuverse/

########################################

id = get_rt_id(cur, 'Respect Aesling! (Thrilling Intent)', 'https://redd.it/118dzqd')
add_data(['Aesling'],
'Aesling',
False,
False,
[
    ['Thrilling Intent']
],
'Thrilling Intent',
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

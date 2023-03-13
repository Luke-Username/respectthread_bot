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

update_respectthread(cur, 3892, "Respect Ajimu Najimi, Anshin''in-san! (Medaka Box)", 'https://redd.it/11nmre2')
update_respectthread(cur, 5606, 'Respect Kat (Gravity Rush)', 'https://redd.it/11pf3cm')
update_respectthread(cur, 5607, 'Respect Raven (Gravity Rush)', 'https://redd.it/11pf44b')
update_respectthread(cur, 12409, '(NSFW) Respect Noi (Dorohedoro)', 'https://redd.it/11qb4gf')

########################################

add_data(['White ?beard'],
'Whitebeard',
False,
False,
[
    ['Kaido']
],
'One Piece',
'{4089}'
)
#https://www.reddit.com/r/whowouldwin/comments/11na0wn/dio_vs_whitebeard/

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['\(Animal\)']
],
'Animal',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/11oqjhz/emperor_penguin_vs_wolverine_animal/jbtwkzg/?context=3

########################################

add_data(['Zeus'],
'Zeus',
False,
False,
[
    ['Zeus, DC']
],
'DC',
'{17373}'
)
#https://www.reddit.com/r/whowouldwin/comments/11p92vn/which_saiyan_hybrid_would_be_powerful/jbwocty/?context=3

########################################

id = get_rt_id(cur, 'Respect Caleb (Blood)', 'https://redd.it/11nal83')
add_data(['Caleb'],
'Caleb',
False,
False,
[
    ['Blood']
],
'Blood',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11nal83/respect_caleb_blood/

########################################

id = get_rt_id(cur, 'Respect Tot Musica (One Piece)', 'https://redd.it/11nc4ve')
add_data(['Tot Musica'],
'Tot Musica',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11nc4ve/respect_tot_musica_one_piece/

########################################

id = get_rt_id(cur, 'Respect General Yunan! (Amphibia)', 'https://redd.it/11njy95')
add_data(['Yunan'],
'Yunan',
False,
False,
[
    ['Amphibia']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11njy95/respect_general_yunan_amphibia/

########################################

id = get_rt_id(cur, 'Respect Odin Borson (Marvel: Earth-616)', 'https://redd.it/edec8v')
add_data(['Odin'],
'Odin',
False,
False,
[
    ['Marvel'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/11p92vn/which_saiyan_hybrid_would_be_powerful/
#https://www.reddit.com/r/Jeff_Harrisons/comments/edec8v/respect_odin_borson_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect Lance Sterling (Spies In Disguise)', 'https://redd.it/11o3b4d')
add_data(['Lance Sterling'],
'Lance Sterling',
False,
True,
[
    ['Spies In Disguise']
],
'Spies In Disguise',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11o3b4d/respect_lance_sterling_spies_in_disguise/

########################################

id = get_rt_id(cur, 'Respect Eddie Blake, The Comedian! (Watchmen 2009)', 'https://redd.it/11o3lpd')
add_data(['Comedian'],
'Comedian',
False,
False,
[
    ['Watchmen', '2009']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11o3lpd/respect_eddie_blake_the_comedian_watchmen_2009/

########################################

id = get_rt_id(cur, 'Respect Iihiko Shishime! (Medaka Box)', 'https://redd.it/11ojx4t')
add_data(['Iihiko'],
'Iihiko',
False,
True,
[
    ['Shishime'], ['Medd?aka']
],
'Medaka Box',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ojx4t/respect_iihiko_shishime_medaka_box/

########################################

id = get_rt_id(cur, 'Respect Koga Itami! (Medaka Box)', 'https://redd.it/11pi3nj')
add_data(['Koga Itami|Itami Koga'],
'Koga Itami',
False,
True,
[
    ['Medd?aka']
],
'Medaka Box',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11pi3nj/respect_koga_itami_medaka_box/

########################################

id = get_rt_id(cur, 'Respect Duke Devlin (Yu-Gi-Oh! Anime)', 'https://redd.it/11okc40')
add_data(['Duke Devlin'],
'Duke Devlin',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11okc40/respect_duke_devlin_yugioh_anime/

########################################

id = get_rt_id(cur, 'Respect Zack Thompson, Tech Jacket (Image Comics)', 'https://redd.it/11okfnj')
add_data(['Tech Jacket'],
'Tech Jacket',
False,
True,
[
    ['Image Comics'], ['Invincible']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11okfnj/respect_zack_thompson_tech_jacket_image_comics/

########################################

id = get_rt_id(cur, 'Respect Hal Jordan (Green Lantern: First Flight)', 'https://redd.it/11omnoc')
add_data(['Hal Jordan'],
'Hal Jordan',
False,
False,
[
    ['First Flight']
],
'Green Lantern: First Flight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11omnoc/respect_hal_jordan_green_lantern_first_flight/

########################################

id = get_rt_id(cur, 'Respect Hal Jordan (Green Lantern: First Flight)', 'https://redd.it/11omnoc')
add_data(['Max Cady'],
'Max Cady',
False,
False,
[
    ['1991']
],
'Cape Fear, 1991',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ordzb/respect_max_cady_cape_fear_1991/

########################################

id = get_rt_id(cur, 'Respect Uta (One Piece)', 'https://redd.it/11ougda')
add_data(['Uta'],
'Uta',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ougda/respect_uta_one_piece/

########################################

id = get_rt_id(cur, 'Respect Salazzle (Pokemon Anime)', 'https://redd.it/11oz7q6')
add_data(['Salazzle'],
'Salazzle',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11oz7q6/respect_salazzle_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect The Hammer! (Regular Show)', 'https://redd.it/11ozriv')
add_data(['The Hammer'],
'The Hammer',
False,
False,
[
    ['Regular Show']
],
'Regular Show',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ozriv/respect_the_hammer_regular_show/

########################################

id = get_rt_id(cur, 'Respect N.N.! (Nyaight of the Living Cat)', 'https://redd.it/11p4aiz')
add_data(['N\.N'],
'N.N.',
False,
False,
[
    ['Nyaight of the Living Cat']
],
'Nyaight of the Living Cat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11p4aiz/respect_nn_nyaight_of_the_living_cat/

########################################

id = get_rt_id(cur, 'Respect Blizzard! (Primal Rage)', 'https://redd.it/11ppe8f')
add_data(['Blizzard'],
'Blizzard',
False,
False,
[
    ['Primal Rage']
],
'Primal Rage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ppe8f/respect_blizzard_primal_rage/

########################################

id = get_rt_id(cur, 'Respect Mala Mala Jong! (Xiaolin Showdown)', 'https://redd.it/11q94gl')
add_data(['Mala Mala Jong'],
'Mala Mala Jong',
False,
True,
[
    ['Xiaolin Showdown']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11q94gl/respect_mala_mala_jong_xiaolin_showdown/

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

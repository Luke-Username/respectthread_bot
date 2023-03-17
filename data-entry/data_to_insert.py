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
update_respectthread(cur, 12442, 'Respect Miyakonojou Oudo! (Medaka Box)', 'https://redd.it/11rgx8a')

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

add_data(['King ?pin'],
'Kingpin',
False,
False,
[
    ['King ?pin ?\(Marvel\)']
],
'616',
'{2053}'
)
#https://www.reddit.com/r/whowouldwin/comments/11t4r7i/who_would_win_jack_horner_puss_in_boots_last_wish/jch60no/?context=3

########################################

id = get_rt_id(cur, 'Respect Evangelion Unit 02 (Neon Genesis Evangelion)', 'https://redd.it/cf8sd0')
add_data(['Asuka'],
'Asuka',
False,
False,
[
    ['Evangelion'], ['Langley Sohryu']
],
'Neon Genesis Evangelion',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/cf8sd0/respect_evangelion_unit_02_neon_genesis_evangelion/
#https://www.reddit.com/r/whowouldwin/comments/11st4tp/asuka_evangelion_vs_vegeta_dragon_ball/

add_data(['Eva(ngelion)? Unit 02'],
'Evangelion Unit 02',
False,
True,
[
    ['Evangelion'], ['Asuka']
],
'Neon Genesis Evangelion',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/cf8sd0/respect_evangelion_unit_02_neon_genesis_evangelion/
#https://www.reddit.com/r/whowouldwin/comments/11st4tp/asuka_evangelion_vs_vegeta_dragon_ball/

add_data(['Unit 02'],
'Unit 02',
False,
False,
[
    ['Evangelion'], ['Asuka'], ['Eva units?']
],
'Neon Genesis Evangelion',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/cf8sd0/respect_evangelion_unit_02_neon_genesis_evangelion/
#https://www.reddit.com/r/whowouldwin/comments/11st4tp/asuka_evangelion_vs_vegeta_dragon_ball/

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

id = get_rt_id(cur, 'Respect Joey Wheeler (Yu-Gi-Oh! Anime)', 'https://redd.it/11r42nc')
add_data(['Joey Wheeler'],
'Joey Wheeler',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11r42nc/respect_joey_wheeler_yugioh_anime/

add_data(['Joey'],
'Joey',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11r42nc/respect_joey_wheeler_yugioh_anime/

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

id = get_rt_id(cur, 'Respect Ybgir! (Regular Show)', 'https://redd.it/11qn0ij')
add_data(['Ybgir'],
'Ybgir',
False,
True,
[
    ['Regular Show']
],
'Regular Show',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11qn0ij/respect_ybgir_regular_show/

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

id = get_rt_id(cur, 'Respect Oishi Kawaii (Oishi high school battle)', 'https://redd.it/11qo3br')
add_data(['Oishi Kawaii'],
'Oishi Kawaii',
False,
True,
[
    ['Oishi High School Battle']
],
'Oishi High School Battle',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11qo3br/respect_oishi_kawaii_oishi_high_school_battle/

########################################

id = get_rt_id(cur, 'Respect Sinbad! (Sinbad: Legend of the Seven Seas)', 'https://redd.it/11qpk8l')
add_data(['Sinbad'],
'Sinbad',
False,
False,
[
    ['Legend of the Seven Seas'], ['DreamWorks']
],
'Legend of the Seven Seas',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11qpk8l/respect_sinbad_sinbad_legend_of_the_seven_seas/

########################################

id = get_rt_id(cur, 'Respect Anti-Lad (DC, Pre-Zero Hour)', 'https://redd.it/11r9scy')
add_data(['Anti(-| )Lad'],
'Anti-Lad',
False,
False,
[
    ['Pre(-| )Zero Hour']
],
'Pre-Zero Hour',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11r9scy/respect_antilad_dc_prezero_hour/

add_data(['Anti(-| )Lad'],
'Anti-Lad',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11r9scy/respect_antilad_dc_prezero_hour/

########################################

id = get_rt_id(cur, 'Respect Polyphemus the Cyclops (Greek Mythology)', 'https://redd.it/11rhb4p')
add_data(['Polyphemus'],
'Polyphemus',
False,
True,
[
    ['myth?(ical|olog(y|ical))'], ['The Odyssey']
],
'Greek Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11rhb4p/respect_polyphemus_the_cyclops_greek_mythology/

########################################

id = get_rt_id(cur, "Respect the Dragonzord (Mighty Morphin'' Power Rangers)", 'https://redd.it/11rw1ja')
add_data(['Dragon ?zord'],
'Dragonzord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11rw1ja/respect_the_dragonzord_mighty_morphin_power/

########################################

id = get_rt_id(cur, "Respect the Thunder Megazord (Mighty Morphin'' Power Rangers)", 'https://redd.it/11t4dt8')
add_data(['Thunder Megazord'],
'Thunder Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11t4dt8/respect_the_thunder_megazord_mighty_morphin_power/

########################################

id = get_rt_id(cur, 'Respect John Shaft (Shaft)', 'https://redd.it/11rymzm')
add_data(['John Shaft'],
'John Shaft',
False,
True,
[
    ['\(Shaft\)']
],
'Shaft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11rymzm/respect_john_shaft_shaft/

########################################

id = get_rt_id(cur, 'Respect The Star-Spirit (The Iron Man)', 'https://redd.it/11s7vvn')
add_data(['Star( |-)Spirit'],
'Star Spirit',
False,
False,
[
    ['The Iron Man']
],
'The Iron Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11s7vvn/respect_the_starspirit_the_iron_man/

########################################

id = get_rt_id(cur, 'Respect Ozymandias! (Watchmen 2009)', 'https://redd.it/11sb642')
add_data(['Ozymandias'],
'Ozymandias',
False,
False,
[
    ['Watchmen','2009']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11sb642/respect_ozymandias_watchmen_2009/

########################################

id = get_rt_id(cur, 'Respect the T-600 (Terminator: Salvation timeline)', 'https://redd.it/11tca21')
add_data(['T-600'],
'T-600',
False,
True,
[
    ['Terminator']
],
'Terminator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11tca21/respect_the_t600_terminator_salvation_timeline/

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

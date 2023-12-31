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

update_respectthread(cur, 13262, 'Respect Slappy the Dummy (Goosebumps, Composite)', 'https://redd.it/18ogcrh')
update_respectthread(cur, 4636, 'Respect Bakura (Yu-Gi-Oh! Anime)', 'https://redd.it/18osa91')
update_respectthread(cur, 4632, 'Respect Marik Ishtar (Yu-Gi-Oh! Anime)', 'https://redd.it/18pbv0a')
update_respectthread(cur, 7582, 'Robot Santa Claus (Futurama)', 'https://redd.it/18qioyf')
update_respectthread(cur, 20520, 'Respect Kelsang The Living Typhoon (Avatar: The Kyoshi Novels)', 'https://redd.it/18qp9vc')

########################################

add_data(['Jack'],
'Jack',
False,
False,
[
    ['Nightmare Before Christmas']
],
'The Nightmare Before Christmas',
'{6581}'
)
#https://www.reddit.com/r/whowouldwin/comments/18qg7i0/can_the_grinch_steal_halloween_from_halloween/keuodph/?context=3

########################################

add_data(['Raj'],
'Raj',
False,
False,
[
    ['RRR']
],
'RRR',
'{22656}'
)
#https://www.reddit.com/r/whowouldwin/comments/18p449v/raj_and_bheem_rrr_vs_predator/keljt2k/?context=3

########################################

add_data(['Sans'],
'Sans',
False,
False,
[
    ['Sans,']
],
'Undertale',
'{5501,5498}'
)
#https://www.reddit.com/r/whowouldwin/comments/18npes4/musical_chairs_except/kecbyiv/?context=3

########################################

add_data(['Control Devil'],
'Control Devil',
False,
True,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{15328}'
)
#https://www.reddit.com/r/whowouldwin/comments/18me9xh/everyone_in_the_world_gets_the_powers_of_the/ke3p5er/?context=3

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla: Here There Be Dragons)', 'https://redd.it/18m9l7i')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Here There Be Dragons']
],
'Godzilla: Here There Be Dragons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18m9l7i/respect_godzilla_godzilla_here_there_be_dragons/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Fest Godzilla Short Films)', 'https://redd.it/18mg2x2')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Fest Godzilla']
],
'Fest Godzilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18mg2x2/respect_godzilla_fest_godzilla_short_films/

########################################

id = get_rt_id(cur, 'Respect Trent Fernandez-Mercer, the White Dino Ranger (Power Rangers Dino Thunder)', 'https://redd.it/18mf2v8')
add_data(['White Dino( Thunder)? Ranger'],
'White Dino Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Trent'],
'Trent',
False,
False,
[
    ['(White|Dino) (Thunder)?Ranger']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18mf2v8/respect_trent_fernandezmercer_the_white_dino/

########################################

id = get_rt_id(cur, 'Respect Murray (Gunbrella)', 'https://redd.it/18mr28x')
add_data(['Murray'],
'Murray',
False,
False,
[
    ['Gunbrella']
],
'Gunbrella',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18mr28x/respect_murray_gunbrella/

########################################

id = get_rt_id(cur, "Respect Jennifer Walters, She-Hulk (Fantastic Four: World''s Greatest Heroes)", 'https://redd.it/18n2hd0')
add_data(['She(-| )?Hulk'],
'She-Hulk',
False,
False,
[
    ['Fantastic Four: World''s Greatest Heroes']
],
"Fantastic Four: World''s Greatest Heroes",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gamma 1 & Gamma 2 (Dragon Ball Super - Manga)', 'https://redd.it/18n3bge')
add_data(['Gamma 1 (&|and)( Gamma)? 2'],
'Gamma 1 & Gamma 2',
True,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
"Dragon Ball",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18n3bge/respect_gamma_1_gamma_2_dragon_ball_super_manga/

########################################

id = get_rt_id(cur, 'Santa Claus! (Markiplier Canon)', 'https://redd.it/18qmyxw')
add_data(['Santa Clause?'],
'Santa Claus',
False,
False,
[
    ['Markiplier']
],
"Markiplier",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18qmyxw/santa_claus_markiplier_canon/

########################################

id = get_rt_id(cur, 'Respect Santa Claus (Regular Show)', 'https://redd.it/18qy80m')
add_data(['Santa Clause?'],
'Santa Claus',
False,
False,
[
    ['Regular Show']
],
"Regular Show",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18qy80m/respect_santa_claus_regular_show/

########################################

id = get_rt_id(cur, 'Respect Lunky! (Markiplier Canon)', 'https://redd.it/18o2dfs')
add_data(['Lunky'],
'Lunky',
False,
False,
[
    ['Markiplier']
],
"Markiplier",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18o2dfs/respect_lunky_markiplier_canon/

########################################

id = get_rt_id(cur, 'Respect the Zeo Megazord (Power Rangers Zeo)', 'https://redd.it/18onqzp')
id2 = get_rt_id(cur, 'Respect the Super Zeo Megazord (Power Rangers Zeo)', 'https://redd.it/18onwzu')
add_data(['Zeo Megazord'],
'Zeo Megazord',
False,
True,
[
    ['Power Rangers?']
],
"Power Rangers",
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18onqzp/respect_the_zeo_megazord_power_rangers_zeo/

########################################

id = get_rt_id(cur, "Respect Minh Kwan (Mighty Morphin'' Power Rangers: Once & Always)", 'https://redd.it/18op6bv')
add_data(['Minh Kwan'],
'Minh Kwan',
False,
True,
[
    ['Power Rangers?']
],
"Power Rangers",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18op6bv/respect_minh_kwan_mighty_morphin_power_rangers/

########################################

id = get_rt_id(cur, 'Respect SCP-6289, THE WIZARD. (SCP Foundation)', 'https://redd.it/18osmbc')
add_data(['SCP-6289'],
'SCP ?(-| )? ?6289',
False,
True,
[
    ['THE WIZARD']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-4666, The Yule Man (SCP Foundation)', 'https://redd.it/18pyu9g')
add_data(['SCP-4666'],
'SCP ?(-| )? ?4666',
False,
True,
[
    ['Yule Man']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18pyu9g/respect_scp4666_the_yule_man_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Bvak Bevzenko (Terra Formars Gaiden: Asimov)', 'https://redd.it/18oxy6t')
add_data(['Bvak Bevzenko'],
'Bvak Bevzenko',
False,
True,
[
    ['Terra Formars']
],
'Terra Formars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18oxy6t/respect_bvak_bevzenko_terra_formars_gaiden_asimov/

########################################

id = get_rt_id(cur, 'Respect Musashi Miyamoto, the Ghost Ronin (Marvel Comics)', 'https://redd.it/18p0m56')
add_data(['Miyamoto Musashi|Musashi Miyamoto'],
'Miyamoto Musashi',
False,
False,
[
    ['Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18p0m56/respect_musashi_miyamoto_the_ghost_ronin_marvel/

########################################

id = get_rt_id(cur, 'Respect Halbergoi (Doubutsu Sentai Zyuohger)', 'https://redd.it/18p0z4q')
add_data(['Halbergoi'],
'Halbergoi',
False,
False,
[
    ['Doubutsu Sentai Zyuohger']
],
'Doubutsu Sentai Zyuohger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18p0z4q/respect_halbergoi_doubutsu_sentai_zyuohger/

########################################

id = get_rt_id(cur, 'Respect Gaburio (Doubutsu Sentai Zyuohger)', 'https://redd.it/18p13u2')
add_data(['Gaburio'],
'Gaburio',
False,
False,
[
    ['Doubutsu Sentai Zyuohger']
],
'Doubutsu Sentai Zyuohger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18p13u2/respect_gaburio_doubutsu_sentai_zyuohger/

########################################

id = get_rt_id(cur, 'Respect Proto-Clown (The Tick)', 'https://redd.it/18p17ez')
add_data(['Proto(-| )Clown'],
'Proto-Clown',
False,
False,
[
    ['Tick']
],
'The Tick',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ken! (Barbie (2023))', 'https://redd.it/18p3hpc')
add_data(['Ken'],
'Ken',
False,
False,
[
    ['Barbie', '2023'], ['Barbie Movie']
],
'Barbie, 2023',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18p3hpc/respect_ken_barbie_2023/

########################################

id = get_rt_id(cur, 'Respect Shogo Sasaki! (Final Fantasy: Lost Stranger)', 'https://redd.it/18qqj8r')
add_data(['Shogo Sasaki'],
'Shogo Sasaki',
False,
False,
[
    ['Final Fantasy'], ['Lost Stranger']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18qqj8r/respect_shogo_sasaki_final_fantasy_lost_stranger/

########################################

id = get_rt_id(cur, 'Respect the Magus Sisters! (Final Fantasy: Lost Stranger)', 'https://redd.it/18rdjo0')
add_data(['Magus Sisters'],
'Magus Sisters',
False,
True,
[
    ['Final Fantasy'], ['Lost Stranger']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18rdjo0/respect_the_magus_sisters_final_fantasy_lost/

########################################

id = get_rt_id(cur, 'Respect Son-O Miyazawa (Tough)', 'https://redd.it/18rervv')
add_data(['Son(-| )O Miyazawa'],
'Son-O Miyazawa',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18rervv/respect_sono_miyazawa_tough/

########################################

id = get_rt_id(cur, 'Respect Gill! (Ice-Head Gill)', 'https://redd.it/18sa61l')
add_data(['Gill'],
'Gill',
False,
False,
[
    ['Ice(-| )Head Gill'], ['Gill Sol']
],
'Ice-Head Gill',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18sa61l/respect_gill_icehead_gill/

########################################

id = get_rt_id(cur, 'Respect Akira Tendo (Zom 100: Bucket List of the Dead)', 'https://redd.it/18skdjs')
add_data(['Akira Tendou?'],
'Akira Tendou',
False,
True,
[
    ['Zom(bie)? 100']
],
'Zom 100: Bucket List of the Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18skdjs/respect_akira_tendo_zom_100_bucket_list_of_the/

########################################

id = get_rt_id(cur, 'Respect the Zombie Bucket List Gang (Zom 100: Bucket List of the Dead)', 'https://redd.it/18skecr')
add_data(['Zombie Bucket List Gang'],
'Zombie Bucket List Gang',
True,
True,
[
    ['Zom(bie)? 100']
],
'Zom 100: Bucket List of the Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18skecr/respect_the_zombie_bucket_list_gang_zom_100/

add_data(['Shizuka Mikazuki'],
'Shizuka Mikazuki',
False,
False,
[
    ['Zom(bie)? 100']
],
'Zom 100: Bucket List of the Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18skecr/respect_the_zombie_bucket_list_gang_zom_100/

add_data(['Beatrix Amerhauser'],
'Beatrix Amerhauser',
False,
True,
[
    ['Zom(bie)? 100']
],
'Zom 100: Bucket List of the Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18skecr/respect_the_zombie_bucket_list_gang_zom_100/

########################################

id = get_rt_id(cur, 'Respect "P-3" Major Sergey Nechayev (Atomic Heart)', 'https://redd.it/18t52jl')
add_data(['P-3'],
'P-3',
False,
False,
[
    ['Atomic Heart']
],
'Atomic Heart',
'{' + '{}'.format(id) + '}'
)
#

add_data(['P3'],
'P3',
False,
False,
[
    ['Atomic Heart']
],
'Atomic Heart',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Predators (Predator If It Bleeds)', 'https://redd.it/18tt33b')
add_data(['Predators'],
'Predators',
False,
False,
[
    ['Predator:? If It Bleeds']
],
'Predator: If It Bleeds',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18tt33b/respect_the_predators_predator_if_it_bleeds/

add_data(['Predator'],
'Predator',
False,
False,
[
    ['Predator:? If It Bleeds']
],
'Predator: If It Bleeds',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18tt33b/respect_the_predators_predator_if_it_bleeds/

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

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

update_respectthread(cur, 591, "Respect Venom (Sony''s Spider-Man Universe)", 'https://redd.it/zbiboj')
update_respectthread(cur, 5735, "Respect Kenny (Telltale''s The Walking Dead Game)", 'https://redd.it/zbwl44')

########################################

id = get_rt_id(cur, 'Respect Thor, The Destroyer (God of War)', 'https://redd.it/zdcr1j')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['God of War']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/zbffpw/god_of_war_ragnarok_thor_vs_kratos_arm_wrestle/iyrgyv2/?context=3

########################################

add_data(['Betsy Braddock'],
'Betsy Braddock',
False,
True,
[
    ['616']
],
'616',
'{2380}'
)
#https://www.reddit.com/r/whowouldwin/comments/zb530m/captain_britain_betsy_braddock_vs_magik_616/iyqiqfl/?context=3

########################################

id = get_rt_id(cur, 'Respect Manny (Swiss Army Man)', 'https://redd.it/zayl6i')
add_data(['Manny'],
'Manny',
False,
False,
[
    ['Swiss Army Man']
],
'Swiss Army Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zayl6i/respect_manny_swiss_army_man/

########################################

id = get_rt_id(cur, 'Respect: Phantom Superman! (Pre-Crisis DC Comics)', 'https://redd.it/zb0uek')
add_data(['Super(-| )?man'],
'Phantom Superman',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zayl6i/respect_manny_swiss_army_man/

########################################

id = get_rt_id(cur, 'Respect Air Man! (Mega Man)', 'https://redd.it/zb21wq')
add_data(['Air Man'],
'Air Man',
False,
False,
[
    ['Mega ?Man'], ['Air ?man ga Taosenai']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Yellow Devil (Mega Man)', 'https://redd.it/zb4f4t')
add_data(['Yellow Devil'],
'Yellow Devil',
False,
True,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zb4f4t/respect_the_yellow_devil_mega_man/

########################################

id = get_rt_id(cur, 'Respect Guts Man! (Mega Man)', 'https://redd.it/zc319r')
add_data(['Guts Man'],
'Guts Man',
False,
True,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zc319r/respect_guts_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Needle Man (Mega Man)', 'https://redd.it/zco44s')
add_data(['Needle Man'],
'Needle Man',
False,
True,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Terra! (Mega Man V)', 'https://redd.it/zcrz8t')
add_data(['Terra'],
'Terra',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcrz8t/respect_terra_mega_man_v/

########################################

id = get_rt_id(cur, 'Respect Sunstar! (Mega Man V)', 'https://redd.it/zcs91t')
add_data(['Sunstar'],
'Sunstar',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcs91t/respect_sunstar_mega_man_v/

########################################

id = get_rt_id(cur, "Respect Riot (Sony''s Spider-Man Universe)", 'https://redd.it/zbicjk')
add_data(['Riot'],
'Riot',
False,
False,
[
    ['Riot ?\(Sonys?'], ['Carnage', '\(Sony\)']
],
'Sony',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbicjk/respect_riot_sonys_spiderman_universe/

########################################

id = get_rt_id(cur, "Respect Carnage (Sony''s Spider-Man Universe)", 'https://redd.it/zbid67')
add_data(['Carnage'],
'Carnage',
False,
False,
[
    ['Carnage ?\(Sonys?'], ['Riot', '\(Sony\)'], ['Let There Be Carnage'], ['Venom 2'], ['LTBC']
],
'Sony',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbid67/respect_carnage_sonys_spiderman_universe/

########################################

id = get_rt_id(cur, 'Respect Frances Barrison, Shriek (Venom: Let There Be Carnage)', 'https://redd.it/zcaloa')
add_data(['Frances Barrison'],
'Frances Barrison',
False,
False,
[
    ['Sonys?']
],
'Sony',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcaloa/respect_frances_barrison_shriek_venom_let_there/

########################################

id = get_rt_id(cur, 'Respect Mori Nagayoshi! (Fate)', 'https://redd.it/zbqssj')
add_data(['Mori Nagayoshi'],
'Mori Nagayoshi',
False,
True,
[
    ['Fate ?verse']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbqssj/respect_mori_nagayoshi_fate/

########################################

id = get_rt_id(cur, 'Respect the Seven Ghosts (Claymore)', 'https://redd.it/zbr5ax')
add_data(['(Seven|7) Ghosts'],
'Seven Ghosts',
True,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbr5ax/respect_the_seven_ghosts_claymore/

########################################

id = get_rt_id(cur, "Respect Spa''ark, the Death Ranger! (Mighty Morphin'' Power Rangers [BOOM! Studios])", 'https://redd.it/zbt4x1')
add_data(["Spa''ark"],
"Spa''ark",
False,
True,
[
    ['Power Rangers?'], ['BOOM!? Studios?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbt4x1/respect_spaark_the_death_ranger_mighty_morphin/

########################################

id = get_rt_id(cur, 'Respect Naruo (Speedboy!)', 'https://redd.it/zbvnqs')
add_data(['Naruo'],
'Naruo',
False,
False,
[
    ['Speedboy']
],
'Speedboy!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zbvnqs/respect_naruo_speedboy/

########################################

id = get_rt_id(cur, 'Respect Balls (Speedboy!)', 'https://redd.it/zbvo8k')
add_data(['Balls'],
'Balls',
False,
False,
[
    ['Speedboy']
],
'Speedboy!',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Bugsy (Pokemon Anime)', 'https://redd.it/zc9hk6')
add_data(['Bugsy'],
'Bugsy',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zc9hk6/respect_bugsy_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Captain Smiley (Comic Jumper)', 'https://redd.it/zcah87')
add_data(['Captain Smiley'],
'Captain Smiley',
False,
True,
[
    ['Comic Jumper']
],
'Comic Jumper',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcah87/respect_captain_smiley_comic_jumper/

########################################

id = get_rt_id(cur, 'Respect Sukapon (Super Smash Bros.)', 'https://redd.it/zcm83r')
add_data(['Sukapon'],
'Sukapon',
False,
False,
[
    ['Smash (Bro(ther)?s?|Ultimate)']
],
'Super Smash Bros',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcm83r/respect_sukapon_super_smash_bros/

########################################

id = get_rt_id(cur, 'Respect John Constantine (Constantine 2005)', 'https://redd.it/zcv919')
add_data(['John Constantine'],
'John Constantine',
False,
False,
[
    ['2005']
],
'2005',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zcv919/respect_john_constantine_constantine_2005/

########################################

id = get_rt_id(cur, 'Respect the Herald (Fortnite)', 'https://redd.it/zcvi8x')
add_data(['Herald'],
'Herald',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Martial Artist (Sifu)', 'https://redd.it/zd77ay')
add_data(['Martial Artist'],
'Martial Artist',
False,
False,
[
    ['Sifu']
],
'Sifu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zd77ay/respect_the_martial_artist_sifu/

add_data(['Sifu'],
'Sifu',
False,
False,
[
    ['Sifu ?\(Sifu'], ['Sifu protagonist']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zd77ay/respect_the_martial_artist_sifu/

add_data(['The Child'],
'The Child',
False,
False,
[
    ['Sifu']
],
'Sifu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zd77ay/respect_the_martial_artist_sifu/


########################################

id = get_rt_id(cur, 'Respect: Smash! (Image Comics)', 'https://redd.it/zdakm4')
add_data(['Smash'],
'Smash',
False,
False,
[
    ['Image Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zdakm4/respect_smash_image_comics/


########################################

id = get_rt_id(cur, 'Respect Django! (Django)', 'https://redd.it/zdm8nh')
add_data(['Django'],
'Django',
False,
True,
[
    ['Django ?\(Django']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zdm8nh/respect_django_django/


########################################

id = get_rt_id(cur, 'Respect Orphan (Young Justice)', 'https://redd.it/zdobjd')
add_data(['Orphan'],
'Orphan',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zdobjd/respect_orphan_young_justice/

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

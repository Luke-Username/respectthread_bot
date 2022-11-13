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

add_data(['Zod'],
'General Zod',
False,
False,
[
    ['Avruskin']
],
'Avruskin',
'{22523}'
)
#https://www.reddit.com/r/respectthreads/comments/yrm4xs/respect_general_zod_dc_postcrisis/
#https://www.reddit.com/r/respectthreads/comments/wwzdga/respect_general_zod_avruskin_dc_postcrisis/

########################################

add_data(['Avengers'],
'Avengers',
True,
False,
[
    ['2012 Avengers']
],
'MCU',
'{233,247,237,264,236,244,235,270,268,242,271,256}'
)
#https://www.reddit.com/r/whowouldwin/comments/yqidsq/the_2012_avengers_vs_taika_waititis_superhero/ivoev1m/?context=3

########################################

add_data(['Homer'],
'Homer',
False,
False,
[
    ['Simpsons'], ['Shaggy', 'eating']
],
'The Simpsons',
'{20516}'
)
#https://www.reddit.com/r/whowouldwin/comments/ypshzx/homer_vs_shaggy_in_an_all_you_can_eat_buffet/ivkqkdn/?context=3

########################################

add_data(['Endeavou?r'],
'Endeavor',
False,
False,
[
    ['Ozai'], ['Peak Endeavou?r']
],
'My Hero Academia',
'{3920}'
)
#https://www.reddit.com/r/whowouldwin/comments/yq50vr/peak_endeavor_vs_phoenix_king_ozai/ivmzz1g/?context=3

########################################

id = get_rt_id(cur, 'Respect Snap (ChalkZone)', 'https://redd.it/ypn2ha')
add_data(['Snap'],
'Snap',
False,
False,
[
    ['Chalk ?Zone']
],
'ChalkZone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ypn2ha/respect_snap_chalkzone/

########################################

id = get_rt_id(cur, 'Respect Rudy Tabootie (ChalkZone)', 'https://redd.it/yomaci')
add_data(['Rudy Tabootie'],
'Rudy Tabootie',
False,
True,
[
    ['Chalk ?Zone']
],
'ChalkZone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yomaci/respect_rudy_tabootie_chalkzone/

add_data(['Rudy'],
'Rudy',
False,
False,
[
    ['Chalk ?Zone']
],
'ChalkZone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yomaci/respect_rudy_tabootie_chalkzone/

########################################

id = get_rt_id(cur, 'Respect: Shadow Supreme! (Image Comics)', 'https://redd.it/yowq62')
add_data(['Shadow Supreme'],
'Shadow Supreme',
False,
False,
[
    ['Image'], ['Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yowq62/respect_shadow_supreme_image_comics/

########################################

id = get_rt_id(cur, 'Respect "Winged" Anastasia, Number 7 (Claymore)', 'https://redd.it/yoxiiq')
add_data(['Anastasia'],
'Anastasia',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yoxiiq/respect_winged_anastasia_number_7_claymore/

########################################

id = get_rt_id(cur, 'Respect Clarice and Miata (Claymore)', 'https://redd.it/ysbckn')
add_data(['Miata'],
'Miata',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ysbckn/respect_clarice_and_miata_claymore/

add_data(['Clarice'],
'Clarice',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ysbckn/respect_clarice_and_miata_claymore/

########################################

id = get_rt_id(cur, 'Respect "Quicksword" Ilena (Claymore)', 'https://redd.it/ypx9be')
add_data(['Ilena'],
'Ilena',
False,
False,
[
    ['Claymore']
],
'Claymore',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ypx9be/respect_quicksword_ilena_claymore/

########################################

id = get_rt_id(cur, 'Respect the Teenage Mutant Ninja Turtles (Batman vs Teenage Mutant Ninja Turtles)', 'https://redd.it/yp82wi')
add_data(['TMNT'],
'Teenage Mutant Ninja Turtles',
True,
False,
[
    ['Batman', 'Teenaged? Mutant Ninja Turtles'], ['Batman', 'TMNT']
],
'Batman vs. Teenage Mutant Ninja Turtles',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yp82wi/respect_the_teenage_mutant_ninja_turtles_batman/

########################################

id = get_rt_id(cur, 'Respect Lynels! (The Legend of Zelda: Breath of the Wild)', 'https://redd.it/ypa4dw')
add_data(['Lynels?'],
'Lynels',
False,
False,
[
    ['Breath of the Wild'], ['BOTW']
],
'Breath of the Wild',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ypa4dw/respect_lynels_the_legend_of_zelda_breath_of_the/

########################################

id = get_rt_id(cur, 'Respect Colonel Miles Quaritch (Avatar)', 'https://redd.it/ypvbi9')
add_data(['Quaritch'],
'Quaritch',
False,
False,
[
    ['AMP'], ['Avatar']
],
'Avatar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ypvbi9/respect_colonel_miles_quaritch_avatar/

add_data(['(Colonel|Miles) Quaritch'],
'Colonel Miles Quaritch',
False,
True,
[
    ['AMP'], ['Avatar']
],
'Avatar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ypvbi9/respect_colonel_miles_quaritch_avatar/

########################################

id = get_rt_id(cur, "Respect Kenji Miyashiro (Amazon''s The Boys)", 'https://redd.it/yq76iu')
add_data(['Kenji Miyashiro'],
'Kenji Miyashiro',
False,
True,
[
    ['The Boys']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yq76iu/respect_kenji_miyashiro_amazons_the_boys/

add_data(['Kenji'],
'Kenji',
False,
False,
[
    ['The Boys']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yq76iu/respect_kenji_miyashiro_amazons_the_boys/

########################################

id = get_rt_id(cur, 'Respect Catboy Jerma (Jerma985)', 'https://redd.it/ysvert')
add_data(['Catboy Jerma(985)?'],
'Catboy Jerma',
False,
True,
[
    ['Jerma985']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ysvert/respect_catboy_jerma_jerma985/

########################################

id = get_rt_id(cur, 'Peep the Horror (Jerma985)', 'https://redd.it/ysvocx')
add_data(['The Horror'],
'The Horror',
False,
False,
[
    ['Jerma985']
],
'Jerma985',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ysvocx/peep_the_horror_jerma985/

########################################

id = get_rt_id(cur, 'Respect Gaia (Baki)', 'https://redd.it/ytc3w1')
add_data(['Gaia'],
'Gaia',
False,
False,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ytc3w1/respect_gaia_baki/

########################################

id = get_rt_id(cur, 'Respect Angelica Longrider (Swamp Angel)', 'https://redd.it/ytdeal')
add_data(['Angelica Longrider'],
'Angelica Longrider',
False,
True,
[
    ['Swamp Angel']
],
'Swamp Angel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ytdeal/respect_angelica_longrider_swamp_angel/

########################################

id = get_rt_id(cur, 'Respect Bahumat! (Fablehaven)', 'https://redd.it/ytzgvo')
add_data(['Bahumat'],
'Bahumat',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ytzgvo/respect_bahumat_fablehaven/

########################################

id = get_rt_id(cur, 'Respect the Revenant of Fablehaven! (Fablehaven)', 'https://redd.it/yu0dnm')
add_data(['Revenant'],
'Revenant',
False,
False,
[
    ['Fablehaven']
],
'Fablehaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/yu0dnm/respect_the_revenant_of_fablehaven_fablehaven/

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

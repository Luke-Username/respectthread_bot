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

update_respectthread(cur, 7544, 'Respect Kokushibo, Upper Moon One (Kimetsu no Yaiba)', 'https://redd.it/ude3zn')
update_respectthread(cur, 3475, 'Respect Alexander Anderson (Hellsing)', 'https://redd.it/uf2cxo')

########################################

add_data(['Josuke'],
'Josuke Higashikata',
False,
False,
[
    ['Soft (&|and) Wet']
],
'Part 8',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/ud2sfm/could_josukes_soft_and_wet_bypass_gojos_limitless/

########################################

add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['(Novel|Book) Dracula']
],
'Bram Stoker',
'{6142}'
)
#https://www.reddit.com/r/whowouldwin/comments/ud2fko/blade_runs_a_vampire_killing_gauntlet_who_does_he/i6e5kl7/?context=3

########################################

add_data(['Death(-| )?stroke'],
'Deathstroke',
False,
False,
[
    ['Teen Titans', '2003']
],
'Teen Titans',
'{974}'
)
#https://www.reddit.com/r/whowouldwin/comments/uea9xw/the_batman_2004_vs_deathstroke_teen_titans_2003/i6n0d1d/?context=3

########################################

id = get_rt_id(cur, 'Respect Super Dinosaur (Super Dinosaur)', 'https://redd.it/ubxw9a')
add_data(['Super Dinosaur'],
'Super Dinosaur',
False,
False,
[
    ['Super Dinosaur.*Super Dinosaur']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ubxw9a/respect_super_dinosaur_super_dinosaur/

########################################

id = get_rt_id(cur, 'Respect Hex! (Ben 10 Classic)', 'https://redd.it/uce280')
add_data(['Hex'],
'Hex',
False,
False,
[
    ['Ben (10|Ten(nyson)?)']
],
'Ben 10',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uce280/respect_hex_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect: Superior! (from Mark Millar''s comic Superior)", 'https://redd.it/ucfq03')
add_data(['Superior'],
'Superior',
False,
False,
[
    ['Mark Millar']
],
'Mark Millar',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ucfq03/respect_superior_from_mark_millars_comic_superior/

########################################

id = get_rt_id(cur, 'Respect Ethan Avery, Damage (DC, Rebirth)', 'https://redd.it/ucg82q')
add_data(['Damage'],
'Damage',
False,
False,
[
    ['Ethan Avery']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ucg82q/respect_ethan_avery_damage_dc_rebirth/

########################################

id = get_rt_id(cur, 'Respect Mr. Worth (DC, Rebirth)', 'https://redd.it/ud4gdn')
add_data(['Mr\.? Worth'],
'Mr. Worth',
False,
False,
[
    ['Prime(-| )Earth'], ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud4gdn/respect_mr_worth_dc_rebirth/

add_data(['Mr\.? Worth'],
'Mr. Worth',
False,
False,
[
    ['DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud4gdn/respect_mr_worth_dc_rebirth/

########################################

id = get_rt_id(cur, 'Respect Atalanta, The Greek Huntress (Fate)', 'https://redd.it/ucn64o')
add_data(['Atalanta'],
'Atalanta',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ucn64o/respect_atalanta_the_greek_huntress_fate/

########################################

id = get_rt_id(cur, 'Respect the Chosen (XCOM 2: War of the Chosen)', 'https://redd.it/ud8m00')
add_data(['The Chosen'],
'The Chosen',
True,
False,
[
    ['XCOM2?']
],
'XCOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud8m00/respect_the_chosen_xcom_2_war_of_the_chosen/

add_data(['Chosen'],
'Chosen',
True,
False,
[
    ['XCOM ?2']
],
'XCOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud8m00/respect_the_chosen_xcom_2_war_of_the_chosen/

add_data(['The Assassin'],
'The Assassin',
False,
False,
[
    ['XCOM2?']
],
'XCOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud8m00/respect_the_chosen_xcom_2_war_of_the_chosen/

add_data(['The Hunter'],
'The Hunter',
False,
False,
[
    ['XCOM2?']
],
'XCOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud8m00/respect_the_chosen_xcom_2_war_of_the_chosen/

add_data(['The Warlock'],
'The Warlock',
False,
False,
[
    ['XCOM2?']
],
'XCOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ud8m00/respect_the_chosen_xcom_2_war_of_the_chosen/

########################################

id = get_rt_id(cur, 'Respect Yuta Okkotsu and Rika (Jujutsu Kaisen)', 'https://redd.it/uddrdy')
add_data(['Yuta'],
'Yuta',
False,
False,
[
    ['Okkotsu'], ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uddrdy/respect_yuta_okkotsu_and_rika_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Ryu Ishigori (Jujutsu Kaisen)', 'https://redd.it/udds27')
add_data(['Ryu Ishigori|Ishigori Ryu'],
'Ryu Ishigori',
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/udds27/respect_ryu_ishigori_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Finn (Star Wars) feat repository', 'https://redd.it/657ysg')
id2 = get_rt_id(cur, 'Star Wars: Finn Respect Thread', 'https://comicvine.gamespot.com/forums/star-wars-universe-1943200/star-wars-finn-respect-thread-1756815/')
add_data(['Finn'],
'Finn',
False,
False,
[
    ['S(tar )?Wars'], ['Rey', 'Kylo|ROS|Poe|Force'], ['Rise of Skywalker']
],
'Star Wars',
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/udunn5/finn_star_wars_vs_okoye_mcu/

########################################

id = get_rt_id(cur, 'Respect Princess Daisy! (Super Smash Bros.)', 'https://redd.it/udr16s')
add_data(['Princess Daisy'],
'Princess Daisy',
False,
False,
[
    ['Smash (Bro(ther)?s?|Ultimate)'], ['SSBB']
],
'Super Smash Bros',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/udr16s/respect_princess_daisy_super_smash_bros/

########################################

id = get_rt_id(cur, 'Respect Nerd Hulk (Marvel, 1610)', 'https://redd.it/udvusz')
add_data(['Nerd Hulk'],
'Nerd Hulk',
False,
True,
[
    ['1610']
],
'1610',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/udvusz/respect_nerd_hulk_marvel_1610/

########################################

id = get_rt_id(cur, 'Respect: Dynasty! (Lone Star Press)', 'https://redd.it/ue0hzh')
add_data(['Dynasty'],
'Dynasty',
False,
False,
[
    ['Lone Star Press'], ['Dynasty.*Pantheon']
],
'Lone Star Press',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue0hzh/respect_dynasty_lone_star_press/

########################################

id = get_rt_id(cur, 'Respect Tangtong (Dragon Boy)', 'https://redd.it/ue123w')
add_data(['Tangtong'],
'Tangtong',
False,
False,
[
    ['Dragon Boy']
],
'Dragon Boy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue123w/respect_tangtong_dragon_boy/

########################################

id = get_rt_id(cur, 'Respect Bumblebee (DC Super Hero Girls)', 'https://redd.it/ue88ry')
add_data(['Bumblebee'],
'Bumblebee',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue88ry/respect_bumblebee_dc_super_hero_girls/

########################################

id = get_rt_id(cur, 'Respect Zatanna (DC Super Hero Girls)', 'https://redd.it/ue8xf0')
add_data(['Zatanna'],
'Zatanna',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue8xf0/respect_zatanna_dc_super_hero_girls/

########################################

id = get_rt_id(cur, 'Respect Batgirl (DC Super Hero Girls)', 'https://redd.it/ue94cs')
add_data(['Batgirl'],
'Batgirl',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Supergirl (DC Super Hero Girls)', 'https://redd.it/ue9nwf')
add_data(['Supergirl'],
'Supergirl',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue9nwf/respect_supergirl_dc_super_hero_girls/

########################################

id = get_rt_id(cur, 'Respect Wonder Woman (DC Super Hero Girls)', 'https://redd.it/ue9wyz')
add_data(['Wonder ?Woman'],
'Wonder Woman',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue9wyz/respect_wonder_woman_dc_super_hero_girls/

########################################

id = get_rt_id(cur, 'Respect Green Lantern (DC Super Hero Girls)', 'https://redd.it/ue8l5d')
add_data(['Green Lantern'],
'Green Lantern',
False,
False,
[
    ['DC Super Hero Girls']
],
'DC Super Hero Girls',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue8l5d/respect_green_lantern_dc_super_hero_girls/

########################################

id = get_rt_id(cur, 'Respect The Ronin (Teenage Mutant Ninja Turtles: The Last Ronin)', 'https://redd.it/ue8iuk')
add_data(['Michelangelo'],
'Michelangelo',
False,
False,
[
    ['Ronin']
],
'The Last Ronin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ue8iuk/respect_the_ronin_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Wilson Fisk, the Kingpin (Marvel Cinematic Universe)', 'https://redd.it/uemrsc')
add_data(['Wilson Fisk'],
'Wilson Fisk',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uemrsc/respect_wilson_fisk_the_kingpin_marvel_cinematic/

add_data(['King ?pin'],
'Kingpin',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uemrsc/respect_wilson_fisk_the_kingpin_marvel_cinematic/

########################################

id = get_rt_id(cur, 'Respect Rojo (Ben 10 Classic)', 'https://redd.it/uf058p')
add_data(['Rojo'],
'Rojo',
False,
False,
[
    ['Ben (10|Ten(nyson)?)']
],
'Ben 10',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uf058p/respect_rojo_ben_10_classic/

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

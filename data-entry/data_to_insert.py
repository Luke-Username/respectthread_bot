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

update_respectthread(cur, 5250, 'Respect Senator Steven Armstrong! (Metal Gear)', 'https://redd.it/vqvd8t')

########################################

add_data(['Steve'],
'Steve',
False,
False,
[
    ['Steve with commands?']
],
'Minecraft',
'{5648, 5647}'
)
#

########################################

add_data(['Queen Maeve'],
'Queen Maeve',
False,
False,
[
    ['Black Noir']
],
'The Boys',
'{13595}'
)
#https://www.reddit.com/r/whowouldwin/comments/vqvimw/soldier_boy_vs_black_noir_queen_maeve_atrain_and/ierm0nl/?context=3

########################################

id = get_rt_id(cur, 'Respect Europa! (Fate)', 'https://redd.it/vqk24k')
add_data(['Europa'],
'Europa',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vqk24k/respect_europa_fate/

########################################

id = get_rt_id(cur, 'Respect Sun-Hee (The Boys Presents: Diabolical)', 'https://redd.it/vqqjc6')
add_data(['Sun(-| )Hee'],
'Sun-Hee',
False,
False,
[
    ['The Boys']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect R. Dorothy Wayneright (The Big O)', 'https://redd.it/vqs7ss')
add_data(['Dorothy Wayneright'],
'Dorothy Wayneright',
False,
True,
[
    ['Big(-| )O']
],
'The Big O',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vqs7ss/respect_r_dorothy_wayneright_the_big_o/

########################################

id = get_rt_id(cur, 'Respect Baiken (Character Scramble)', 'https://redd.it/vqvaw2')
add_data(['Baiken'],
'Baiken',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vqvaw2/respect_baiken_character_scramble/

########################################

id = get_rt_id(cur, 'Respect Carolina (Character Scramble)', 'https://redd.it/vr3wjf')
add_data(['Carolina'],
'Carolina',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Fall Barros (Character Scramble)', 'https://redd.it/vrum59')
add_data(['Fall Barros'],
'Fall Barros',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrum59/respect_fall_barros_character_scramble/

########################################

id = get_rt_id(cur, 'Respect Captain Marvel (Marvel Cinematic Universe: What If...?)', 'https://redd.it/vr0icz')
add_data(['Captain Marvel'],
'Captain Marvel',
False,
False,
[
    ['What If']
],
'What if...?',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr0icz/respect_captain_marvel_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Guile! (Udon Comics Street Fighter)', 'https://redd.it/vr5hp1')
add_data(['Guile'],
'Guile',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr5hp1/respect_guile_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Roberta Mendez, Captain America 2099 (Marvel, Earth-23291)', 'https://redd.it/vr5rzy')
add_data(['Capt(ai|ia)n America 2099'],
'Captain America 2099',
False,
True,
[
    ['23291']
],
'23291',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr5rzy/respect_roberta_mendez_captain_america_2099/

add_data(['Roberta Mendez'],
'Roberta Mendez',
False,
True,
[
    ['23291']
],
'23291',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr5rzy/respect_roberta_mendez_captain_america_2099/

########################################

id = get_rt_id(cur, 'Respect Captain America, The Thing from Another Time (Marvel, Earth-44921)', 'https://redd.it/vrl0ul')
add_data(['Capt(ai|ia)n America'],
'Captain America',
False,
False,
[
    ['44921'], ['Thing from Another Time']
],
'The Thing from Another Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrl0ul/respect_captain_america_the_thing_from_another/

########################################

id = get_rt_id(cur, 'Respect Ryu Hanbin (Latna Saga: Survival of a Sword King)', 'https://redd.it/vr7n62')
add_data(['Ryu Han(-| )?bin'],
'Ryu Han-bin',
False,
True,
[
    ['Latna Saga'], ['Survival of a Sword King']
],
'Survival of a Sword King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Soldier Boy (Amazon''s The Boys)", 'https://redd.it/vr93dt')
add_data(['Soldier Boy'],
'Soldier Boy',
False,
False,
[
    ['The Boys'], ['MCU'], ['Homelander']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr93dt/respect_soldier_boy_amazons_the_boys/

########################################

id = get_rt_id(cur, 'Respect Benjamin Franklin! (Ben 10 Franklin)', 'https://redd.it/vr9zv6')
add_data(['Ben 10 Franklin'],
'Ben 10 Franklin',
False,
True,
[
    ['MAD']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vr9zv6/respect_benjamin_franklin_ben_10_franklin/

########################################

id = get_rt_id(cur, 'Respect George Washington, Citizen Soldier (WildStorm)', 'https://redd.it/vrcfzb')
add_data(['George Washington'],
'George Washington',
False,
False,
[
    ['WildStorm']
],
'WildStorm',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrcfzb/respect_george_washington_citizen_soldier/

########################################

id = get_rt_id(cur, "Respect General Steel''s H.M.E.R (Sym-Bionic Titan)", 'https://redd.it/vrcnfq')
add_data(['H\.M\.E\.R'],
'H.M.E.R',
False,
False,
[
    ['Sym(-| )?Bionic Titan'], ['General Steels?']
],
'Sym-Bionic Titan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrcnfq/respect_general_steels_hmer_symbionic_titan/

########################################

id = get_rt_id(cur, 'Respect General Washingtoad (The Super Mario Bros. Super Show!)', 'https://redd.it/vre97o')
add_data(['General Washingtoad'],
'General Washingtoad',
False,
True,
[
    ['Super Mario Brothers Super Show']
],
'Super Mario Brothers Super Show!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vre97o/respect_general_washingtoad_the_super_mario_bros/

########################################

id = get_rt_id(cur, 'Respect Goldlewis Dickinson! (Guilty Gear)', 'https://redd.it/vrgo8g')
add_data(['Goldlewis Dickinson'],
'Goldlewis Dickinson',
False,
True,
[
    ['Guilty Gear']
],
'Guilty Gear',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrgo8g/respect_goldlewis_dickinson_guilty_gear/

########################################

id = get_rt_id(cur, 'Respect Nikaido! (Dorohedoro)', 'https://redd.it/vrlafl')
add_data(['Nikaido'],
'Nikaido',
False,
False,
[
    ['Dorohedoro']
],
'Dorohedoro',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrlafl/respect_nikaido_dorohedoro/

########################################

id = get_rt_id(cur, 'Respect John Grimm (Doom [2005 Film])', 'https://redd.it/vrspg4')
add_data(['John Grimm'],
'John Grimm',
False,
False,
[
    ['Doom ?\(2005 film']
],
'Doom [2005 Film]',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrspg4/respect_john_grimm_doom_2005_film/

add_data(['John "Reaper" Grimm'],
'John "Reaper" Grimm',
False,
False,
[
    ['Doom', '2005']
],
'Doom [2005 Film]',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vrspg4/respect_john_grimm_doom_2005_film/

########################################

id = get_rt_id(cur, 'Respect Neon White (Neon White)', 'https://redd.it/vs9vkt')
add_data(['Neon White'],
'Neon White',
False,
True,
[
    ['Neon White ?\(Neon White']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vs9vkt/respect_neon_white_neon_white/

########################################

id = get_rt_id(cur, 'Respect Herbie Popnecker (Herbie)', 'https://redd.it/vsagk7')
add_data(['Herbie Popnecker'],
'Herbie Popnecker',
False,
True,
[
    ['Herbie Popnecker ?\(Herbie']
],
'Herbie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vsagk7/respect_herbie_popnecker_herbie/

########################################

id = get_rt_id(cur, 'Respect the "Merciless Demon" Kyouichirou Sabu (Grappler Baki)', 'https://redd.it/vsc4a9')
add_data(['Kyouichirou Sabu'],
'Kyouichirou Sabu',
False,
True,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vsc4a9/respect_the_merciless_demon_kyouichirou_sabu/

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

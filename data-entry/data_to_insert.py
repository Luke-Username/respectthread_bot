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

update_respectthread(cur, 15348, 'Respect Kairi Shishigou! (Fate)', 'https://redd.it/td701q')

########################################

add_data(['(Seven|7) Homuncul(i|us)'],
'Seven Homunculi',
True,
True,
[
    ['Full ?metal'], ['FMA:?B?']
],
'Fullmetal Alchemist',
'{3411, 3410, 9297, 3407, 9301, 3406, 12495, 3422, 3414, 9300, 13608, 9292}'
)
#https://www.reddit.com/r/whowouldwin/comments/tcgnl1/the_seven_homunculi_fmab_vs_voldemorts_horcruxes/i0dkp5f/?context=3

########################################

add_data(['The Thing'],
'The Thing',
False,
False,
[
    ['The Thing.*vs\.? The Thing']
],
'John Carpenter',
'{14803}'
)
#https://www.reddit.com/r/whowouldwin/comments/td269w/impostor_vs_the_thing_among_us_vs_the_thing/i0h331n/?context=3

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Christian Bale']
],
'Nolanverse',
'{6531}'
)
#https://www.reddit.com/r/whowouldwin/comments/tdifpw/robert_pattinsons_batman_vs_christian_bales/i0jriao/?context=3

########################################

add_data(['Elsa'],
'Elsa',
False,
False,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{13098}'
)
#

########################################

add_data(['Guts'],
'Guts',
False,
False,
[
    ['Guts.*Punisher|Punisher.*Guts', 'or']
],
'Berserk',
'{3076}'
)
#

########################################

add_data(['Battinson'],
'Battinson',
False,
True,
[
    ['The Batman'], ['2022']
],
'The Batman, 2022',
'{}'
)
#


add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Bat(-| )?mans? ?\(2022']
],
'The Batman, 2022',
'{}'
)
#

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Burton']
],
'1989 film',
'{387}'
)
#https://www.reddit.com/r/respectthreads/comments/54hrjc/respect_batman_michael_keaton/

########################################

id = get_rt_id(cur, 'Respect Batman (DC Animated Universe)', 'https://redd.it/fvksky')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/DCAUrts/comments/fvksky/respect_batman_dc_animated_universe/
#https://www.reddit.com/r/whowouldwin/comments/tbvhyy/black_noirthe_boys_composite_vs_robotinvincible/i0a8mou/?context=3

########################################

id = get_rt_id(cur, 'Robot Respect Thread', 'https://comicvine.gamespot.com/forums/gen-discussion-1/robot-respect-thread-1935289/')
add_data(['Robot'],
'Robot',
False,
False,
[
    ['Robot.*Invincible'], ['Invincible', 'Guardians'], ['Robot vs', 'Omni(-| )?Man', 'Invincible'], ['Invincible ?verse'], ['Invincible', 'Friends']
],
'Invincible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/tbvhyy/black_noirthe_boys_composite_vs_robotinvincible/i0a8mou/?context=3
#https://comicvine.gamespot.com/forums/gen-discussion-1/robot-respect-thread-1935289/

########################################

id = get_rt_id(cur, 'Respect Reptar (Rugrats) (Video Games)', 'https://redd.it/tc8cim')
add_data(['Reptar'],
'Reptar',
False,
False,
[
    ['Rugrats', 'Games']
],
'Rugrats Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tc8cim/respect_reptar_rugrats_video_games/

########################################

id = get_rt_id(cur, 'Respect Cyborg (DCEU)', 'https://redd.it/tchl8f')
add_data(['Cyborg'],
'Cyborg',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tchl8f/respect_cyborg_dceu/

########################################

id = get_rt_id(cur, 'Respect Dude (Free Guy)', 'https://redd.it/tcihxa')
add_data(['Dude'],
'Dude',
False,
False,
[
    ['Free Guy']
],
'Free Guy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tcihxa/respect_dude_free_guy/

########################################

id = get_rt_id(cur, 'Respect Blue Shirt Guy (Free Guy)', 'https://redd.it/tcii6f')
add_data(['Blue Shirt Guy'],
'Blue Shirt Guy',
False,
False,
[
    ['Free Guy']
],
'Free Guy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tcii6f/respect_blue_shirt_guy_free_guy/

########################################

id = get_rt_id(cur, 'Respect: Gladiator! (Supercrooks comic)', 'https://redd.it/tcjtif')
add_data(['Gladiator'],
'Gladiator',
False,
False,
[
    ['Supercrooks?']
],
'Supercrooks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tcjtif/respect_gladiator_supercrooks_comic/

########################################

id = get_rt_id(cur, 'Respect Xing Tian, the Relentless (SMITE)', 'https://redd.it/tcv1tn')
add_data(['Xing Tian'],
'Xing Tian',
False,
False,
[
    ['SMITE']
],
'SMITE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tcv1tn/respect_xing_tian_the_relentless_smite/

########################################

id = get_rt_id(cur, 'Respect The Red Panda Spirit (Turning Red)', 'https://redd.it/td9jcv')
add_data(['Ming'],
'Ming',
False,
False,
[
    ['Turning Red']
],
'Turning Red',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/td9jcv/respect_the_red_panda_spirit_turning_red/

add_data(['Red Panda Spirit'],
'Red Panda Spirit',
False,
False,
[
    ['Turning Red']
],
'Turning Red',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/td9jcv/respect_the_red_panda_spirit_turning_red/

########################################

########################################

id = get_rt_id(cur, 'Respect Rainer Miller, SCP-4051! (SCP Foundation)', 'https://redd.it/tdaprv')
add_data(['SCP ?(-| )? ?<4051'],
'SCP-4051',
False,
False,
[
    ['Rainer Miller']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdaprv/respect_rainer_miller_scp4051_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect The Eternals (Marvel Cinematic Universe)', 'https://redd.it/tdaxj6')
add_data(['Eternals'],
'Eternals',
True,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdaxj6/respect_the_eternals_marvel_cinematic_universe/

add_data(['Ikaris'],
'Ikaris',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCUs?']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdaxj6/respect_the_eternals_marvel_cinematic_universe/

add_data(['Makkari'],
'Makkari',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCUs?']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdaxj6/respect_the_eternals_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Kro (Marvel Cinematic Universe)', 'https://redd.it/tdb3kq')
add_data(['Kro'],
'Kro',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdb3kq/respect_kro_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Daredevil! (The Trial of the Incredible Hulk (1989))', 'https://redd.it/tdgnt4')
add_data(['Daredevil'],
'Daredevil',
False,
False,
[
    ['Trial of the Incredible Hulk']
],
'The Trial of the Incredible Hulk',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tdgnt4/respect_daredevil_the_trial_of_the_incredible/
#https://www.reddit.com/r/whowouldwin/comments/tdihm7/daredevil_2003_vs_daredevil_mcu_vs_daredevil_the/i0jpq0f/?context=3

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

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

add_data(['Storm'],
'Storm',
False,
False,
[
    ['X-Men vs']
],
'616',
'{2386}'
)
#https://www.reddit.com/r/whowouldwin/comments/1l9y9vx/xmen_vs_justice_league/mxhr5qu/?context=3

########################################

add_data(['Bloodsport'],
'Bloodsport',
False,
False,
[
    ['DC', 'Mercenary Soldier']
],
'DC',
'{25566}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ld530r/dc_and_marvel_mercenary_soldier_type_ffa/my5iewl/?context=3

add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['DC', 'Mercenary Soldier']
],
'DC',
'{21323}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ld530r/dc_and_marvel_mercenary_soldier_type_ffa/my5iewl/?context=3

########################################

id = get_rt_id(cur, 'Respect the Humans (Predator: Killer of Killers)', 'https://redd.it/1l8qtjd')
add_data(['Humans'],
'Humans',
False,
False,
[
    ['Predator:? Killer of Killers']
],
'Predator: Killer of Killers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l8qtjd/respect_the_humans_predator_killer_of_killers/

add_data(['Ursa'],
'Ursa',
False,
False,
[
    ['Predator:? Killer of Killers']
],
'Predator: Killer of Killers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l8qtjd/respect_the_humans_predator_killer_of_killers/

add_data(['Kenji'],
'Kenji',
False,
False,
[
    ['Predator:? Killer of Killers']
],
'Predator: Killer of Killers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l8qtjd/respect_the_humans_predator_killer_of_killers/

########################################

id = get_rt_id(cur, 'Respect Kiyoshi (Predator: Killer of Killers)', 'https://redd.it/1l8433a')
add_data(['Kiyoshi'],
'Kiyoshi',
False,
False,
[
    ['Predator:? Killer of Killers']
],
'Predator: Killer of Killers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the monstrosity (Predator: Killer of Killers)', 'https://redd.it/1l8kuwa')
add_data(['Monstrosity'],
'Monstrosity',
False,
False,
[
    ['Predator:? Killer of Killers']
],
'Predator: Killer of Killers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect David Bruce Banner, The Incredible Hulk (The Incredible Hulk (1978 Television Series))', 'https://redd.it/1l95a5m')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['David Banner'], ['(Incredible|TV) Hulk', '1978'], ['1978 Hulk']
],
'The Incredible Hulk, 1978',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Concrete (Paul Chadwick''s Concrete)", 'https://redd.it/1l95tkt')
add_data(['Concrete'],
'Concrete',
False,
False,
[
    ['Chadwick'], ['Ronald Lithgow']
],
'Paul Chadwick',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Saurolophus (Dinosaur King)', 'https://redd.it/1l9tiok')
add_data(['Saurolophus'],
'Saurolophus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l9tiok/respect_saurolophus_dinosaur_king/

########################################

id = get_rt_id(cur, 'Respect Deltadromeus (Dinosaur King)', 'https://redd.it/1lat5dd')
add_data(['Deltadromeus'],
'Deltadromeus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Predator (Fortnite)', 'https://redd.it/1layps7')
add_data(['Predator'],
'Predator',
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

id = get_rt_id(cur, 'Respect Puk Puck! (Magical Girl Raising Project)', 'https://redd.it/1lbdai9')
add_data(['Puk Puck'],
'Puk Puck',
False,
False,
[
    ['Magical Girl Raising Project'], ['Mahou Shoujo Ikusei Keikaku']
],
'Magical Girl Raising Project',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lbdai9/respect_puk_puck_magical_girl_raising_project/

########################################

id = get_rt_id(cur, 'Respect Magneto (Fortnite)', 'https://redd.it/1lbp6z7')
add_data(['Magneto'],
'Magneto',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lbp6z7/respect_magneto_fortnite/

########################################

id = get_rt_id(cur, 'Respect Iguanodon (Dinosaur King)', 'https://redd.it/1lbqnyd')
add_data(['Iguanodon'],
'Iguanodon',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lbqnyd/respect_iguanodon_dinosaur_king/

########################################

id = get_rt_id(cur, 'Respect Azuka (Dreamwalker)', 'https://redd.it/1lbrlq4')
add_data(['Azuka'],
'Azuka',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lbrlq4/respect_azuka_dreamwalker/

########################################

id = get_rt_id(cur, "Respect Ruti Ragnason! (Banished from the Hero''s Party)", 'https://redd.it/1lc45v1')
add_data(['Ruti Ragnason'],
'Ruti Ragnason',
False,
True,
[
    ['Banished from the Hero''?s Party']
],
"Banished from the Hero''s Party",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lc45v1/respect_ruti_ragnason_banished_from_the_heros/

add_data(['Ruti'],
'Ruti',
False,
False,
[
    ['Banished from the Hero''?s Party']
],
"Banished from the Hero''s Party",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1lc45v1/respect_ruti_ragnason_banished_from_the_heros/

########################################

id = get_rt_id(cur, 'Respect Mantra (Malibu Comics, Ultraverse)', 'https://redd.it/1ld9lwf')
add_data(['Mantra'],
'Mantra',
False,
False,
[
    ['Ultraverse']
],
"Ultraverse",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ld9lwf/respect_mantra_malibu_comics_ultraverse/

########################################

id = get_rt_id(cur, 'Respect Marvin the Martian (Looney Tunes - DC Comics)', 'https://redd.it/1lcs5uk')
add_data(['Marvin the Martian'],
'Marvin the Martian',
False,
False,
[
    ['DC']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Johnathan Smatten''s Robotic Knight and the Super-Sword of Krypton (DC Comics, Pre-Crisis)", 'https://redd.it/1ld5unt')
add_data(["Johnathan Smatten''s Robotic Knight"],
"Johnathan Smatten''s Robotic Knight",
False,
True,
[
    ['DC Comics']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#

add_data(['Super(-| )Sword of Krypton'],
'Super-Sword of Krypton',
False,
True,
[
    ['DC Comics']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#

add_data(["Johnathan Smatten''s Robotic Knight"],
"Johnathan Smatten''s Robotic Knight",
False,
True,
[
    ['Pre(-| )?Crisis']
],
"Pre-Crisis",
'{' + '{}'.format(id) + '}'
)
#

add_data(['Super(-| )Sword of Krypton'],
'Super-Sword of Krypton',
False,
True,
[
    ['Pre(-| )?Crisis']
],
"Pre-Crisis",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ld5unt/respect_johnathan_smattens_robotic_knight_and_the/


########################################

id = get_rt_id(cur, 'Respect Lar-On, the Werewolf of Krypton! (DC, Pre-Crisis)', 'https://redd.it/1ld86mm')
add_data(['Lar(-| )On'],
'Lar-On',
False,
False,
[
    ['DC Comics'], ['Krypton(ian|ite)?'], ['Werewolf']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lar(-| )On'],
'Lar-On',
False,
False,
[
    ['Pre(-| )?Crisis']
],
"Pre-Crisis",
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Susan Terry, the Were-Unicorn! (DC, Pre-Crisis)', 'https://redd.it/1ld86nr')
add_data(['Susan Terry,? the Were(-| )Unicorn'],
'Susan Terry, the Were-Unicorn',
False,
True,
[
    ['DC Comics']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#

add_data(['Susan Terry,? the Were(-| )Unicorn'],
'Susan Terry, the Were-Unicorn',
False,
False,
[
    ['Pre(-| )?Crisis']
],
"Pre-Crisis",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ld86nr/respect_susan_terry_the_wereunicorn_dc_precrisis/


########################################

id = get_rt_id(cur, 'Respect Batman, the Were-Bat! (DC, Pre-Crisis)', 'https://redd.it/1ld86ox')
add_data(['Batman,? the Were(-| )Bat'],
'Batman, the Were-Bat',
False,
True,
[
    ['DC Comics']
],
"DC",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ld86ox/respect_batman_the_werebat_dc_precrisis/

add_data(['Batman,? the Were(-| )Bat'],
'Batman, the Were-Bat',
False,
False,
[
    ['Pre(-| )?Crisis']
],
"Pre-Crisis",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ld86ox/respect_batman_the_werebat_dc_precrisis/

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

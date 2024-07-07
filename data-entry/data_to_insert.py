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

update_respectthread(cur, 16852, 'Respect The Immortal (Invincible Amazon Series)', 'https://redd.it/1dv7oi1')

########################################

id = get_rt_id(cur, 'Re-spook-t the Crypt Keeper (Tales from the Crypt, HBO)', 'https://redd.it/1dtopby')
add_data(['Crypt ?Keeper'],
'Crypt Keeper',
False,
True,
[
    ['Tales from the Crypt']
],
'Tales from the Crypt',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dtopby/respookt_the_crypt_keeper_tales_from_the_crypt_hbo/

########################################

id = get_rt_id(cur, 'Respect: Khonshu (Marvel, 616)', 'https://redd.it/1dtpskw')
add_data(['Khonshu'],
'Khonshu',
False,
False,
[
    ['616'], ['Marvel'], ['Khonshu.*comics']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dtpskw/respect_khonshu_marvel_616/

add_data(['Khonshu'],
'Khonshu',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dtpskw/respect_khonshu_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Ultimate Spider-Man (Marvel, Earth-6160)', 'https://redd.it/1dwtna4')
add_data(['Ultimate Spider(-| )?Man'],
'Ultimate Spider-Man',
False,
False,
[
    ['6160']
],
'6160',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Iron Man Armor Model 8: Silver Centurion (Marvel, 616)', 'https://redd.it/1dvzwis')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Silver Centurion'], ['Model 8']
],
'Silver Centurion',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dvzwis/respect_iron_man_armor_model_8_silver_centurion/

########################################

id = get_rt_id(cur, "Respect Wild Cat Size (Jojo''s Bizarre Adventure)", 'https://redd.it/1du0sv0')
add_data(['Wild Cat Size'],
'Wild Cat Size',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Usagi Alohaoe (Jojo''s Bizarre Adventure)", 'https://redd.it/1dwb4py')
add_data(['Usagi Alohaoe'],
'Usagi Alohaoe',
False,
True,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Charming Man (Jojo''s Bizarre Adventure)", 'https://redd.it/1dw90o7')
add_data(['Charming Man'],
'Charming Man',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dw90o7/respect_charming_man_jojos_bizarre_adventure/

########################################

id = get_rt_id(cur, 'Respect Kei Uzuki (Sakamoto Days)', 'https://redd.it/1dujo5i')
add_data(['Kei Uzuki'],
'Kei Uzuki',
False,
True,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dujo5i/respect_kei_uzuki_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Rion Akao (Sakamoto Days)', 'https://redd.it/1dujoi9')
add_data(['Rion Akao'],
'Rion Akao',
False,
True,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dujoi9/respect_rion_akao_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Akira Akao (Sakamoto Days)', 'https://redd.it/1dwsgnb')
add_data(['Akira Akao'],
'Akira Akao',
False,
True,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dwsgnb/respect_akira_akao_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Satoda (Sakamoto Days)', 'https://redd.it/1dwsfbk')
add_data(['Satoda'],
'Satoda',
False,
False,
[
    ['Sakamoto Days'], ['Etsuko Satoda']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dwsfbk/respect_satoda_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Abigail Lazar (Abigail)', 'https://redd.it/1duph2v')
add_data(['Abigail'],
'Abigail',
False,
False,
[
    ['Abigail Lazar'], ['Abigail ?\(Abigail\)'], ['Abigail ?\(2024\)'], ['vampire', '2024']
],
'2024',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1duph2v/respect_abigail_lazar_abigail/

########################################

id = get_rt_id(cur, 'Respect the Seven Great Monsters (The Ocean Hunter)', 'https://redd.it/1duy5s7')
add_data(['Seven Great Monsters'],
'Seven Great Monsters',
True,
False,
[
    ['Ocean Hunter']
],
'The Ocean Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1duy5s7/respect_the_seven_great_monsters_the_ocean_hunter/

########################################

id = get_rt_id(cur, 'Respect Chris and Torel (The Ocean Hunter)', 'https://redd.it/1dv0ora')
add_data(['Chris (&|and) Torel'],
'Chris & Torel',
True,
False,
[
    ['Ocean Hunter']
],
'The Ocean Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dv0ora/respect_chris_and_torel_the_ocean_hunter/

########################################

id = get_rt_id(cur, 'Respect Vigilante (DCEU)', 'https://redd.it/1dv7kfy')
add_data(['Vigilante'],
'Vigilante',
False,
False,
[
    ['Vigilante ?\(DC Extended Universe'], ['DC ?(E|C)U']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dv7kfy/respect_vigilante_dceu/

########################################

id = get_rt_id(cur, 'Respect Peacemaker (Mortal Kombat)', 'https://redd.it/1dv7mje')
add_data(['Peace ?maker'],
'Peacemaker',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dv7mje/respect_peacemaker_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect Superior Man (Superman Red Son Animated Movie)', 'https://redd.it/1dv7mje')
add_data(['Superior Man'],
'Superior Man',
False,
False,
[
    ['Red Son']
],
'Red Son',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dv7n4x/respect_superior_man_superman_red_son_animated/

########################################

id = get_rt_id(cur, 'Respect Liberty Prime (Fallout)', 'https://redd.it/1dv95t6')
add_data(['Liberty Prime'],
'Liberty Prime',
False,
False,
[
    ['Fallout']
],
'Fallout',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dv95t6/respect_liberty_prime_fallout/

########################################

id = get_rt_id(cur, 'Respect Wonder Woman! (DC Animated Movie Universe)', 'https://redd.it/1dvjtc0')
add_data(['Wonder ?Woman'],
'Wonder Woman',
False,
False,
[
    ['DC Animated Film Universe'], ['DCA(F|M)U'], ['DC Animated Movies?']
],
'DC Animated Movie Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dvjtc0/respect_wonder_woman_dc_animated_movie_universe/

########################################

id = get_rt_id(cur, 'Respect Westerner Franklin Harlock Jr (Gun Frontier)', 'https://redd.it/1dvm8ue')
add_data(['Franklin Harlock,? Jr'],
'Franklin Harlock, Jr.',
False,
True,
[
    ['Gun Frontier']
],
'Gun Frontier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dvm8ue/respect_westerner_franklin_harlock_jr_gun_frontier/

########################################

id = get_rt_id(cur, 'Respect Christopher Chance, the Human Target (DC Comics, Composite)', 'https://redd.it/1dw1kpu')
add_data(['Christopher Chance'],
'Christopher Chance',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dw1kpu/respect_christopher_chance_the_human_target_dc/

########################################

id = get_rt_id(cur, 'Respect Harrison (Pokemon Anime)', 'https://redd.it/1dwqibz')
add_data(['Harrison'],
'Harrison',
False,
False,
[
    ['Harrison ?\(Pok(e|é)m(o|a)n\)']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dwqibz/respect_harrison_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Guchuko (Potemayo Anime)', 'https://redd.it/1dxa52l')
add_data(['Guchuko'],
'Guchuko',
False,
False,
[
    ['Potemayo']
],
'Potemayo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dxa52l/respect_guchuko_potemayo_anime/

########################################

id = get_rt_id(cur, 'Respect the Krites (Critters)', 'https://redd.it/1dxb9hm')
add_data(['(K|C)rites'],
'Krites',
False,
False,
[
    ['Critters']
],
'Critters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dxb9hm/respect_the_krites_critters/

########################################

id = get_rt_id(cur, 'Respect the Super Predator trio (Predators 2010)', 'https://redd.it/1dxkudq')
add_data(['Super Predator (Trio|Clan)'],
'Super Predator Trio',
True,
True,
[
    ['2010']
],
'Predators, 2010',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Berserker Predator'],
'Berserker Predator',
False,
True,
[
    ['2010']
],
'Predators, 2010',
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

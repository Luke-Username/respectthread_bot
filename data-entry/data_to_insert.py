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

update_respectthread(cur, 5478, 'Respect Saxton Hale! (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1mohvi5/respect_saxton_hale_team_fortress_2/')

########################################

add_data(['Dragon ?borne?'],
'Dragonborn',
False,
False,
[
    ['Durge', "Baldur''?s Gate"]
],
"Baldur''s Gate",
'{}'
)
#

########################################

add_data(['Sentry'],
'Sentry',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{}'
)
#


########################################

id = get_rt_id(cur, 'Respect Hanzo Hattori (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mqgkw7/respect_hanzo_hattori_dinosaur_king/')
add_data(['Hattori Hanz(ō|o)|Hanz(ō|o) Hattori'],
'Hattori Hanzo',
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

id = get_rt_id(cur, 'Respect Pentaceratops (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mqhcht/respect_pentaceratops_dinosaur_king/')
add_data(['Pentaceratops'],
'Pentaceratops',
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

id = get_rt_id(cur, 'Respect Deinonychus (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1mqgiuy/respect_deinonychus_dinosaur_king/')
add_data(['Deinonychus'],
'Deinonychus',
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

id = get_rt_id(cur, 'Respect Gokuraku (Ichi the Witch)', 'https://www.reddit.com/r/respectthreads/comments/1mq0uoa/respect_gokuraku_ichi_the_witch/')
add_data(['Gokuraku'],
'Gokuraku',
False,
False,
[
    ['Ichi the Witch']
],
'Ichi the Witch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the World-Hater Majik (Ichi the Witch)', 'https://www.reddit.com/r/respectthreads/comments/1mq0ulg/respect_the_worldhater_majik_ichi_the_witch/')
add_data(['World(-| )Hater Majik'],
'World-Hater Majik',
False,
True,
[
    ['Ichi the Witch']
],
'Ichi the Witch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Desscaras! (Ichi the Witch)', 'https://www.reddit.com/r/respectthreads/comments/1mq0ck8/respect_desscaras_ichi_the_witch/')
add_data(['Desscaras'],
'Desscaras',
False,
False,
[
    ['Ichi the Witch']
],
'Ichi the Witch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ichi the Witch! (Ichi the Witch)', 'https://www.reddit.com/r/respectthreads/comments/1mq03dg/respect_ichi_the_witch_ichi_the_witch/')
add_data(['Ichi the Witch'],
'Ichi the Witch',
False,
True,
[
    ['Ichi the Witch ?\(Ichi the Witch']
],
'Ichi the Witch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jason Voorhees (Jason Universe: Sweet Revenge)', 'https://www.reddit.com/r/respectthreads/comments/1mpyyn5/respect_jason_voorhees_jason_universe_sweet/')
add_data(['Jason Voo?rhee?s'],
'Jason Voorhees',
False,
False,
[
    ['Jason Universe', 'Sweet Revenge']
],
'Jason Universe: Sweet Revenge',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect: Solitaire (Author''s Nightmare)", 'https://www.reddit.com/r/respectthreads/comments/1mpoev7/respect_solitaire_authors_nightmare/')
add_data(['Solitaire'],
'Solitaire',
False,
False,
[
    ["Author''?s Nightmare"]
],
"Author''s Nightmare",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Dilophosaurus (Jurassic Park Comics)', 'https://www.reddit.com/r/respectthreads/comments/1movb17/respect_the_dilophosaurus_jurassic_park_comics/')
add_data(['Dilophosaurus'],
'Dilophosaurus',
False,
False,
[
    ['Jurassic Park Comics']
],
'Jurassic Park Comics',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla Galaxy Odyssey)', 'https://www.reddit.com/r/respectthreads/comments/1mpqa93/respect_godzilla_godzilla_galaxy_odyssey/')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Godzilla.*Godzilla Galaxy Odyssey']
],
'Godzilla Galaxy Odyssey',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Volga (Godzilla Galaxy Odyssey)', 'https://www.reddit.com/r/respectthreads/comments/1mpqvqu/respect_volga_godzilla_galaxy_odyssey/')
add_data(['Volga'],
'Volga',
False,
False,
[
    ['Godzilla Galaxy Odyssey']
],
'Godzilla Galaxy Odyssey',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marvel Godzilla (Slick)', 'https://www.reddit.com/r/respectthreads/comments/1mprrz3/respect_marvel_godzilla_slick/')
add_data(['Marvel Godzilla'],
'Marvel Godzilla',
False,
False,
[
    ['Slick']
],
'Slick',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Showa Godzilla (Kurso Animations)', 'https://www.reddit.com/r/respectthreads/comments/1mqba9h/respect_showa_godzilla_kurso_animations/')
add_data(['Showa Godzilla'],
'Showa Godzilla',
False,
False,
[
    ['Kurso Animations']
],
'Kurso Animations',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla: Nightmare Option)', 'https://www.reddit.com/r/respectthreads/comments/1mosep7/respect_godzilla_godzilla_nightmare_option/')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Godzilla.*Godzilla:? Nightmare Option']
],
'Godzilla: Nightmare Option',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mr. Freeze (DC Comics, Absolute Universe)', 'https://www.reddit.com/r/respectthreads/comments/1moku4o/respect_mr_freeze_dc_comics_absolute_universe/')
add_data(['(Mister|Mr)\.? Freeze'],
'Mr. Freeze',
False,
False,
[
    ['Absolute Universe']
],
'Absolute Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mr. Freeze (The Batman, 2004)', 'https://www.reddit.com/r/respectthreads/comments/1mne0m1/respect_mr_freeze_the_batman_2004/')
add_data(['(Mister|Mr)\.? Freeze'],
'Mr. Freeze',
False,
False,
[
    ['The Batman,? 2004']
],
'The Batman, 2004-2008',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Spenser (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1mnhr0v/respect_spenser_pokemon_anime/')
add_data(['Spenser'],
'Spenser',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jack Walker (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1mq1vr8/respect_jack_walker_pokemon_anime/')
add_data(['Jack Walker'],
'Jack Walker',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tucker (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1mpgiri/respect_tucker_pokemon_anime/')
add_data(['Tucker'],
'Tucker',
False,
False,
[
    ['Tucker ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Phantom (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1mq1vtp/respect_the_phantom_pokemon_anime/')
add_data(['Phantom'],
'Phantom',
False,
False,
[
    ['Phantom ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Brock''s Marshtomp (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1mo402w/respect_brocks_marshtomp_pokemon_anime/')
add_data(['Marshtomp'],
'Marshtomp',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mudkip'],
'Mudkip',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Brock''s Ludicolo (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1mnhhvz/respect_brocks_ludicolo_pokemon_anime/')
add_data(['Ludicolo'],
'Ludicolo',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lotad'],
'Lotad',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lombre'],
'Lombre',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Brock''s Forretress (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1mo48gj/respect_brocks_forretress_pokemon_anime/')
add_data(['Pineco'],
'Pineco',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Forretress'],
'Forretress',
False,
False,
[
    ['Brock']
],
'Brock',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Jessie''s Dustox (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1mpgdmg/respect_jessies_dustox_pokemon_anime/')
add_data(['Dustox'],
'Dustox',
False,
False,
[
    ['Jessie']
],
'Jessie',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Treeshaker (Son of the White Mare)', 'https://www.reddit.com/r/respectthreads/comments/1mnftrj/respect_treeshaker_son_of_the_white_mare/')
add_data(['Treeshaker'],
'Treeshaker',
False,
False,
[
    ['Son of the White Mare']
],
'Son of the White Mare',
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

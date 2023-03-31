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

update_respectthread(cur, 3477, 'The Captain (Hellsing)', 'https://redd.it/12437nj')
update_respectthread(cur, 3480, 'Respect Walter C. Dornez! (Hellsing)', 'https://redd.it/124ym2r')
update_respectthread(cur, 3478, 'Respect Seras Victoria! (Hellsing)', 'https://redd.it/126pkyd')
update_respectthread(cur, 3476, 'Respect Alucard! (Hellsing)', 'https://redd.it/126pl7w')
update_respectthread(cur, 1763, 'Respect Superboy-Prime! (DC Comics)', 'https://redd.it/126o1fq')

########################################

add_data(['Baki'],
'Baki',
False,
False,
[
    ['Baki ?\(Baki']
],
'Baki',
'{3446}'
)
#https://www.reddit.com/r/whowouldwin/comments/124nrqk/baki_baki_vs_chunli_street_fighter/jdzy9vk/?context=3

########################################

add_data(['Tim Drake'],
'Tim Drake',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{1500, 1501}'
)
#https://www.reddit.com/r/whowouldwin/comments/124ngb9/bakugo_mha_vs_tim_drake_dc/jdzwy2o/?context=3

########################################

id = get_rt_id(cur, 'Featuring The Gatewatch! (Magic: The Gathering)', 'https://redd.it/121wy7d')
add_data(['The Gatewatch'],
'The Gatewatch',
True,
True,
[
    ['Magic:? The Gathering'], ['M:?TG'], ['Planeswalk(er)?s?']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/124azhq/the_gatewatch_magic_the_gathering_vs_brockton_bay/jdymo8d/?context=3

########################################

id = get_rt_id(cur, 'Respect the Xenomorph! (Mortal Kombat)', 'https://redd.it/12454yo')
add_data(['Xenomorph'],
'Xenomorphs',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12454yo/respect_the_xenomorph_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect The Last Spartan! (God of War)', 'https://redd.it/124qwe0')
add_data(['Last Spartan'],
'Last Spartan',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/124qwe0/respect_the_last_spartan_god_of_war/

########################################

id = get_rt_id(cur, 'Respect Hercules! (God of War)', 'https://redd.it/125q5kj')
add_data(['Hercules'],
'Hercules',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125q5kj/respect_hercules_god_of_war/

########################################

id = get_rt_id(cur, 'Respect Deimos! (God of War)', 'https://redd.it/127t5v4')
add_data(['Deimos'],
'Deimos',
False,
False,
[
    ['God of War'], ['G\.?O\.?W']
],
'God of War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127t5v4/respect_deimos_god_of_war/

########################################

id = get_rt_id(cur, 'Respect Malzeno! (Monster Hunter)', 'https://redd.it/124sv3c')
add_data(['Malzeno'],
'Malzeno',
False,
True,
[
    ['Monster Hunter']
],
'Monster Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/124sv3c/respect_malzeno_monster_hunter/

########################################

id = get_rt_id(cur, 'Rip Van Winkle (Hellsing)', 'https://redd.it/1252okd')
add_data(['Rip Van Winkle'],
'Rip Van Winkle',
False,
False,
[
    ['Hell?sing']
],
'Hellsing',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1252okd/rip_van_winkle_hellsing/

########################################

id = get_rt_id(cur, 'Tubalcain Alhambra (Hellsing)', 'https://redd.it/125y5k5')
add_data(['Tubalcain Alhambra'],
'Tubalcain Alhambra',
False,
True,
[
    ['Hell?sing']
],
'Hellsing',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125y5k5/tubalcain_alhambra_hellsing/

add_data(['Dandy Man'],
'Dandy Man',
False,
False,
[
    ['Hell?sing']
],
'Hellsing',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125y5k5/tubalcain_alhambra_hellsing/

########################################

id = get_rt_id(cur, 'Respect M. Kruger! (Elysium)', 'https://redd.it/125886b')
add_data(['Kruger'],
'Kruger',
False,
False,
[
    ['Elysium']
],
'Elysium',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125886b/respect_m_kruger_elysium/

########################################

id = get_rt_id(cur, 'Respect Harry Potter (A Very Potter Musical)', 'https://redd.it/125mw0c')
add_data(['Harry Potter'],
'Harry Potter',
False,
False,
[
    ['A Very Potter Musical']
],
'A Very Potter Musical',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125mw0c/respect_harry_potter_a_very_potter_musical/

########################################

id = get_rt_id(cur, 'Respect The Predator! (Mortal Kombat)', 'https://redd.it/125of59')
add_data(['Predator'],
'Predator',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125of59/respect_the_predator_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect: The Parasite! (The New Adventures of Superman)', 'https://redd.it/125udoy')
add_data(['Parasite'],
'Parasite',
False,
False,
[
    ['The New Adventures of Superman']
],
'The New Adventures of Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/125udoy/respect_the_parasite_the_new_adventures_of/


########################################

id = get_rt_id(cur, "Respect Morrigan Aensland (Night Warriors: Darkstalkers'' Revenge) (The anime OVA)", 'https://redd.it/12659og')
add_data(['Morrigan Aensland'],
'Morrigan Aensland',
False,
True,
[
    ['Darkstalkers']
],
'Darkstalkers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12659og/respect_morrigan_aensland_night_warriors/

########################################

id = get_rt_id(cur, 'Respect V1! (ULTRAKILL)', 'https://redd.it/126h4hv')
add_data(['V1'],
'V1',
False,
False,
[
    ['ULTRAKILL']
],
'ULTRAKILL',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/126h4hv/respect_v1_ultrakill/

########################################

id = get_rt_id(cur, 'Respect SuperDoom (DC, New 52)', 'https://redd.it/126o2pa')
add_data(['SuperDoom'],
'SuperDoom',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/126o2pa/respect_superdoom_dc_new_52/

########################################

id = get_rt_id(cur, "Respect: Superman''s Superman Armor! (DC, Post Crisis)", 'https://redd.it/127umvx')
add_data(['Superman Armor'],
'Superman Armor',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127umvx/respect_supermans_superman_armor_dc_post_crisis/

########################################

id = get_rt_id(cur, 'Respect The Destroyer (Marvel 616)', 'https://redd.it/127x7j3')
add_data(['(Kevin|Keene) Marlow'],
'Keene Marlow',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127x7j3/respect_the_destroyer_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Dr. Andonuts (Earthbound Halloween Hack)', 'https://redd.it/12754m3')
add_data(['Dr\.? Andonuts'],
'Dr. Andonuts',
False,
False,
[
    ['Earth(-| )?bound', 'Halloween Hack']
],
'Earthbound Halloween Hack',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12754m3/respect_dr_andonuts_earthbound_halloween_hack/

########################################

id = get_rt_id(cur, "Respect Molly (Telltale''s The Walking Dead Game)", 'https://redd.it/12785kj')
add_data(['Molly'],
'Molly',
False,
False,
[
    ['Wa(lk|kl)ing Dead']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12785kj/respect_molly_telltales_the_walking_dead_game/

########################################

id = get_rt_id(cur, 'Respect Hunahpu and Xbalanque! (Popol Vuh)', 'https://redd.it/127dcwg')
add_data(['Hunahpu'],
'Hunahpu',
False,
True,
[
    ['Popol Vuh']
],
'Popol Vuh',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127dcwg/respect_hunahpu_and_xbalanque_popol_vuh/

add_data(['Xbalanque'],
'Xbalanque',
False,
True,
[
    ['Popol Vuh']
],
'Popol Vuh',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127dcwg/respect_hunahpu_and_xbalanque_popol_vuh/

add_data(['Hunahpu (and|&) Xbalanque'],
'Hunahpu and Xbalanque',
True,
True,
[
    ['Popol Vuh']
],
'Popol Vuh',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127dcwg/respect_hunahpu_and_xbalanque_popol_vuh/

add_data(['Maya Hero Twins'],
'Maya Hero Twins',
True,
True,
[
    ['Popol Vuh']
],
'Popol Vuh',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127dcwg/respect_hunahpu_and_xbalanque_popol_vuh/

########################################

id = get_rt_id(cur, 'Respect Tyranitar (Pokemon Anime)', 'https://redd.it/127lkhw')
add_data(['Tyranitar'],
'Tyranitar',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127lkhw/respect_tyranitar_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Spons! (Caddicarus)', 'https://redd.it/127v3h5')
add_data(['Spons'],
'Spons',
False,
False,
[
    ['Caddicarus']
],
'Caddicarus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127v3h5/respect_spons_caddicarus/

########################################

id = get_rt_id(cur, 'Respect The Yellow King! (Fear & Hunger)', 'https://redd.it/127yltx')
add_data(['Yellow King'],
'Yellow King',
False,
False,
[
    ['Fear (&|and) Hunger']
],
'Fear & Hunger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/127yltx/respect_the_yellow_king_fear_hunger/

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

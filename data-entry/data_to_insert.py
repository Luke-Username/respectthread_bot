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

update_respectthread(cur, 24701, 'Respect Jack Xaver (Image Comics, Local Man)', 'https://redd.it/1h7c4un')

########################################

id = get_rt_id(cur, 'Respect The Predators (AVP Hunters Planet)', 'https://redd.it/1h5y0ly')
add_data(['Predators'],
'Predators',
False,
False,
[
    ["Hunter''?s Planet"]
],
"Aliens vs. Predator: Hunter''s Planet",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h5y0ly/respect_the_predators_avp_hunters_planet/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla: Singular Point)', 'https://redd.it/1h6f2j7')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Singular Point']
],
'Godzilla Singular Point',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h6f2j7/respect_godzilla_godzilla_singular_point/

########################################

id = get_rt_id(cur, 'Respect Jet Jaguar (Godzilla: Singular Point)', 'https://redd.it/1h6f2kd')
add_data(['Jet Jaguar'],
'Jet Jaguar',
False,
False,
[
    ['Godzilla', 'Singular Point']
],
'Godzilla Singular Point',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Gaijin (Manifold Series)', 'https://redd.it/1h6gikk')
add_data(['Gaijin'],
'Gaijin',
False,
False,
[
    ['Manifold']
],
'Manifold Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h6gikk/respect_the_gaijin_manifold_series/

########################################

id = get_rt_id(cur, 'Respect the Blues (Manifold Series)', 'https://redd.it/1h79qju')
add_data(['The Blues'],
'The Blues',
False,
False,
[
    ['Manifold']
],
'Manifold Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h79qju/respect_the_blues_manifold_series/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 28: the Hypervelocity Armor (Marvel, 616)', 'https://redd.it/1h6glb4')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Hypervelocity Armor'], ['Model 28']
],
'Hypervelocity Armor',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Arachnoid from the Creepypasta Arachnoid', 'https://redd.it/1h6it4t')
add_data(['Arachnoid'],
'Arachnoid',
False,
False,
[
    ['Arachnoid Creepypasta|Creepypasta Arachnoid'], ['Creepypasta', 'Dorkpool']
],
'Creepypasta',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect the Aquitar Rangers (Mighty Morphin'' Alien Rangers)", 'https://redd.it/1h784lj')
add_data(['Aquitar Rangers?'],
'Aquitar Rangers',
True,
True,
[
    ['Alien Rangers']
],
"Mighty Morphin'' Alien Rangers",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h784lj/respect_the_aquitar_rangers_mighty_morphin_alien/

########################################

id = get_rt_id(cur, 'Respect the Rescue Megazord (Power Rangers Turbo)', 'https://redd.it/1h86poj')
add_data(['Rescue Megazord'],
'Rescue Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers Turbo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h86poj/respect_the_rescue_megazord_power_rangers_turbo/

########################################

id = get_rt_id(cur, 'Respect the Hulk (Hulk vs Wolverine)', 'https://redd.it/1h79kw4')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Hulk ?\(Hulk vs\.? Wolverine\)']
],
'Hulk vs Wolverine',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h79kw4/respect_the_hulk_hulk_vs_wolverine/

########################################

id = get_rt_id(cur, 'Respect The Joker (The Dark Knight Returns Animated Movie)', 'https://redd.it/1h7boxz')
add_data(['Joker'],
'Joker',
False,
False,
[
    ['Dark Knight Returns', 'Animated|2013']
],
'The Dark Knight Returns Animated',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h7boxz/respect_the_joker_the_dark_knight_returns/

########################################

id = get_rt_id(cur, 'Respect Cheetahs (Cheetah.org)', 'https://redd.it/1h7cflx')
add_data(['Cheetah'],
'Cheetah',
False,
False,
[
    ['(Hu)?man.*Cheetah'],
    ['(beat|or|vs\.?) a cheetah'],
    ['cat family'],
    ['fully grown? cheetah'],
    ['(which|these|land) animals?'],
    ['or Cheetah', 'run'],
    ['Male Cheetah'],
    ['Snow leopard'],
    ['speed of a cheetah'],
    ['Both (are )?males?'],
    ['Cheetah vs', 'race'],
    ['big cats?'],
    ['Kangal']
],
'Cheetah.org',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h7cflx/respect_cheetahs_cheetahorg/


add_data(['Cheetahs'],
'Cheetahs',
False,
False,
[
    ['Human.*Cheetahs'],
    ['\d+ Cheetahs', 'vs'],
    ['cat family'],
    ['fully grown? cheetahs'],
    ['(which|these|land) animals?'],
    ['or Cheetahs', 'run'],
    ['Male Cheetahs'],
    ['big cats?'],
    ['Kangal']
],
'Cheetah.org',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h7cflx/respect_cheetahs_cheetahorg/

#https://www.reddit.com/r/whowouldwin/comments/r82o0f/me_or_a_cheetah/
#https://www.reddit.com/r/whowouldwin/comments/198txh6/if_the_biggest_members_of_the_cat_family_were_to/
#https://www.reddit.com/r/whowouldwin/comments/1gx0wsq/4_cheetahs_vs_1_lion/
#https://www.reddit.com/r/whowouldwin/comments/1abllvi/2_cheetahs_vs_a_tiger/
#https://www.reddit.com/r/whowouldwin/comments/1b5im6p/mike_tyson_has_70_free_punches_to_ko_these/
#https://www.reddit.com/r/whowouldwin/comments/14m0340/which_animal_would_an_adult_human_fair_better/
#https://www.reddit.com/r/whowouldwin/comments/debm37/human_vs_cheetah_in_a_boxed_room/
#https://www.reddit.com/r/whowouldwin/comments/1c6fep9/out_of_100_battles_how_many_times_could_a_human/
#https://www.reddit.com/r/whowouldwin/comments/1gx0wsq/4_cheetahs_vs_1_lion/
#https://www.reddit.com/r/whowouldwin/comments/o4o8gm/who_would_win_a_person_that_moves_at_the_speed_of/
#https://www.reddit.com/r/whowouldwin/comments/190tnk8/cheetah_vs_snow_leopard/
#https://www.reddit.com/r/whowouldwin/comments/8apjhw/serious_you_your_mother_and_a_400_lbs_man_vs_a/
#https://www.reddit.com/r/whowouldwin/comments/15tc3mz/cheetah_vs_coyote/
#https://www.reddit.com/r/whowouldwin/comments/16203s0/cheetah_vs_jakob_ingebrigtsen/
#https://www.reddit.com/r/whowouldwin/comments/13wvru0/cheetah_vs_silverback_gorilla/
#https://www.reddit.com/r/whowouldwin/comments/13dsigr/black_belt_bjj_vs_cheetah/
#https://www.reddit.com/r/whowouldwin/comments/10u6b9q/kangal_vs_cheetah/
#https://www.reddit.com/r/whowouldwin/comments/1c8ox79/the_flash_vs_1000_cheetahs/


########################################

id = get_rt_id(cur, 'Respect Brandon (Pokemon Anime)', 'https://redd.it/1h80uz6')
add_data(['Brandon'],
'Brandon',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h80uz6/respect_brandon_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Regis (Pokemon Anime)', 'https://redd.it/1h80v8h')
add_data(['Regis'],
'Regis',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Regi Trio'],
'Regi Trio',
True,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Regirock'],
'Regirock',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Regice'],
'Regice',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#


add_data(['Registeel'],
'Registeel',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Regigigas'],
'Regigigas',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Regieleki'],
'Regieleki',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kamau (Primal)', 'https://redd.it/1h83dz0')
add_data(['Kamau'],
'Kamau',
False,
False,
[
    ['Primal']
],
'Primal',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Billy (Black Christmas)', 'https://redd.it/1h84dbz')
add_data(['Billy'],
'Billy',
False,
False,
[
    ['Black Christmas']
],
'Black Christmas',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alchemy (The Design of Homicide)', 'https://redd.it/1h8ibqp')
add_data(['Alchemy'],
'Alchemy',
False,
False,
[
    ['Designs of Homicide']
],
'The Designs of Homicide',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1h8do4m/respect_alchemy_the_designs_of_homicide/

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

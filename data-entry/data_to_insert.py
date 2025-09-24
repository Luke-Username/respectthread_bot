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

update_respectthread(cur, 813, 'Respect Naga (The Legend of Korra)', 'https://www.reddit.com/r/respectthreads/comments/1njzk2w/respect_naga_the_legend_of_korra/')

########################################

id = get_rt_id(cur, 'New-52 DCAU Batman Respect Thread', 'https://comicvine.gamespot.com/profile/thevivas/blog/new-52-dcau-batman-respect-thread/129367/')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['DC Animated Film Universe'], ['DCA(F|M)U'], ['DC Animated Movies?']
],
'DC Animated Movie Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1nlzsmb/various_versions_of_batman_vs_various_versions_of/nf94nwu/?context=3

########################################

id = get_rt_id(cur, 'Respect Ao Run, the Sky Splitter [Ne Zha (2019/2025)]', 'https://www.reddit.com/r/respectthreads/comments/1nkufr9/respect_ao_run_the_sky_splitter_ne_zha_20192025/')
add_data(['Ao Run'],
'Ao Run',
False,
False,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ne Zha & Ao Bing (Ne Zha 1 & 2)', 'https://www.reddit.com/r/respectthreads/comments/1nor4ti/respect_ne_zha_ao_bing_ne_zha_1_2/')
add_data(['Ne Zha'],
'Ne Zha',
False,
True,
[
    ['(movie|film)s?']
],
'',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Ao Bing'],
'Ao Bing',
False,
False,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Feraligatr (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1nl31o0/respect_feraligatr_pokemon_anime/')
add_data(['Feraligatr'],
'Feraligatr',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Totodile'],
'Totodile',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Croconaw'],
'Croconaw',
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

id = get_rt_id(cur, 'Respect Phione (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1nm5tho/respect_phione_pokemon_anime/')
add_data(['Phione'],
'Phione',
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

id = get_rt_id(cur, 'Respect the Hungarian Horntail (Harry Potter Movies)', 'https://www.reddit.com/r/respectthreads/comments/1nmp3fd/respect_the_hungarian_horntail_harry_potter_movies/')
add_data(['Hungarian Horntail'],
'Hungarian Horntail',
False,
True,
[
    ['Harry Potter']
],
'Harry Potter',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect William "B.J." Blazkowicz! (The Golden Nazi Vampire from Absam 2 - The Secret of Castle Kottlitz)', 'https://www.reddit.com/r/respectthreads/comments/1nn0cao/respect_william_bj_blazkowicz_the_golden_nazi/')
add_data(['B\.?J\.? Blazkowicz'],
'B.J. Blazkowicz',
False,
False,
[
    ['The Golden Nazi Vampire from Absam 2|The Secret of Castle Kottlitz']
],
'The Golden Nazi Vampire from Absam 2 - The Secret of Castle Kottlitz',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Megatron (Image Comics, Energon Universe)', 'https://www.reddit.com/r/respectthreads/comments/1nn12k3/respect_megatron_image_comics_energon_universe/')
add_data(['Megatron'],
'Megatron',
False,
False,
[
    ['Energon']
],
'Energon Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Baobhan Sith/Tam Lin Tristan (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nncvxj/respect_baobhan_sithtam_lin_tristan_fategrand/')
add_data(['Baobhan Sith'],
'Baobhan Sith',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tam Lin Tristan'],
'Tam Lin Tristan',
False,
True,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zia Zanna (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/1nnukm1/respect_zia_zanna_star_wars_canon/')
add_data(['Zia Zanna'],
'Zia Zanna',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Vertigo (Savage Land Mutate) (Marvel Comics, Earth 616)', 'https://www.reddit.com/r/respectthreads/comments/1no244g/respect_vertigo_savage_land_mutate_marvel_comics/')
add_data(['Vertigo'],
'Vertigo',
False,
False,
[
    ['Savage Land Mutate']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Schneckeczar, the Snail Emperor! (Godzilla: 70th Anniversary, The Big One) [IDW]', 'https://www.reddit.com/r/respectthreads/comments/1no8msi/respect_schneckeczar_the_snail_emperor_godzilla/')
add_data(['Schneckeczar'],
'Schneckeczar',
False,
False,
[
    ['Godzilla']
],
'Godzilla: 70th Anniversary',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Usuru! (Godzilla: 70th Anniversary, Contagion) [IDW]', 'https://www.reddit.com/r/respectthreads/comments/1no8t5w/respect_usuru_godzilla_70th_anniversary_contagion/')
add_data(['Usuru'],
'Usuru',
False,
False,
[
    ['Godzilla:? 70th Anniversary']
],
'Godzilla: 70th Anniversary',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Monstrum Üpsilon! (Godzilla''s Monsterpiece Theatre) [IDW]", 'https://www.reddit.com/r/respectthreads/comments/1nouf0w/respect_monstrum_%C3%BCpsilon_godzillas_monsterpiece/')
add_data(['Monstrum (Ü|U)psilon'],
'Monstrum Üpsilon',
False,
False,
[
    ['Godzilla']
],
"Godzilla''s Monsterpiece Theatre",
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect Count Dracula! (Godzilla''s Monsterpiece Theatre) [IDW]", 'https://www.reddit.com/r/respectthreads/comments/1nouf9k/respect_count_dracula_godzillas_monsterpiece/')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ["Godzilla''?s Monsterpiece Theatre"]
],
"Godzilla''s Monsterpiece Theatre",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Utma Utep! (Godzilla''s Monsterpiece Theatre) [IDW]", 'https://www.reddit.com/r/respectthreads/comments/1noufe1/respect_utma_utep_godzillas_monsterpiece_theatre/')
add_data(['Utma Utep'],
'Utma Utep',
False,
False,
[
    ["Godzilla''?s Monsterpiece Theatre"]
],
"Godzilla''s Monsterpiece Theatre",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Jay Gatsby! (Godzilla''s Monsterpiece Theatre) [IDW]", 'https://www.reddit.com/r/respectthreads/comments/1noufvv/respect_jay_gatsby_godzillas_monsterpiece_theatre/')
add_data(['Jay Gatsby'],
'Jay Gatsby',
False,
False,
[
    ["Godzilla''?s Monsterpiece Theatre"]
],
"Godzilla''s Monsterpiece Theatre",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Megaguirus! (Mothra: Queen of the Monsters) [IDW]', 'https://www.reddit.com/r/respectthreads/comments/1novbwm/respect_megaguirus_mothra_queen_of_the_monsters/')
add_data(['Megaguirus'],
'Megaguirus',
False,
False,
[
    ['Mothra:? Queen of the Monsters']
],
'Mothra: Queen of the Monsters',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect MechaMothra! (Mothra: Queen of the Monsters) [IDW]', 'https://www.reddit.com/r/respectthreads/comments/1novf5o/respect_mechamothra_mothra_queen_of_the_monsters/')
add_data(['MechaMothra'],
'MechaMothra',
False,
False,
[
    ['Mothra:? Queen of the Monsters']
],
'Mothra: Queen of the Monsters',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Antra! (Mothra: Queen of the Monsters) [IDW]', 'https://www.reddit.com/r/respectthreads/comments/1now9ik/respect_antra_mothra_queen_of_the_monsters_idw/')
add_data(['Antra'],
'Antra',
False,
False,
[
    ['Mothra:? Queen of the Monsters']
],
'Mothra: Queen of the Monsters',
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

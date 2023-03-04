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

update_respectthread(cur, 5506, 'Respect Shulk (Xenoblade Chronicles)', 'https://redd.it/11efam8')
update_respectthread(cur, 3895, 'Respect Misogi Kumagawa! (Medaka Box)', 'https://redd.it/11euydv')
update_respectthread(cur, 7602, 'Respect Jimmy Neutron (The Adventures of Jimmy Neutron, Boy Genius)', 'https://redd.it/11f8q78')
update_respectthread(cur, 2283, 'Respect Doppelganger (Marvel 616)', 'https://redd.it/11fp3ru')
update_respectthread(cur, 23129, 'Respect Scrapeface! (Madness Combat)', 'https://redd.it/11i7g9d')

########################################

add_data(['Calamity Trio'],
'Calamity Trio',
True,
True,
[
    ['Amphibia']
],
'Amphibia',
'{22017, 22016, 22028}'
)
#https://www.reddit.com/r/whowouldwin/comments/11e5lly/the_calamity_trio_amphibia_vs_the_crystal_gems/jacg80d/?context=3

########################################

id = get_rt_id(cur, "Respect Dante Alighieri (EA''s Dante's Inferno)", 'https://redd.it/a5xp34')
add_data(['Dante'],
'Dante',
False,
False,
[
    ["Dante''s Inferno", 'Movie', 'Game']
],
"Dante''s Inferno, EA",
'{' + '{}, 1195'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/a5xp34/respect_dante_alighieri_eas_dantes_inferno/
#https://www.reddit.com/r/respectthreads/comments/673x9u/respect_dante_alighieri_dantes_inferno_an/
#https://en.wikipedia.org/wiki/Dante%27s_Inferno:_An_Animated_Epic

########################################

id = get_rt_id(cur, 'Respect Falyce, the Emerald Empress (DC, Pre-Zero Hour)', 'https://redd.it/11dpyfi')
add_data(['Falyce'],
'Falyce',
False,
True,
[
    ['Pre(-| )Zero Hour']
],
'Pre-Zero Hour',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11dpyfi/respect_falyce_the_emerald_empress_dc_prezero_hour/

add_data(['Falyce'],
'Falyce',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11dpyfi/respect_falyce_the_emerald_empress_dc_prezero_hour/

########################################

id = get_rt_id(cur, 'Respect Hecate (DC, New 52/Rebirth)', 'https://redd.it/11eohrg')
add_data(['Hecate'],
'Hecate',
False,
False,
[
    ['Goddess of Magic'], ['DC Hecate'], ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['The Presence'], ['Lucifer Morningstar'], ['The Darkest Knight']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11eohrg/respect_hecate_dc_new_52rebirth/

add_data(['Hecate'],
'Hecate',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11eohrg/respect_hecate_dc_new_52rebirth/

########################################

id = get_rt_id(cur, 'Respect Markus Velafi! (Thrilling Intent)', 'https://redd.it/11esxer')
add_data(['Markus Velafi'],
'Markus Velafi',
False,
True,
[
    ['Thrilling Intent']
],
'Thrilling Intent',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11esxer/respect_markus_velafi_thrilling_intent/

########################################

id = get_rt_id(cur, 'Respect Fiora (Xenoblade Chronicles)', 'https://redd.it/11dxfxn')
add_data(['Fiora'],
'Fiora',
False,
False,
[
    ['Xenoblade']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11dxfxn/respect_fiora_xenoblade_chronicles/

########################################

id = get_rt_id(cur, 'Respect Melia (Xenoblade Chronicles)', 'https://redd.it/11e45td')
add_data(['Melia'],
'Melia',
False,
False,
[
    ['Xenoblade']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11e45td/respect_melia_xenoblade_chronicles/

########################################

id = get_rt_id(cur, 'Auggie Smith, The White Dragon (DCEU)', 'https://redd.it/11ehjuz')
add_data(['White Dragon'],
'White Dragon',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe'],
    ['Peacemaker'], ['Auggie Smith']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ehjuz/auggie_smith_the_white_dragon_dceu/

########################################

id = get_rt_id(cur, 'Respect Charlie the Gorilla! (DCEU)', 'https://redd.it/11i2us8')
add_data(['Charlie the Gorilla'],
'Charlie the Gorilla',
False,
True,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe'],
    ['Peacemaker']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11i2us8/respect_charlie_the_gorilla_dceu/

########################################

id = get_rt_id(cur, 'Respect Judomaster! (DCEU)', 'https://redd.it/11f547q')
add_data(['Judomaster'],
'Judomaster',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe'],
    ['Peacemaker']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yugi Muto (Yu-Gi-Oh! Capsule Monsters)', 'https://redd.it/11ei2fs')
add_data(['Yugi Muto'],
'Yugi Muto',
False,
False,
[
    ['Capsule Monsters']
],
'Yu-Gi-Oh! Capsule Monsters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ei2fs/respect_yugi_muto_yugioh_capsule_monsters/

########################################

id = get_rt_id(cur, 'Respect Joey Wheeler (Yu-Gi-Oh! Capsule Monsters)', 'https://redd.it/11ei2ho')
add_data(['Joey Wheeler'],
'Joey Wheeler',
False,
False,
[
    ['Capsule Monsters']
],
'Yu-Gi-Oh! Capsule Monsters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ei2ho/respect_joey_wheeler_yugioh_capsule_monsters/

########################################

id = get_rt_id(cur, 'Respect Yuki Tsukumo! (Jujutsu Kaisen)', 'https://redd.it/11ei8td')
add_data(['Yuki Tsukumo'],
'Yuki Tsukumo',
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ei8td/respect_yuki_tsukumo_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Professor Fig - (Hogwarts Legacy)', 'https://redd.it/11eke4o')
add_data(['Professor Fig'],
'Professor Fig',
False,
False,
[
    ['Hogwarts Legacy']
],
'Hogwarts Legacy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11eke4o/respect_professor_fig_hogwarts_legacy/

########################################

id = get_rt_id(cur, 'Respect Ranrok - (Hogwarts Legacy)', 'https://redd.it/11ekh5a')
add_data(['Ranrok'],
'Ranrok',
False,
False,
[
    ['Hogwarts Legacy']
],
'Hogwarts Legacy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ekh5a/respect_ranrok_hogwarts_legacy/

########################################

id = get_rt_id(cur, 'Respect the Rev-9 (Terminator: Dark Fate)', 'https://redd.it/11eu4ek')
add_data(['Rev-9'],
'Rev-9',
False,
True,
[
    ['Terminator'], ['Dark Fate']
],
'Terminator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11eu4ek/respect_the_rev9_terminator_dark_fate/

########################################

id = get_rt_id(cur, 'Respect Splinter (Teenage Mutant Ninja Turtles) [Mirage Comics]', 'https://redd.it/11dm9v2')
add_data(['Splinter'],
'Splinter',
False,
False,
[
    ['Mirage']
],
'Mirage Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11dm9v2/respect_splinter_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, 'Respect Lityerses! (Heroes of Olympus)', 'https://redd.it/11eurs4')
add_data(['Lityerses'],
'Lityerses',
False,
True,
[
    ['Heroe?s of Olympus'], ['Riordan(-| )?(verse)?']
],
'Heroes of Olympus',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shimada Death! (Dai Dark)', 'https://redd.it/11euutv')
add_data(['Shimada Death'],
'Shimada Death',
False,
True,
[
    ['Dai Dark']
],
'Dai Dark',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11euutv/respect_shimada_death_dai_dark/

########################################

id = get_rt_id(cur, 'Respect Goddard! (The Adventures of Jimmy Neutron: Boy Genius)', 'https://redd.it/11f8okg')
add_data(['Goddard'],
'Goddard',
False,
False,
[
    ['Jimmy Neutron']
],
'Jimmy Neutron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11f8okg/respect_goddard_the_adventures_of_jimmy_neutron/

########################################

id = get_rt_id(cur, 'Respect The N-Men! (The Adventures of Jimmy Neutron: Boy Genius)', 'https://redd.it/11f8prl')
add_data(['N-Men'],
'N-Men',
True,
True,
[
    ['Jimmy Neutron']
],
'Jimmy Neutron',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11f8prl/respect_the_nmen_the_adventures_of_jimmy_neutron/

########################################

id = get_rt_id(cur, 'Respect the Red Locust (Marvel, 616)', 'https://redd.it/11g2y7c')
add_data(['Red Locust'],
'Red Locust',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11g2y7c/respect_the_red_locust_marvel_616/

########################################

id = get_rt_id(cur, 'Respect: Anti-Superman! (Pre-Crisis DC Comics)', 'https://redd.it/11g3ih1')
add_data(['Anti-Superman'],
'Anti-Superman',
False,
False,
[
    ['Anti-Superman ?\(Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11g3ih1/respect_antisuperman_precrisis_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Count Dragorin of Transilvane (DC, Post Crisis)', 'https://redd.it/11i1s5e')
add_data(['Dragorin'],
'Dragorin',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11i1s5e/respect_count_dragorin_of_transilvane_dc_post/

add_data(['Dragorin'],
'Dragorin',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11i1s5e/respect_count_dragorin_of_transilvane_dc_post/

########################################

id = get_rt_id(cur, 'Respect Shriek (DC Animated Universe)', 'https://redd.it/11g86su')
add_data(['Shriek'],
'Shriek',
False,
False,
[
    ['DC Animated Universe'], ['DCAU']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11g86su/respect_shriek_dc_animated_universe/

########################################

id = get_rt_id(cur, "Respect I.M. Meen (Animation Magic''s I.M. Meen)", 'https://redd.it/11fongd')
add_data(['I\. ?M\.? Meen'],
'I.M. Meen',
False,
True,
[
    ['Animation Magic']
],
'Animation Magic',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Robin the Frog! (Muppet Monster Adventure)', 'https://redd.it/11frado')
add_data(['Robin the Frog'],
'Robin the Frog',
False,
False,
[
    ['Muppet Monster Adventure']
],
'Muppet Monster Adventure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11frado/respect_robin_the_frog_muppet_monster_adventure/

########################################

id = get_rt_id(cur, 'Respect Tony Farms, the Pumaman! (Pumaman)', 'https://redd.it/11frafh')
add_data(['Pumaman'],
'Pumaman',
False,
True,
[
    ['Tony Farms']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11frafh/respect_tony_farms_the_pumaman_pumaman/

########################################

id = get_rt_id(cur, 'Respect Choo-Choo Charles (Choo-Choo Charles)', 'https://redd.it/11g2y9f')
add_data(['Choo(-| )Choo Charles'],
'Choo-Choo Charles',
False,
True,
[
    ['game']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11g2y9f/respect_choochoo_charles_choochoo_charles/

########################################

id = get_rt_id(cur, 'Respect Hugh Glass (The Revenant)', 'https://redd.it/11g2yb8')
add_data(['Hugh Glass'],
'Hugh Glass',
False,
False,
[
    ['The Revenant']
],
'The Revenant',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11g2yb8/respect_hugh_glass_the_revenant/

########################################

id = get_rt_id(cur, 'Respect the Warrior of Light (Final Fantasy XIV Trailers)', 'https://redd.it/11g74uu')
add_data(['Warriors? of Light'],
'Warrior of Light',
False,
True,
[
    ['Final Fantasy'], ['FF(14|XIV)']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tomoyo Sakagami! (Clannad)', 'https://redd.it/11ge1nk')
add_data(['Tomoyo Sakagami'],
'Tomoyo Sakagami',
False,
True,
[
    ['Clannad']
],
'Clannad',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ge1nk/respect_tomoyo_sakagami_clannad/

########################################

id = get_rt_id(cur, 'Respect The Titan Pokemon (Pokemon Games)', 'https://redd.it/11h3k4n')
add_data(['Titan Pok(e|é)m(o|a)n'],
'Titan Pokémon',
True,
True,
[
    ['Pok(e|é)m(o|a)n Games']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11h3k4n/respect_the_titan_pokemon_pokemon_games/

########################################

id = get_rt_id(cur, 'Respect SCP-6345, "Huesos Malos/Bad Bones" (SCP Foundation)', 'https://redd.it/11hn8gd')
add_data(['SCP ?(-| )? ?6345'],
'SCP-6345',
False,
True,
[
    ['Huesos Malos|Bad Bones']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11hn8gd/respect_scp6345_huesos_malosbad_bones_scp/



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

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

update_respectthread(cur, 4126, 'Respect Ash Ketchum (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/cn97u8/respect_ash_ketchum_pokemon_anime/')
update_respectthread(cur, 256, 'Respect Quicksilver (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/jvs26s/respect_quicksilver_marvel_cinematic_universe/')
update_respectthread(cur, 242, 'Respect Sam Wilson, Captain America (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/1ku9apg/respect_sam_wilson_captain_america_marvel/')
update_respectthread(cur, 26090, 'Respect Chrollo Lucifer, Boss of the Phantom Troupe (Hunter x Hunter)', 'https://www.reddit.com/r/respectthreads/comments/1kvajlm/respect_chrollo_lucifer_boss_of_the_phantom/')
update_respectthread(cur, 21730, 'Respect Hank Rutherford Hill! (King of the Hill)', 'https://www.reddit.com/r/respectthreads/comments/tx8xiw/respect_hank_rutherford_hill_king_of_the_hill/')
update_respectthread(cur, 1131, 'Respect Mr. Incredible (The Incredibles)', 'https://www.reddit.com/r/respectthreads/comments/fygb5s/respect_mr_incredible_the_incredibles/')
update_respectthread(cur, 20570, 'Respect The Parr Family (The Incredibles comics)', 'https://www.reddit.com/r/respectthreads/comments/q82emz/respect_the_parr_family_the_incredibles_comics/')
update_respectthread(cur, 23348, 'Respect Yelena Belova (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/117ckm6/respect_yelena_belova_marvel_cinematic_universe/')
update_respectthread(cur, 17487, 'Respect Alexei Alanovich Shostakov, The Red Guardian (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/ok5vpg/respect_alexei_alanovich_shostakov_the_red/')
update_respectthread(cur, 21271, 'Respect John F. Walker! (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/mwz5vm/respect_john_f_walker_marvel_cinematic_universe/')
update_respectthread(cur, 314, 'Respect Darth Vader (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/iaalhi/respect_darth_vader_star_wars_canon/')
update_respectthread(cur, 17674, 'Respect Darth Vader (Star Wars Legends)', 'https://www.reddit.com/r/respectthreads/comments/ph7pyp/respect_darth_vader_star_wars_legends/')
update_respectthread(cur, 26025, 'Respect the Death Star (Star Wars Legends)', 'https://www.reddit.com/r/respectthreads/comments/1k9wr8s/respect_the_death_star_star_wars_legends/')
update_respectthread(cur, 14797, 'Respect the Forerunners (Halo)', 'https://www.reddit.com/r/respectthreads/comments/cq6ywk/respect_the_forerunners_halo/')
update_respectthread(cur, 381, 'Respect the Xenomorph (Alien) (Canon)', 'https://www.reddit.com/r/respectthreads/comments/v6u73b/respect_the_xenomorph_alien_canon/')
update_respectthread(cur, 22087, 'Respect Ellen Ripley (Alien)', 'https://www.reddit.com/r/respectthreads/comments/v5drkt/respect_ellen_ripley_alien/')


########################################

add_data(['Allied Master ?computer'],
'Allied Mastercomputer',
False,
True,
[
    ['Have No Mouth'], ['IHNMAIMS']
],
'I Have No Mouth And Must Scream',
'{16570}'
)
#https://www.reddit.com/r/whowouldwin/comments/1m4xfve/allied_mastercomputer_vs_gojo/

########################################

add_data(['Ripley'],
'Ripley',
False,
False,
[
    ['Xenomorphs?']
],
'Alien',
'{22087}'
)
#https://www.reddit.com/r/whowouldwin/comments/1mbalek/ds_necromorphs_vs_alien_movies_xenomorphs/n5kpbig/?context=3

########################################

add_data(['Thunderbolts'],
'Thunderbolts',
True,
False,
[
    ['Thunderbolts ?\(MCU'], ['The Thunderbolts.*\(MCU\)'], ['Thunderbolts Team', 'MCU'], ['New Avengers', 'MCU'], ['MCU Thunderbolts'], ['MCU: Thunderbolts'], ['Marvel Studios Thunderbolts']
],
'MCU',
'{23348, 17487, 21271, 6502, 274}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hri6a7/marvel_studios_thunderbolts_dc_the_suicide_squad/
#https://www.reddit.com/r/whowouldwin/comments/1kkqlc8/who_is_the_most_powerful_mcu_villain_the/
#https://www.reddit.com/r/whowouldwin/comments/1k95y5g/the_full_thunderbolts_team_mcu_lineup_vs_sentry/
#https://www.reddit.com/r/whowouldwin/comments/1kik9co/mcu_the_avengers_vs_the_new_avengers_formerly/
#https://www.reddit.com/r/whowouldwin/comments/1ktdudq/mcu_thunderbolts_vs_dceu_suicide_squad/
#https://www.reddit.com/r/whowouldwin/comments/1ke28uw/mcu_thunderbolts_vs_dceu_11th_street_kids/


########################################

id = get_rt_id(cur, 'Respect Last Sun! (DC Comics)', 'https://www.reddit.com/r/respectthreads/comments/1m76bi8/respect_last_sun_dc_comics/')
add_data(['Last Sun'],
'Last Sun',
False,
False,
[
    ['Last Sun ?\(DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Reiji Nogi/Cassis Worm (Kamen Rider Kabuto)', 'https://www.reddit.com/r/respectthreads/comments/1m7upqu/respect_reiji_nogicassis_worm_kamen_rider_kabuto/')
add_data(['Cassis Worm'],
'Cassis Worm',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Reiji Nogi'],
'Reiji Nogi',
False,
True,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect: Beam (Author''s Nightmare)", 'https://www.reddit.com/r/respectthreads/comments/1m8aq8p/respect_beam_authors_nightmare/')
add_data(['Beam'],
'Beam',
False,
False,
[
    ["Author''?s Nightmare"]
],
'Author''s Nightmare',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect generic Garou! (Werewolf: The Apocalypse)', 'https://www.reddit.com/r/respectthreads/comments/1m8s8fb/respect_generic_garou_werewolf_the_apocalypse/')
add_data(['Garou'],
'Garou',
False,
False,
[
    ['Werewolf:? The Apocalypse']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bane (DC Comics, Absolute Universe)', 'https://www.reddit.com/r/respectthreads/comments/1m97udi/respect_bane_dc_comics_absolute_universe/')
add_data(['Bane'],
'Bane',
False,
False,
[
    ['Absolute Universe']
],
'Absolute Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m97udi/respect_bane_dc_comics_absolute_universe/

########################################

id = get_rt_id(cur, 'Respect TFC Heavy (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1m9d1sh/respect_tfc_heavy_team_fortress_2/')
add_data(['TFC Heavy'],
'TFC Heavy',
False,
True,
[
    ['TF2'], ['Team Fortress']
],
'TF2',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1m9d1sh/respect_tfc_heavy_team_fortress_2/

########################################

id = get_rt_id(cur, 'Respect Alluka Zoldyck (Hunter x Hunter)', 'https://www.reddit.com/r/respectthreads/comments/1m9idal/respect_alluka_zoldyck_hunter_x_hunter/')
add_data(['Alluka'],
'Alluka',
False,
False,
[
    ['Hunter ?(x ?)?Hunter'], ['HxH'], ['Zoldycks?'], ['wish(es|ing)?']
],
'Hunter x Hunter',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Megaraptor (Dinosaur King)', 'https://www.reddit.com/r/respectthreads/comments/1m9n10l/respect_megaraptor_dinosaur_king/')
add_data(['Megaraptor'],
'Megaraptor',
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

id = get_rt_id(cur, 'Respect Bashnag Gro-Gorzoth! (The Elder Scrolls)', 'https://www.reddit.com/r/respectthreads/comments/1m9u5w4/respect_bashnag_grogorzoth_the_elder_scrolls/')
add_data(['Bashnag'],
'Bashnag',
False,
False,
[
    ['Elder Scrolls'], ['Gro(-| )?Gorzoth']
],
'Elder Scrolls',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Pedestrian (The Pedestrian)', 'https://www.reddit.com/r/respectthreads/comments/1ma576s/respect_the_pedestrian_the_pedestrian/')
add_data(['The Pedestrian'],
'The Pedestrian',
False,
False,
[
    ['The Pedestrian ?\(The Pedestrian\)']
],
'',
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

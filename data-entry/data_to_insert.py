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

update_respectthread(cur, 264, 'Respect Thor Odinson (Marvel Cinematic Universe)', 'https://redd.it/xguqef')
update_respectthread(cur, 664, 'Respect Batman! (Batman: The Brave and the Bold)', 'https://redd.it/xgxk4q')
update_respectthread(cur, 2917, "Respect Ava Ire (Ava''s Demon)", 'https://redd.it/xflbp3')

########################################

add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['TARDIS']
],
'Doctor Who',
'{14419,40,15401}'
)
#https://www.reddit.com/r/whowouldwin/comments/xfizoi/can_the_doctor_save_the_milky_way_of_the_41st/

########################################

add_data(['Vi'],
'Vi',
False,
False,
[
    ['Arcane']
],
'League of Legends',
'{5201}'
)
#https://www.reddit.com/r/whowouldwin/comments/xej36u/kamen_rider_accel_kamen_rider_w_vs_vi_arcane/ioh1lom/

########################################

id = get_rt_id(cur, 'Respect Touka Toudou (Rakudai Kishi no Cavalry)', 'https://redd.it/xdcc1w')
add_data(['Touka Toudou'],
'Touka Toudou',
False,
True,
[
    ['Chivalry of a Failed Knight'], ['Rakudai']
],
'Chivalry of a Failed Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xdcc1w/respect_touka_toudou_rakudai_kishi_no_cavalry/

########################################

id = get_rt_id(cur, 'Respect Blaine (Pokemon Anime)', 'https://redd.it/xe2a1k')
add_data(['Blaine'],
'Blaine',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xe2a1k/respect_blaine_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect the Giant Ancient Alakazam (Pokemon)', 'https://redd.it/xgi3or')
add_data(['Giant( Ancient)? Alakazam'],
'Giant Ancient Alakazam',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xgi3or/respect_the_giant_ancient_alakazam_pokemon/

########################################

id = get_rt_id(cur, 'Respect Hermit Worms (The Fifth Science)', 'https://redd.it/xe3787')
add_data(['Hermit Worms?'],
'Hermit Worm',
False,
False,
[
    ['The Fifth Science']
],
'The Fifth Science',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xe3787/respect_hermit_worms_the_fifth_science/

########################################

id = get_rt_id(cur, 'Respect Everett Donnelly, Frost (Marvel, 616)', 'https://redd.it/xe4kyo')
add_data(['Everett Donnelly'],
'Everett Donnelly',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xe4kyo/respect_everett_donnelly_frost_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Baron Mordo (Marvel 616)', 'https://redd.it/xg0eti')
add_data(['Baron Mordo'],
'Baron Mordo',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg0eti/respect_baron_mordo_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Gorr, the God Butcher (Marvel Cinematic Universe)!', 'https://redd.it/xg4dnu')
add_data(['Gorr,? the God Butcher'],
'Gorr the God Butcher',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg4dnu/respect_gorr_the_god_butcher_marvel_cinematic/

add_data(['Gorr'],
'Gorr',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg4dnu/respect_gorr_the_god_butcher_marvel_cinematic/

########################################

id = get_rt_id(cur, 'Respect Moon Knight (Marvel Cinematic Universe)', 'https://redd.it/xg93oa')
add_data(['Moon Knight'],
'Moon Knight',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg93oa/respect_moon_knight_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect Jane Foster, The Mighty Thor (Marvel Cinematic Universe)', 'https://redd.it/xhfowd')
add_data(['Jane Foster'],
'Jane Foster',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Rex Splode (Invincible) Respect Thread', 'https://comicvine.gamespot.com/forums/gen-discussion-1/rex-splode-invincible-respect-thread-2229067/')
add_data(['Rex( |-)Splode'],
'Rex Splode',
False,
True,
[
    ['Invincible']
],
'Invincible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/xew9al/rex_splode_invincible_vs_gambit_marvel_616/ioixkjn/?context=3

########################################

id = get_rt_id(cur, 'Respect Sprig Plantar! (Amphibia)', 'https://redd.it/xh3w3a')
add_data(['Sprig Plantar'],
'Sprig Plantar',
False,
True,
[
    ['Amphibia']
],
'Amphibia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xh3w3a/respect_sprig_plantar_amphibia/

########################################

id = get_rt_id(cur, 'Respect Jaime Reyes, The Blue Beetle! (Batman: The Brave and the Bold)', 'https://redd.it/xemrnv')
add_data(['Blue Beetle'],
'Blue Beetle',
False,
False,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xemrnv/respect_jaime_reyes_the_blue_beetle_batman_the/

########################################

id = get_rt_id(cur, 'Respect Plastic Man! (Batman: The Brave and the Bold)', 'https://redd.it/xg024o')
add_data(['Plastic Man'],
'Plastic Man',
False,
False,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg024o/respect_plastic_man_batman_the_brave_and_the_bold/

########################################

id = get_rt_id(cur, 'Respect The Heretic (DC, New 52/Rebirth)', 'https://redd.it/xevjwu')
add_data(['Heretic'],
'Heretic',
False,
False,
[
    ['Heretic ?(DC']
],
'DC',
'{' + '{}, 1540'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xevjwu/respect_the_heretic_dc_new_52rebirth/

add_data(['Heretic'],
'Heretic',
False,
False,
[
    ['Heretic ?(DC'], ['The Heretic.*DC']
],
'DC',
'{' + '{}, 1540'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xevjwu/respect_the_heretic_dc_new_52rebirth/

add_data(['Heretic'],
'Heretic',
False,
False,
[
    ['New 52', 'Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xevjwu/respect_the_heretic_dc_new_52rebirth/

########################################

id = get_rt_id(cur, "Respect Maggie Lacivi (Ava''s Demon)", 'https://redd.it/xf9w92')
add_data(['Maggie Lacivi'],
'Maggie Lacivi',
False,
True,
[
    ["Ava''?s Demon"]
],
"Ava''s Demon",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xf9w92/respect_maggie_lacivi_avas_demon/

########################################

id = get_rt_id(cur, "Respect ''The Monk who Calls the Real Name'', Ichibe Hyosube (Bleach)", 'https://redd.it/xfe5xq')
add_data(['Ichibe Hyosube'],
'Ichibe Hyosube',
False,
True,
[
    ['Bleach']
],
'Bleach',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xfe5xq/respect_the_monk_who_calls_the_real_name_ichibe/

########################################

id = get_rt_id(cur, 'Respect Darth Vader (Fortnite)', 'https://redd.it/xffw4t')
add_data(['Vader'],
'Darth Vader',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xffw4t/respect_darth_vader_fortnite/

########################################

id = get_rt_id(cur, 'Respect Bulma! (Fortnite)', 'https://redd.it/xg5a7x')
add_data(['Bulma'],
'Bulma',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/xg5a7x/respect_bulma_fortnite/

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

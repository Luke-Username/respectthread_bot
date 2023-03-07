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

update_respectthread(cur, 6477, 'Respect Nahiri, the Lithomancer! (Magic: The Gathering)', 'https://redd.it/11j1old')
update_respectthread(cur, 4555, 'Respect Medusa Gorgon! (Soul Eater)', 'https://redd.it/11j2dzn')

########################################

add_data(['Anya'],
'Anya',
False,
False,
[
    ['Spy x Family']
],
'Spy x Family',
'{22142}'
)
#https://www.reddit.com/r/whowouldwin/comments/11jhhhg/miri_buddy_daddies_vs_anya_spy_x_family/jb2mifc/?context=3

########################################

id = get_rt_id(cur, 'Respect Godwynn (Nocturne of the Heaven) [Nijisanji Kamigakari campaign]', 'https://redd.it/11l19bi')
add_data(['Godwynn'],
'Godwynn',
False,
False,
[
    ['Nocturne of the Heaven'], ['NOTH'], ['Kamigakari'], ['Nijisanji']
],
'Nocturne of the Heaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11l19bi/respect_godwynn_nocturne_of_the_heaven_nijisanji/

########################################

id = get_rt_id(cur, 'Respect St George, the Mighty Dragon (Ex-Heroes)', 'https://redd.it/11iqamq')
add_data(['St\.? George'],
'St. George',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11iqamq/respect_st_george_the_mighty_dragon_exheroes/

########################################

id = get_rt_id(cur, 'Respect Garfield (The Animation Picture Company trilogy)', 'https://redd.it/11iuf93')
add_data(['Garfield'],
'Garfield',
False,
False,
[
    ['Animation Picture Company']
],
'The Animation Picture Company',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11iuf93/respect_garfield_the_animation_picture_company/

########################################

id = get_rt_id(cur, 'Respect Saiko Bichitaru! (SMG4)', 'https://redd.it/11iyoh0')
add_data(['Saiko Bichitaru'],
'Saiko Bichitaru',
False,
True,
[
    ['SMG4'], ['SuperMarioGlitchy4']
],
'SMG4 Bloopers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11iyoh0/respect_saiko_bichitaru_smg4/


########################################

id = get_rt_id(cur, 'Respect Billy (Undead Unluck)', 'https://redd.it/11iyuek')
add_data(['Billy'],
'Billy',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11iyuek/respect_billy_undead_unluck/


########################################

id = get_rt_id(cur, 'Respect Anno Un (Undead Unluck)', 'https://redd.it/11jzt2l')
add_data(['Anno Un'],
'Anno Un',
False,
True,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jzt2l/respect_anno_un_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect the Egyptian God Cards (Yu-Gi-Oh! Anime)', 'https://redd.it/11ia22m')
add_data(['Egyptian God Cards?'],
'Egyptian God Cards',
True,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Egyptian Gods'],
'Egyptian Gods',
True,
False,
[
    ['Yu(-| )?Gi(-| )?Oh'], ['Slifer']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ia22m/respect_the_egyptian_god_cards_yugioh_anime/


add_data(['Slifer'],
'Slifer',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ia22m/respect_the_egyptian_god_cards_yugioh_anime/

add_data(['Slifer the Sky Dragon'],
'Slifer the Sky Dragon',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ia22m/respect_the_egyptian_god_cards_yugioh_anime/

add_data(['Obelisk the Tormentor'],
'Obelisk the Tormentor',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ia22m/respect_the_egyptian_god_cards_yugioh_anime/

add_data(['Winged Dragon of Ra'],
'Winged Dragon of Ra',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ia22m/respect_the_egyptian_god_cards_yugioh_anime/

########################################

id = get_rt_id(cur, 'Respect Dark Magician Girl (Yu-Gi-Oh! Anime)', 'https://redd.it/11ibzwf')
add_data(['Dark Magician Girl'],
'Dark Magician Girl',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ibzwf/respect_dark_magician_girl_yugioh_anime/

########################################

id = get_rt_id(cur, 'Respect Dark Magician (Yu-Gi-Oh! Anime)', 'https://redd.it/11jwzzi')
add_data(['Dark Magician'],
'Dark Magician',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ibzwf/respect_dark_magician_girl_yugioh_anime/

########################################

id = get_rt_id(cur, 'Respect Magical Hats (Yu-Gi-Oh! Anime)', 'https://redd.it/11icny2')
add_data(['Magical Hats'],
'Magical Hats',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yugi Muto (Yu-Gi-Oh! Anime)', 'https://redd.it/11jwzxi')
add_data(['Yugi Muto'],
'Yugi Muto',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jwzxi/respect_yugi_muto_yugioh_anime/

add_data(['Yugi'],
'Yugi',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jwzxi/respect_yugi_muto_yugioh_anime/

########################################

id = get_rt_id(cur, 'Respect Lloyd Crayton, Doombreaker (DC, Rebirth)', 'https://redd.it/11j5emv')
add_data(['Doombreaker'],
'Doombreaker',
False,
False,
[
    ['Rebirth']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11j5emv/respect_lloyd_crayton_doombreaker_dc_rebirth/

add_data(['Doombreaker'],
'Doombreaker',
False,
False,
[
    ['Lloyd Crayton'], ['DC']
],
'Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11j5emv/respect_lloyd_crayton_doombreaker_dc_rebirth/

########################################

id = get_rt_id(cur, 'Respect Rescue (Marvel Comics)', 'https://redd.it/11j9psl')
add_data(['Rescue'],
'Rescue',
False,
False,
[
    ['Rescue ?\(Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11j9psl/respect_rescue_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect Shadow the Hedgehog (Sonic Boom)', 'https://redd.it/11jaxtd')
add_data(['Shadow the Hedgehog'],
'Shadow the Hedgehog',
False,
False,
[
    ['Sonic Boom']
],
'Sonic Boom',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jaxtd/respect_shadow_the_hedgehog_sonic_boom/

########################################

id = get_rt_id(cur, 'Respect the Sidekicks (Sky High)', 'https://redd.it/11jsk6h')
add_data(['Sidekicks'],
'Sidekicks',
True,
False,
[
    ['Sky High']
],
'Sky High',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jsk6h/respect_the_sidekicks_sky_high/

add_data(['Sidekick'],
'Sidekick',
False,
False,
[
    ['Sky High']
],
'Sky High',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11jsk6h/respect_the_sidekicks_sky_high/


########################################

id = get_rt_id(cur, 'Respect: Supergirl! (Earth-1098)', 'https://redd.it/11k7nvo')
add_data(['Super(-| )?girl'],
'Supergirl',
False,
False,
[
    ['Sky High']
],
'Sky High',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11k7nvo/respect_supergirl_earth1098/

########################################

id = get_rt_id(cur, 'Respect Aang! (Cas van de pol)', 'https://redd.it/11ke3xt')
add_data(['Aang'],
'Aang',
False,
False,
[
    ['Cas van de pol']
],
'Cas van de pol',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ke3xt/respect_aang_cas_van_de_pol/

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

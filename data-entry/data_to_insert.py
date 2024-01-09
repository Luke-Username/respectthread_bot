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

update_respectthread(cur, 1807, 'Respect Lex Luthor (DC Comics, Post-Crisis)', 'https://redd.it/18xqo80')

########################################

add_data(['Wolverine'],
'Wolverine',
False,
False,
[
    ['Days of Future Past'], ['DOFP']
],
'FOX',
'{158,24039}'
)
#https://www.reddit.com/r/whowouldwin/comments/18xsspr/the_terminator_terminator_joins_wolverine_in/kg6at0t/?context=3

add_data(['Magneto'],
'Magneto',
False,
False,
[
    ['Days of Future Past'], ['DOFP']
],
'FOX',
'{152}'
)
#https://www.reddit.com/r/whowouldwin/comments/18xsspr/the_terminator_terminator_joins_wolverine_in/kg6at0t/?context=3

add_data(['Mystique'],
'Mystique',
False,
False,
[
    ['Days of Future Past'], ['DOFP']
],
'FOX',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/18xsspr/the_terminator_terminator_joins_wolverine_in/kg6at0t/?context=3

########################################

id = get_rt_id(cur, 'Respect The Predator (Marvels Wolverine Vs Predator)', 'https://redd.it/18x2i1z')
add_data(['Predator'],
'Predator',
False,
False,
[
    ['Wolverine Vs\.? Predator'], ['Predator vs\.? Wolverine']
],
'Predator vs. Wolverine',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18x2i1z/respect_the_predator_marvels_wolverine_vs_predator/

########################################

id = get_rt_id(cur, 'Respect the Sand King (Epithet Erased)', 'https://redd.it/18x8ph3')
add_data(['Sand King'],
'Sand King',
False,
False,
[
    ['Epithet Erased']
],
'Epithet Erased',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18x8ph3/respect_the_sand_king_epithet_erased/

########################################

id = get_rt_id(cur, 'Respect Metallo (DC Comics, Post-Flashpoint)', 'https://redd.it/18xk3xt')
add_data(['Metallo'],
'Metallo',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18xk3xt/respect_metallo_dc_comics_postflashpoint/

add_data(['Metallo'],
'Metallo',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18xk3xt/respect_metallo_dc_comics_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect Goku (Dragon Ball Kakumei)', 'https://redd.it/18xr0tl')
add_data(['Goku'],
'Goku',
False,
False,
[
    ['Dragon Ball Kakumei']
],
'Dragon Ball Kakumei',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18xr0tl/respect_goku_dragon_ball_kakumei/

########################################

id = get_rt_id(cur, 'Respect Yoshiki Takaishi (Tough)', 'https://redd.it/18xuitb')
add_data(['Yoshiki Takaishi'],
'Yoshiki Takaishi',
False,
False,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18xuitb/respect_yoshiki_takaishi_tough/

########################################

id = get_rt_id(cur, 'Respect Jhin, the Virtuoso (League of Legends)', 'https://redd.it/18ycbm9')
add_data(['Jhin'],
'Jhin',
False,
False,
[
    ['League ?of ?Legends?'], ['LOL']
],
'League of Legends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18ycbm9/respect_jhin_the_virtuoso_league_of_legends/

########################################

id = get_rt_id(cur, 'Respect the Scarred Hunter (Undead Unluck)', 'https://redd.it/18ydln0')
add_data(['Scarred Hunter'],
'Scarred Hunter',
False,
False,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18ydln0/respect_the_scarred_hunter_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect the Condiment King (DC Comics, Post-Crisis)', 'https://redd.it/18z8o5w')
add_data(['Condiment King'],
'Condiment King',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18z8o5w/respect_the_condiment_king_dc_comics_postcrisis/

add_data(['Condiment King'],
'Condiment King',
False,
True,
[
    ['\(DC\)']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18z8o5w/respect_the_condiment_king_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Satono Nishida and Mai Teireida (Touhou)', 'https://redd.it/1903799')
add_data(['Satono Nishida'],
'Satono Nishida',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mai Teireida'],
'Mai Teireida',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Okina Matara (Touhou)', 'https://redd.it/192fzz4')
add_data(['Okina Matara'],
'Okina Matara',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/192fzz4/respect_okina_matara_touhou/

########################################

id = get_rt_id(cur, 'Respect the Plutonium Man (DC Comics)', 'https://redd.it/190anal')
add_data(['Plutonium Man'],
'Plutonium Man',
False,
False,
[
    ['DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/190anal/respect_the_plutonium_man_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Manta, the Flaming Fiend (DC Comics)', 'https://redd.it/190b5kh')
add_data(['Plutonium Man'],
'Plutonium Man',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/190b5kh/respect_manta_the_flaming_fiend_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Uranium (DC Comics)', 'https://redd.it/190br20')
add_data(['Uranium'],
'Uranium',
False,
False,
[
    ['Uranium ?\(DC( Comics)?\)'], ['Uranium ?\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/190br20/respect_uranium_dc_comics/

########################################

id = get_rt_id(cur, 'Respect the Ambassadors (Image Comics)', 'https://redd.it/191tjs2')
add_data(['The Ambassadors'],
'The Ambassadors',
True,
False,
[
    ['Image Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/191tjs2/respect_the_ambassadors_image_comics/

########################################

id = get_rt_id(cur, 'Respect Enjin! (Undead Unluck)', 'https://redd.it/191nglt')
add_data(['Enjin'],
'Enjin',
False,
False,
[
    ['Undead Unluck'], ['Enjin Banba']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/191nglt/respect_enjin_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect the Chopman! (Yu-Gi-Oh!)', 'https://redd.it/190cgjx')
add_data(['Chopman'],
'Chopman',
False,
False,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/190cgjx/respect_the_chopman_yugioh/

########################################

id = get_rt_id(cur, 'Respect Guren! (Naruto [Anime])', 'https://redd.it/1912kjv')
add_data(['Guren'],
'Guren',
False,
False,
[
    ['Naruto']
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Connor (Buffyverse)', 'https://redd.it/19176uq')
add_data(['Connor'],
'Connor',
False,
False,
[
    ['Buffy the Vampire Slayer'], ['\(Buffy\)'], ['Buffyverse']
],
'Buffy the Vampire Slayer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19176uq/respect_connor_buffyverse/

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

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

update_respectthread(cur, 25516, 'Respect Desire of The Endless (DC Comics, The Sandman)', 'https://www.reddit.com/r/DCCosmology/comments/1qm42vb/respect_desire_of_the_endless_dc_comics_the/')

########################################

id = get_rt_id(cur, 'Respect Rui Kanoya (Re:Creators)', 'https://www.reddit.com/r/respectthreads/comments/1qhezxk/respect_rui_kanoya_recreators/')
add_data(['Rui Kanoya'],
'Rui Kanoya',
False,
False,
[
    ['Re(:| )?CREATORS']
],
'Re:CREATORS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Magane Chikujoin (Re:Creators)', 'https://www.reddit.com/r/respectthreads/comments/1qhiy6c/respect_magane_chikujoin_recreators/')
add_data(['Magane Chikujoin'],
'Magane Chikujoin',
False,
False,
[
    ['Re(:| )?CREATORS']
],
'Re:CREATORS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alicetaria February (Re:Creators anime)', 'https://www.reddit.com/r/respectthreads/comments/1qho722/respect_alicetaria_february_recreators_anime/')
add_data(['Alicetaria February'],
'Alicetaria February',
False,
False,
[
    ['Re(:| )?CREATORS']
],
'Re:CREATORS',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Diamond! (Pokemon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1qid8qx/respect_diamond_pokemon_adventures/')
add_data(['Diamond'],
'Diamond',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Pearl! (Pokemon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1qid8yv/respect_pearl_pokemon_adventures/')
add_data(['Pearl'],
'Pearl',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Platinum! (Pokemon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1qisyg4/respect_platinum_pokemon_adventures/')
add_data(['Platinum'],
'Platinum',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alicia Masters, the Spider-Woman (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1qkrqx5/respect_alicia_masters_the_spiderwoman_marvel/')
add_data(['Alicia Masters'],
'Alicia Masters',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dhomochevsky and Iko (Blame!)', 'https://www.reddit.com/r/respectthreads/comments/1ql6lew/respect_dhomochevsky_and_iko_blame/')
add_data(['Dhomochevsky'],
'Dhomochevsky',
False,
False,
[
    ['Blame']
],
'Blame!',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Iko'],
'Iko',
False,
False,
[
    ['Blame!']
],
'Blame!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marty Mcfly/Doc Brown (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1qllegn/respect_marty_mcflydoc_brown_fortnite/')
add_data(['Marty Mcfly'],
'Marty Mcfly',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Doc Brown'],
'Doc Brown',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Micheal Scott/Dwight Schrute (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1qmh4rd/respect_micheal_scottdwight_schrute_fortnite/')
add_data(['Mich(ae|ae)l Scott'],
'Michael Scott',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Dwight Schrute'],
'Dwight Schrute',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yuya Mirokuji and Hangaku (Re:Creators anime)', 'https://www.reddit.com/r/respectthreads/comments/1qlukzw/respect_yuya_mirokuji_and_hangaku_recreators_anime/')
add_data(['Yuya Mirokuji'],
'Yuya Mirokuji',
False,
True,
[
    ['Re(:| )?CREATORS']
],
'Re:CREATORS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Musubi Susono (NOiSE)', 'https://www.reddit.com/r/respectthreads/comments/1qlvmgl/respect_musubi_susono_noise/')
add_data(['Musubi Susono|Susono Musubi'],
'Musubi Susono',
False,
True,
[
    ['NOiSE']
],
'NOiSE',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Susono'],
'Susono',
False,
False,
[
    ['NOiSE']
],
'NOiSE',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Jack Knight, the Seventh Starman (DC Comics, Post-Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1qmr1h9/respect_jack_knight_the_seventh_starman_dc_comics/')
add_data(['Jack Knight'],
'Jack Knight',
False,
False,
[
    ['Starman'], ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Jack Knight'],
'Jack Knight',
False,
False,
[
    ['Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Star Wars: Ewok respect thread(Legends Canon)', 'https://comicvine.gamespot.com/profile/wolfrazer/blog/star-wars-ewok-respect-thread-legends-canon/126732/')
add_data(['Ewok'],
'Ewok',
False,
True,
[
    ['S(tar )?Wars'], ['(1|One) Ewok'], ['with a spear'], ['Endor']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Ewoke?s'],
'Ewoks',
False,
True,
[
    ['S(tar )?Wars'], ['Endor']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1qjuunb/10_ewoks_star_wars_vs_a_navi_avatar/
#https://www.reddit.com/r/whowouldwin/comments/1jcm8xs/pitbull_vs_1_ewok_star_wars/
#https://www.reddit.com/r/whowouldwin/comments/1jxsvxn/when_the_biblical_saul_goes_to_meet_with_the/
#https://www.reddit.com/r/whowouldwin/comments/ek5jmc/danny_devito_with_a_gun_vs_an_ewok_with_a_spear/
#https://www.reddit.com/r/whowouldwin/comments/1dfvlk1/8_year_old_boy_vs_1_ewokstar_wars/


########################################

id = get_rt_id(cur, 'Respect Thalia (Magic: The Gathering)', 'https://www.reddit.com/r/respectthreads/comments/1qo5xgq/respect_thalia_magic_the_gathering/')
add_data(['Thalia'],
'Thalia',
False,
False,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Web-Man (Marvel Comics Earth-55780)', 'https://www.reddit.com/r/respectthreads/comments/1qo5ea8/respect_webman_marvel_comics_earth55780/')
add_data(['Web(-| )Man'],
'Web-Man',
False,
False,
[
    ['55780']
],
'55780',
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

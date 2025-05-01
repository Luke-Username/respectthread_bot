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

id = get_rt_id(cur, 'Respect Odd Thomas (Odd Thomas [2013 Film])', 'https://redd.it/1k7oobj')
add_data(['Odd Thomas'],
'Odd Thomas',
False,
False,
[
    ['(Film|Movie)s?'], ['2013']
],
'2013 Film',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Wattson (Pokemon Anime)', 'https://redd.it/1k7qra8')
add_data(['Wattson'],
'Wattson',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k7qra8/respect_wattson_pokemon_anime/


########################################

id = get_rt_id(cur, 'Respect Nero the Whiscash (Pokemon Anime)', 'https://redd.it/1ka7iuv')
add_data(['Nero the Whiscash'],
'Nero the Whiscash',
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

id = get_rt_id(cur, 'Respect Aura Sphere Riolu (Pokemon Anime)', 'https://redd.it/1kanb2l')
add_data(['Aura Sphere Riolu'],
'Aura Sphere Riolu',
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

id = get_rt_id(cur, "Respect Guy''s Exploud (Pokemon Anime)", 'https://redd.it/1k8d58l')
add_data(['Exploud'],
'Exploud',
False,
False,
[
    ['Guy']
],
'Guy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k8d58l/respect_guys_exploud_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Computer Jack (Gone)', 'https://redd.it/1k8s65p')
add_data(['Computer Jack'],
'Computer Jack',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Orc (Gone)', 'https://redd.it/1kb72lu')
add_data(['Orc'],
'Orc',
False,
False,
[
    ['Orc ?\(Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kb72lu/respect_orc_gone/


########################################

id = get_rt_id(cur, 'Respect Tsurugi Kamishiro/Scorpio Worm (Kamen Rider Kabuto)', 'https://redd.it/1k8vpqj')
add_data(['Scorpio Worm'],
'Scorpio Worm',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tsurugi Kamishiro'],
'Tsurugi Kamishiro',
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

id = get_rt_id(cur, 'Respect Dark Kabuto (Kamen Rider Kabuto)', 'https://redd.it/1kabu0h')
add_data(['Dark Kabuto'],
'Dark Kabuto',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Takamura (Sakamoto Days)', 'https://redd.it/1k9fhny')
add_data(['Takamura'],
'Takamura',
False,
False,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9fhny/respect_takamura_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect the Death Star (Star Wars Legends)', 'https://redd.it/1k9wr8s')
add_data(['Death Star'],
'Death Star',
False,
True,
[
    ['S(tar )?Wars'], ['Vader']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9wr8s/respect_the_death_star_star_wars_legends/

add_data(['Deathstar'],
'Deathstar',
False,
False,
[
    ['S(tar )?Wars'], ['plans'], ['episode'], ['Vader'], ['Destroy']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9wr8s/respect_the_death_star_star_wars_legends/

########################################

id = get_rt_id(cur, 'Respect Mosquito (Loop Hero)', 'https://redd.it/1k9t3fb')
add_data(['Mosquitos'],
'Mosquitos',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9t3fb/respect_mosquito_loop_hero/

########################################

id = get_rt_id(cur, 'Respect Witch (Loop Hero)', 'https://redd.it/1k9tci6')
add_data(['Witch'],
'Witch',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9t3fb/respect_mosquito_loop_hero/

########################################

id = get_rt_id(cur, 'Respect Scarecrow (Loop Hero)', 'https://redd.it/1k9thj9')
add_data(['Scarecrow'],
'Scarecrow',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1k9t3fb/respect_mosquito_loop_hero/

########################################

id = get_rt_id(cur, 'Respect The Womb Ripper (Bloodwash)', 'https://redd.it/1kapd98')
add_data(['Womb Ripper'],
'Womb Ripper',
False,
False,
[
    ['Bloodwash']
],
'Bloodwash',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kapd98/respect_the_womb_ripper_bloodwash/

########################################

id = get_rt_id(cur, 'Respect Cecily Bain! (Vampire: the Masquerade)', 'https://redd.it/1kasowf')
add_data(['Cecily Bain'],
'Cecily Bain',
False,
True,
[
    ['Vampire:? the Masquerade'], ['VTM']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Duke (Image Comics, Energon Universe)', 'https://redd.it/1kbju5q')
add_data(['Duke'],
'Duke',
False,
False,
[
    ['Energon Universe']
],
'Energon Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kbju5q/respect_duke_image_comics_energon_universe/

########################################

id = get_rt_id(cur, 'Respect Julith (Dofus)', 'https://redd.it/1kbq345')
add_data(['Julith'],
'Julith',
False,
False,
[
    ['Dofus']
],
'Dofus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kbq345/respect_julith_dofus/

########################################

id = get_rt_id(cur, 'Respect Kilowog, the Green Lantern (DC Comics, Post-Crisis)', 'https://redd.it/1kbtvtu')
add_data(['Kilowog'],
'Kilowog',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Kilowog'],
'Kilowog',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kbtvtu/respect_kilowog_the_green_lantern_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Zatanna Zatara (DC, Post-Flashpoint)', 'https://redd.it/1kc0qti')
add_data(['Zatanna'],
'Zatanna',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kc0qti/respect_zatanna_zatara_dc_postflashpoint/

########################################

id = get_rt_id(cur, "Respect Max (Man''s Best Friend)", 'https://redd.it/1kc846s')
add_data(['Max'],
'Max',
False,
False,
[
    ["Man''?s Best Friend"]
],
"Man''s Best Friend",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kc846s/respect_max_mans_best_friend/

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

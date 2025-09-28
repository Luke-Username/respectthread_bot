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

# https://www.reddit.com/r/whowouldwin/comments/1nsije6/xmen_1992_cartoon_juggernaut_vs_mcu_thanos/ngmo8ni/?context=3
update_respectthread(cur, 24971, 'X-Men the animated series feats.', 'https://comicvine.gamespot.com/forums/feats-and-analysis-2311599/x-men-the-animated-series-feats-2340196/')

update_respectthread(cur, 5477, 'Respect The Pyro (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1npk10x/respect_the_pyro_team_fortress_2/')

########################################

id = get_rt_id(cur, 'Respect The Poliwag Line (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1npbihf/respect_the_poliwag_line_pokemon_anime/')
add_data(['Poliwag'],
'Poliwag',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Poliwrath'],
'Poliwrath',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Megalon (GEMSTONE)', 'https://www.reddit.com/r/respectthreads/comments/1npd9z1/respect_megalon_gemstone/')
add_data(['Megalon'],
'Megalon',
False,
False,
[
    ['GEMSTONE'], ['Godzilla vs\.? Megalon', '2023']
],
'GEMSTONE',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Maxwell Lord (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1nq8r82/respect_maxwell_lord_dc_comics_postflashpoint/')
add_data(['Maxwell Lord'],
'Maxwell Lord',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Maxwell Lord'],
'Maxwell Lord',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}, 1660'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shen Zhengdao (Ne Zha 2)', 'https://www.reddit.com/r/respectthreads/comments/1nqeaol/respect_shen_zhengdao_ne_zha_2/')
add_data(['Shen Zhengdao'],
'Shen Zhengdao',
False,
True,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Deero & Crana (Ne Zha 2)', 'https://www.reddit.com/r/respectthreads/comments/1nrvi6u/respect_deero_crana_ne_zha_2/')
add_data(['Deero'],
'Deero',
False,
False,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Crana'],
'Crana',
False,
False,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#


add_data(['Deero (&|and) Crana'],
'Deero & Crana',
True,
True,
[
    ['Ne Zha']
],
'Ne Zha',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Superman! (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1nqs1r0/respect_superman_fortnite/')
add_data(['Super(-| )?man'],
'Superman',
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

id = get_rt_id(cur, 'Respect Sandy Balgan(Flight)', 'https://www.reddit.com/r/respectthreads/comments/1nrjqg6/respect_sandy_balganflight/')
add_data(['Sandy Balgan'],
'Sandy Balgan',
False,
False,
[
    ['Flight']
],
'Flight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Morgan Le Fay (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nrmrq5/respect_morgan_le_fay_fategrand_order/')
add_data(['Morgan Le Fay'],
'Morgan Le Fay',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Melusine/Tam Lin Lancelot (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nsbcys/respect_melusinetam_lin_lancelot_fategrand_order/')
add_data(['Melusine'],
'Melusine',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tam Lin Lancelot'],
'Tam Lin Lancelot',
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

id = get_rt_id(cur, 'Respect the Valkyria Underground Fighting Organization! (Star: Strike It Rich!)', 'https://www.reddit.com/r/respectthreads/comments/1nrmyf9/respect_the_valkyria_underground_fighting/')
add_data(['Valkyria Underground Fighting Organization'],
'Valkyria Underground Fighting Organization',
True,
True,
[
    ['Strike It Rich']
],
'Star: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tenma Nozomi'],
'Tenma Nozomi',
False,
False,
[
    ['Strike It Rich']
],
'Star: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lee Yuzuha'],
'Lee Yuzuha',
False,
False,
[
    ['Strike It Rich']
],
'Star: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Yukihira Sara'],
'Yukihira Sara',
False,
False,
[
    ['Strike It Rich']
],
'Star: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gwen Stacy AKA Weapon X-31 AKA Gwenpool (Marvel Comics, Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/1nsa58t/respect_gwen_stacy_aka_weapon_x31_aka_gwenpool/')
add_data(['Weapon X-?31'],
'Weapon X-31',
False,
False,
[
    ['616|Gwen(pool)?|Marvel']
],
'616',
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

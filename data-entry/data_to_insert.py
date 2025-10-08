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

update_respectthread(cur, 1338, 'Respect Trivia Vanille/Neopolitan (RWBY)', 'https://www.reddit.com/r/respectthreads/comments/1nz88xe/respect_trivia_vanilleneopolitan_rwby/')
update_respectthread(cur, 2498, 'Respect Owen Reece, the Molecule Man (Marvel Comics, Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/1nzy4q1/respect_owen_reece_the_molecule_man_marvel_comics/')
update_respectthread(cur, 591, "Respect Eddie Brock/Venom (Sony''s Spider-Man Universe)", 'https://www.reddit.com/r/respectthreads/comments/1o02up4/respect_eddie_brockvenom_sonys_spiderman_universe/')
update_respectthread(cur, 17487, 'Respect Alexei Shostakov, The Red Guardian (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/1o0cklm/respect_alexei_shostakov_the_red_guardian_marvel/')

########################################

add_data(['Titus'],
'Titus',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{9241}'
)
#https://www.reddit.com/r/whowouldwin/comments/1o0c10z/bumblebee_transformers_vs_titus_wh40k/ni88a88/?context=3

########################################

add_data(['HUNTRiX'],
'HUNTRiX',
True,
False,
[
    ['Rumi|Mina|Zoey']
],
'KPop Demon Hunters',
'{26193}'
)
#https://www.reddit.com/r/whowouldwin/comments/1o1c56o/huntrix_vs_the_ninja_turtles/nifhjyi/?context=3

########################################

id = get_rt_id(cur, 'Respect Bubba Ritter, The Scarecrow (Dark Night of the Scarecrow)', 'https://www.reddit.com/r/respectthreads/comments/1nzhlfx/respect_bubba_ritter_the_scarecrow_dark_night_of/')
add_data(['Bubba Ritter'],
'Bubba Ritter',
False,
True,
[
    ['Dark Night of the Scarecrow']
],
'Dark Night of the Scarecrow',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Scare ?crow,Scarecrow'],
'Scarecrow',
False,
False,
[
    ['Scarecrow.*Dark Night of the Scarecrow']
],
'Dark Night of the Scarecrow',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect T-A.L.O.S. (Resident Evil: Umbrella Chronicles)', 'https://www.reddit.com/r/respectthreads/comments/1nzwfx5/respect_talos_resident_evil_umbrella_chronicles/')
add_data(['T-A\.L\.O\.S'],
'T-A.L.O.S.',
False,
False,
[
    ['Resident Evil', 'Umbrella Chronicles']
],
'Resident Evil: Umbrella Chronicles',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect the Xenophage (Sony''s Spider-Man Universe)", 'https://www.reddit.com/r/respectthreads/comments/1o0368o/respect_the_xenophage_sonys_spiderman_universe/')
add_data(['Xenophage'],
'Xenophage',
False,
False,
[
    ['Sony'], ['Last Dance']
],
'Sony',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect John O''Malley! (Hunter: the Reckoning)", 'https://www.reddit.com/r/respectthreads/comments/1o0evcl/respect_john_omalley_hunter_the_reckoning/')
add_data(["John O(''| )Malley"],
"John O''Malley",
False,
False,
[
    ['World of Darkness'], ['Hunter:? the Reckoning']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Michael Myers (Call of Duty)', 'https://www.reddit.com/r/respectthreads/comments/1o0x444/respect_michael_myers_call_of_duty/')
add_data(['Mich(ae|ea)l Me?y(er|re)s'],
'Michael Myers',
False,
False,
[
    ['Call of Duty']
],
'Call of Duty',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zero (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1o19utg/respect_zero_pokemon_anime/')
add_data(['Zero'],
'Zero',
False,
False,
[
    ['Zero ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rok Buran (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/1o1l9gk/respect_rok_buran_star_wars_canon/')
add_data(['Rok Buran'],
'Rok Buran',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
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

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

update_respectthread(cur, 12106, "Respect Kumoko! (So I''m a Spider, So What? [Manga])", 'https://redd.it/1dg4t9o')

########################################

add_data(['Reva'],
'Reva',
False,
False,
[
    ['Obi(-| )Wan'], ['Kenobi']
],
'Star Wars',
'{22447}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ddctvp/mae_the_acolyte_vs_reva_obiwan_kenobi/l83u6i4/?context=3

########################################

add_data(['Goku'],
'Goku',
False,
False,
[
    ['Aang', 'Goku.*Live Action'], ['Goku.*Dragonball.*Live Action']
],
'Dragonball Evolution',
'{418}'
)
#https://www.reddit.com/r/whowouldwin/comments/1deonfc/goku_dragonball_vs_aang_avatar_but_its_the_live/

########################################

add_data(['Kai'],
'Kai',
False,
False,
[
    ['Kai the Collector']
],
'Kung Fu Panda',
'{1144}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ddbiqq/kai_the_collector_kung_fu_pands_3_vs_master_yoda/

########################################

id = get_rt_id(cur, 'Respect Tank Girl! (Tank Girl, 1995 Movie)', 'https://redd.it/1dcph1n')
add_data(['Tank Girl'],
'Tank Girl',
False,
False,
[
    ['1995'], ['Tank Girl.*(Film|Movie)']
],
'1995',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dcph1n/respect_tank_girl_tank_girl_1995_movie/

########################################

id = get_rt_id(cur, 'Respect: Super Mom! (Coca-Cola Commercials)', 'https://redd.it/1dcw9kz')
add_data(['Super Mom'],
'Super Mom',
False,
False,
[
    ['Coca(-| )Cola'], ['Coke']
],
'Coca-Cola',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dcw9kz/respect_super_mom_cocacola_commercials/

########################################

id = get_rt_id(cur, 'Respect Kavik (Avatar: The Yangchen Novels)', 'https://redd.it/1ddlqi8')
add_data(['Kavik'],
'Kavik',
False,
False,
[
    ['Yangchen'], ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ddlqi8/respect_kavik_avatar_the_yangchen_novels/

########################################

id = get_rt_id(cur, 'Respect Jujinta (Avatar: The Yangchen Novels)', 'https://redd.it/1degxpx')
add_data(['Jujinta'],
'Jujinta',
False,
False,
[
    ['Yangchen'], ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1degxpx/respect_jujinta_avatar_the_yangchen_novels/

########################################

id = get_rt_id(cur, 'Respect Meatwad (Aqua Teen Hunger Force)', 'https://redd.it/1ddn1l0')
add_data(['Meatwad'],
'Meatwad',
False,
False,
[
    ['Aqua Teen Hunger Force'], ['ATHF']
],
'Aqua Teen Hunger Force',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ddn1l0/respect_meatwad_aqua_teen_hunger_force/

########################################

id = get_rt_id(cur, 'Respect Shan Zhu (Fog Hill of Five Elements)', 'https://redd.it/1ddu4hu')
add_data(['Shan Zhu'],
'Shan Zhu',
False,
False,
[
    ['Fog Hill of Five Elements']
],
'Fog Hill of Five Elements',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ddu4hu/respect_shan_zhu_fog_hill_of_five_elements/

########################################

id = get_rt_id(cur, "Respect Brock''s Geodude (Pokemon Anime)", 'https://redd.it/1deyoxc')
add_data(['Geodude'],
'Geodude',
False,
True,
[
    ['Pok(e|é)m(o|a)n'], ['Brock']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1deyoxc/respect_brocks_geodude_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect Misty''s Goldeen (Pokemon Anime)", 'https://redd.it/1dfosjn')
add_data(['Goldeen'],
'Goldeen',
False,
True,
[
    ['Pok(e|é)m(o|a)n'], ['Misty']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dfosjn/respect_mistys_goldeen_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Santa Claus (SCP Foundation) [The Alpha-9 Holiday Special]', 'https://redd.it/1dfag69')
add_data(['Santa Clause?'],
'Santa Claus',
False,
False,
[
    ['Alpha-9 Holiday Special']
],
'The Alpha-9 Holiday Special',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dfag69/respect_santa_claus_scp_foundation_the_alpha9/

########################################

id = get_rt_id(cur, 'Respect Optimus Prime (Image Comics, Energon Universe)', 'https://redd.it/1dfbl8a')
add_data(['Optimus Prime'],
'Optimus Prime',
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

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

add_data(['Trunks'],
'Trunks',
False,
False,
[
    ['Future Trunks']
],
'Dragon Ball',
'{3284,22116}'
)
#https://www.reddit.com/r/whowouldwin/comments/12xfhxs/future_trunks_and_buu_replace_tien_and_krillen/jhilg47/?context=3

########################################

add_data(['Ben'],
'Ben',
False,
False,
[
    ['Rey', 'S(tar )?Wars']
],
'Star Wars',
'{325, 12433}'
)
#

########################################

id = get_rt_id(cur, "Kas''im Respect Thread", 'https://comicvine.gamespot.com/profile/wollfmyth209/blog/kasim-respect-thread/109082/')
add_data(["Kas''im"],
"Kas''im",
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1301hsp/rey_and_kylo_ren_vs_kasim/jhuf4zi/?context=3

########################################

id = get_rt_id(cur, 'Respect Arika McClure (Fine Structure)', 'https://redd.it/12wy5gg')
add_data(['Arika McClure'],
'Arika McClure',
False,
True,
[
    ['Fine Structure']
],
'Fine Structure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12wy5gg/respect_arika_mcclure_fine_structure/

########################################

id = get_rt_id(cur, 'Respect Jason Chilton (Fine Structure)', 'https://redd.it/12wy5x8')
add_data(['Jason Chilton'],
'Jason Chilton',
False,
False,
[
    ['Fine Structure']
],
'Fine Structure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12wy5x8/respect_jason_chilton_fine_structure/

########################################

id = get_rt_id(cur, 'Respect Entity 99, "The Game Master" (The Backrooms, Wikidot)', 'https://redd.it/12x0sic')
add_data(['Entity 99'],
'Entity 99',
False,
False,
[
    ['Backrooms']
],
'The Backrooms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12x0sic/respect_entity_99_the_game_master_the_backrooms/

add_data(['Game Master'],
'Game Master',
False,
False,
[
    ['Backrooms']
],
'The Backrooms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12x0sic/respect_entity_99_the_game_master_the_backrooms/

########################################

id = get_rt_id(cur, 'Respect Entity 67, The Sanguine Festivus (The Backrooms, Fandom)', 'https://redd.it/12y23rp')
add_data(['Entity 67'],
'Entity 67',
False,
False,
[
    ['Backrooms']
],
'The Backrooms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12y23rp/respect_entity_67_the_sanguine_festivus_the/

add_data(['Sanguine Festivus'],
'Sanguine Festivus',
False,
True,
[
    ['Backrooms']
],
'The Backrooms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12x0sic/respect_entity_99_the_game_master_the_backrooms/

########################################

id = get_rt_id(cur, "Respect Trini Kwan, the Yellow Ranger (Mighty Morphin'' Power Rangers)", 'https://redd.it/12xasyn')
add_data(['Trini'],
'Trini',
False,
False,
[
    ['Power Rangers?'], ['Trini Kwan'], ['Yellow Ranger']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xasyn/respect_trini_kwan_the_yellow_ranger_mighty/

########################################

id = get_rt_id(cur, "Respect Zack Taylor, the Black Ranger (Mighty Morphin'' Power Rangers)", 'https://redd.it/12zeuo1')
add_data(['Zack Taylor'],
'Zack Taylor',
False,
True,
[
    ['Power Rangers?'], ['Black Ranger']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12zeuo1/respect_zack_taylor_the_black_ranger_mighty/

########################################

id = get_rt_id(cur, 'Respect Countess Carmilla Karstein (Carmilla)', 'https://redd.it/12xh7qn')
add_data(['Carmilla Karstein'],
'Carmilla Karstein',
False,
True,
[
    ['Carmilla']
],
'Carmilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xh7qn/respect_countess_carmilla_karstein_carmilla/

add_data(['Carmilla'],
'Carmilla',
False,
False,
[
    ['Carmilla ?\(Carmilla']
],
'Carmilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xh7qn/respect_countess_carmilla_karstein_carmilla/

add_data(['Carmilla'],
'Carmilla',
False,
False,
[
    ['Castle(-| )?vania']
],
'Castlevania',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/12xh7qn/respect_countess_carmilla_karstein_carmilla/

########################################

id = get_rt_id(cur, 'Respect Nanao, AKA Ladybug! (Bullet Train/Maria Beetle)', 'https://redd.it/12xq90k')
id2 = get_rt_id(cur, 'Respect Ladybug! (Bullet Train)', 'https://redd.it/12xq9sa')
add_data(['Ladybug'],
'Ladybug',
False,
False,
[
    ['Bullet Train'], ['Maria Beetle']
],
'Bullet Train',
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xq90k/respect_nanao_aka_ladybug_bullet_trainmaria_beetle/

add_data(['Nanao'],
'Nanao',
False,
False,
[
    ['Bullet Train'], ['Maria Beetle']
],
'Bullet Train',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xq90k/respect_nanao_aka_ladybug_bullet_trainmaria_beetle/

########################################

id = get_rt_id(cur, 'Respect Shaun (Shaun of the Dead)', 'https://redd.it/12xr8eb')
add_data(['Shaun'],
'Shaun',
False,
False,
[
    ['Shaun of the Dead']
],
'Shaun of the Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12xr8eb/respect_shaun_shaun_of_the_dead/


########################################

id = get_rt_id(cur, 'Respect Charlie Bucket (Chili and the Chocolate Factory: Fudge Revelation)', 'https://redd.it/12yj6h6')
add_data(['Charlie Bucket'],
'Charlie Bucket',
False,
False,
[
    ['Chili and the Chocolate Factory']
],
'Chili and the Chocolate Factory',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12yj6h6/respect_charlie_bucket_chili_and_the_chocolate/

########################################

id = get_rt_id(cur, 'Respect Terrako (Hyrule Warriors: Age of Calamity)', 'https://redd.it/12zg92e')
add_data(['Terrako'],
'Terrako',
False,
False,
[
    ['Hyrule Warriors']
],
'Hyrule Warriors',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12zg92e/respect_terrako_hyrule_warriors_age_of_calamity/

########################################

id = get_rt_id(cur, 'Respect Nate Sutter! (The Candy Shop War)', 'https://redd.it/12zz7n8')
add_data(['Nate Sutter'],
'Nate Sutter',
False,
False,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12zz7n8/respect_nate_sutter_the_candy_shop_war/

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

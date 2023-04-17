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

update_respectthread(cur, 1998, 'Respect Sentry! (Marvel, 616) [Pre-Siege]', 'https://redd.it/12pkjc3')

########################################

id = get_rt_id(cur, 'Respect Absalom (One Piece)', 'https://redd.it/12nsvky')
add_data(['Absalom'],
'Absalom',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12nsvky/respect_absalom_one_piece/

########################################

id = get_rt_id(cur, 'Respect Dellinger (One Piece)', 'https://redd.it/12oixl1')
add_data(['Dellinger'],
'Dellinger',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12oixl1/respect_dellinger_one_piece/

########################################

id = get_rt_id(cur, 'Respect Rolo Lamperouge! (Code Geass (Anime Timeline))', 'https://redd.it/12okpwd')
add_data(['Rolo'],
'Rolo',
False,
False,
[
    ['Lamperouge'], ['Code Geass']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12okpwd/respect_rolo_lamperouge_code_geass_anime_timeline/

########################################

id = get_rt_id(cur, 'Respect Kallen Kozuki! (Code Geass (Anime Timeline))', 'https://redd.it/12pry8l')
add_data(['Kallen'],
'Kallen',
False,
False,
[
    ['Code Geass'], ['Guren'], ['Kozuki|Stadtfeld']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12pry8l/respect_kallen_kozuki_code_geass_anime_timeline/

########################################

id = get_rt_id(cur, 'Respect Jeremiah Gottwald! (Code Geass (Anime Timeline))', 'https://redd.it/12ptgvn')
add_data(['Jeremiah'],
'Jeremiah',
False,
False,
[
    ['Code Geass'], ['Cyborg Jeremiah'], ['Gottwald']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12ptgvn/respect_jeremiah_gottwald_code_geass_anime/

########################################

id = get_rt_id(cur, 'The 98th Emperor of the Holy Britannian Empire, Charles zi Britannia (Code Geass (Anime Timeline))', 'https://redd.it/12oqgn5')
add_data(['Charles (zi|of) Britannia'],
'Charles zi Britannia',
False,
True,
[
    ['Code Geass']
],
'Code Geass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12oqgn5/the_98th_emperor_of_the_holy_britannian_empire/

########################################

id = get_rt_id(cur, 'Respect Paul "Pigeon" Bowlen! (The Candy Shop War)', 'https://redd.it/12omxx6')
add_data(['Pigeon'],
'Pigeon',
False,
False,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12omxx6/respect_paul_pigeon_bowlen_the_candy_shop_war/

########################################

id = get_rt_id(cur, 'Respect Trevor! (The Candy Shop War)', 'https://redd.it/12pyjk1')
add_data(['Trevor'],
'Trevor',
False,
False,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12pyjk1/respect_trevor_the_candy_shop_war/

########################################

id = get_rt_id(cur, 'Respect John Dart! (The Candy Shop War)', 'https://redd.it/12omzmg')
add_data(['John Dart'],
'John Dart',
False,
False,
[
    ['Candy Shop War']
],
'The Candy Shop War',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect M.O.D.O.K. (Marvel Cinematic Universe)', 'https://redd.it/12omzy4')
add_data(['M\.?O\.?D\.?O\.?K'],
'M.O.D.O.K',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12omzy4/respect_modok_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect John Smith (Hitman: Agent 47)', 'https://redd.it/12oot77')
add_data(['John Smith'],
'John Smith',
False,
False,
[
    ['Hitman']
],
'Hitman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12oot77/respect_john_smith_hitman_agent_47/

########################################

id = get_rt_id(cur, 'Respect Knuckles! (Sonic the Comic)', 'https://redd.it/12owyyq')
add_data(['Knuckles'],
'Knuckles',
False,
False,
[
    ['Sonic the Comic']
],
'Sonic the Comic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12owyyq/respect_knuckles_sonic_the_comic/

########################################

id = get_rt_id(cur, 'Respect Jake Vietnam (The Hidden Wizard)', 'https://redd.it/12plru5')
add_data(['Jake Vietnam'],
'Jake Vietnam',
False,
True,
[
    ['The Hidden Wizard']
],
'The Hidden Wizard',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12plru5/respect_jake_vietnam_the_hidden_wizard/

########################################

id = get_rt_id(cur, 'Respect The Thing (The Thing from Another World)', 'https://redd.it/12pjruz')
add_data(['The Thing'],
'The Thing',
False,
False,
[
    ['from Another World']
],
'The Thing from Another World',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12pjruz/respect_the_thing_the_thing_from_another_world/

########################################

id = get_rt_id(cur, 'Respect Sentry! (Marvel, 21119, What If Norman Osborn Won Siege)', 'https://redd.it/12pk142')
add_data(['Sentry'],
'Sentry',
False,
False,
[
    ['21119'], ['What If', 'Norman Osborn Won.*Siege']
],
'21119',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12pk142/respect_sentry_marvel_21119_what_if_norman_osborn/

########################################

id = get_rt_id(cur, 'Respect Gaismagorm! (Monster Hunter)', 'https://redd.it/12pudji')
add_data(['Gaismagorm'],
'Gaismagorm',
False,
True,
[
    ['Monster Hunter']
],
'Monster Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12pudji/respect_gaismagorm_monster_hunter/

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

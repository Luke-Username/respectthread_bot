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

update_respectthread(cur, 2395, 'Respect Juggernaut! (Marvel, 616)', 'https://redd.it/13x7kbz')

########################################

add_data(['Space ?Marines?'],
'Space Marine',
False,
False,
[
    ['Ultra ?marines?'], ['Bolter|Chainsword']
],
'Warhammer 40k',
'{21139,6466}'
)
#https://www.reddit.com/r/whowouldwin/comments/13x7jhp/in_a_fight_between_avatar_kyoshi_and_a_regular/jmg0ve1/?context=3

########################################

add_data(['Flashpoint Superman'],
'Flashpoint Superman',
False,
True,
[
    ['DC']
],
'',
'{22457}'
)
#https://www.reddit.com/r/whowouldwin/comments/13xccn3/current_deku_my_hero_academia_vs_flashpoint/

########################################

id = get_rt_id(cur, 'Respect Death (Have A Nice Death)', 'https://redd.it/13w6bvh')
add_data(['Death'],
'Death',
False,
False,
[
    ['Have A Nice Death']
],
'Have A Nice Death',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13w6bvh/respect_death_have_a_nice_death/

########################################

id = get_rt_id(cur, 'Respect: Uriel Ventris (Warhammer 40k)', 'https://redd.it/13wayx7')
add_data(['Uriel Ventris'],
'Uriel Ventris',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13wayx7/respect_uriel_ventris_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect: Marneus Calgar (Warhammer 40k)', 'https://redd.it/13x44fa')
add_data(['Marneus Calgar'],
'Marneus Calgar',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13x44fa/respect_marneus_calgar_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect the Ex-Virus (Ex-Heroes)', 'https://redd.it/13wueyi')
add_data(['Ex-Virus'],
'Ex-Virus',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13wueyi/respect_the_exvirus_exheroes/

########################################

id = get_rt_id(cur, 'Respect Jervis Tetch, the Mad Hatter (DC Comics, Post Crisis)', 'https://redd.it/13wlm7m')
add_data(['Mad Hatter'],
'Mad Hatter',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13wlm7m/respect_jervis_tetch_the_mad_hatter_dc_comics/

add_data(['Mad Hatter'],
'Mad Hatter',
False,
False,
[
    ['Mad Hatter ?\(DC( Comics)?\)'], ['Mad Hatter ?\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13wlm7m/respect_jervis_tetch_the_mad_hatter_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Baron Blood (Marvel 616)', 'https://redd.it/13xhp4z')
add_data(['Baron Blood'],
'Baron Blood',
False,
False,
[
    ['\(Marvel\)'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13xhp4z/respect_baron_blood_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Darkoth the Death-Demon (Marvel, Earth-616)', 'https://redd.it/13xkk7w')
add_data(['Darkoth'],
'Darkoth',
False,
True,
[
    ['\(Marvel\)'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13xkk7w/respect_darkoth_the_deathdemon_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect Reed Richards (Marvel, Earth X)', 'https://redd.it/13xhow1')
add_data(['Reed Richards'],
'Reed Richards',
False,
False,
[
    ['Earth X']
],
'Earth X',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13xhow1/respect_reed_richards_marvel_earth_x/

########################################

id = get_rt_id(cur, 'Respect Night Man (Malibu Comics)', 'https://redd.it/13xhozu')
add_data(['Night Man'],
'Night Man',
False,
False,
[
    ['Malibu']
],
'Malibu Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/13xhozu/respect_night_man_malibu_comics/

########################################

id = get_rt_id(cur, 'Respect the Tomatoes (Attack of the Killer Tomatoes)', 'https://redd.it/13xpm7q')
add_data(['Tomatoes'],
'Tomatoes',
False,
False,
[
    ['Attack of the Killer Tomatoes']
],
'Attack of the Killer Tomatoes',
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

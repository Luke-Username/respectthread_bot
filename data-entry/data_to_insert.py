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

add_data(['Marik'],
'Marik',
False,
False,
[
    ['YGO']
],
'Yu-Gi-Oh!',
'{4632}'
)
#

########################################

add_data(['Odin'],
'Odin',
False,
False,
[
    ['Prose Edda'], ['Poetic Edda'], ['Gesta Danorum']
],
'Norse Mythology',
'{23549}'
)
#https://www.reddit.com/r/whowouldwin/comments/1edqfim/zeus_vs_odin/lf9wl9l/?context=3

########################################

id = get_rt_id(cur, 'Respect the Maternal Wraith (I Heard It Too)', 'https://redd.it/1e9ekqu')
add_data(['Maternal Wraith'],
'Maternal Wraith',
False,
True,
[
    ['I Heard It Too']
],
'I Heard It Too',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1e9ekqu/respect_the_maternal_wraith_i_heard_it_too/

########################################

id = get_rt_id(cur, 'Respect The Monstrous Visitor (Pleasant Inn)', 'https://redd.it/1eabc8t')
add_data(['Monstrous Visitor'],
'Monstrous Visitor',
False,
False,
[
    ['Pleasant Inn']
],
'Pleasant Inn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eabc8t/respect_the_monstrous_visitor_pleasant_inn/

########################################

id = get_rt_id(cur, 'Respect Leodo! (Ultraman Arc)', 'https://redd.it/1ebjhbr')
add_data(['Leodo'],
'Leodo',
False,
False,
[
    ['Ultraman']
],
'Ultraman Arc',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ebjhbr/respect_leodo_ultraman_arc/

########################################

id = get_rt_id(cur, 'Respect Elvira (Elvira, Mistress of the Dark)', 'https://redd.it/1ecf6i2')
add_data(['Elvira'],
'Elvira',
False,
False,
[
    ['Mistress of the Dark'], ['Film|Movie']
],
'Elvira, Mistress of the Dark',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ecf6i2/respect_elvira_elvira_mistress_of_the_dark/

########################################

id = get_rt_id(cur, 'Respect Maui (Polynesian Mythology)', 'https://redd.it/1eco4g3')
add_data(['Maui'],
'Maui',
False,
False,
[
    ['Mythology'], ['Polynesian']
],
'Polynesian Mythology',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Xa-Du, the Phantom King (DC Comics, Post-Flashpoint)', 'https://redd.it/1ecp1ah')
add_data(['Xa(-| )Du'],
'Xa-Du',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ecp1ah/respect_xadu_the_phantom_king_dc_comics/

add_data(['Xa(-| )Du'],
'Xa-Du',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ecp1ah/respect_xadu_the_phantom_king_dc_comics/

########################################

id = get_rt_id(cur, 'Respect the Gotham Bad Blood (DC/Dark Horse Comics, Batman versus Predator II)', 'https://redd.it/1edi0hy')
add_data(['Gotham Bad Blood'],
'Gotham Bad Blood',
False,
False,
[
    ['Predator']
],
'Batman versus Predator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1edi0hy/respect_the_gotham_bad_blood_dcdark_horse_comics/

########################################

id = get_rt_id(cur, 'Respect the See-Through Slasher! (DC/Dark Horse Comics, Batman versus Predator)', 'https://redd.it/1edhjxu')
add_data(['See(-| )Through Slasher'],
'See-Through Slasher',
False,
True,
[
    ['Predator']
],
'Batman versus Predator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1edhjxu/respect_the_seethrough_slasher_dcdark_horse/

########################################

id = get_rt_id(cur, 'Respect: Shroud (Marvel, 616)', 'https://redd.it/1edcadp')
add_data(['Shroud'],
'Shroud',
False,
False,
[
    ['Shroud ?\(616\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Maximillain Coleridge'],
'Maximillain Coleridge',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1edcadp/respect_shroud_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Kai Brightstar (Star Wars Canon)', 'https://redd.it/1ed11yu')
add_data(['Kai Brightstar'],
'Kai Brightstar',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ed11yu/respect_kai_brightstar_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Flowey! (Undertale Yellow)', 'https://redd.it/1ee187s')
add_data(['Flowey'],
'Flowey',
False,
False,
[
    ['Undertale Yellow']
],
'Undertale Yellow',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ee187s/respect_flowey_undertale_yellow/

########################################

id = get_rt_id(cur, 'Respect Flowey! (Flowey is Not a Good Life Coach)', 'https://redd.it/1ee18dp')
add_data(['Flowey'],
'Flowey',
False,
False,
[
    ['Flowey is Not a Good Life Coach']
],
'Flowey is Not a Good Life Coach',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ee18dp/respect_flowey_flowey_is_not_a_good_life_coach/

########################################

id = get_rt_id(cur, 'Respect the Revolution Princess, Hongou Hina! (STAR: Strike It Rich)', 'https://redd.it/1ee3sgd')
add_data(['Hongou Hina'],
'Hongou Hina',
False,
True,
[
    ['STAR:? Strike It Rich']
],
'STAR: Strike It Rich',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ee3sgd/respect_the_revolution_princess_hongou_hina_star/

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

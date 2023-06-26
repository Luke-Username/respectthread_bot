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

update_respectthread(cur, 1123, 'Respect Cheetah! (DC Animated Movie Universe)', 'https://redd.it/14i87fm')
update_respectthread(cur, 1602, 'Respect Hartley Rathaway, The Pied Piper! (DC Comics, Pre-Flashpoint)', 'https://redd.it/14imu7r')

########################################

add_data(['Hancock'],
'Hancock',
False,
False,
[
    ['DCEU', 'Superman'], ['Homelander']
],
'Hancock',
'{457}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bahamut (Stranger of Paradise: Final Fantasy Origin)', 'https://redd.it/14hosgb')
add_data(['Bahamut'],
'Bahamut',
False,
False,
[
    ['Stranger of Paradise']
],
'Stranger of Paradise',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14hosgb/respect_bahamut_stranger_of_paradise_final/

########################################

id = get_rt_id(cur, 'Respect Jack Garland (Final Fantasy)', 'https://redd.it/14i23yz')
add_data(['Jack Garland'],
'Jack Garland',
False,
True,
[
    ['Final Fantasy'], ['FF\d?\d?'], ['FF\w\w?\w?']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14i23yz/respect_jack_garland_final_fantasy/

########################################

id = get_rt_id(cur, 'Respect Willy Wonka (Charlie and the Chocolate Factory)', 'https://redd.it/14hy282')
id2 = get_rt_id(cur, 'Respect Willy Wonka (Wonka Adverts)', 'https://redd.it/14hy2i5')
add_data(['Willy Wonka'],
'Willy Wonka',
False,
True,
[
    ['Chocolate Factory']
],
'Charlie and the Chocolate Factory',
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14hy282/respect_willy_wonka_charlie_and_the_chocolate/

########################################

id = get_rt_id(cur, 'Respect Char-Ryl-Roy (Star Wars Canon)', 'https://redd.it/14i27th')
add_data(['Char-Ryl-Roy'],
'Char-Ryl-Roy',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14i27th/respect_charrylroy_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Orin Darhga (Star Wars Canon)', 'https://redd.it/14i3fpl')
add_data(['Orin Darhga'],
'Orin Darhga',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14i3fpl/respect_orin_darhga_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Cippa Tarko (Star Wars Canon)', 'https://redd.it/14i6c10')
add_data(['Cippa Tarko'],
'Cippa Tarko',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14i6c10/respect_cippa_tarko_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Creighton Sun (Star Wars Canon)', 'https://redd.it/14i9ppw')
add_data(['Creighton Sun'],
'Creighton Sun',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14i9ppw/respect_creighton_sun_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Aida Forte (Star Wars Canon)', 'https://redd.it/14itqcy')
add_data(['Aida Forte'],
'Aida Forte',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14itqcy/respect_aida_forte_star_wars_canon/


########################################

id = get_rt_id(cur, 'Respect Silandra Sho (Star Wars Canon)', 'https://redd.it/14j5ijx')
add_data(['Silandra Sho'],
'Silandra Sho',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14j5ijx/respect_silandra_sho_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Mr. Fox (Fantastic Mr. Fox) [1970 Book]', 'https://redd.it/14ixqgo')
id2 = get_rt_id(cur, 'Respect Mr. Fox (Fantastic Mr. Fox) [2009 Movie]', 'https://redd.it/14ixqhr')
add_data(['Fantastic Mr\.? Fox'],
'Fantastic Mr. Fox',
False,
True,
[
    ['Fantastic Mr\.? Fox ?\(Fantastic Mr\.? Fox\)']
],
'',
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ixqgo/respect_mr_fox_fantastic_mr_fox_1970_book/

########################################

id = get_rt_id(cur, 'Respect Michiru Kagemori! (BNA: Brand New Animal)', 'https://redd.it/14j0vzr')
add_data(['Michiru Kagemori'],
'Michiru Kagemori',
False,
True,
[
    ['Brand New Animal'], ['My Hero Academia'], ['\(My Hero\)'], ['(M|BN?)HA'], ['Boku no Hero']
],
'My Hero Academia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14j0vzr/respect_michiru_kagemori_bna_brand_new_animal/

########################################

id = get_rt_id(cur, 'Respect Wanze (One Piece)', 'https://redd.it/14j7u7s')
add_data(['Wanze'],
'Wanze',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14j7u7s/respect_wanze_one_piece/

########################################

id = get_rt_id(cur, 'Respect Kipo Oak! (Kipo and the Age of Wonderbeasts)', 'https://redd.it/14jr3sx')
add_data(['Kipo Oak'],
'Kipo Oak',
False,
True,
[
    ['Kipo and the Age of Wonderbeasts']
],
'Kipo and the Age of Wonderbeasts',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14jr3sx/respect_kipo_oak_kipo_and_the_age_of_wonderbeasts/

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

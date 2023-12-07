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

update_respectthread(cur, 522, 'Respect Gipsy Danger! (Pacific Rim)', 'https://redd.it/18al6w2')
update_respectthread(cur, 595, 'Respect Wesley Gibson! (Wanted)', 'https://redd.it/18avn9s')
update_respectthread(cur, 2532, 'Respect Ultimate Hawkeye (Marvel, 1610)', 'https://redd.it/18b478v')
update_respectthread(cur, 12144, 'Respect Hanno of Arwad, the White Knight (A Practical Guide to Evil)', 'https://redd.it/18bx6y1')
update_respectthread(cur, 2053, 'Respect Wilson Fisk, the Kingpin (Marvel Comics, Earth 616)', 'https://redd.it/18c6pfy')

########################################

add_data(['Ultraman'],
'Ultraman',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{3971}'
)
#https://www.reddit.com/r/whowouldwin/comments/18csihh/goku_variants_vs_superman_variants/kcclvjz/?context=3

########################################

add_data(['Sakura'],
'Sakura',
False,
False,
[
    ['Sanji', 'Sakura vs|vs\.? Sakura'], ['Base Sakura'], ['Jutsu']
],
'Naruto',
'{3971}'
)
#https://www.reddit.com/r/whowouldwin/comments/18cb5gp/sanji_vs_sakura/kc9gl03/?context=3

########################################

add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Minus One'], ['-1\.0']
],
'Minus One',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/18apgu8/godzilla_from_10_shows_up_a_few_years_earlier_and/kbz9cjv/?context=3

########################################

id = get_rt_id(cur, 'Respect Yuugi Hoshiguma (Touhou)', 'https://redd.it/18akhal')
add_data(['Yuugi Hoshiguma'],
'Yuugi Hoshiguma',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18akhal/respect_yuugi_hoshiguma_touhou/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 26: the Gamma Killer (Marvel Comics, 616)', 'https://redd.it/18alhgt')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Gamma Killer'], ['Model 26']
],
'Gamma Killer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18alhgt/respect_iron_man_model_26_the_gamma_killer_marvel/

########################################

add_data(['Bishamon'],
'Bishamon',
False,
False,
[
    ['Noragami']
],
'Noragami',
'{3994}'
)
#https://www.reddit.com/r/respectthreads/comments/18alhgt/respect_iron_man_model_26_the_gamma_killer_marvel/

add_data(['Bishamonten'],
'Bishamonten',
False,
False,
[
    ['Noragami']
],
'Noragami',
'{3994}'
)
#https://www.reddit.com/r/respectthreads/comments/18alhgt/respect_iron_man_model_26_the_gamma_killer_marvel/

########################################

add_data(['Ebisu'],
'Ebisu',
False,
False,
[
    ['Noragami']
],
'Noragami',
'{3995}'
)
#

add_data(['Yato'],
'Yato',
False,
False,
[
    ['Noragami']
],
'Noragami',
'{3996}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Man in the Suit (Unknowingly/Godzilla Analog Horror)', 'https://redd.it/18bloxy')
add_data(['Man in the Suit'],
'Man in the Suit',
False,
False,
[
    ['Unknowingly'], ['Godzilla Analog Horror']
],
'Unknowingly/Godzilla Analog Horror',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18alhgt/respect_iron_man_model_26_the_gamma_killer_marvel/

########################################

id = get_rt_id(cur, 'Respect Board James (Board James, Cinemassacre)', 'https://redd.it/18c6n3s')
add_data(['Board James'],
'Board James',
False,
True,
[
    ['Cinemassacre']
],
'Cinemassacre',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Grendel (The Guy Who Cried Grendel)', 'https://redd.it/18c6n7z')
add_data(['Grendel'],
'Grendel',
False,
False,
[
    ['Guy Who Cried Grendel']
],
'The Guy Who Cried Grendel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18c6n7z/respect_grendel_the_guy_who_cried_grendel/

########################################

id = get_rt_id(cur, 'Respect the Darkness Devil! (Chainsaw Man)', 'https://redd.it/18c7roj')
add_data(['Darkness Devil'],
'Darkness Devil',
False,
True,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18c7roj/respect_the_darkness_devil_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Kiryu Miyazawa (Tough)', 'https://redd.it/18cetpd')
add_data(['Kiryuu? Miyazawa'],
'Kiryu Miyazawa',
False,
True,
[
    ['Tough']
],
'Tough',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18cetpd/respect_kiryu_miyazawa_tough/

########################################

id = get_rt_id(cur, 'Respect Google! (Markiplier Canon)', 'https://redd.it/18cjdez')
add_data(['Google'],
'Google',
False,
False,
[
    ['Markiplier']
],
'Markiplier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/18cjdez/respect_google_markiplier_canon/

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

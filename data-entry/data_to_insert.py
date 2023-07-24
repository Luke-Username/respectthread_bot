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

update_respectthread(cur, 7608, 'Respect Absol (Pokémon: Jirachi: Wish Maker)', 'https://redd.it/1578z0q')
update_respectthread(cur, 2103, 'Respect Paladin (Marvel 616)', 'https://redd.it/157v6aw')

########################################

add_data(['The Thing'],
'The Thing',
False,
False,
[
    ['The Thing ?\(Fantastic Four\)']
],
'616',
'{2072,22166}'
)
#https://www.reddit.com/r/whowouldwin/comments/15860e2/homelander_the_boys_vs_the_thing_fantastic_four/

########################################

id = get_rt_id(cur, 'Respect The Blue Border (Scott The Woz)', 'https://redd.it/1567h5a')
add_data(['Blue Border'],
'Blue Border',
False,
False,
[
    ['Scott The Woz']
],
'Scott The Woz',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1567h5a/respect_the_blue_border_scott_the_woz/

########################################

id = get_rt_id(cur, 'Respect Maxwell Hale (Ex-Heroes)', 'https://redd.it/156vmcy')
add_data(['Maxwell Hale'],
'Maxwell Hale',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/156vmcy/respect_maxwell_hale_exheroes/

########################################

id = get_rt_id(cur, 'Respect Dr. Michihiko Zaizen, Dr. Pac-Man (Kamen Rider Ex-Aid)', 'https://redd.it/157aofc')
add_data(['Dr\.? Pac(-| )?Man'],
'Dr. Pac-Man',
False,
False,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/157aofc/respect_dr_michihiko_zaizen_dr_pacman_kamen_rider/

add_data(['Michihiko Zaizen'],
'Michihiko Zaizen',
False,
True,
[
    ['Kamen Rider']
],
'Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/157aofc/respect_dr_michihiko_zaizen_dr_pacman_kamen_rider/

########################################

id = get_rt_id(cur, 'Respect Countess Belzebeth (DC Comics)', 'https://redd.it/1583k8v')
add_data(['Belzebeth'],
'Belzebeth',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583k8v/respect_countess_belzebeth_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Man-Ape! (DC Comics, Pre-Crisis)', 'https://redd.it/1583lnx')
add_data(['Man(-| )Ape'],
'Man-Ape',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583lnx/respect_manape_dc_comics_precrisis/

########################################

id = get_rt_id(cur, 'Respect Killa the Gorilla! (DC Comics, Post-Crisis)', 'https://redd.it/1583lu8')
add_data(['Killa the Gorilla'],
'Killa the Gorilla',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583lu8/respect_killa_the_gorilla_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Corpse Girl (Ex-Heroes)', 'https://redd.it/157w9wc')
add_data(['Corpse Girl'],
'Corpse Girl',
False,
False,
[
    ['Ex(-| )Heroes']
],
'Ex-Heroes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/157w9wc/respect_corpse_girl_exheroes/

########################################

id = get_rt_id(cur, 'Respect Alex Rex! (Keyman: The Hand of Judgement)', 'https://redd.it/1583kql')
add_data(['Alex Rex'],
'Alex Rex',
False,
False,
[
    ['Keyman'], ['Hand of Judgement']
],
'Keyman: The Hand of Judgement',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583kql/respect_alex_rex_keyman_the_hand_of_judgement/

########################################

id = get_rt_id(cur, 'Respect the Mother (The Sims 4)', 'https://redd.it/1583l6r')
add_data(['The Mother'],
'The Mother',
False,
False,
[
    ['The Sims']
],
'The Sims',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583l6r/respect_the_mother_the_sims_4/

add_data(['Mother Plant'],
'Mother Plant',
False,
False,
[
    ['The Sims']
],
'The Sims',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583l6r/respect_the_mother_the_sims_4/

########################################

id = get_rt_id(cur, 'Respect Izuku Midoriya (Fortnite)', 'https://redd.it/1583mtu')
add_data(['Midoriya'],
'Izuku Midoriya',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583mtu/respect_izuku_midoriya_fortnite/

add_data(['Deku'],
'Deku',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583mtu/respect_izuku_midoriya_fortnite/

########################################

id = get_rt_id(cur, 'Respect Neymar Jr (Fortnite)', 'https://redd.it/1583n3p')
add_data(['Neymar Jr'],
'Neymar Jr',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1583n3p/respect_neymar_jr_fortnite/

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

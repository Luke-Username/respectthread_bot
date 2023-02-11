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

update_respectthread(cur, 4117, 'Respect Tatsumaki, the Tornado of Terror! (One Punch-Man [Manga])', 'https://redd.it/10xamw3')
update_respectthread(cur, 20353, 'Respect Christopher Smith, Peacemaker! (DCEU)', 'https://redd.it/10yb77r')
update_respectthread(cur, 6470, 'Respect Chandra Nalaar! (Magic: The Gathering - Moe Tsukinu Honoo)', 'https://redd.it/10yy42t')
update_respectthread(cur, 8239, 'Respect Shinra Kusakabe! (Fire Force)', 'https://redd.it/10zrl8k')

########################################

add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Earth(-| )Prime']
],
'Rebirth',
'{7632}'
)
#https://www.reddit.com/r/whowouldwin/comments/10zvdms/superman_with_the_venom_symbiote_vs_ultraman/j85dv1r/?context=3

########################################

add_data(['The Emperor'],
'The Emperor',
False,
False,
[
    ['(WH)?40K']
],
'Warhammer 40k',
'{6465}'
)
#https://www.reddit.com/r/whowouldwin/comments/10z0wor/one_punch_man_vs_40k/

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Mythos', 'Pantheons?']
],
'Norse Mythology',
'{23298}'
)
#https://www.reddit.com/r/whowouldwin/comments/10xwn2k/greek_vs_norse_vs_egyptian_vs_hindu_vs_shinto_vs/j7ukxng/?context=3

########################################

add_data(['Witch-king'],
'Witch-king',
False,
True,
[
    ['L(ord )?o(f )?t(he )?R(ings)?']
],
'Lord of the Rings',
'{5862}'
)
#https://www.reddit.com/r/whowouldwin/comments/10wx4ka/witchking_of_angmar_vs_treebeard_lotr/j7pef4a/?context=3

add_data(['Witch(-| )king of Angmar'],
'Witch-king of Angmar',
False,
True,
[
    ['L(ord )?o(f )?t(he )?R(ings)?']
],
'Lord of the Rings',
'{5862}'
)
#https://www.reddit.com/r/whowouldwin/comments/10wx4ka/witchking_of_angmar_vs_treebeard_lotr/j7pef4a/?context=3

########################################

add_data(['Butcher'],
'Butcher',
False,
False,
[
    ['The Boys']
],
'The Boys',
'{22740}'
)
#https://www.reddit.com/r/whowouldwin/comments/10y869m/baby_lasertag_butcher_the_boys_vs_mr_incredible/j7wl2bt/?context=3

########################################

add_data(['Rocky'],
'Rocky',
False,
False,
[
    ['Miyagi']
],
'',
'{546,547}'
)
#https://www.reddit.com/r/whowouldwin/comments/10y01ia/rocky_vs_mr_miyagi/

########################################

id = get_rt_id(cur, 'Respect: Corvus Corax (Warhammer 40k)', 'https://redd.it/10wkrd3')
add_data(['Corvus Corax'],
'Corvus Corax',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10wkrd3/respect_corvus_corax_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Ruri! (RuriDragon)', 'https://redd.it/10wnhzd')
add_data(['Ruri'],
'Ruri',
False,
False,
[
    ['RuriDragon']
],
'RuriDragon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10wnhzd/respect_ruri_ruridragon/

########################################

id = get_rt_id(cur, 'Respect the Pteracuda (Sharktopus vs. Pteracuda)', 'https://redd.it/10x16xw')
add_data(['Pteracuda'],
'Pteracuda',
False,
True,
[
    ['Sharktopus']
],
'Sharktopus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10x16xw/respect_the_pteracuda_sharktopus_vs_pteracuda/

########################################

id = get_rt_id(cur, 'Respect the Whalewolf (Sharktopus vs. Whalewolf)', 'https://redd.it/10x174p')
add_data(['Whalewolf'],
'Whalewolf',
False,
True,
[
    ['Sharktopus']
],
'Sharktopus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10x174p/respect_the_whalewolf_sharktopus_vs_whalewolf/

########################################

id = get_rt_id(cur, 'Respect Diana Cavendish! (Little Witch Academia [TV Series])', 'https://redd.it/10xo8k0')
add_data(['Diana Cavendish'],
'Diana Cavendish',
False,
True,
[
    ['Little Witch Academia']
],
'Little Witch Academia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10xo8k0/respect_diana_cavendish_little_witch_academia_tv/

########################################

id = get_rt_id(cur, 'Respect Ransik! (Power Rangers Time Force)', 'https://redd.it/10xvnip')
add_data(['Ransik'],
'Ransik',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10xvnip/respect_ransik_power_rangers_time_force/

########################################

id = get_rt_id(cur, 'Respect Rintaro Shindo, aka Kamen Rider Blades (Kamen Rider Saber)!', 'https://redd.it/10yelp8')
add_data(['Kamen Rider Blades?'],
'Kamen Rider Blades',
False,
True,
[
    ['Rintaro Shindo']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10yelp8/respect_rintaro_shindo_aka_kamen_rider_blades/

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

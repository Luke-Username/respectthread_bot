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

update_respectthread(cur, 5976, 'Respect Jasnah Kholin (The Stormlight Archive)', 'https://redd.it/166ukvx')
update_respectthread(cur, 5975, 'Respect Adolin Kholin (The Stormlight Archive)', 'https://redd.it/1695176')

########################################

add_data(['Cyberm(e|a)n'],
'Cybermen',
False,
True,
[
    ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{44, 45}'
)
#https://www.reddit.com/r/whowouldwin/comments/167grbk/scp_foundation_runs_doctor_who_gauntlet/jyplo8y/?context=3

########################################

add_data(['Mighty Mouse'],
'Mighty Mouse',
False,
False,
[
    ['UFC'], ['Demetrious']
],
'UFC',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/168omof/mighty_mouse_vs_brian_shaw/jywtmtu/?context=3

########################################

add_data(['Soft (&|and) Wet'],
'Soft & Wet',
False,
False,
[
    ['Josuke'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3628}'
)
#

########################################

add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['(Doctor|Dr\.?) ?Who']
],
'Doctor Who',
'{14419,23159,22631,23115,40,15401,23253}'
)
#https://www.reddit.com/r/whowouldwin/comments/167grbk/scp_foundation_runs_doctor_who_gauntlet/jyplo8y/?context=3

########################################

id = get_rt_id(cur, 'Respect Adiane (Gurren Lagann anime)', 'https://redd.it/166l4pl')
add_data(['Adiane'],
'Adiane',
False,
True,
[
    ['Gurren Lagann?']
],
'Gurren Lagann',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/166l4pl/respect_adiane_gurren_lagann_anime/

########################################

id = get_rt_id(cur, 'Respect Lift (The Stormlight Archive)', 'https://redd.it/166m6d7')
add_data(['Lift'],
'Lift',
False,
False,
[
    ['Storm ?light']
],
'The Stormlight Archive',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/166m6d7/respect_lift_the_stormlight_archive/

########################################

id = get_rt_id(cur, 'Respect Renarin Kholin (The Stormlight Archive)', 'https://redd.it/166t1zw')
add_data(['Renarin Kholin'],
'Renarin Kholin',
False,
True,
[
    ['Storm ?light']
],
'The Stormlight Archive',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/166t1zw/respect_renarin_kholin_the_stormlight_archive/

########################################

id = get_rt_id(cur, 'Respect Shallan Davar (The Stormlight Archive)', 'https://redd.it/167gk7q')
add_data(['Shallan Davar'],
'Shallan Davar',
False,
True,
[
    ['Storm ?light']
],
'The Stormlight Archive',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 15 “The Crossing” Armor (Earth - 616)', 'https://redd.it/167ct63')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 15']
],
'Model 15',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/167ct63/respect_iron_man_model_15_the_crossing_armor/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 11: War Machine (Marvel, 616)', 'https://redd.it/1691kws')
add_data(['War Machine'],
'War Machine',
False,
False,
[
    ['Model 11']
],
'Model 11',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1691kws/respect_iron_man_model_11_war_machine_marvel_616/

add_data(['War Machine'],
'War Machine',
False,
False,
[
    ['616']
],
'616',
'{' + '24138, {}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1691kws/respect_iron_man_model_11_war_machine_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Norman Osborn, the Iron Patriot (Marvel Comics, 616)', 'https://redd.it/1698uqj')
add_data(['Iron Patriot'],
'Iron Patriot',
False,
False,
[
    ['Norman Osborn']
],
'Norman Osborn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1698uqj/respect_norman_osborn_the_iron_patriot_marvel/

########################################

id = get_rt_id(cur, 'Respect Sam Fisher (Splinter Cell, Games)', 'https://redd.it/167d9ez')
id2 = get_rt_id(cur, 'Respect Sam Fisher (Splinter Cell, Comics)', 'https://redd.it/167dbbx')
id3 = get_rt_id(cur, 'Respect Sam Fisher (Splinter Cell, Novels)', 'https://redd.it/167ddj2')
add_data(['Sam Fisher'],
'Sam Fisher',
False,
True,
[
    ['Splinter Cell']
],
'Splinter Cell',
'{' + '{}, {}, {}'.format(id, id2, id3) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/167ddj2/respect_sam_fisher_splinter_cell_novels/

########################################

id = get_rt_id(cur, "Respect Dracule \"Hawk-Eye\" Mihawk (Netflix''s One Piece, Live Action)", 'https://redd.it/1689e8i')
add_data(['Mihawk'],
'Mihawk',
False,
False,
[
    ["(Netflix(''?s?)?|Live(-| )Action) ?One Piece"]
],
"Netflix''s One Piece",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1689e8i/respect_dracule_hawkeye_mihawk_netflixs_one_piece/

########################################

id = get_rt_id(cur, "Respect Captain Kuro (Netflix''s One Piece, Live Action)", 'https://redd.it/1691ilx')
add_data(['Kuro'],
'Kuro',
False,
False,
[
    ["(Netflix(''?s?)?|Live(-| )Action) ?One Piece"]
],
"Netflix''s One Piece",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1689e8i/respect_dracule_hawkeye_mihawk_netflixs_one_piece/

########################################

id = get_rt_id(cur, 'Respect Clone Trooper "Glitch" (Star Wars)', 'https://redd.it/168c44u')
add_data(['Glitch'],
'Glitch',
False,
False,
[
    ['The clone trooper']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/168c44u/respect_clone_trooper_glitch_star_wars/

########################################

id = get_rt_id(cur, 'Respect Kohane (Nocturne of the Heaven) [Nijisanji Kamigakari campaign]', 'https://redd.it/168j9vp')
add_data(['Kohane'],
'Kohane',
False,
False,
[
    ['Nocturne of the Heaven'], ['NOTH'], ['Kamigakari'], ['Nijisanji'], ['Ono Kohane']
],
'Nocturne of the Heaven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/168j9vp/respect_kohane_nocturne_of_the_heaven_nijisanji/?

########################################

id = get_rt_id(cur, 'Respect the BLU Heavy (Heavy is spy)', 'https://redd.it/1695nzw')
add_data(['BLU Heavy'],
'BLU Heavy',
False,
False,
[
    ['Heavy is spy']
],
'Heavy is spy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1695nzw/respect_the_blu_heavy_heavy_is_spy/

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

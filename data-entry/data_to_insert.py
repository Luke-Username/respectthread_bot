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

update_respectthread(cur, 5625, 'Respect Kain, The Scion of Balance (Legacy of Kain)', 'https://redd.it/1fx3l4j')

########################################

add_data(['Power'],
'Power',
False,
False,
[
    ['Chainsaw(-| )?Man', 'Denji']
],
'Chainsaw Man',
'{15966}'
)
#https://www.reddit.com/r/whowouldwin/comments/1fy57oy/josuke_higashikata_jojos_bizarre_adventure/lqreodn/?context=3

########################################

id = get_rt_id(cur, 'Respect The Leeches (The Vaults of Yoh-Vombis)', 'https://redd.it/1fv7qh5')
add_data(['Leeches'],
'Leeches',
False,
False,
[
    ['Vaults of Yoh(-| )Vombis']
],
'The Vaults of Yoh-Vombis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fv7qh5/respect_the_leeches_the_vaults_of_yohvombis/

########################################

id = get_rt_id(cur, 'Respect Keitaro Gentoga (Dark Gathering)', 'https://redd.it/1fv7qh5')
add_data(['Keitaro Gentoga'],
'Keitaro Gentoga',
False,
True,
[
    ['Dark Gathering']
],
'Dark Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fv7x17/respect_keitaro_gentoga_dark_gathering/

########################################

id = get_rt_id(cur, 'Respect Nobara Kugisaki! (Jujutsu Kaisen)', 'https://redd.it/1fv89sw')
add_data(['Kugisaki'],
'Kugisaki',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fv89sw/respect_nobara_kugisaki_jujutsu_kaisen/

add_data(['Nobara'],
'Nobara',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Hammer']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fv89sw/respect_nobara_kugisaki_jujutsu_kaisen/

add_data(['Nobara Kugisaki'],
'Nobara Kugisaki',
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fv89sw/respect_nobara_kugisaki_jujutsu_kaisen/

########################################

id = get_rt_id(cur, "Respect Maki Zen''in! (Jujutsu Kaisen)", 'https://redd.it/1fxhiv2')
add_data(['Maki'],
'Maki',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fxhiv2/respect_maki_zenin_jujutsu_kaisen/

add_data(["Maki Zen''?in"],
"Maki Zen''in",
False,
True,
[
    ['Jujus?t?s?u Kaisen'], ['JJK']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fxhiv2/respect_maki_zenin_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect The Degenerate (DC)', 'https://redd.it/1fvlb59')
add_data(['Degenerate'],
'Degenerate',
False,
False,
[
    ['Degenerate ?\(DC( Comics)?\)']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fvlb59/respect_the_degenerate_dc/

########################################

id = get_rt_id(cur, 'Respect Beast Girl (DC)', 'https://redd.it/1fvwvzj')
add_data(['Beast Girl'],
'Beast Girl',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fvwvzj/respect_beast_girl_dc/

########################################

id = get_rt_id(cur, 'Respect Lotion the Cat (DC)', 'https://redd.it/1fwyn1p')
add_data(['Lotion the Cat'],
'Lotion the Cat',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fwyn1p/respect_lotion_the_cat_dc/

########################################

id = get_rt_id(cur, 'Respect Lucius Reynolds (DC)', 'https://redd.it/1fwrik9')
add_data(['Lucius Reynolds'],
'Lucius Reynolds',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fwrik9/respect_lucius_reynolds_dc/

########################################

id = get_rt_id(cur, 'Respect Terry None (DC)', 'https://redd.it/1fwogcf')
add_data(['Terry None'],
'Terry None',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fwogcf/respect_terry_none_dc/

########################################

id = get_rt_id(cur, 'Respect the Arcadia [Captain Harlock]', 'https://redd.it/1fvlikt')
add_data(['Arcadia'],
'Arcadia',
False,
False,
[
    ['Captain Harlock']
],
'Captain Harlock',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fvlikt/respect_the_arcadia_captain_harlock/

########################################

id = get_rt_id(cur, 'Respect Baal (Ash vs Evil Dead)', 'https://redd.it/1fvxx9s')
add_data(['Baal'],
'Baal',
False,
False,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fvxx9s/respect_baal_ash_vs_evil_dead/

########################################

id = get_rt_id(cur, 'Respect the Necronomicon (Evil Dead THQ Games)', 'https://redd.it/1fxskzb')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['Evil Dead', 'THQ']
],
'Evil Dead THQ Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fxskzb/respect_the_necronomicon_evil_dead_thq_games/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Evil Dead THQ Games)', 'https://redd.it/1fxs5iu')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Evil Dead', 'THQ']
],
'Evil Dead THQ Games',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fxs5iu/respect_ash_williams_evil_dead_thq_games/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Dead by Daylight)', 'https://redd.it/1fx22je')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Dead by Daylight'], ['DBD']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fx22je/respect_ash_williams_dead_by_daylight/

########################################

id = get_rt_id(cur, 'Respect White Fox! (Scissor Seven)', 'https://redd.it/1fwtzrc')
add_data(['White Fox'],
'White Fox',
False,
False,
[
    ['Scissor Seven']
],
'Scissor Seven',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fwtzrc/respect_white_fox_scissor_seven/


########################################

id = get_rt_id(cur, 'Respect: Orson Randall, Iron Fist (Marvel, 616)', 'https://redd.it/1fwsobj')
add_data(['Orson Randall'],
'Orson Randall',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fwsobj/respect_orson_randall_iron_fist_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Cassandra Nova (Marvel Cinematic Universe)', 'https://redd.it/1fw0sai')
add_data(['Cassandra Nova'],
'Cassandra Nova',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fw0sai/respect_cassandra_nova_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, 'Respect the Mitchells! (The Mitchells vs. the Machines)', 'https://redd.it/1fvzngu')
add_data(['The Mitchells'],
'The Mitchells',
True,
False,
[
    ['The Mitchells vs\.? the Machines']
],
'The Mitchells vs. the Machines',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fvzngu/respect_the_mitchells_the_mitchells_vs_the/

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

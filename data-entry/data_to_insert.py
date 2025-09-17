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

update_respectthread(cur, 746, 'Respect Amazo (DCAU)', 'https://www.reddit.com/r/respectthreads/comments/1neko6j/respect_amazo_dcau/')
update_respectthread(cur, 1236, 'Respect The Thief (The Thief and The Cobbler)', 'https://www.reddit.com/r/respectthreads/comments/1nenfg6/respect_the_thief_the_thief_and_the_cobbler/')
update_respectthread(cur, 811, 'Respect Lin Beifong (The Legend of Korra)', 'https://www.reddit.com/r/respectthreads/comments/1nfpc3v/respect_lin_beifong_the_legend_of_korra/')
update_respectthread(cur, 3791, 'Respect the Nastika King, Gandharva! (One Last God: Kubera)', 'https://www.reddit.com/r/respectthreads/comments/1ng22l0/respect_the_nastika_king_gandharva_one_last_god/')
update_respectthread(cur, 7524, 'Respect The Killer Klowns From Outer Space (Killer Klowns From Outer Space)', 'https://www.reddit.com/r/respectthreads/comments/1nh2mst/respect_the_killer_klowns_from_outer_space_killer/')
update_respectthread(cur, 5474, 'Respect The Heavy (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1nhs850/respect_the_heavy_team_fortress_2/')
update_respectthread(cur, 3787, 'Respect Agni, The God of Fire! (One Last God: Kubera)', 'https://www.reddit.com/r/respectthreads/comments/1ni3fhk/respect_agni_the_god_of_fire_one_last_god_kubera/')
update_respectthread(cur, 5475, 'Respect The Medic (Team Fortress 2)', 'https://www.reddit.com/r/respectthreads/comments/1niyi4n/respect_the_medic_team_fortress_2/')

########################################

add_data(['AM'],
'AM',
False,
False,
[
    ['AM.*IHNM']
],
'I Have No Mouth And Must Scream',
'{16570}'
)
#

########################################

add_data(['Wonder ?Woman'],
'Wonder Woman',
False,
False,
[
    ['Snyder(verse)?']
],
'DCEU',
'{131}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ng0yuz/omniman_vs_wonder_woman_snyder_verse/



########################################

id = get_rt_id(cur, 'Respect The Hulk, The World Breaker (What if the Heroes lost to World War Hulk)', 'https://www.reddit.com/r/respectthreads/comments/1nfpxr9/respect_the_hulk_the_world_breaker_what_if_the/')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['What if the Heroes lost to World War Hulk']
],
'What if the Heroes lost to World War Hulk',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Mouri Katsunaga(Joujuu Senjin Mushibugyo)', 'https://www.reddit.com/r/respectthreads/comments/1nfzvqs/respect_mouri_katsunagajoujuu_senjin_mushibugyo/')
add_data(['Mouri Katsunaga'],
'Mouri Katsunaga',
False,
False,
[
    ['Joujuu Senjin|Mushibugyo']
],
'Joujuu Senjin!! Mushibugyo',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Infernal Hulk (Marvel Comics Earth-11638)', 'https://www.reddit.com/r/respectthreads/comments/1ng6f3j/respect_the_infernal_hulk_marvel_comics_earth11638/')
add_data(['Infernal Hulk'],
'Infernal Hulk',
False,
False,
[
    ['11638']
],
'11638',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Blue Hulk (Marvel Comics Earth 616)', 'https://www.reddit.com/r/respectthreads/comments/1ng6qze/respect_the_blue_hulk_marvel_comics_earth_616/')
add_data(['Blue Hulk'],
'Blue Hulk',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect El Mariachi (Robert Rodriguez''s Mexico Trilogy)", 'https://www.reddit.com/r/respectthreads/comments/1ngbuzh/respect_el_mariachi_robert_rodriguezs_mexico/')
add_data(['El Mariachi'],
'El Mariachi',
False,
True,
[
    ['Robert Rodriguez'], ['Mexico'], ['Desperado']
],
'Mexico Trilogy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-1057, Absence of Shark (SCP Foundation)', 'https://www.reddit.com/r/respectthreads/comments/1nh34dy/respect_scp1057_absence_of_shark_scp_foundation/')
add_data(['SCP ?(-| )? ?1057'],
'SCP-1057',
False,
True,
[
    ['Absence of Shark']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jinbei Tsukishima ( Joujuu Senjin!! Mushibugyo)', 'https://www.reddit.com/r/respectthreads/comments/1nib5j7/respect_jinbei_tsukishima_joujuu_senjin_mushibugyo/')
add_data(['Jinbei Tsukishima'],
'Jinbei Tsukishima',
False,
True,
[
    ['Mushibugy(ō|o)']
],
'Mushibugyō',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect This Unnamed Vampire Vagrant (Jojo''s Bizarre Adventure)", 'https://www.reddit.com/r/respectthreads/comments/1niz5jk/respect_this_unnamed_vampire_vagrant_jojos/')
add_data(['Vampire Vagrant'],
'Vampire Vagrant',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gareth (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nj08j3/respect_gareth_fategrand_order/')
add_data(['Gareth'],
'Gareth',
False,
False,
[
    ['Fate']
],
'Fate',
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

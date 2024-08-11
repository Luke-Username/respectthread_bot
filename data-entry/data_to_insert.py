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

update_respectthread(cur, 15995, 'Respect Max Rockatansky (Mad Max)', 'https://redd.it/1emafdu')
update_respectthread(cur, 251, 'Respect Loki (Marvel Cinematic Universe)', 'https://redd.it/1eoe3ur')

########################################

id = get_rt_id(cur, 'Respect Jonas Taylor (The Meg)', 'https://redd.it/1ephbyr')
add_data(['Jonas Taylor'],
'Jonas Taylor',
False,
False,
[
    ['The Meg']
],
'The Meg',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ephbyr/respect_jonas_taylor_the_meg/

########################################

id = get_rt_id(cur, 'Respect Nicolas Cage Superman (DCEU)', 'https://redd.it/1eovy5f')
add_data(["Nicolas Cage''?S? Superman"],
'Nicolas Cage Superman',
False,
True,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eovy5f/respect_nicolas_cage_superman_dceu/

########################################

id = get_rt_id(cur, 'Respect the Lifeforce Megazord (Power Rangers Lightspeed Rescue)', 'https://redd.it/1empm10')
add_data(['Lifeforce Megazord'],
'Lifeforce Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1empm10/respect_the_lifeforce_megazord_power_rangers/

########################################

id = get_rt_id(cur, 'Respect Dana Mitchell, the Pink Lightspeed Ranger (Power Rangers Lightspeed Rescue)', 'https://redd.it/1emplzb')
add_data(['Dana Mitchell'],
'Dana Mitchell',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Pink Lightspeed Ranger'],
'Pink Lightspeed Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1emplzb/respect_dana_mitchell_the_pink_lightspeed_ranger/

########################################

id = get_rt_id(cur, 'Respect Ryan Mitchell, the Titanium Ranger (Power Rangers Lightspeed Rescue)', 'https://redd.it/1enj13s')
add_data(['Ryan Mitchell'],
'Ryan Mitchell',
False,
False,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Titanium Ranger'],
'Titanium Ranger',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1enj13s/respect_ryan_mitchell_the_titanium_ranger_power/

########################################

id = get_rt_id(cur, 'Respect Olympius (Power Rangers Lightspeed Rescue)', 'https://redd.it/1enj14q')
add_data(['Olympius'],
'Olympius',
False,
False,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1enj14q/respect_olympius_power_rangers_lightspeed_rescue/

########################################

id = get_rt_id(cur, 'Respect Kara Zor-El, Supergirl! (My Adventures with Superman)', 'https://redd.it/1elp74v')
add_data(['Super(-| )?girl'],
'Supergirl',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1elp74v/respect_kara_zorel_supergirl_my_adventures_with/ 

########################################

id = get_rt_id(cur, 'Respect Ethan Avery, Damage! (My Adventures with Superman)', 'https://redd.it/1elp6gb')
add_data(['Damage'],
'Damage',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1elp6gb/respect_ethan_avery_damage_my_adventures_with/

########################################

id = get_rt_id(cur, 'Respect Joseph Martin, Atomic Skull! (My Adventures with Superman)', 'https://redd.it/1elp4w2')
add_data(['Atomic Skull'],
'Atomic Skull',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1elp4w2/respect_joseph_martin_atomic_skull_my_adventures/

########################################

add_data(['Blade'],
'Blade',
False,
False,
[
    ['Susan Storm', 'Plastic Man', 'Team']
],
'616',
'{2204}'
)
#https://www.reddit.com/r/whowouldwin/comments/1eo57t9/disparate_team_vs_godzilla/lhb05gu/?context=3

########################################

add_data(['Guilliman'],
'Guilliman',
False,
True,
[
    ['Warhammer']
],
'Warhammer 40k',
'{6032}'
)
#https://www.reddit.com/r/respectthreads/comments/no4to5/respect_roboute_guilliman_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Atom (Pluto)', 'https://redd.it/1en8fqe')
add_data(['Atom'],
'Atom',
False,
False,
[
    ['Atom.*\(Pluto\)']
],
'Pluto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1en8fqe/respect_atom_pluto/

########################################

id = get_rt_id(cur, 'Respect Heracles (Pluto)', 'https://redd.it/1en8fr4')
add_data(['Heracles'],
'Heracles',
False,
False,
[
    ['Heracles.*\(Pluto\)']
],
'Pluto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1en8fr4/respect_heracles_pluto/

########################################

id = get_rt_id(cur, 'Respect Epsilon (Pluto)', 'https://redd.it/1en8fsa')
add_data(['Epsilon'],
'Epsilon',
False,
False,
[
    ['Epsilon.*\(Pluto\)']
],
'Pluto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1en8fsa/respect_epsilon_pluto/

########################################

id = get_rt_id(cur, 'Respect Pluto (Pluto)', 'https://redd.it/1eo3ec9')
add_data(['Pluto'],
'Pluto',
False,
False,
[
    ['Pluto.*\(Pluto\)']
],
'Pluto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eo3ec9/respect_pluto_pluto/

########################################

id = get_rt_id(cur, 'Respect The Seven Strongest Robots (Pluto)', 'https://redd.it/1eo3edn')
add_data(['Seven Strongest Robots'],
'Seven Strongest Robots',
True,
False,
[
    ['Seven Strongest Robots.*\(Pluto\)']
],
'Pluto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eo3edn/respect_the_seven_strongest_robots_pluto/

########################################

id = get_rt_id(cur, 'Respect Nigel the Cockatoo (Rio)', 'https://redd.it/1enby0o')
add_data(['Nigel'],
'Nigel',
False,
False,
[
    ['Rio']
],
'Rio',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1enby0o/respect_nigel_the_cockatoo_rio/


########################################

id = get_rt_id(cur, 'Respect Geiger (Image Comics, Ghost Machine)', 'https://redd.it/1eoasbn')
add_data(['Geiger'],
'Geiger',
False,
False,
[
    ['Ghost Machine']
],
'Ghost Machine',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Junkyard Joe (Image Comics, Ghost Machine)', 'https://redd.it/1eoxrp9')
add_data(['Junkyard Joe'],
'Junkyard Joe',
False,
True,
[
    ['Ghost Machine']
],
'Ghost Machine',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1eoxrp9/respect_junkyard_joe_image_comics_ghost_machine/

########################################

id = get_rt_id(cur, 'Respect Nezutron! (Ultraman Arc)', 'https://redd.it/1epl2yt')
add_data(['Nezutron'],
'Nezutron',
False,
False,
[
    ['Ultraman']
],
'Ultraman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1epl2yt/respect_nezutron_ultraman_arc/

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

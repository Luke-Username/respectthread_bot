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

update_respectthread(cur, 535, 'Respect Nick Gant (Push 2009)', 'https://www.reddit.com/r/respectthreads/comments/1ntxwbk/respect_nick_gant_push_2009/')
update_respectthread(cur, 214, 'Respect Hellboy (2004-2008 films)', 'https://www.reddit.com/r/respectthreads/comments/1nw3s94/respect_hellboy_20042008_films/')


########################################

id = get_rt_id(cur, 'Respect the Spooky Space Kook (Scooby Doo, Where Are You?)', 'https://www.reddit.com/r/respectthreads/comments/1nt4bjs/respect_the_spooky_space_kook_scooby_doo_where/')
add_data(['Spooky Space Kook'],
'Spooky Space Kook',
False,
True,
[
    ['Scooby(-| )?Doo']
],
'Scooby-Doo',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marshmello! (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1nt72m5/respect_marshmello_fortnite/')
add_data(['Marshmello'],
'Marshmello',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hades! (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1nt8clv/respect_hades_fortnite/')
add_data(['Hades'],
'Hades',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Visitor (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1nt9mai/respect_the_visitor_fortnite/')
add_data(['The Visitor'],
'The Visitor',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Synthwave (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1nta5xj/respect_synthwave_fortnite/')
add_data(['Synthwave'],
'Synthwave',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Swampert (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1nuqrxo/respect_swampert_pokemon_anime/')
add_data(['Swampert'],
'Swampert',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mudkip'],
'Mudkip',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Marshtomp'],
'Marshtomp',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect J''onn J'onzz (DCAU)", 'https://www.reddit.com/r/respectthreads/comments/1nv50if/respect_jonn_jonzz_dcau/')
add_data(['Martian Manhunter'],
'Martian Manhunter',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#

add_data(["J''onn"],
"J''onn",
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Winnie the Pooh (The Twisted Childhood Universe)', 'https://www.reddit.com/r/respectthreads/comments/1nv8rwz/respect_winnie_the_pooh_the_twisted_childhood/')
add_data(['Winnie the Pooh'],
'Winnie the Pooh',
False,
False,
[
    ['Twisted Childhood Universe']
],
'The Twisted Childhood Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Old Man McGucket (Gravity Falls)', 'https://www.reddit.com/r/respectthreads/comments/1nv9vbb/respect_old_man_mcgucket_gravity_falls/')
add_data(['McGucket'],
'McGucket',
False,
False,
[
    ['Gravity Falls']
],
'Gravity Falls',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Old Man McGucket'],
'Old Man McGucket',
False,
False,
[
    ['Gravity Falls']
],
'Gravity Falls',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Oberon (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nvvaxi/respect_oberon_fategrand_order/')
add_data(['Oberon'],
'Oberon',
False,
False,
[
    ['Grande? Order'], ['F(ate )?/?GO'], ['Oberon Vortigern'], ['Fate Series']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Woodwose (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nw5q6v/respect_woodwose_fategrand_order/')
add_data(['Woodwose'],
'Woodwose',
False,
False,
[
    ['Grande? Order'], ['F(ate )?/?GO'], ['Woodwose.*Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Barghest/Tam Lin Gawain (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nwni96/respect_barghesttam_lin_gawain_fategrand_order/')
add_data(['Barghest'],
'Barghest',
False,
False,
[
    ['Grande? Order'], ['F(ate )?/?GO'], ['Fate Series']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Tam Lin Gawain'],
'Tam Lin Gawain',
False,
True,
[
    ['Grande? Order'], ['F(ate )?/?GO'], ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cernunnos (Fate/Grand Order)', 'https://www.reddit.com/r/respectthreads/comments/1nxdv0n/respect_cernunnos_fategrand_order/')
add_data(['Cernunnos'],
'Cernunnos',
False,
False,
[
    ['Grande? Order'], ['F(ate )?/?GO'], ['Lostbelt'], ['Fate Series']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Irving Wallace, The Night Owl (StageFright: Aquarius)', 'https://www.reddit.com/r/respectthreads/comments/1nw4qw2/respect_irving_wallace_the_night_owl_stagefright/')
add_data(['Irving Wallace'],
'Irving Wallace',
False,
False,
[
    ['Stage ?Fright']
],
'StageFright: Aquarius',
'{' + '{}'.format(id) + '}'
)
#https://en.wikipedia.org/wiki/Stage_Fright_(1987_film)

########################################

id = get_rt_id(cur, 'Respect Brian (Quest 64)', 'https://www.reddit.com/r/respectthreads/comments/1nw8e2s/respect_brian_quest_64/')
add_data(['Brian'],
'Brian',
False,
False,
[
    ['Quest 64']
],
'Quest 64',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Ronan O''Conner (Murdered: Soul Suspect)", 'https://www.reddit.com/r/respectthreads/comments/1nwvwzc/respect_ronan_oconner_murdered_soul_suspect/')
add_data(["Ronan O(''| )?Conner"],
"Ronan O''Conner",
False,
False,
[
    ['Soul Suspect']
],
'Murdered: Soul Suspect',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Vampires (Sinners)', 'https://www.reddit.com/r/respectthreads/comments/1nwwskz/respect_the_vampires_sinners/')
add_data(['Vampires'],
'Vampires',
False,
False,
[
    ['Vampires?.*\(Sinners\)'], ['vampires from recent films', 'Sinners'], ['Irish Vampire', 'Sinners']
],
'Sinners',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ntrl0v/two_vampires_from_recent_films_abigail_and/
#https://www.reddit.com/r/whowouldwin/comments/1kbez4q/sinners_vs_from_dusk_till_dawn_vampires/
#https://www.reddit.com/r/whowouldwin/comments/1k2tttm/how_much_of_1932_usa_could_a_vampire_hive_mind/
#https://www.reddit.com/r/whowouldwin/comments/1mrp0sj/smoke_moore_sinners_vs_the_predator/
#https://www.reddit.com/r/whowouldwin/comments/1m31cfs/rupert_the_ripper_giles_buffy_the_vampire_slayer/
#https://www.reddit.com/r/whowouldwin/comments/1l6g9bm/vampires_sinners_vs_blade_wesley_snipes_films/

########################################

id = get_rt_id(cur, 'Respect Dracula (Dynamite Entertainment)', 'https://www.reddit.com/r/respectthreads/comments/1nwykdj/respect_dracula_dynamite_entertainment/')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Dracula ?\(Dynamite Entertainment']
],
'Dynamite Entertainment',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-6453 (SCP Foundation)', 'https://www.reddit.com/r/respectthreads/comments/1nx6aks/respect_scp6453_scp_foundation/')
add_data(['SCP ?(-| )? ?6453'],
'SCP-6453',
False,
True,
[
    ['SHIT YETI']
],
'',
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

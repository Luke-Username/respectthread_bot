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

update_respectthread(cur, 4078, 'Respect Marco the Phoenix (One Piece)', 'https://redd.it/woc935')

########################################

add_data(['Buddha'],
'Buddha',
False,
False,
[
    ['World of Darkness']
],
'World of Darkness',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/wngfeq/buddha_the_enlightened_world_of_darkness_vs_scp/ik4v16j/?context=3

########################################

add_data(['Dante'],
'Dante',
False,
False,
[
    ['S(hin)? ?M(egami)? ?T(ensei)?']
],
'Shin Megami Tensei',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/wns01w/dante_shin_megami_tensei_vs_goku_dbs/ik6x0bd/?context=3

########################################

add_data(['Kars'],
'Kars',
False,
False,
[
    ['spin(-| )off']
],
'Jorge Joestar',
'{6168}'
)
#https://www.reddit.com/r/whowouldwin/comments/wnqf17/what_character_got_the_most_extreme_power_leap/ik6mlsl/?context=3

########################################

add_data(['Dio'],
'Dio',
False,
False,
[
    ['spin(-| )off', 'Kars']
],
'Jorge Joestar',
'{6167}'
)
#https://www.reddit.com/r/whowouldwin/comments/wnqf17/what_character_got_the_most_extreme_power_leap/ik6mlsl/?context=3

########################################

id = get_rt_id(cur, 'Respect the Detective (Disco Elysium)', 'https://redd.it/wmk2f5')
add_data(['Detective'],
'Detective',
False,
False,
[
    ['Disco Elysium']
],
'Disco Elysium',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wmk2f5/respect_the_detective_disco_elysium/

########################################

id = get_rt_id(cur, 'Respect Guts (Death Battle!)', 'https://redd.it/wmyjzn')
add_data(['Guts'],
'Guts',
False,
False,
[
    ['Guts.*Death Battle']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wmyjzn/respect_guts_death_battle/

########################################

id = get_rt_id(cur, 'Respect Dovin Baan! (Magic: The Gathering)', 'https://redd.it/wnicpz')
add_data(['Dovin Baan'],
'Dovin Baan',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG'], ['Planeswalk(er)?s?']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wnicpz/respect_dovin_baan_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Takeshi Hongo aka Kamen Rider Ichigo! (Kamen Rider The First/Next)', 'https://redd.it/wnnklr')
add_data(['Kamen Rider(-| )Ichigo'],
'Kamen Rider Ichigo',
False,
True,
[
    ['First|Next']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wnnklr/respect_takeshi_hongo_aka_kamen_rider_ichigo/

########################################

id = get_rt_id(cur, 'Respect Hayato Ichimonji aka Kamen Rider Nigo! (Kamen Rider The First/Next)', 'https://redd.it/wnnkol')
add_data(['Kamen Rider Nigo'],
'Kamen Rider Nigo',
False,
True,
[
    ['First|Next']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wnnkol/respect_hayato_ichimonji_aka_kamen_rider_nigo/

########################################

id = get_rt_id(cur, 'Respect Shiro Kazami aka Kamen Rider V3! (Kamen Rider The First/Next)', 'https://redd.it/wnnkrd')
add_data(['Kamen Rider V3'],
'Kamen Rider V3',
False,
True,
[
    ['First|Next']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wnnkrd/respect_shiro_kazami_aka_kamen_rider_v3_kamen/

########################################

id = get_rt_id(cur, 'Respect The Sheep (Black Sheep) [NSFW] (gore)', 'https://redd.it/wno1ba')
add_data(['Sheep'],
'Sheep',
False,
False,
[
    ['Black Sheep', 'Oldfield']
],
'Black Sheep',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wno1ba/respect_the_sheep_black_sheep_nsfw_gore/

########################################

id = get_rt_id(cur, 'Respect X-23 (X-Men: Evolution)', 'https://redd.it/wnude6')
add_data(['X-?23'],
'X-23',
False,
True,
[
    ['X(-| )?Men:? Evolution']
],
'X-Men: Evolution',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wnude6/respect_x23_xmen_evolution/

########################################

id = get_rt_id(cur, 'Respect Elaine Coll, Scorpia (Marvel, 616)', 'https://redd.it/wo7x1k')
add_data(['Scorpia'],
'Scorpia',
False,
False,
[
    ['Elaine Coll', '616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wo7x1k/respect_elaine_coll_scorpia_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Highfather! (New 52)', 'https://redd.it/woszhn')
add_data(['High ?father'],
'Highfather',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/woszhn/respect_highfather_new_52/

########################################

id = get_rt_id(cur, 'Respect Darren Shan! (Cirque Du Freak Manga)', 'https://redd.it/wo8rll')
add_data(['Darren Shan'],
'Darren Shan',
False,
False,
[
    ['Cirque Du Freak', 'Manga'], ['CDF', 'Manga']
],
'Cirque Du Freak Manga',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wo8rll/respect_darren_shan_cirque_du_freak_manga/

########################################

id = get_rt_id(cur, 'Respect Larten Crepsley! (Cirque Du Freak Manga)', 'https://redd.it/wo8tdn')
add_data(['Larten Crepsley'],
'Larten Crepsley',
False,
False,
[
    ['Cirque Du Freak', 'Manga'], ['CDF', 'Manga']
],
'Cirque Du Freak Manga',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wo8tdn/respect_larten_crepsley_cirque_du_freak_manga/

########################################

id = get_rt_id(cur, 'Respect the Vord! (Codex Alera)', 'https://redd.it/wp0f79')
add_data(['Vord'],
'Vord',
False,
False,
[
    ['Codex Alera']
],
'Codex Alera',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wp0f79/respect_the_vord_codex_alera/

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

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

update_respectthread(cur, 317, 'Respect General Grievous (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/1pzzo40/respect_general_grievous_star_wars_canon/')
update_respectthread(cur, 5707, 'Respect the Demi-Fiend (Shin Megami Tensei)', 'https://www.reddit.com/r/respectthreads/comments/1q0hah4/respect_the_demifiend_shin_megami_tensei/')
update_respectthread(cur, 1469, 'Respect Logan Wayne, Dark Claw (Amalgam Comics)', 'https://www.reddit.com/r/respectthreads/comments/1q1g66m/respect_logan_wayne_dark_claw_amalgam_comics/')

########################################

id = get_rt_id(cur, 'Respect Bode Akuna (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/1q0s1cb/respect_bode_akuna_star_wars_canon/')
add_data(['Bode Akuna'],
'Bode Akuna',
False,
True,
[
    ['S(tar )?Wars'], ['Jedi:? Survivor']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Effigy (DC Comics, Post-Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1q020ed/respect_effigy_dc_comics_postcrisis/')
add_data(['Effigy'],
'Effigy',
False,
False,
[
    ['Effigy ?\(Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Effigy'],
'Effigy',
False,
False,
[
    ['Effigy from DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/33t3uh/who_is_the_strongest_the_flametastic_4_can_beat/

########################################

id = get_rt_id(cur, 'Respect Wile E Coyote (Looney Tunes)', 'https://www.reddit.com/r/respectthreads/comments/1q056nx/respect_wile_e_coyote_looney_tunes/')
add_data(['Wile E\.? Coyote'],
'Wile E. Coyote',
False,
True,
[
    ['Looney Tunes']
],
'Looney Tunes',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ash Ketchum! (Death Battle)', 'https://www.reddit.com/r/respectthreads/comments/1q0pmy2/respect_ash_ketchum_death_battle/')
add_data(['Ash Ketchum'],
'Ash Ketchum',
False,
False,
[
    ['Death Battle']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect John Egbert! (Homestuck the Animated Pilot)', 'https://www.reddit.com/r/respectthreads/comments/1q0urw6/respect_john_egbert_homestuck_the_animated_pilot/')
add_data(['John Egbert'],
'John Egbert',
False,
False,
[
    ['Homestuck the Animated Pilot']
],
'Homestuck the Animated Pilot',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Smoke! (Cartoon All-Stars to the Rescue)', 'https://www.reddit.com/r/respectthreads/comments/1q0vyxb/respect_smoke_cartoon_allstars_to_the_rescue/')
add_data(['Smoke'],
'Smoke',
False,
False,
[
    ['Cartoon All(-| )Stars to the Rescue']
],
'Cartoon All-Stars to the Rescue',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Captain Hook (Hook)', 'https://www.reddit.com/r/respectthreads/comments/1q0w0de/respect_captain_hook_hook/')
add_data(['Captain Hook'],
'Captain Hook',
False,
False,
[
    ['\(Hook\)']
],
'Hook',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect William Afton (Five Nights at Freddy''s Movie)", 'https://www.reddit.com/r/respectthreads/comments/1q0woj9/respect_william_afton_five_nights_at_freddys_movie/')
add_data(['William Afton'],
'William Afton',
False,
False,
[
    ["(Five Nights at Freddy''?s?|FNAF) (Movie|Film)"]
],
"Five Nights at Freddy''s, 2023",
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect the Justice Society (DCEU)', 'https://www.reddit.com/r/respectthreads/comments/1q17psv/respect_the_justice_society_dceu/')
add_data(['Justice Society'],
'Justice Society',
True,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Hawkman'],
'Hawkman',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ocho Tootmorsel (The Amazing World of Gumball)', 'https://www.reddit.com/r/respectthreads/comments/1q1da6h/respect_ocho_tootmorsel_the_amazing_world_of/')
add_data(['Ocho'],
'Ocho',
False,
False,
[
    ['Elmore', 'High|Gumball'], ['Tootmorsel'], ['Amazing World of Gumball']
],
'The Amazing World of Gumball',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect Andrew Emory''s Pack (World of Darkness)", 'https://www.reddit.com/r/respectthreads/comments/1q1fcr0/respect_andrew_emorys_pack_world_of_darkness/')
add_data(['Andrew Emory'],
'Andrew Emory',
False,
False,
[
    ['World of Darkness']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Year 2012 (2012 Movie)', 'https://www.reddit.com/r/respectthreads/comments/1q1fwrh/respect_the_year_2012_2012_movie/')
add_data(['2012'],
'2012',
False,
False,
[
    ['2012.*\(2012 (Movie|Film)\)'], ['2012 ?\(2009\)']
],
'2009',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cyn, and the Absolute Solver! (Murder Drones)', 'https://www.reddit.com/r/respectthreads/comments/1q1mhpu/respect_cyn_and_the_absolute_solver_murder_drones/')
add_data(['Cyn'],
'Cyn',
False,
False,
[
    ['Murder Drones']
],
'Murder Drones',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Wonder Woman (Batman: The Brave and the Bold)', 'https://www.reddit.com/r/respectthreads/comments/1q1po58/respect_wonder_woman_batman_the_brave_and_the_bold/')
add_data(['Wonder ?Woman'],
'Wonder Woman',
False,
False,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Scorch Worm (Loop Hero)', 'https://www.reddit.com/r/respectthreads/comments/1q1stf1/respect_scorch_worm_loop_hero/')
add_data(['Scorch Worms?'],
'Scorch Worm',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Sand Spirit (Loop Hero)', 'https://www.reddit.com/r/respectthreads/comments/1q1t3q5/respect_sand_spirit_loop_hero/')
add_data(['Sand Spirits?'],
'Sand Spirit',
False,
False,
[
    ['Loop Hero']
],
'Loop Hero',
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

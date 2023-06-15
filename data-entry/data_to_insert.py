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

id = get_rt_id(cur, 'Respect Meatgardener Venom! (Marvel)', 'https://redd.it/145m5r0')
add_data(['Meatgardener Venom'],
'Meatgardener Venom',
False,
True,
[
    ['23203']
],
'23203',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/145m5r0/respect_meatgardener_venom_marvel/


########################################

id = get_rt_id(cur, 'Respect Astral Regulator Thanos! (Marvel Earth-81488)', 'https://redd.it/146fdx2')
add_data(['AR Thanos'],
'AR Thanos',
False,
True,
[
    ['81488']
],
'81488',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146fdx2/respect_astral_regulator_thanos_marvel_earth81488/

add_data(['Thanos'],
'Thanos',
False,
False,
[
    ['Astral Regulator']
],
'Astral Regulator',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146fdx2/respect_astral_regulator_thanos_marvel_earth81488/

########################################

id = get_rt_id(cur, 'Respect Arachknight (Marvel Comics)', 'https://redd.it/146u4at')
add_data(['Arachknight'],
'Arachknight',
False,
True,
[
    ['Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146u4at/respect_arachknight_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect Creature Z (Marvel, 616)', 'https://redd.it/146ybx8')
add_data(['Creature Z'],
'Creature Z',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146ybx8/respect_creature_z_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Little Monster (Marvel Comics)', 'https://redd.it/146zko2')
add_data(['Little Monster'],
'Little Monster',
False,
False,
[
    ['Marvel', 'Comics']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146zko2/respect_little_monster_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect: Ben Reilly, The Scarlet Spider (Marvel Animated Universe)', 'https://redd.it/149gey6')
add_data(['Scarlet Spider'],
'Scarlet Spider',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/149gey6/respect_ben_reilly_the_scarlet_spider_marvel/

########################################

id = get_rt_id(cur, 'Respect: Peter Parker, the Armored Spider-Man (Marvel Animated Universe)', 'https://redd.it/14a7g3h')
add_data(['Armou?red Spider(-| )?Man'],
'Armored Spider-Man',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14a7g3h/respect_peter_parker_the_armored_spiderman_marvel/

########################################

id = get_rt_id(cur, 'Respect Milkman Man (DC Comics)', 'https://redd.it/146vvhm')
add_data(['Milkman (Super)?Man'],
'Milkman Man',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146vvhm/respect_milkman_man_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Mandrakk (DC post-crisis)', 'https://redd.it/149agqy')
add_data(['Mandrakk'],
'Mandrakk',
False,
True,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/149agqy/respect_mandrakk_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Chrom (Fire Emblem Awakening)', 'https://redd.it/145ucpi')
add_data(['Chrom'],
'Chrom',
False,
False,
[
    ['Fire Emblem'], ['Awakening'], ['Robin|Lucina|Marth']
],
'Fire Emblem Awakening',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Minimum Tarnished (Elden Ring)', 'https://redd.it/146cxz5')
add_data(['Tarnished'],
'Tarnished',
False,
False,
[
    ['The Tarnished vs|vs\.? The Tarnished'], ['Elden (Ring|Lord)'], ['Tarnished ?\(ER\)'],
    ['Can a Tarnished'], ['vs\.? Tarnished|Tarnished vs', 'Dragon ?borne?|LOTR']
],
'Elden Ring',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/146cxz5/respect_minimum_tarnished_elden_ring/

########################################

id = get_rt_id(cur, 'Respect SCP-049-J, The Plague Fellow (SCP Foundation)', 'https://redd.it/1474wsg')
add_data(['SCP ?(-| )? ?049 ?(-| )? ?J'],
'SCP-049-J',
False,
True,
[
    ['Plague Fellow']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1474wsg/respect_scp049j_the_plague_fellow_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Clifford DeVoe, The Thinker (Arrowverse)', 'https://redd.it/149cuia')
add_data(['Thinker'],
'Thinker',
False,
False,
[
    ['Thinker ?\((from )?CW'], ['(Fl)?arrow(-| )?verse'], ['The Thinker CW'], ['The Thinker', 'DC CW']
],
'CW Arrowverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/149cuia/respect_clifford_devoe_the_thinker_arrowverse/

########################################

id = get_rt_id(cur, 'Respect Hotstreak (Static Shock)', 'https://redd.it/14a2fpd')
add_data(['Hotstreak'],
'Hotstreak',
False,
False,
[
    ['Static Shock'], ['DCAU']
],
'DCAU',
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

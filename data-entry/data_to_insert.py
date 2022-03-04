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

add_data(['Optimus Prime'],
'Optimus Prime',
False,
False,
[
    ['Optimus Prime ?\(Live(-| )Action'], ['Optimus Prime ?\(Movies?'],
    ['Revenge of the Fallen']
],
'Transformers Films',
'{339}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6dlr1/optimus_prime_live_action_films_vs_the_hulk_mcu/

########################################

add_data(['Optimus Prime'],
'Optimus Prime',
False,
False,
[
    ['Optimus Prime ?\(Live(-| )Action'], ['Optimus Prime ?\(Movies?'],
    ['Revenge of the Fallen']
],
'Transformers Films',
'{339}'
)
#

########################################

add_data(['Maya Lopez'],
'Maya Lopez',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{21147}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6jax6/us_agent_vs_kate_bishop_maya_lopez_and_jack/hzbdsro/?context=3

########################################

add_data(['Jack Duquesne'],
'Jack Duquesne',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{21148}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6jax6/us_agent_vs_kate_bishop_maya_lopez_and_jack/hzbdsro/?context=3

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Bat(-| )?mans?.*2022'], ['The Batman', '2022'],
    ['Pattin?son']
],
'The Batman, 2022',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6gups/batman_and_catwoman_2022_vs_bane_tdk/

########################################

id = get_rt_id(cur, 'Respect SCP-056, A Beautiful Person (SCP Foundation)', 'https://redd.it/t680j7')
add_data(['SCP ?(-| )? ?056'],
'SCP-056',
False,
False,
[
    ['Beautiful Person']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t680j7/respect_scp056_a_beautiful_person_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Kate Bishop, Hawkeye! {MCU}', 'https://comicvine.gamespot.com/forums/gen-discussion-1/respect-kate-bishop-hawkeye-mcu-2249411/')
add_data(['Kate Bishop'],
'Kate Bishop',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6jax6/us_agent_vs_kate_bishop_maya_lopez_and_jack/hzbdsro/?context=3

########################################

id = get_rt_id(cur, 'Vehicles BatmanMegaRT', 'https://redd.it/859k0m')
add_data(['Bat(-| )?mobile'],
'Batmobile',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6sze3/batman_vs_mr_incrediblewith_a_twist/hzd8g82/?context=3
#https://www.reddit.com/r/BatmanMegaRT/comments/859k0m/vehicles/

add_data(['Bat(-| )?mobile'],
'Batmobile',
False,
True,
[
    ['\(DC\)'], ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/t6sze3/batman_vs_mr_incrediblewith_a_twist/hzd8g82/?context=3

add_data(['Bat(-| )?mobile'],
'Batmobile',
False,
False,
[
    ['Bale']
],
'Nolanverse',
'{}'
)
#

add_data(['Bat(-| )?mobile'],
'Batmobile',
False,
False,
[
    ['Arkham city']
],
'Batman: Arkham',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Angela Baker (Sleepaway Camp)', 'https://redd.it/t6joe8')
add_data(['Angela Baker'],
'Angela Baker',
False,
True,
[
    ['Sleepaway Camp']
],
'Sleepaway Camp',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t6joe8/respect_angela_baker_sleepaway_camp/

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

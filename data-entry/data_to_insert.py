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

update_respectthread(cur, 23995, 'Protagonist (What Gun for Home Protection Would Be a Very Bad Idea?)', 'https://redd.it/1558euc')
update_respectthread(cur, 12425, 'Respect Seth Brundle (The Fly, 1986)', 'https://redd.it/1558jx2')

########################################

add_data(['Brundlefly'],
'Brundlefly',
False,
True,
[
    ['The Fly']
],
'The Fly',
'{12425}'
)
#

########################################

add_data(['Raven'],
'Raven',
False,
False,
[
    ['Raven from DC']
],
'DC',
'{1832}'
)
#https://www.reddit.com/r/whowouldwin/comments/15289c0/death_battle_phoenix_jean_grey_vs_raven_from_dc/jscj33h/?context=3

########################################

add_data(['Dom'],
'Dom',
False,
False,
[
    ['Fast and (the )?Furious'], ['Fast & Furious']
],
'The Fast and the Furious',
'{135}'
)
#https://www.reddit.com/r/whowouldwin/comments/152wtkc/who_is_the_most_powerful_anime_character_that_the/jsg0dhq/?context=3

########################################

add_data(['Big Hero 6'],
'Big Hero 6',
True,
False,
[
    ['Big Hero 6 \(Disney\) vs'], ['vs\.? Big Hero 6'], ['Big Hero 6 \(Team\)'], [['Big Hero 6 Team']]
],
'Disney',
'{10863, 10869, 10870, 10873, 10872, 10851}'
)
#https://www.reddit.com/r/whowouldwin/comments/1528f3g/big_hero_6_disney_vs_guardians_of_the_galaxy_mcu/jscft5i/?context=3

########################################

id = get_rt_id(cur, 'Respect Sise-Neg (Marvel, Earth-74113)', 'https://redd.it/151qxz3')
add_data(['Sise(-| )Neg'],
'Sise-Neg',
False,
True,
[
    ['74113']
],
'74113',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/151qxz3/respect_siseneg_marvel_earth74113/

########################################

id = get_rt_id(cur, 'Respect Assassin Spider-Man (Marvel Comics: Earth 8351)', 'https://redd.it/153vm46')
add_data(['Assassin Spider(-| )?Man'],
'Assassin Spider-Man',
False,
True,
[
    ['8351']
],
'8351',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/153vm46/respect_assassin_spiderman_marvel_comics_earth/

########################################

id = get_rt_id(cur, 'Respect Peter Parker, The Punishing Spider (Marvel Comics: Earth 71928)', 'https://redd.it/1551bzc')
add_data(['Punish(ing|er) Spider'],
'Punishing Spider',
False,
True,
[
    ['71928']
],
'71928',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1551bzc/respect_peter_parker_the_punishing_spider_marvel/

########################################

id = get_rt_id(cur, 'Respect Duff Killigan (Kim Possible)', 'https://redd.it/1534z9d')
add_data(['Duff Killigan'],
'Duff Killigan',
False,
True,
[
    ['Kim Possible']
],
'Kim Possible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1534z9d/respect_duff_killigan_kim_possible/

########################################

id = get_rt_id(cur, 'Respect Darth Vader (Death Battle)', 'https://redd.it/1544nu3')
add_data(['Vader'],
'Darth Vader',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1544nu3/respect_darth_vader_death_battle/

########################################

id = get_rt_id(cur, 'Respect Obito Uchiha! (DEATH BATTLE!)', 'https://redd.it/1544po8')
add_data(['Obito'],
'Uchiha',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1544po8/respect_obito_uchiha_death_battle/

########################################

id = get_rt_id(cur, 'Respect Q! (Q)', 'https://redd.it/1557x7d')
add_data(['Q'],
'Q',
False,
False,
[
    ['Q ?\(Q\)']
],
'Q',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1557x7d/respect_q_q/

########################################

id = get_rt_id(cur, "Respect Ruby Gillman (DreamWorks'' Ruby Gillman, Teenage Kraken)", 'https://redd.it/155d0mr')
add_data(['Ruby Gillman'],
'Ruby Gillman',
False,
True,
[
    ['Teenage Kraken']
],
'Ruby Gillman, Teenage Kraken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/155d0mr/respect_ruby_gillman_dreamworks_ruby_gillman/

########################################

id = get_rt_id(cur, 'Respect Dargo Ktor, the Once and Future Thor (Marvel Comics, Earth-8710)', 'https://redd.it/155wufm')
add_data(['Dargo Kth?or'],
'Dargo Ktor',
False,
True,
[
    ['8710']
],
'8710',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/155wufm/respect_dargo_ktor_the_once_and_future_thor/

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

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

update_respectthread(cur, 6147, "Respect Wan ShaiLu (The Emporer''s Soul)", 'https://redd.it/10e3q2r')
update_respectthread(cur, 5720, 'Respect Rick Taylor (Splatterhouse) (Classic)', 'https://redd.it/10ebojc')

########################################

add_data(['Aku'],
'Aku',
False,
False,
[
    ['Ganon(dorf)?', 'vs\.? Aku']
],
'Samurai Jack',
'{879}'
)
#https://www.reddit.com/r/whowouldwin/comments/10d68up/ganondorf_vs_aku/j4jvcsu/?context=3

########################################

add_data(['Afton'],
'Afton',
False,
False,
[
    ['William']
],
'FNAF',
'{21263}'
)
#https://www.reddit.com/r/whowouldwin/comments/10dxnz8/another_isekaid_hero_midoriya_vs_afton/j4nrqx4/?context=3

########################################

add_data(['Din Djarin'],
'Din Djarin',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{8117}'
)
#https://www.reddit.com/r/whowouldwin/comments/10ecvbn/whos_the_best_jedi_that_peak_din_djarin_beats_in/j4q36g8/?context=3

add_data(['Mando'],
'Mando',
False,
False,
[
    ['S(tar )?Wars'], ['Boba|Fett'], ['Greef Karga'], ['Disintegrat(ing|or)', 'rifle'],
    ['Mando vs|vs\.? Mando', 'Captain America|Black Panther|Geralt|Predator'], ['Din'], ['Dark ?saber'], ['Grievous'], ['Yoda'], ['Ahsoka'], ['MCU Gauntlet'],
    ['Bounty Hunters?']
],
'Star Wars',
'{8117}'
)
#https://www.reddit.com/r/whowouldwin/comments/10ecvbn/whos_the_best_jedi_that_peak_din_djarin_beats_in/j4q36g8/?context=3

########################################

id = get_rt_id(cur, 'Respect AonDor and the Elantrians (Elantris)', 'https://redd.it/10d655u')
add_data(['AonDor'],
'AonDor',
False,
True,
[
    ['Elantris'], ['Elantrians?'], ['Cosmere']
],
'Elantris',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10d655u/respect_aondor_and_the_elantrians_elantris/

add_data(['Elantrians?'],
'Elantrians',
False,
True,
[
    ['Elantris'], ['Cosmere']
],
'Elantris',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10d655u/respect_aondor_and_the_elantrians_elantris/

########################################

id = get_rt_id(cur, 'Respect Crunch (Crash Bandicoot)', 'https://redd.it/10di7h3')
add_data(['Crunch'],
'Crunch',
False,
False,
[
    ['Crash Bandicoot'], ['Crunch Bandicoot']
],
'Crash Bandicoot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10di7h3/respect_crunch_crash_bandicoot/

########################################

id = get_rt_id(cur, 'Respect Blade (Marvel Anime, Madhouse)', 'https://redd.it/10dihwn')
add_data(['Blade'],
'Blade',
False,
False,
[
    ['Blade ?\(Marvel Anime'], ['Marvel Anime', 'Madhouse']
],
'Marvel Anime',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10dihwn/respect_blade_marvel_anime_madhouse/

########################################

id = get_rt_id(cur, 'Respect Nanako! (Tsukihime)', 'https://redd.it/10dxc0l')
add_data(['Nanako'],
'Nanako',
False,
False,
[
    ['Tsukihime']
],
'Tsukihime',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10dxc0l/respect_nanako_tsukihime/

########################################

id = get_rt_id(cur, 'Respect Ciel! (Tsukihime)', 'https://redd.it/10dxe7p')
add_data(['Ciel'],
'Ciel',
False,
False,
[
    ['Tsukihime']
],
'Tsukihime',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10dxe7p/respect_ciel_tsukihime/

########################################

id = get_rt_id(cur, "Respect Aquaman (La''gaan, Young Justice)", 'https://redd.it/10e1dby')
add_data(["La''gaan"],
"La''gaan",
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10e1dby/respect_aquaman_lagaan_young_justice/

########################################

id = get_rt_id(cur, 'Respect Anguirus (Godzilla Singular Point)', 'https://redd.it/10e3tbj')
add_data(['Anguirus'],
'Anguirus',
False,
False,
[
    ['Godzilla Singular Point']
],
'Godzilla Singular Point',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10e3tbj/respect_anguirus_godzilla_singular_point/

########################################

id = get_rt_id(cur, 'Respect Rick Taylor (Splatterhouse: Wanpaku Graffiti)', 'https://redd.it/10ebok6')
add_data(['Rick Taylor'],
'Rick Taylor',
False,
False,
[
    ['Wanpaku Graffiti']
],
'Splatterhouse: Wanpaku Graffiti',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10ebok6/respect_rick_taylor_splatterhouse_wanpaku_graffiti/

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

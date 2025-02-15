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

add_data(['Tricky'],
'Tricky',
False,
False,
[
    ['Hank', 'Accelerant']
],
'Madness Combat',
'{1284}'
)
#

add_data(['Hank'],
'Hank',
False,
False,
[
    ['Tricky', 'Accelerant']
],
'Madness Combat',
'{23044}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ine2mi/goku_vs_shaggy_matt_tricky_accelerant_hank_bob/mca7lo6/?context=3

########################################

id = get_rt_id(cur, 'Respect Orla Jareni (Star Wars Canon)', 'https://redd.it/1ing0ca')
add_data(['Orla Jareni'],
'Orla Jareni',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shovel-Man (Wizards with Guns)', 'https://redd.it/1iobc37')
add_data(['Shovel(-| )Man'],
'Shovel-Man',
False,
False,
[
    ['Wizards with Guns']
],
'Wizards with Guns',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1iobc37/respect_shovelman_wizards_with_guns/

########################################

id = get_rt_id(cur, "Respect Beatrice''s Demons! (Umineko: When They Cry [Manga])", 'https://redd.it/1io7436')
add_data(["Beatrice''?s Demons"],
"Beatrice''s Demons",
True,
False,
[
    ['Umineko']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1io7436/respect_beatrices_demons_umineko_when_they_cry/

add_data(['Ronove'],
'Ronove',
False,
False,
[
    ['Umineko'], ['Beatrice']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1io7436/respect_beatrices_demons_umineko_when_they_cry/

add_data(['Gaap'],
'Gaap',
False,
False,
[
    ['Umineko'], ['Beatrice']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1io7436/respect_beatrices_demons_umineko_when_they_cry/

add_data(['(Seven|7) Sisters of Purgatory'],
'Seven Sisters of Purgatory',
True,
False,
[
    ['Umineko'], ['Beatrice']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1io7436/respect_beatrices_demons_umineko_when_they_cry/

########################################

id = get_rt_id(cur, 'Respect the Chiester Imperial Guard Corps (Umineko: When They Cry [Manga])', 'https://redd.it/1io7u64')
add_data(['Chiesters?'],
'Chiesters',
True,
False,
[
    ['Umineko']
],
'Umineko',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Hulk (Marvel Rivals)', 'https://redd.it/1ipdlif')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['Marvel Rivals']
],
'Marvel Rivals',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Professor Hugo Strange (DC Comics, Post-Crisis)', 'https://redd.it/1ionl93')
add_data(['Hugo Strange'],
'Hugo Strange',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Hugo Strange'],
'Hugo Strange',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#


add_data(['Hugo Strange'],
'Hugo Strange',
False,
False,
[
    ['Arkham.?verse'], ['\(Arkham\)'], ['Arkham (ga(m|n)es?|series)'], ['Batman: Arkham']
],
'Post-Crisis',
'{}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ares (Fortnite)', 'https://redd.it/1ip65zp')
add_data(['Ares'],
'Ares',
False,
False,
[
    ['Ares.*Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shaq! (Fortnite)', 'https://redd.it/1ipt4ay')
add_data(['Shaq'],
'Shaq',
False,
False,
[
    ['Shaq.*Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Peelverine (Fortnite)', 'https://redd.it/1iptxhm')
add_data(['Peelverine'],
'Peelverine',
False,
True,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Megalo Don (Fortnite)', 'https://redd.it/1ipvadj')
add_data(['Megalo Don'],
'Megalo Don',
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

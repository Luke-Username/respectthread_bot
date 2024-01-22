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

update_respectthread(cur, 5196, 'Respect Pantheon, the Unbreakable Spear (League of Legends)', 'https://redd.it/19bew8s')

########################################

add_data(['Naruto'],
'Naruto',
False,
False,
[
    ['Smiths', 'Rick (&|and) Morty']
],
'Rick and Morty',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/199eto2/strongest_character_all_of_the_smiths_from_rick/kidrh6x/?context=3

########################################

id = get_rt_id(cur, 'Respect Xerath, the Magus Ascendant (League of Legends)', 'https://redd.it/199hmqo')
add_data(['Xerath'],
'Xerath',
False,
True,
[
    ['League'], ['LOL'], ['Syndra']
],
'League of Legends',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/199hmqo/respect_xerath_the_magus_ascendant_league_of/

########################################

id = get_rt_id(cur, "Respect Dr. Michael Morbius, Cinema''s Most Tragically Memed-Upon Superhero! (SCP Explained)", 'https://redd.it/19bba15')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['SCP Explained']
],
'SCP Explained',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/199hmqo/respect_xerath_the_magus_ascendant_league_of/

########################################

id = get_rt_id(cur, 'Respect the Host! (Cyndago)', 'https://redd.it/19bbdg4')
add_data(['The Host'],
'The Host',
False,
False,
[
    ['Cyndago']
],
'Cyndago',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19bbdg4/respect_the_host_cyndago/

########################################

id = get_rt_id(cur, 'Respect the Fifth Doctor (Doctor Who)', 'https://redd.it/19c7mye')
add_data(['(Fif|5)th Doctor'],
'The Fifth Doctor',
False,
True,
[
    ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19c7mye/respect_the_fifth_doctor_doctor_who/

########################################

id = get_rt_id(cur, "Respect Spider-Man 2099 (Sony''s Spider-Verse)", 'https://redd.it/19cb8k4')
add_data(['Spider(-| )?Man 2099'],
'Spider-Man 2099',
False,
False,
[
    ['Spider(-| )?Verse'], ['ITSV']
],
'Into the Spider-Verse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19cb8k4/respect_spiderman_2099_sonys_spiderverse/

########################################

id = get_rt_id(cur, 'Respect Wesley Gibson! (Wanted)', 'https://redd.it/19cgnco')
add_data(['Wesley Gibson'],
'Wesley Gibson',
False,
True,
[
    ['Wanted']
],
'Wanted',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/19cgnco/respect_wesley_gibson_wanted/

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

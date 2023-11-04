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

update_respectthread(cur, 1935, 'Respect Godzilla (Marvel Comics, Earth-616)', 'https://redd.it/17mvoiu')
update_respectthread(cur, 182, 'Respect Godzilla (Godzilla Franchise, Heisei Continuity)', 'https://redd.it/17mvoua')

########################################

id = get_rt_id(cur, 'Respect Gigan (Godzilla Franchise, Gemstone Creative Label)', 'https://redd.it/17l3kr6')
add_data(['Gigan'],
'Gigan',
False,
False,
[
    ['Gemstone']
],
'Gemstone Creative Label',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17l3kr6/respect_gigan_godzilla_franchise_gemstone/

########################################

id = get_rt_id(cur, 'Respect Godzilla (Gemstone Creative Label)', 'https://redd.it/17mvofx')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Gemstone']
],
'Gemstone Creative Label',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17mvofx/respect_godzilla_gemstone_creative_label/

########################################

id = get_rt_id(cur, 'Respect Mothra Leo (Rebirth Of Mothra)', 'https://redd.it/17l71um')
add_data(['Mothra Leo'],
'Mothra Leo',
False,
False,
[
    ['Rebirth']
],
'Rebirth Of Mothra',
'{' + '{}'.format(id) + '}'
)
#

########################################

########################################

id = get_rt_id(cur, 'Respect the Swine-Things! (The House on the Borderland)', 'https://redd.it/17lq56o')
add_data(['Swine(-| )Things?'],
'Swine-Things',
False,
False,
[
    ['House on the Borderland']
],
'The House on the Borderland',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17lq56o/respect_the_swinethings_the_house_on_the/

########################################

id = get_rt_id(cur, 'Respect Tiny Box Tim! (Markiplier Animated)', 'https://redd.it/17lqeny')
add_data(['Tiny Box Tim'],
'Tiny Box Tim',
False,
True,
[
    ['Markiplier']
],
'Markiplier Animated',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17lqeny/respect_tiny_box_tim_markiplier_animated/

########################################

id = get_rt_id(cur, 'Respect Trish (Devil May Cry)', 'https://redd.it/17ma459')
add_data(['Trish'],
'Trish',
False,
False,
[
    ['Devil May Cry'], ['DMC\d?']
],
'Devil May Cry',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ma459/respect_trish_devil_may_cry/

########################################

id = get_rt_id(cur, "Respect Sam Riordan (Amazon''s The Boys: Gen V)", 'https://redd.it/17mthf7')
add_data(['Sam Riordan'],
'Sam Riordan',
False,
True,
[
    ['The Boys'], ['Gen V']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17mthf7/respect_sam_riordan_amazons_the_boys_gen_v/

########################################

id = get_rt_id(cur, 'Test Scooby-Doo! (Velma Meets the Original Velma)', 'https://redd.it/17ls3ds')
add_data(['Scooby'],
'Scooby-Doo',
False,
False,
[
    ['Velma Meets the Original Velma']
],
'Velma Meets the Original Velma',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ls3ds/test_scoobydoo_velma_meets_the_original_velma/

########################################

id = get_rt_id(cur, "Respect Ma''alefa''ak J''onzz! (DC Comics, Post-Crisis)", 'https://redd.it/17mwf74')
add_data(["Ma''alefa''ak"],
"Ma''alefa''ak",
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17mwf74/respect_maalefaak_jonzz_dc_comics_postcrisis/

add_data(["Ma''alefa''ak"],
"Ma''alefa''ak",
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17mwf74/respect_maalefaak_jonzz_dc_comics_postcrisis/

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

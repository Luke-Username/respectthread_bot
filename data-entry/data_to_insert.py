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

update_respectthread(cur, 2177, 'Respect Iron Man Model 50: the Endo-Sym Armor (Marvel, Earth-616)', 'https://redd.it/16gwyiq')
update_respectthread(cur, 923, 'Respect Embo (Star Wars Canon)', 'https://redd.it/16glcz3')

########################################

id = get_rt_id(cur, 'Respect Gin Ichimaru (Bleach)', 'https://redd.it/csbw41')
add_data(['Gin Ichimaru|Ichimaru Gin'],
'Gin Ichimaru',
False,
True,
[
    ['Bleach']
],
'Bleach',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/csbw41/respect_gin_ichimaru_bleach/

add_data(['Gin'],
'Gin',
False,
False,
[
    ['Bleach']
],
'Bleach',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/csbw41/respect_gin_ichimaru_bleach/

########################################

id = get_rt_id(cur, 'Respect Majima (Lycoris Recoil)', 'https://redd.it/16f9w8t')
add_data(['Majima'],
'Majima',
False,
False,
[
    ['Lycoris Recoil']
],
'Lycoris Recoil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16f9w8t/respect_majima_lycoris_recoil/

########################################

id = get_rt_id(cur, 'Respect Takina Inoue (Lycoris Recoil)', 'https://redd.it/16fbqb5')
add_data(['Takina'],
'Takina',
False,
False,
[
    ['Lycoris Recoil'], ['Takina Inoue']
],
'Lycoris Recoil',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Chisato Nishikigi (Lycoris Recoil)', 'https://redd.it/16fbqeg')
add_data(['Chisato'],
'Chisato',
False,
False,
[
    ['Lycoris Recoil'], ['Chisato Nishikigi']
],
'Lycoris Recoil',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fbqeg/respect_chisato_nishikigi_lycoris_recoil/

########################################

id = get_rt_id(cur, 'Respect El Gusano Gigante (Godzilla: The Series)', 'https://redd.it/16fhu6w')
add_data(['El Gusano Gigante'],
'El Gusano Gigante',
False,
True,
[
    ['Godzilla']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fhu6w/respect_el_gusano_gigante_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect the Mutant Bees (Godzilla: The Series)', 'https://redd.it/16fi4ms')
add_data(['Mutant Bees?'],
'Mutant Bees',
False,
False,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fi4ms/respect_the_mutant_bees_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect the Tachyon Aliens (Godzilla: The Series)', 'https://redd.it/16fkdho')
add_data(['Tachyon Aliens?'],
'Tachyon Aliens',
False,
False,
[
    ['Godzilla']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fi4ms/respect_the_mutant_bees_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect the King Cobra (Godzilla: The Series)', 'https://redd.it/16fy2zl')
add_data(['King Cobra'],
'King Cobra',
False,
False,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fy2zl/respect_the_king_cobra_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Crustaceous Rex (Godzilla: The Series)', 'https://redd.it/16fycfx')
add_data(['Crustaceous Rex'],
'Crustaceous Rex',
False,
True,
[
    ['Godzilla']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fycfx/respect_crustaceous_rex_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect the Giant Bat (Godzilla: The Series)', 'https://redd.it/16fykg8')
add_data(['Giant Bat'],
'Giant Bat',
False,
False,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fykg8/respect_the_giant_bat_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Skeetera (Godzilla: The Series)', 'https://redd.it/16fz6ug')
add_data(['Skeetera'],
'Skeetera',
False,
True,
[
    ['Godzilla']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16fz6ug/respect_skeetera_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 16: the Renaissance Armor (Marvel, Earth-616)', 'https://redd.it/16g60n5')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 16'], ['Renaissance Armor']
],
'Renaissance Armor',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16g60n5/respect_iron_man_model_16_the_renaissance_armor/

########################################

id = get_rt_id(cur, 'Respect the Iron Man Safe/Sentient Armor (Marvel, Earth-616)', 'https://redd.it/16g62tl')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Sentient Armor'], ['The I(ro|or)n(-| )?Man Safe', '616']
],
'Sentient Armor',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16g62tl/respect_the_iron_man_safesentient_armor_marvel/

########################################

id = get_rt_id(cur, 'Respect Venom (Marvel Animated Universe)', 'https://redd.it/16gb1iu')
add_data(['Venom'],
'Venom',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16gb1iu/respect_venom_marvel_animated_universe/

########################################

id = get_rt_id(cur, 'Respect Carnage (Marvel Animated Universe)', 'https://redd.it/16gb1tf')
add_data(['Carnage'],
'Carnage',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16gb1tf/respect_carnage_marvel_animated_universe/

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

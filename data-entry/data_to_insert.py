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

update_respectthread(cur, 17395, 'Respect The Devil of the Rhine, Tanya von Degurechaff! (The Saga of Tanya the Evil)', 'https://redd.it/1dry5rr')
update_respectthread(cur, 5611, 'Respect Agent 47 (Hitman)', 'https://redd.it/1ds4c3y')

########################################

id = get_rt_id(cur, 'Respect Diana Burnwood (Hitman)', 'https://redd.it/1ds4c8x')
add_data(['Diana Burnwood'],
'Diana Burnwood',
False,
False,
[
    ['Hitman']
],
'Hitman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1ds4c8x/respect_diana_burnwood_hitman/

########################################

id = get_rt_id(cur, 'Respect Vincent/Jackson (Pokemon Anime)', 'https://redd.it/1dpr3j7')
add_data(['Vincent'],
'Vincent',
False,
False,
[
    ['Vincent.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dpr3j7/respect_vincentjackson_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Malekith the Accursed! (Marvel Comics, Earth-616)', 'https://redd.it/1dpxr5z')
add_data(['Malekith'],
'Malekith',
False,
False,
[
    ['Marvel'], ['616']
    ['Malekith the Accursed']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dpxr5z/respect_malekith_the_accursed_marvel_comics/


########################################

id = get_rt_id(cur, 'Respect Ironman model 10: Space Armour Mark II (Marvel Comics, Earth-616)', 'https://redd.it/1drftn2')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 10'], ['Space Armou?r Mark (2|II)']
],
'Model 10',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drftn2/respect_ironman_model_10_space_armour_mark_ii/

########################################

id = get_rt_id(cur, 'Respect Kobayashi (Sakamoto Days)', 'https://redd.it/1drbt35')
add_data(['Kobayashi'],
'Kobayashi',
False,
False,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drbt35/respect_kobayashi_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Nagumo (Sakamoto Days)', 'https://redd.it/1dsfev0')
add_data(['Nagumo'],
'Nagumo',
False,
False,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsfev0/respect_nagumo_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Higuchi (Sakamoto Days)', 'https://redd.it/1dqgznm')
add_data(['Higuchi'],
'Higuchi',
False,
False,
[
    ['Sakamoto Days']
],
'Sakamoto Days',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dqgznm/respect_higuchi_sakamoto_days/

########################################

id = get_rt_id(cur, 'Respect Garland! (Final Fantasy)', 'https://redd.it/1dshxdg')
add_data(['Garland'],
'Garland',
False,
False,
[
    ['Final Fantasy'], ['FF\d?\d?']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dshxdg/respect_garland_final_fantasy/

########################################

id = get_rt_id(cur, 'Respect Silver Banshee and Intergang! (My Adventures with Superman)', 'https://redd.it/1drko0t')
add_data(['Intergang'],
'Intergang',
True,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drko0t/respect_silver_banshee_and_intergang_my/

add_data(['Silver Banshee'],
'Silver Banshee',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drko0t/respect_silver_banshee_and_intergang_my/

########################################

id = get_rt_id(cur, 'Respect Dr. Anthony Ivo, Parasite! (My Adventures with Superman)', 'https://redd.it/1drkogp')
add_data(['Parasite'],
'Parasite',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mr. Mxyzptlk (My Adventures with Superman)', 'https://redd.it/1dros3c')
add_data(['Mxyzptlk'],
'Mister Mxyzptlk',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dros3c/respect_mr_mxyzptlk_my_adventures_with_superman/

########################################

id = get_rt_id(cur, 'Respect Slade Wilson, Deathstroke! (My Adventures with Superman)', 'https://redd.it/1drotbv')
add_data(['Death(-| )?stroke'],
'Deathstroke',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drotbv/respect_slade_wilson_deathstroke_my_adventures/

########################################

id = get_rt_id(cur, 'Respect Superman! (My Adventures with Superman)', 'https://redd.it/1dsb7e9')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsb7e9/respect_superman_my_adventures_with_superman/

########################################

id = get_rt_id(cur, 'Respect Leslie Willis, Livewire! (My Adventures with Superman)', 'https://redd.it/1dsb5z5')
add_data(['Livewire'],
'Livewire',
False,
False,
[
    ['My Adventures with Superman']
],
'My Adventures with Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsb5z5/respect_leslie_willis_livewire_my_adventures_with/

########################################

id = get_rt_id(cur, 'Respect Zapp Renfro (Kekkai Sensen)', 'https://redd.it/1drvzbe')
add_data(['Zapp Renfro'],
'Zapp Renfro',
False,
True,
[
    ['Kekkai Sensen']
],
'Kekkai Sensen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drvzbe/respect_zapp_renfro_kekkai_sensen/

########################################

id = get_rt_id(cur, 'Respect Steven A. Starphase (Kekkai Sensen)', 'https://redd.it/1drw1jv')
add_data(['Steven A\.? Starphase'],
'Steven A. Starphase',
False,
True,
[
    ['Kekkai Sensen']
],
'Kekkai Sensen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drw1jv/respect_steven_a_starphase_kekkai_sensen/

########################################

id = get_rt_id(cur, 'Respect Klaus von Reinherz (Kekkai Sensen)', 'https://redd.it/1drw3ht')
add_data(['Klaus Von Reinherz'],
'Klaus Von Reinherz',
False,
True,
[
    ['Kekkai Sensen']
],
'Kekkai Sensen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drw3ht/respect_klaus_von_reinherz_kekkai_sensen/

########################################

id = get_rt_id(cur, 'Respect Johnny (In A Violent Nature)', 'https://redd.it/1drw2y1')
add_data(['Johnny'],
'Johnny',
False,
False,
[
    ['In A Violent Nature']
],
'In A Violent Nature',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1drw2y1/respect_johnny_in_a_violent_nature/

########################################

id = get_rt_id(cur, 'Respect SCP-239, The Witch Child (SCP Foundation)', 'https://redd.it/1dsfrp8')
add_data(['SCP ?(-| )? ?239'],
'SCP-239',
False,
False,
[
    ['Witch Child']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsfrp8/respect_scp239_the_witch_child_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Togo Shigekata (Tenkaichi)', 'https://redd.it/1dsuspg')
add_data(['Togo Shigekata'],
'Togo Shigekata',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yasuke (Tenkaichi)', 'https://redd.it/1dsusr3')
add_data(['Yasuke'],
'Yasuke',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsusr3/respect_yasuke_tenkaichi/

########################################

id = get_rt_id(cur, 'Respect The Prowler (The Prowler 1981)', 'https://redd.it/1dsw0br')
add_data(['Prowler'],
'Prowler',
False,
False,
[
    ['1981']
],
'1981',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dsw0br/respect_the_prowler_the_prowler_1981/

########################################

id = get_rt_id(cur, 'Respect Fung Sheng Wu Chi (Master of the Flying Guillotine)', 'https://redd.it/1dt1x75')
add_data(['Fung Sheng Wu Chi'],
'Fung Sheng Wu Chi',
False,
True,
[
    ['Master of the Flying Guillotine']
],
'Master of the Flying Guillotine',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dt1x75/respect_fung_sheng_wu_chi_master_of_the_flying/

########################################

id = get_rt_id(cur, 'Respect the Local Heroes (Kid Cosmic)', 'https://redd.it/1dt1x96')
add_data(['Local Heroes'],
'Local Heroes',
True,
False,
[
    ['Kid Cosmic']
],
'Kid Cosmic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dt1x96/respect_the_local_heroes_kid_cosmic/

add_data(['Kid Cosmic'],
'Kid Cosmic',
False,
True,
[
    ['Stones']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dt1x96/respect_the_local_heroes_kid_cosmic/

add_data(['Fantos'],
'Fantos',
False,
False,
[
    ['Kid Cosmic']
],
'Kid Cosmic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1dt1x96/respect_the_local_heroes_kid_cosmic/

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

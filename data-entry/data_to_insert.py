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

update_respectthread(cur, 4907, 'Respect Adlet Mayer, the Strongest Man in the World (Rokka no Yuusha Anime)', 'https://redd.it/unb809')
update_respectthread(cur, 638, 'Respect Avatar Aang (Avatar: The Last Airbender)', 'https://redd.it/uo2yl5')

########################################

add_data(['Aang'],
'Aang',
False,
False,
[
    ['Shyamalan']
],
'The Last Airbender movie',
'{489}'
)
#https://www.reddit.com/r/respectthreads/comments/8fl1d9/respect_aang_the_last_airbender/

########################################

add_data(['Machete'],
'Machete',
False,
False,
[
    ['\(Machete\)'], ['Spy Kids']
],
'Machete',
'{21930}'
)
#https://www.reddit.com/r/whowouldwin/comments/uo180j/machete_spy_kidsmachete_vs_jason_voorhees_friday/i8bebc6/?context=3

########################################

id = get_rt_id(cur, 'Respect Oscar (Toon Sandwich)', 'https://redd.it/umu0dw')
add_data(['Oscar'],
'Oscar',
False,
False,
[
    ['Toon Sandwich']
],
'Toon Sandwich',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/umu0dw/respect_oscar_toon_sandwich/

########################################

id = get_rt_id(cur, 'Respect Baby 5 and Buffalo (One Piece)', 'https://redd.it/umxlgl')
add_data(['Baby 5'],
'Baby 5',
False,
False,
[
    ['One ?Piece?'], ['Buffalo'], ['Donquixote|Doflamingo']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/umxlgl/respect_baby_5_and_buffalo_one_piece/

########################################

id = get_rt_id(cur, 'Respect Destiny (takt op.Destiny)', 'https://redd.it/un8r8w')
add_data(['Destiny'],
'Destiny',
False,
False,
[
    ['Takt Op']
],
'Takt Op',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/un8r8w/respect_destiny_takt_opdestiny/

########################################

id = get_rt_id(cur, 'Respect Cuddles (American Dad!)', 'https://redd.it/un9lue')
add_data(['Cuddles'],
'Cuddles',
False,
False,
[
    ['American Dad']
],
'American Dad!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/un9lue/respect_cuddles_american_dad/

########################################

id = get_rt_id(cur, 'Respect the "Joint Fetishist" Roland Istaz/Eustass (Grappler Baki)', 'https://redd.it/unnr4h')
add_data(['Roland Istaz'],
'Roland Istaz',
False,
True,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/unnr4h/respect_the_joint_fetishist_roland_istazeustass/

########################################

id = get_rt_id(cur, 'Respect Alexia (Blood of Zeus)', 'https://redd.it/unqf4v')
add_data(['Alexia'],
'Alexia',
False,
False,
[
    ['Blood of Zeus']
],
'Blood of Zeus',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/unqf4v/respect_alexia_blood_of_zeus/

########################################

id = get_rt_id(cur, 'Respect Fiona Belli and Hewie (Haunting Ground)', 'https://redd.it/unxoo3')
add_data(['Fiona'],
'Fiona',
False,
False,
[
    ['Haunting Ground']
],
'Haunting Ground',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/unxoo3/respect_fiona_belli_and_hewie_haunting_ground/

########################################

id = get_rt_id(cur, 'Respect SCP-4450, "Sometimes Things Break" (SCP Foundation)', 'https://redd.it/uo3k0h')
add_data(['SCP ?(-| )? ?4450'],
'SCP-4450',
False,
True,
[
    ['Sometimes Things Break']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo3k0h/respect_scp4450_sometimes_things_break_scp/

########################################

id = get_rt_id(cur, 'Respect: Captain Dynamo! (Image Comics)', 'https://redd.it/uo4jk9')
add_data(['Captain Dynamo'],
'Captain Dynamo',
False,
True,
[
    ['Image|comics?']
],
'Invincible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo4jk9/respect_captain_dynamo_image_comics/

########################################

id = get_rt_id(cur, 'Respect Koushako Chouno, Papillion Mask! (Busou Renkin)', 'https://redd.it/uo7pjc')
add_data(['K(ō|o)u?shak(u|o) Ch(ō|o)u?no|Ch(ō|o)u?no K(ō|o)u?shak(u|o)'],
'Koushaku Chouno',
False,
True,
[
    ['Busou? Renkin']
],
'Buso Renkin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo7pjc/respect_koushako_chouno_papillion_mask_busou/

add_data(['Papillon'],
'Papillon',
False,
False,
[
    ['Busou? Renkin']
],
'Buso Renkin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo7pjc/respect_koushako_chouno_papillion_mask_busou/

########################################

id = get_rt_id(cur, 'Respect Captain Bravo! (Busou Renkin)', 'https://redd.it/uo85dq')
add_data(['Captain Bravo'],
'Captain Bravo',
False,
False,
[
    ['Busou? Renkin']
],
'Buso Renkin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo85dq/respect_captain_bravo_busou_renkin/

########################################

id = get_rt_id(cur, 'Respect Kazuki Muto! (Busou Renkin)', 'https://redd.it/uo871p')
add_data(['Kazuki Mut(ō|o)|Mut(ō|o) Kazuki'],
'Kazuki Muto',
False,
True,
[
    ['Busou? Renkin']
],
'Buso Renkin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo7pjc/respect_koushako_chouno_papillion_mask_busou/

add_data(['Kazuki'],
'Kazuki',
False,
False,
[
    ['Busou? Renkin']
],
'Buso Renkin',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo871p/respect_kazuki_muto_busou_renkin/

########################################

id = get_rt_id(cur, 'Respect "The King of Hades" Edward Wu (Kengan Omega)', 'https://redd.it/uo7xaz')
add_data(['Edward Wu'],
'Edward Wu',
False,
False,
[
    ['Kengan(verse)?']
],
'Kengan Asura',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/uo7xaz/respect_the_king_of_hades_edward_wu_kengan_omega/

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

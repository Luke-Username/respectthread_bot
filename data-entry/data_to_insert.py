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

add_data(['Ann?asui'],
'Annasui',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3612}'
)
#https://www.reddit.com/r/whowouldwin/comments/1hr7fsf/deadpool_and_wolverine_mcufox_vs_anasui_and/m4vg78a/?context=3


########################################

add_data(['Taylor( Anne)? Hebert'],
'Taylor Hebert',
False,
True,
[
    ['Worm']
],
'Worm',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zhane (Power Rangers In Space)', 'https://redd.it/1hp4kmc')
add_data(['Zhane'],
'Zhane',
False,
False,
[
    ['Power ?Rangers?'], ['Silver', 'Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ashley Hammond (Power Rangers)', 'https://redd.it/1hp4kla')
add_data(['Ashley Hammond'],
'Ashley Hammond',
False,
True,
[
    ['Power ?Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Ashley'],
'Ashley',
False,
False,
[
    ['Power ?Rangers?'], ['Turbo', 'Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Theo Bell! (Vampire: the Masquerade)', 'https://redd.it/1hp99yg')
add_data(['Theo Bell'],
'Theo Bell',
False,
False,
[
    ['Vampire:? the Masquerade'], ['VTM']
],
'Vampire: the Masquerade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hp99yg/respect_theo_bell_vampire_the_masquerade/

########################################

id = get_rt_id(cur, 'Respect Moby Dick (Moby-Dick)', 'https://redd.it/1hpaq5t')
add_data(['Moby( |-)Dick'],
'Moby Dick',
False,
True,
[
    ['Moby Dick ?\(Moby( |-)Dick\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Moby( |-)Dick'],
'Moby Dick',
False,
False,
[
    ['In The Heart of the Sea']
],
'In The Heart of the Sea',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Queequeg (Moby-Dick)', 'https://redd.it/1hpaqj4')
add_data(['Queequeg'],
'Queequeg',
False,
True,
[
    ['Moby( |-)Dick']
],
'Moby-Dick',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect the Kaftar (Cabela''s Dangerous Hunts 2011)", 'https://redd.it/1hpbcco')
add_data(['Kaftar'],
'Kaftar',
False,
False,
[
    ["Cabela''?s Dangerous Hunts", "2011"]
],
'Cabela''s Dangerous Hunts, 2011',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hpbcco/respect_the_kaftar_cabelas_dangerous_hunts_2011/

########################################

id = get_rt_id(cur, 'Respect Firearm! (Malibu Comics/Ultraverse)', 'https://redd.it/1hpxsf8')
add_data(['Firearm'],
'Firearm',
False,
False,
[
    ['Ultraverse']
],
'Ultraverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hpxsf8/respect_firearm_malibu_comicsultraverse/

########################################

id = get_rt_id(cur, 'Respect WolfCop! (WolfCop)', 'https://redd.it/1hpxtai')
add_data(['WolfCop'],
'WolfCop',
False,
False,
[
    ['Lou Garou']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla: Skate or Die)', 'https://redd.it/1hpy0fe')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Skate or Die']
],
'Godzilla: Skate or Die',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Master of the Forest - (Metro Exodus)', 'https://redd.it/1hq13qd')
add_data(['Master of the Forest'],
'Master of the Forest',
False,
False,
[
    ['Metro']
],
'Metro',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Thor (The Incredible Hulk Returns)', 'https://redd.it/1hq141b')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['The Incredible Hulk Returns']
],
'The Incredible Hulk Returns',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hq141b/respect_thor_the_incredible_hulk_returns/

########################################

id = get_rt_id(cur, 'Respect Doctor Strange - (Doctor Strange 1978 film)', 'https://redd.it/1hq18mj')
add_data(['(Doctor|Dr\.?|Stephen) ?Strange'],
'Doctor Strange',
False,
False,
[
    ['(Doctor|Dr\.?|Stephen) ?Strange ?\(1978\)'], ['(Doctor|Dr\.?|Stephen) ?Strange 1978 film']
],
'1978',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hq141b/respect_thor_the_incredible_hulk_returns/


########################################

id = get_rt_id(cur, 'Respect Gamera (Kaiju War Chronicles Multimedia #11)', 'https://redd.it/1hqj1mo')
add_data(['Gamera'],
'Gamera',
False,
False,
[
    ['Kaiju War Chronicles Multimedia #11']
],
'Kaiju War Chronicles Multimedia #11',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqj1mo/respect_gamera_kaiju_war_chronicles_multimedia_11/

########################################

id = get_rt_id(cur, 'Respect Aziraphale (Good Omens)', 'https://redd.it/1hqnty5')
add_data(['Azira?phale'],
'Aziraphale',
False,
False,
[
    ['Good Omens']
],
'Good Omens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqnty5/respect_aziraphale_good_omens/

########################################

id = get_rt_id(cur, 'Respect Crowley (Good Omens)', 'https://redd.it/1hqntz5')
add_data(['Crowley'],
'Crowley',
False,
False,
[
    ['Good Omens']
],
'Good Omens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqntz5/respect_crowley_good_omens/

add_data(['Crowly'],
'Crowly',
False,
False,
[
    ['Good Omens']
],
'Good Omens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqntz5/respect_crowley_good_omens/

########################################

id = get_rt_id(cur, 'Respect Adam Young (Good Omens)', 'https://redd.it/1hqntzu')
add_data(['Adam Young'],
'Adam Young',
False,
False,
[
    ['Good Omens']
],
'Good Omens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqntzu/respect_adam_young_good_omens/

########################################

id = get_rt_id(cur, 'Respect the Machine Corps (Spriggan 1998)', 'https://redd.it/1hqttjz')
add_data(['Machine Corps'],
'Machine Corps',
True,
False,
[
    ['Spriggan', '1998']
],
'Spriggan, 1998',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Wish Tokens! (The Fairly Oddparents: Nick Zone: Token Wishes)', 'https://redd.it/1hqw1lx')
add_data(['Wish Tokens?'],
'Wish Tokens',
False,
False,
[
    ['Fairly Odd ?parents']
],
'Fairly Oddparents',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Token Wishes'],
'Token Wishes',
False,
False,
[
    ['Fairly Odd ?parents']
],
'Fairly Oddparents',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Esteban The Wishing Star! (The Adventures of Puss in Boots)', 'https://redd.it/1hqw774')
add_data(['Esteban'],
'Esteban',
False,
False,
[
    ['Adventures of Puss in Boots']
],
'The Adventures of Puss in Boots',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hqw774/respect_esteban_the_wishing_star_the_adventures/

########################################

id = get_rt_id(cur, 'Respect Sanji! (One Piece [Live Action Series])', 'https://redd.it/1hqwdao')
add_data(['Sanji'],
'Sanji',
False,
False,
[
    ["(Netflix(''?s?)?|Live(-| )Action) ?One Piece"]
],
"Netflix''s One Piece",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the God-Lizard Tyrannosaurus rex (Tyrannosaurus Rex by Image Comics)', 'https://redd.it/1hqwdzg')
add_data(['Tyrannosaurus'],
'Tyrannosaurus Rex',
False,
False,
[
    ['Image Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)

########################################

id = get_rt_id(cur, 'Respect Redcoat (Image Comics, Ghost Machine)', 'https://redd.it/1hr4cne')
add_data(['Redcoat'],
'Redcoat',
False,
False,
[
    ['Image Comics'], ['Ghost Machine']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hr4cne/respect_redcoat_image_comics_ghost_machine/

########################################

id = get_rt_id(cur, 'Respect Roundhouse (DC Comics, Post-Flashpoint)', 'https://redd.it/1hr60wn')
add_data(['Roundhouse'],
'Roundhouse',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hr60wn/respect_roundhouse_dc_comics_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect the Banana Splits (The Banana Splits Movie)', 'https://redd.it/1hrtz36')
add_data(['Banana Splits'],
'Banana Splits',
False,
False,
[
    ['The Banana Splits Movie']
],
'The Banana Splits Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1hrtz36/respect_the_banana_splits_the_banana_splits_movie/

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

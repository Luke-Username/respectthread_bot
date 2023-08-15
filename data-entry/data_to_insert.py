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

update_respectthread(cur, 8144, 'Respect Nakia (Marvel Cinematic Universe)', 'https://redd.it/15qrhdk')

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Arkham Batman']
],
'Batman: Arkham',
'{17381}'
)
#https://www.reddit.com/r/whowouldwin/comments/15rokx0/the_batman_cartoon_vs_arkham_batman_video_games/jw9ksnv/?context=3

########################################

add_data(['Gojos'],
'Gojos',
False,
False,
[
    ['Jujus?t?s?u Kaisen'], ['JJK'], ['Infinity']
],
'Jujutsu Kaisen',
'{14809}'
)
#https://www.reddit.com/r/whowouldwin/comments/15qt4in/could_a_timestop_bypass_gojos_infinity_jjk/

add_data(['Gojo'],
'Gojo',
False,
False,
[
    ['Infinity']
],
'Jujutsu Kaisen',
'{14809}'
)
#https://www.reddit.com/r/whowouldwin/comments/15qt4in/could_a_timestop_bypass_gojos_infinity_jjk/

########################################

id = get_rt_id(cur, 'Respect the Model 4 War Machine (Marvel Comics, 616)', 'https://redd.it/15qcfz9')
add_data(['War Machine'],
'War Machine',
False,
False,
[
    ['Model 4']
],
'Model 4',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15qcfz9/respect_the_model_4_war_machine_marvel_comics_616/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 6: Hydro Armor Mark 1 (Marvel, Earth-616)', 'https://redd.it/15rtok8')
add_data(['Hydro Armor Mark (I|1)'],
'Hydro Armor Mark I',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kokken Sabi (Katanagatari/Kyotou Yasuri)', 'https://redd.it/15qgmbt')
add_data(['Kokken Sabi'],
'Kokken Sabi',
False,
True,
[
    ['Katanagatari'], ['Kyotou Yasuri']
],
'Katanagatari',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15qgmbt/respect_kokken_sabi_katanagatarikyotou_yasuri/

########################################

id = get_rt_id(cur, 'Respect Stellan Gios (Star Wars Canon)', 'https://redd.it/15qil1d')
add_data(['Stellan Gios'],
'Stellan Gios',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15qil1d/respect_stellan_gios_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Bilbo Baggins (The Hobbit/Lord of the Rings)', 'https://redd.it/15rxne6')
add_data(['Bilbo Baggins'],
'Bilbo Baggins',
False,
True,
[
    ['L(ord )?o(f )?t(he )?R(ings)?'], ['Hobbit']
],
'Lord of the Rings',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15rxne6/respect_bilbo_baggins_the_hobbitlord_of_the_rings/

add_data(['Bilbo'],
'Bilbo',
False,
True,
[
    ['L(ord )?o(f )?t(he )?R(ings)?'], ['Hobbit']
],
'Lord of the Rings',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15rxne6/respect_bilbo_baggins_the_hobbitlord_of_the_rings/


########################################

id = get_rt_id(cur, 'Respect Artoria Caster! (Fate/Grand Order)', 'https://redd.it/15r6iom')
add_data(['Artoria Caster'],
'Artoria Caster',
False,
True,
[
    ['Fate(verse)?'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15r6iom/respect_artoria_caster_fategrand_order/

add_data(['Artoria'],
'Artoria',
False,
False,
[
    ['Artoria \(Caster\)']
],
'Caster',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15r6iom/respect_artoria_caster_fategrand_order/

########################################

id = get_rt_id(cur, 'Respect Nale, Herald of Justice (The Stormlight Archive)', 'https://redd.it/15r4jve')
add_data(['Nale'],
'Nale',
False,
False,
[
    ['Storm ?light']
],
'The Stormlight Archive',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/15r4jve/respect_nale_herald_of_justice_the_stormlight/

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

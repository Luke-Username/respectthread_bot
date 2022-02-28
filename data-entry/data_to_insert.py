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

update_respectthread(cur, 4695, 'Respect Douji Kodama (Black Joke) [NSFW]', 'https://redd.it/t1lgkh')

########################################

id = get_rt_id(cur, 'Respect Ed (Ed Edd n Eddy)', 'https://redd.it/nv5dgu')
add_data(['Ed'],
'Ed',
False,
False,
[
    ['Edd', 'Eddy']
],
'Ed, Edd n Eddy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/WhoWouldWinWorkshop/comments/nv5dgu/respect_ed_ed_edd_n_eddy/
#https://www.reddit.com/r/whowouldwin/comments/t233as/deadpool_vs_ed_the_dumb_one_from_ed_edd_and_eddy/hyjh0jl/?context=3

########################################

id = get_rt_id(cur, 'Respect Fuuma Kotarou! (Fate)', 'https://redd.it/t1crao')
add_data(['Kotar(ō|o)u?'],
'Kotaro',
False,
False,
[
    ['Fate(staynight|grandorder)?']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1crao/respect_fuuma_kotarou_fate/

########################################

id = get_rt_id(cur, 'Respect Christopher Columbus! (Fate)', 'https://redd.it/t1dcd8')
add_data(['Christopher Columbus'],
'Christopher Columbus',
False,
False,
[
    ['Christopher Columbus ?\(Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1dcd8/respect_christopher_columbus_fate/

########################################

id = get_rt_id(cur, 'Respect Katou Danzo! (Fate)', 'https://redd.it/t1g09i')
add_data(['Kat(ō|o)u? Danz(ō|o)'],
'Katō Danzō',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1g09i/respect_katou_danzo_fate/

########################################

id = get_rt_id(cur, 'Respect Mandricardo! (Fate)', 'https://redd.it/t1nmv8')
add_data(['Mandricardo'],
'Mandricardo',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1nmv8/respect_mandricardo_fate/

########################################

id = get_rt_id(cur, 'Respect Osakabehime! (Fate)', 'https://redd.it/t1o5s5')
add_data(['Osakabehime'],
'Osakabehime',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1o5s5/respect_osakabehime_fate/

########################################

id = get_rt_id(cur, 'Respect Sei Shounagon! (Fate)', 'https://redd.it/t1p9mf')
add_data(['Sei Sh(ō|o)u?nagon'],
'Sei Shōnagon',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1p9mf/respect_sei_shounagon_fate/

########################################

id = get_rt_id(cur, 'Respect Circe! (Fate)', 'https://redd.it/t23zq2')
add_data(['Circe'],
'Circe',
False,
False,
[
    ['Circe ?\(Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t23zq2/respect_circe_fate/

########################################

id = get_rt_id(cur, 'Respect Wolfgang Amadeus Mozart! (Fate)', 'https://redd.it/t243kk')
add_data(['Mozart'],
'Mozart',
False,
False,
[
    ['Mozart ?\(Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t243kk/respect_wolfgang_amadeus_mozart_fate/

########################################

id = get_rt_id(cur, 'Respect Houzouin Inshun! (Fate)', 'https://redd.it/t25gz0')
add_data(['H(ō|o)u?z(ō|o)u?in Inshun'],
'Hōzōin Inshun',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t25gz0/respect_houzouin_inshun_fate/

########################################

id = get_rt_id(cur, 'Respect Shirou Emiya! (Miyuverse)', 'https://redd.it/t2xvnb')
add_data(['Shirou'],
'Emiya Shirou',
False,
False,
[
    ['Miyu(-| )?verse']
],
'Miyuverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t2xvnb/respect_shirou_emiya_miyuverse/

########################################

id = get_rt_id(cur, 'Respect The One Below All (Marvel)', 'https://redd.it/t1w5mn')
add_data(['One Below All'],
'One Below All',
False,
True,
[
    ['Marvel'], ['Hulk']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1w5mn/respect_the_one_below_all_marvel/

add_data(['TOBA'],
'TOBA',
False,
False,
[
    ['Hulk']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1w5mn/respect_the_one_below_all_marvel/

########################################

id = get_rt_id(cur, 'Respect Marnie! (Pokemon Anime)', 'https://redd.it/t1wn1p')
add_data(['Marnie'],
'Marnie',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t1wn1p/respect_marnie_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Black Adam (DC, Earth S)', 'https://redd.it/t22t6x')
add_data(['Black Adam'],
'Black Adam',
False,
False,
[
    ['Earth(-| )S']
],
'Earth-S',
'{' + '{}'.format(id) + '}'
)
#https://old.reddit.com/r/respectthreads/comments/t22t6x/respect_black_adam_dc_earth_s/

########################################

id = get_rt_id(cur, "Respect Grigori Rasputin (The King''s Man)", 'https://redd.it/t2f5pz')
add_data(['Rasputin'],
'Rasputin',
False,
False,
[
    ["The King''?s Man"]
],
"The King''s Man",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t2f5pz/respect_grigori_rasputin_the_kings_man/

########################################

id = get_rt_id(cur, 'Respect The Flying Dutchman! (Spongebob Squarepants)', 'https://redd.it/t2sreq')
add_data(['Flying Dutchman'],
'Flying Dutchman',
False,
False,
[
    ['SpongeBob']
],
'SpongeBob',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t2sreq/respect_the_flying_dutchman_spongebob_squarepants/

########################################

id = get_rt_id(cur, 'Respect Tangath Toborn (Chaotic)', 'https://redd.it/t32m5w')
add_data(['Tangath Toborn'],
'Tangath Toborn',
False,
True,
[
    ['Chaotic']
],
'Chaotic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t32m5w/respect_tangath_toborn_chaotic/

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

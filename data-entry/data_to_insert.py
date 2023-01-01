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

update_respectthread(cur, 6467, 'Respect Ajani Goldmane! (Magic: The Gathering)', 'https://redd.it/zzf2wq')
update_respectthread(cur, 6422, 'Respect The Guy (Distrurbed)', 'https://redd.it/1005evf')
update_respectthread(cur, 525, 'Respect Captain Jack Sparrow (Pirates of the Caribbean)', 'https://redd.it/100hd9l')

########################################

add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['MAX!Punisher']
],
'Punisher MAX',
'{2226}'
)
#https://www.reddit.com/r/whowouldwin/comments/zzzxj9/punisher_is_transferred_into_silent_hill_how_well/j2el5dr/?context=3

########################################

add_data(['Black ?beard'],
'Blackbeard',
False,
False,
[
    ['Yami Yami no Mi'], ['Gura Gura no Mi']
],
'One Piece',
'{4039}'
)
#https://www.reddit.com/r/whowouldwin/comments/zzzxj9/punisher_is_transferred_into_silent_hill_how_well/j2el5dr/?context=3

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 57: the Fin Fang Foombuster (Marvel, Earth-616)', 'https://redd.it/zzgxm6')
add_data(['Fin Fang Foombuster'],
'Fin Fang Foombuster',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zzgxm6/respect_iron_man_model_57_the_fin_fang_foombuster/

########################################

id = get_rt_id(cur, 'Respect the War Doctor (Doctor Who)', 'https://redd.it/zz4tvf')
add_data(['War Doctor'],
'War Doctor',
False,
False,
[
    ['Sonic Screwdriver'], ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zz4tvf/respect_the_war_doctor_doctor_who/

########################################

id = get_rt_id(cur, 'Respect the Sixth Doctor (Doctor Who)', 'https://redd.it/zzxsti')
add_data(['(Six|6)th Doctor'],
'The Sixth Doctor',
False,
True,
[
    ['Sonic Screwdriver'], ['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
'Doctor Who',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zzxsti/respect_the_sixth_doctor_doctor_who/

########################################

id = get_rt_id(cur, 'Respect Jock! (Nerd and Jock)', 'https://redd.it/zzy5on')
add_data(['Jock'],
'Jock',
False,
False,
[
    ['Jock ?\(Nerd and Jock']
],
'Nerd and Jock',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zzy5on/respect_jock_nerd_and_jock/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 63: the Godbuster (Marvel, Earth-616)', 'https://redd.it/100106s')
add_data(['Tony Stark'],
'Iron Man',
False,
False,
[
    ['God(-| )?buster']
],
'Godbuster',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100106s/respect_iron_man_model_63_the_godbuster_marvel/

########################################

id = get_rt_id(cur, 'Respect Thor (Marvel, Earth-2301 [Mangaverse])', 'https://redd.it/1005pkm')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['Mangaverse'], ['2301']
],
'2301',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1005pkm/respect_thor_marvel_earth2301_mangaverse/

########################################

id = get_rt_id(cur, "Respect Chuck Norris''s World of Warcraft character (World of Warcraft advertisement)", 'https://redd.it/100779o')
add_data(['Chuck Norris'],
'Chuck Norris',
False,
False,
[
    ['World of Warcraft']
],
'World of Warcraft',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100779o/respect_chuck_norriss_world_of_warcraft_character/

########################################

id = get_rt_id(cur, 'Respect Sir Lancelot the Brave (Monty Python and the Holy Grail/Spamalot)', 'https://redd.it/100ca50')
add_data(['Lancelot'],
'Lancelot',
False,
False,
[
    ['Monty Python'], ['Spamalot']
],
'Monty Python and the Holy Grail',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100ca50/respect_sir_lancelot_the_brave_monty_python_and/

########################################

id = get_rt_id(cur, 'Respect Bellona! (SMITE)', 'https://redd.it/100ccd6')
add_data(['Bellona'],
'Bellona',
False,
False,
[
    ['SMITE']
],
'SMITE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100ccd6/respect_bellona_smite/

########################################

id = get_rt_id(cur, 'Respect Lego Captain Jack Sparrow (Lego Pirates of the Caribbean)', 'https://redd.it/100hdsh')
add_data(['Lego( Captain)? Jack Sparrow'],
'Lego Captain Jack Sparrow',
False,
True,
[
    ['Lego Pirates of the Caribbean']
],
'Lego Pirates of the Caribbean',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100hdsh/respect_lego_captain_jack_sparrow_lego_pirates_of/

########################################

id = get_rt_id(cur, 'Respect Dr. Who (Dr. Who and the Daleks)', 'https://redd.it/100lg6g')
add_data(['Dr\.? Who'],
'Dr. Who',
False,
False,
[
    ['Dr\.? Who and the Daleks']
],
'Dr. Who and the Daleks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100lg6g/respect_dr_who_dr_who_and_the_daleks/

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

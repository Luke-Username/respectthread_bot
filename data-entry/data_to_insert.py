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

id = get_rt_id(cur, "Respect: Mizuha''s nokker (To your eternity)", 'https://redd.it/121r2lc')
add_data(['Mizuha'],
'Mizuha',
False,
False,
[
    ['To your eternity']
],
'To your eternity',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/121r2lc/respect_mizuhas_nokker_to_your_eternity/

########################################

id = get_rt_id(cur, 'Respect Mizuki Okiura! (AI: the Somnium Files - Nirvana Initiative)', 'https://redd.it/1229cf7')
add_data(['Mizuki Okiura'],
'Mizuki Okiura',
False,
True,
[
    ['Somnium Files']
],
'AI: the Somnium Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1229cf7/respect_mizuki_okiura_ai_the_somnium_files/

########################################

id = get_rt_id(cur, 'Respect Pikachu! (PokéPark)', 'https://redd.it/121wb3r')
add_data(['Pikachus?'],
'Pikachu',
False,
False,
[
    ['Pok(é|e)Park']
],
'PokéPark',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/121wb3r/respect_pikachu_pok%C3%A9park/

########################################

id = get_rt_id(cur, 'Respect: Ferrus Manus (Warhammer 40k)', 'https://redd.it/122b4to')
add_data(['Ferrus Manus'],
'Ferrus Manus',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122b4to/respect_ferrus_manus_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Sky Striker Ace - Raye (Yu-Gi-Oh OCG Stories)', 'https://redd.it/122b4ue')
add_data(['Sky Striker Ace( -)? Raye'],
'Sky Striker Ace - Raye',
False,
True,
[
    ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122b4ue/respect_sky_striker_ace_raye_yugioh_ocg_stories/

########################################

id = get_rt_id(cur, 'Respect Shinobu (One Piece)', 'https://redd.it/122ceo9')
add_data(['Shinobu'],
'Shinobu',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122ceo9/respect_shinobu_one_piece/

########################################

id = get_rt_id(cur, "Respect Anita (Night Warriors: Darkstalkers'' Revenge) (the anime OVA)", 'https://redd.it/122qh00')
add_data(['Anita'],
'Anita',
False,
False,
[
    ['Night Warriors', 'Darkstalkers?']
],
"Night Warriors: Darkstalkers'' Revenge",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122qh00/respect_anita_night_warriors_darkstalkers_revenge/


########################################

id = get_rt_id(cur, "Respect Ruby! (Ruby Quest)", 'https://redd.it/122wsre')
add_data(['Ruby'],
'Ruby',
False,
False,
[
    ['Ruby ?\(Ruby Quest']
],
'Ruby Quest',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122wsre/respect_ruby_ruby_quest/

########################################

id = get_rt_id(cur, 'Respect Tom! (Ruby Quest)', 'https://redd.it/1231cqe')
add_data(['Tom'],
'Tom',
False,
False,
[
    ['Ruby Quest']
],
'Ruby Quest',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1231cqe/respect_tom_ruby_quest/

########################################

id = get_rt_id(cur, 'Respect Prophet Muhammad (Qasida Al-Burda)', 'https://redd.it/122yluj')
add_data(['Muhammad'],
'Muhammad',
False,
False,
[
    ['Al-Burda']
],
'Qasīdat Al-Burda',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/122yluj/respect_prophet_muhammad_qasida_alburda/

########################################

id = get_rt_id(cur, 'Respect Higgs Monaghan! (Death Stranding)', 'https://redd.it/12313w8')
add_data(['Higgs Monaghan'],
'Higgs Monaghan',
False,
True,
[
    ['Death Stranding']
],
'Death Stranding',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12313w8/respect_higgs_monaghan_death_stranding/

########################################

id = get_rt_id(cur, 'Respect Zeon and Dufaux (Gash Bell)', 'https://redd.it/1234kka')
add_data(['Zeon'],
'Zeon',
False,
False,
[
    ['(Zatch|Gash) Bell'], ['Zeon Bell'], ['Duf(ort|aux)']
],
'Zatch Bell!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1234kka/respect_zeon_and_dufaux_gash_bell/

########################################

id = get_rt_id(cur, "Respect David Garcia (Telltale''s The Walking Dead Game)", 'https://redd.it/1236vp4')
add_data(['David Garcia'],
'David Garcia',
False,
False,
[
    ['Wa(lk|kl)ing Dead'], ['TWD']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1236vp4/respect_david_garcia_telltales_the_walking_dead/

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

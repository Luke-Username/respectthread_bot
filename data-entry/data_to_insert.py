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

update_respectthread(cur, 13082, 'Respect Beatrice (Re:Zero, Anime)', 'https://redd.it/w2spbr')

########################################

add_data(['Thor'],
'Thor',
False,
False,
[
    ['Nor(se|dic) Mythology']
],
'Norse Mythology',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/w0rj7c/the_norse_gods_norse_mythology_vs_the_alternates/igg3mqq/?context=3

########################################

add_data(['Carrie'],
'Carrie',
False,
False,
[
    ['Chloe Grace Moretz']
],
'2013',
'{396}'
)
#https://www.reddit.com/r/whowouldwin/comments/w1no9e/jane_hopper_vs_chloe_grace_moretz_version_of/

########################################

id = get_rt_id(cur, 'Respect Patrick Bateman (American Psycho)', 'https://redd.it/ulbvnq')
add_data(['Patrick Bateman'],
'Patrick Bateman',
False,
True,
[
    ['American Psycho']
],
'American Psycho',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/CasualRespectThreads/comments/ulbvnq/respect_patrick_bateman_american_psycho/

########################################

id = get_rt_id(cur, 'Respect Twitch! (Five Kingdoms)', 'https://redd.it/vzzrr3')
add_data(['Twitch'],
'Twitch',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vzzrr3/respect_twitch_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Carnag! (Five Kingdoms)', 'https://redd.it/w1yk77')
add_data(['Carnag'],
'Carnag',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jace! (Five Kingdoms)', 'https://redd.it/w2wtln')
add_data(['Jace'],
'Jace',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2wtln/respect_jace_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Liam! (Five Kingdoms)', 'https://redd.it/w2wujf')
add_data(['Liam'],
'Liam',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2wujf/respect_liam_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Raizo (One Piece)', 'https://redd.it/w0a9to')
add_data(['Raizo'],
'Raizo',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w0a9to/respect_raizo_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Alphas (The Dresden Files)', 'https://redd.it/w0r5uy')
add_data(['The Alphas'],
'The Alphas',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w0r5uy/respect_the_alphas_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Lara Raith, Queen of the White Court (The Dresden Files)', 'https://redd.it/w1lig6')
add_data(['Lara Raith'],
'Lara Raith',
False,
True,
[
    ['Dresden( Files|verse)']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1lig6/respect_lara_raith_queen_of_the_white_court_the/

########################################

id = get_rt_id(cur, 'Respect Mouse (The Dresden Files)', 'https://redd.it/w399eo')
add_data(['Mouse'],
'Mouse',
False,
False,
[
    ['Mouse ?\((The )?Dresden( Files|verse)'], ['Dresden Files Mouse']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w399eo/respect_mouse_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Little Mac (Brothers in Arms)', 'https://redd.it/w1gh2z')
add_data(['Little Mac'],
'Little Mac',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1gh2z/respect_little_mac_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Robin (Brothers in Arms)', 'https://redd.it/w1gk76')
add_data(['Robin'],
'Robin',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1gk76/respect_robin_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Leaf (Brothers in Arms)', 'https://redd.it/w20ktp')
add_data(['Leaf'],
'Leaf',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w20ktp/respect_leaf_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Sheik (Brothers in Arms)', 'https://redd.it/w2122q')
add_data(['Sheik'],
'Sheik',
False,
False,
[
    ['Brothers in Arms']
],
'Brothers in Arms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2122q/respect_sheik_brothers_in_arms/

########################################

id = get_rt_id(cur, 'Respect Team Vashyron (Resonance of Fate)', 'https://redd.it/w1k4eo')
add_data(['Vashyron'],
'Vashyron',
False,
True,
[
    ['Resonance of Fate']
],
'Resonance of Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1k4eo/respect_team_vashyron_resonance_of_fate/

########################################

id = get_rt_id(cur, 'Respect Fohhder (FIGHTERS)', 'https://redd.it/w1pg1s')
add_data(['Fohhder'],
'Fohhder',
False,
True,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1pg1s/respect_fohhder_fighters/

########################################

id = get_rt_id(cur, 'Respect Sani Kuh (FIGHTERS)', 'https://redd.it/w1q6ts')
add_data(['Sani Kuh'],
'Sani Kuh',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1q6ts/respect_sani_kuh_fighters/

########################################

id = get_rt_id(cur, 'Respect Apollo Don (FIGHTERS)', 'https://redd.it/w217xs')
add_data(['Apollo Don'],
'Apollo Don',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w217xs/respect_apollo_don_fighters/

########################################

id = get_rt_id(cur, 'Respect Lawliet Kuh (FIGHTERS)', 'https://redd.it/w2hrmk')
add_data(['Lawliet Kuh'],
'Lawliet Kuh',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2hrmk/respect_lawliet_kuh_fighters/

########################################

id = get_rt_id(cur, 'Respect President Jackuss Kingski (FIGHTERS)', 'https://redd.it/w383q0')
add_data(['Jackuss'],
'Jackuss',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2hrmk/respect_lawliet_kuh_fighters/

########################################

id = get_rt_id(cur, 'Respect the Witches of Sin (Re:Zero, Anime)', 'https://redd.it/w1z2zu')
add_data(['Witches of Sin'],
'Witches of Sin',
True,
False,
[
    ['Re:? ?Zero']
],
'Re:Zero',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w1z2zu/respect_the_witches_of_sin_rezero_anime/

########################################

id = get_rt_id(cur, 'Respect Gorr the Golden Gorilla (Marvel Comics)', 'https://redd.it/w2gcp9')
add_data(['Gorr the Golden Gorilla'],
'Gorr the Golden Gorilla',
False,
True,
[
    ['Marvel']
],
'Marvel',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2gcp9/respect_gorr_the_golden_gorilla_marvel_comics/

########################################

id = get_rt_id(cur, 'Respect Vaccine Man! (One-Punch Man)', 'https://redd.it/w2hxrr')
add_data(['Vaccine Man'],
'Vaccine Man',
False,
True,
[
    ['One(-| )Punch Man'], ['OPM']
],
'One Punch Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2hxrr/respect_vaccine_man_onepunch_man/

########################################

id = get_rt_id(cur, "Respect Light Turner (Netflix''s Death Note, 2017 movie)", 'https://redd.it/w2twzs')
add_data(['Light Turner'],
'Light Turner',
False,
True,
[
    ['Death Note']
],
"Netflix''s Death Note",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2twzs/respect_light_turner_netflixs_death_note_2017/

########################################

id = get_rt_id(cur, "Respect L (Netflix''s Death Note, 2017 movie)", 'https://redd.it/w2txrq')
add_data(['L'],
'L',
False,
False,
[
    ['Netflix.*Death Note']
],
"Netflix''s Death Note",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w2txrq/respect_l_netflixs_death_note_2017_movie/

########################################

id = get_rt_id(cur, 'Respect Blackfire (Teen Titans)', 'https://redd.it/w30bwh')
add_data(['Blackfire'],
'Blackfire',
False,
False,
[
    ['\(Teen Titans\)']
],
"Teen Titans",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w30bwh/respect_blackfire_teen_titans/

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

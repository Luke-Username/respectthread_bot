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

add_data(['Chucky'],
'Chucky',
False,
False,
[
    ['Monokuma', 'Chucky vs|vs\.? Chucky']
],
"Child''s Play",
'{13094}'
)
#https://www.reddit.com/r/whowouldwin/comments/1g0n9uu/monokuma_vs_chucky/lr9y4ux/?context=3

########################################

add_data(['Samara'],
'Samara',
False,
False,
[
    ['The Ring']
],
"The Ring",
'{25158}'
)
#https://www.reddit.com/r/whowouldwin/comments/1g0n19v/kevin_mcallister_vs_samara_the_ring/

########################################

id = get_rt_id(cur, 'Respect the Great God Cay, the Brontosaurus (Beyond the Great South Wall)', 'https://redd.it/1fzjlke')
add_data(['Brontosaurus'],
'Brontosaurus',
False,
False,
[
    ['Beyond the Great South Wall']
],
'Beyond the Great South Wall',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzjlke/respect_the_great_god_cay_the_brontosaurus_beyond/

add_data(['Cay'],
'Cay',
False,
False,
[
    ['Beyond the Great South Wall']
],
'Beyond the Great South Wall',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzjlke/respect_the_great_god_cay_the_brontosaurus_beyond/

########################################

id = get_rt_id(cur, 'Respect The Butcher (Emesis Blue)', 'https://redd.it/1fzqnif')
add_data(['Butcher'],
'Butcher',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzqnif/respect_the_butcher_emesis_blue/

########################################

id = get_rt_id(cur, 'Respect Stalingrad (Emesis Blue)', 'https://redd.it/1fzrwk1')
add_data(['Stalingrad'],
'Stalingrad',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzrwk1/respect_stalingrad_emesis_blue/

########################################

id = get_rt_id(cur, 'Respect The Detective (Emesis Blue)', 'https://redd.it/1fzrzvd')
add_data(['Detective'],
'Detective',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzrzvd/respect_the_detective_emesis_blue/

add_data(['Jacques Murnau'],
'Jacques Murnau',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzrzvd/respect_the_detective_emesis_blue/

########################################

id = get_rt_id(cur, 'Respect The Soldier (Emesis Blue)', 'https://redd.it/1fzsdbq')
add_data(['Soldier'],
'Soldier',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzsdbq/respect_the_soldier_emesis_blue/

########################################

id = get_rt_id(cur, 'Respect Dr. Fritz Ludwig (Emesis Blue)', 'https://redd.it/1fzsdwd')
add_data(['Dr\.? Fritz Ludwig'],
'Dr. Fritz Ludwig',
False,
False,
[
    ['Emesis Blue']
],
'Emesis Blue',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzsdwd/respect_dr_fritz_ludwig_emesis_blue/

########################################

id = get_rt_id(cur, 'Respect The Headless Horseman (The Legend of Sleepy Hollow)', 'https://redd.it/1fzr94o')
add_data(['Headless Horseman'],
'Headless Horseman',
False,
False,
[
    ['Legend of Sleepy Hollow']
],
'The Legend of Sleepy Hollow',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzr94o/respect_the_headless_horseman_the_legend_of/

########################################

id = get_rt_id(cur, 'Respect Ruby Knowby (Ash vs Evil Dead)', 'https://redd.it/1fzr9r7')
add_data(['Ruby Knowby'],
'Ruby Knowby',
False,
True,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzr9r7/respect_ruby_knowby_ash_vs_evil_dead/

add_data(['Ruby Knowby'],
'Ruby Knowby',
False,
False,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzr9r7/respect_ruby_knowby_ash_vs_evil_dead/

########################################

id = get_rt_id(cur, 'Respect Ash Williams (Evil Dead: The Musical)', 'https://redd.it/1g0oqr4')
add_data(['Ash Williams'],
'Ash Williams',
False,
False,
[
    ['Evil Dead:? The Musical']
],
'Evil Dead: The Musical',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g0oqr4/respect_ash_williams_evil_dead_the_musical/

########################################

id = get_rt_id(cur, 'Respect the Necronomicon (Evil Dead: The Musical)', 'https://redd.it/1g0oqaa')
add_data(['Necronomicon'],
'Necronomicon',
False,
False,
[
    ['Evil Dead:? The Musical']
],
'Evil Dead: The Musical',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g0oqaa/respect_the_necronomicon_evil_dead_the_musical/

########################################

id = get_rt_id(cur, 'Respect the Unnamed Demon that Possessed Marcus (Ash vs Evil Dead)', 'https://redd.it/1fzsieu')
add_data(['Demon that Possessed Marcus'],
'Demon that Possessed Marcus',
False,
False,
[
    ['Ash vs\.? Evil Dead']
],
'Ash vs Evil Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzsieu/respect_the_unnamed_demon_that_possessed_marcus/

########################################

id = get_rt_id(cur, 'Respect Senro Grumer! (Bakauge Sentai BoonBoomger)', 'https://redd.it/1fzrihc')
add_data(['Senro Grumer'],
'Senro Grumer',
False,
False,
[
    ['Bakauge Sentai BoonBoomger']
],
'Bakauge Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzrihc/respect_senro_grumer_bakauge_sentai_boonboomger/

########################################

id = get_rt_id(cur, "Respect James'' Weezing (Pokemon Anime)", 'https://redd.it/1g0jhkp')
add_data(['Weezing'],
'Weezing',
False,
False,
[
    ['James']
],
'James',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g0jhkp/respect_james_weezing_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Han & his Den of Thieves (Kung Fu Panda)', 'https://redd.it/1fzy8wa')
add_data(['Han'],
'Han',
False,
False,
[
    ['Han.*Kung Fu Panda'], ['Han the Pangolin']
],
'Kung Fu Panda',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1fzy8wa/respect_han_his_den_of_thieves_kung_fu_panda/

########################################

id = get_rt_id(cur, "Respect Kino (Kino''s Journey —the Beautiful World—, 2003)", 'https://redd.it/1fzzwg0')
add_data(['Kino'],
'Kino',
False,
False,
[
    ["Kino''s Journey"]
],
"Kino''s Journey",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Partridge Creek Monster (The Monster of "Partridge Creek")', 'https://redd.it/1g0h5x0')
add_data(['Monster'],
'Monster',
False,
False,
[
    ['Partridge Creek']
],
'The Monster of "Partridge Creek"',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g0h5x0/respect_the_partridge_creek_monster_the_monster/

########################################

id = get_rt_id(cur, 'Respect Reverend Lester Lowe, The Werewolf (Cycle of the Werewolf)', 'https://redd.it/1g0hlio')
add_data(['Lester Lowe'],
'Lester Lowe',
False,
False,
[
    ['Cycle of the Werewolf']
],
'Cycle of the Werewolf',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1g0hlio/respect_reverend_lester_lowe_the_werewolf_cycle/

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

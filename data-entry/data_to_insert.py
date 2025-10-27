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

update_respectthread(cur, 1343, 'Respect Qrow Branwen (RWBY)', 'https://www.reddit.com/r/respectthreads/comments/1ofw5zm/respect_qrow_branwen_rwby/')

########################################

add_data(['Predator'],
'Predator',
False,
False,
[
    ['Predator.*Predator series']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/1oh3cam/who_would_win_a_space_marine_from_warhammer_40k/


########################################

add_data(['Kenshin'],
'Kenshin',
False,
False,
[
    ['Kenshin vs', 'Rurouni Kenshin']
],
'Rurouni Kenshin',
'{4462}'
)
#https://www.reddit.com/r/whowouldwin/comments/1ofd0j7/the_rurouni_kenshin_verse_vs_the_demon_slayer/nl84hrk/?context=3

########################################

id = get_rt_id(cur, 'Respect Linnya Wazzo/Phantom Girl (DC Comics, Post Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1oenjs5/respect_linnya_wazzophantom_girl_dc_comics_post/')
add_data(['Linnya Wazzo'],
'Linnya Wazzo',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Linnya Wazzo'],
'Linnya Wazzo',
False,
True,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Malice, Mistress of Hate (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1oexstu/respect_malice_mistress_of_hate_marvel_comics_616/')
add_data(['(Susan|Sue) Storm'],
'Susan Storm',
False,
False,
[
    ['Malice']
],
'Malice',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yuri Watanabe, Wraith! (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1ofltl6/respect_yuri_watanabe_wraith_marvel_616/')
add_data(['Yuri(ko)? Watanabe'],
'Yuri Watanabe',
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

id = get_rt_id(cur, '[NSFW] Respect Yi Xi! (Butcher Vanity)', 'https://www.reddit.com/r/respectthreads/comments/1oewce2/nsfw_respect_yi_xi_butcher_vanity/')
add_data(['Yi Xi'],
'Yi Xi',
False,
False,
[
    ['Butcher Vanity']
],
'Butcher Vanity',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Thanatos (Pantheum)', 'https://www.reddit.com/r/respectthreads/comments/1of0wrt/respect_thanatos_pantheum/')
add_data(['Thanatos'],
'Thanatos',
False,
False,
[
    ['Thanatos ?\(Pantheum\)']
],
'Pantheum',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Stuff (The Stuff)', 'https://www.reddit.com/r/respectthreads/comments/1ofqz1g/respect_the_stuff_the_stuff/')
add_data(['The Stuff'],
'The Stuff',
False,
False,
[
    ['The Stuff ?\(The Stuff\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Candice (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1ofs1oa/respect_candice_pokemon_anime/')
add_data(['Candice'],
'Candice',
False,
False,
[
    ['Candice.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Burgh (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1ofw70k/respect_burgh_pokemon_anime/')
add_data(['Burgh'],
'Burgh',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Roxie (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1og5cbg/respect_roxie_pokemon_anime/')
add_data(['Roxie'],
'Roxie',
False,
False,
[
    ['Roxie.*Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect This Wild Magnezone (Pokemon Anime - DP158)', 'https://www.reddit.com/r/respectthreads/comments/1ogm89b/respect_this_wild_magnezone_pokemon_anime_dp158/')
add_data(['Wild Magnezone'],
'Wild Magnezone',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect This Wild Metagross (Pokemon Anime - DP158)', 'https://www.reddit.com/r/respectthreads/comments/1ogm8a2/respect_this_wild_metagross_pokemon_anime_dp158/')
add_data(['Wild Metagross'],
'Wild Metagross',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Frank Drebin Jr. (The Naked Gun)', 'https://www.reddit.com/r/respectthreads/comments/1og3dcd/respect_frank_drebin_jr_the_naked_gun/')
add_data(['Frank Drebin Jr'],
'Frank Drebin Jr.',
False,
True,
[
    ['Naked Gun']
],
'The Naked Gun',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Death (Dreamwalker)', 'https://www.reddit.com/r/respectthreads/comments/1ogb16m/respect_death_dreamwalker/')
add_data(['Death'],
'Death',
False,
False,
[
    ['Dreamwalker']
],
'Dreamwalker',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Dakwara (Isles of the Emberdark)', 'https://www.reddit.com/r/respectthreads/comments/1oguf79/respect_the_dakwara_isles_of_the_emberdark/')
add_data(['Dakwara'],
'Dakwara',
False,
False,
[
    ['Isles of the Emberdark']
],
'Isles of the Emberdark',
'{' + '{}'.format(id) + '}'
)
#

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

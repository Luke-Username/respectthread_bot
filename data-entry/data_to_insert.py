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


id = get_rt_id(cur, 'Respect Purugly (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1pidn3i/respect_purugly_pokemon_anime/')
add_data(['Purugly'],
'Purugly',
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

id = get_rt_id(cur, 'Respect Jinguji Tsukasa (Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout)', 'https://www.reddit.com/r/respectthreads/comments/1piqj23/respect_jinguji_tsukasa_life_with_an_ordinary_guy/')
add_data(['Jinguji Tsukasa|Tsukasa Jinguji'],
'Tsukasa Jinguji',
False,
True,
[
    ['Ordinary Guy|Total Fantasy Knockout']
],
'Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hinata Tachibana (Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout)', 'https://www.reddit.com/r/respectthreads/comments/1pjb73j/respect_hinata_tachibana_life_with_an_ordinary/')
add_data(['Hinata Tachibana'],
'Hinata Tachibana',
False,
False,
[
    ['Ordinary Guy|Total Fantasy Knockout']
],
'Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Maypom (Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout)', 'https://www.reddit.com/r/respectthreads/comments/1pjhbhj/respect_maypom_life_with_an_ordinary_guy_who/')
add_data(['Maypom'],
'Maypom',
False,
False,
[
    ['Ordinary Guy|Total Fantasy Knockout']
],
'Life With an Ordinary Guy Who Reincarnated into a Total Fantasy Knockout',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Miko Kubota (Glitch Techs)', 'https://www.reddit.com/r/respectthreads/comments/1pium9q/respect_miko_kubota_glitch_techs/')
add_data(['Miko Kubota'],
'Miko Kubota',
False,
False,
[
    ['Glitch Techs?']
],
'Glitch Techs',
'{' + '{}'.format(id) + '}'
)
#

add_data(['ME_K\.?O\.?'],
'ME_K.O.',
False,
False,
[
    ['Glitch Techs?']
],
'Glitch Techs',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Dick Tracy (Chester Gould''s Dick Tracy)", 'https://www.reddit.com/r/respectthreads/comments/1pj1qxd/respect_dick_tracy_chester_goulds_dick_tracy/')
add_data(['Dick Tracy'],
'Dick Tracy',
False,
True,
[
    ['Chester Goulds?']
],
'Chester Gould',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect the Space Coupe (Chester Gould''s Dick Tracy)", 'https://www.reddit.com/r/respectthreads/comments/1pj1r34/respect_the_space_coupe_chester_goulds_dick_tracy/')
add_data(['Space Coupe'],
'Space Coupe',
False,
False,
[
    ['Dick Tracy']
],
'Dick Tracy',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Dick Tracy (Dick Tracy)', 'https://www.reddit.com/r/respectthreads/comments/1pj1r0m/respect_dick_tracy_dick_tracy/')
add_data(['Dick Tracy'],
'Dick Tracy',
False,
False,
[
    ['1990'], ['(film|movie)s?']
],
'1990',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Frank Castle, The Punisher (THE PUNISHER: DIRTY LAUNDRY)', 'https://www.reddit.com/r/respectthreads/comments/1pjaue7/respect_frank_castle_the_punisher_the_punisher/')
add_data(['Punisher'],
'Punisher',
False,
False,
[
    ['The Punisher:? Dirty Laundry']
],
'The Punisher: Dirty Laundry',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ondai (Oban Star Racers)', 'https://www.reddit.com/r/respectthreads/comments/1pjk4g8/respect_ondai_oban_star_racers/')
add_data(['Ondai'],
'Ondai',
False,
False,
[
    ['Oban Star Racers']
],
'Oban Star Racers',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Human Bill (Fortnite)', 'https://www.reddit.com/r/respectthreads/comments/1pjlz5p/respect_human_bill_fortnite/')
add_data(['Human Bill'],
'Human Bill',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rafael Santoro! (Joe Ledger)', 'https://www.reddit.com/r/respectthreads/comments/1pjrewh/respect_rafael_santoro_joe_ledger/')
add_data(['Rafael Santoro'],
'Rafael Santoro',
False,
False,
[
    ['Joe Ledger']
],
'Joe Ledger',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Avatar (Street Fighter 6)', 'https://www.reddit.com/r/respectthreads/comments/1pi7664/respect_the_avatar_street_fighter_6/')
add_data(['Avatar'],
'Avatar',
False,
False,
[
    ['Street Fighter 6']
],
'Street Fighter 6',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Nicolaus Maduro (Súper Bigote TV Show)', 'https://www.reddit.com/r/respectthreads/comments/1pjxb8j/respect_nicolaus_maduro_s%C3%BAper_bigote_tv_show/')
add_data(['Nicolaus Maduro'],
'Nicolaus Maduro',
False,
False,
[
    ['S(ú|u)per Bigote']
],
'Súper Bigote',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Francis York Morgan (Deadly Premonition)', 'https://www.reddit.com/r/respectthreads/comments/1pjvzzm/respect_francis_york_morgan_deadly_premonition/')
add_data(['Francis York Morgan'],
'Francis York Morgan',
False,
True,
[
    ['Deadly Premonition']
],
'Deadly Premonition',
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

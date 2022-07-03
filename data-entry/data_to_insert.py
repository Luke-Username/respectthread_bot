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

update_respectthread(cur, 1801, 'Respect Doomsday (DC Post-Crisis)', 'https://redd.it/vptkbp')

########################################

id = get_rt_id(cur, 'Respect the Allosaurus (Allosaurus vs Tyrannosaurus Claymation)', 'https://redd.it/vomcrw')
add_data(['Allosaurus'],
'Allosaurus',
False,
False,
[
    ['Allosaurus vs Tyrannosaurus Claymation']
],
'Allosaurus vs Tyrannosaurus (Claymation)',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vomcrw/respect_the_allosaurus_allosaurus_vs/

########################################

id = get_rt_id(cur, 'Respect The Bad Guys! (The Bad Guys Film)', 'https://redd.it/vomfic')
add_data(['The Bad Guys'],
'The Bad Guys',
True,
False,
[
    ['The Bad Guys ?\(The Bad Guys'], ['The Bad Guys (film|movie)'],
    ['The Bad Guys.*Dreamworks']
],
'Dreamworks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vomfic/respect_the_bad_guys_the_bad_guys_film/

add_data(['Mr\.? Wolf'],
'Mr. Wolf',
False,
False,
[
    ['The Bad Guys']
],
'The Bad Guys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vomfic/respect_the_bad_guys_the_bad_guys_film/

add_data(['Mr\.? Snake'],
'Mr. Snake',
False,
False,
[
    ['The Bad Guys']
],
'The Bad Guys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vomfic/respect_the_bad_guys_the_bad_guys_film/

add_data(['Mr\.? Shark'],
'Mr. Shark',
False,
False,
[
    ['The Bad Guys']
],
'The Bad Guys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vomfic/respect_the_bad_guys_the_bad_guys_film/

########################################

id = get_rt_id(cur, 'Respect Ashura Doji, Kawamatsu, and Denjiro (One Piece)', 'https://redd.it/von3n4')
add_data(['Ashura Doji'],
'Ashura Doji',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/von3n4/respect_ashura_doji_kawamatsu_and_denjiro_one/

add_data(['Kawamatsu'],
'Kawamatsu',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/von3n4/respect_ashura_doji_kawamatsu_and_denjiro_one/

add_data(['Denjiro'],
'Denjiro',
False,
False,
[
    ['One ?Piece?'], ['Zoro']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/von3n4/respect_ashura_doji_kawamatsu_and_denjiro_one/

########################################

id = get_rt_id(cur, 'Respect Kiku (One Piece)', 'https://redd.it/vpftoy')
add_data(['Kiku'],
'Kiku',
False,
False,
[
    ['One ?Piece?'], ['Kawamatsu']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vpftoy/respect_kiku_one_piece/

########################################

id = get_rt_id(cur, 'Respect Vasilii Vorishikin, Love Sausage (The Boys)', 'https://redd.it/voo53g')
add_data(['Love Sausage'],
'Love Sausage',
False,
True,
[
    ['The Boys']
],
'The Boys',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/voo53g/respect_vasilii_vorishikin_love_sausage_the_boys/

########################################

id = get_rt_id(cur, "Respect Malcolm Turner (Big Momma''s House)", 'https://redd.it/vooarr')
add_data(['Malcolm Turner'],
'Malcolm Turner',
False,
False,
[
    ['Big Mommas?']
],
"Big Momma''s House",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vooarr/respect_malcolm_turner_big_mommas_house/

add_data(['Big Momma'],
'Big Momma',
False,
True,
[
    ['Big Momma ?\(Big Mommas?'], ['Doubtfire']
],
"Big Momma''s House",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vooarr/respect_malcolm_turner_big_mommas_house/

########################################

id = get_rt_id(cur, 'Respect The Slayer/The Rat King (2003 Teenage Mutant Ninja Turtles)', 'https://redd.it/voqg1c')
add_data(['Rat King'],
'Rat King',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2003'], ['TMNT', '2003']
],
'TMNT 2003',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/voqg1c/respect_the_slayerthe_rat_king_2003_teenage/

########################################

id = get_rt_id(cur, "Respect Edward Kenway! (Assassin''s Creed)", 'https://redd.it/vorbpz')
add_data(['Edward Kenway'],
'Edward Kenway',
False,
True,
[
    ['Assassin', 'Creed'], ['AC\d']
],
"Assassin''s Creed",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vorbpz/respect_edward_kenway_assassins_creed/

########################################

id = get_rt_id(cur, 'Respect Heracles! (Greek Mythology)', 'https://redd.it/voremj')
add_data(['Heracles'],
'Heracles',
False,
True,
[
    ['myth?(ical|olog(y|ical))?']
],
'Greek Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/voremj/respect_heracles_greek_mythology/

########################################

id = get_rt_id(cur, 'Respect Lunatik (Marvel, 616)', 'https://redd.it/voremy')
add_data(['Lunatik'],
'Lunatik',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/voremy/respect_lunatik_marvel_616/

########################################

id = get_rt_id(cur, 'Respect the Tyrannosaurus rex Bull (Jurassic Park 3)', 'https://redd.it/vot5pj')
add_data(['Tyrannosaurus rex Bull'],
'Tyrannosaurus rex Bull',
False,
False,
[
    ['Jurassic Park']
],
'Jurassic Park',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vot5pj/respect_the_tyrannosaurus_rex_bull_jurassic_park_3/

########################################

id = get_rt_id(cur, 'Respect Prophet Elijah (Holy Bible)', 'https://redd.it/vp38cz')
add_data(['Elijah'],
'Elijah',
False,
False,
[
    ['Prophet']
],
'Prophet',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vp38cz/respect_prophet_elijah_holy_bible/

########################################

id = get_rt_id(cur, 'Respect Taiyo Asano (Mission: Yozakura Family)', 'https://redd.it/vpjari')
add_data(['Taiyo Asano'],
'Taiyo Asano',
False,
True,
[
    ['Yozakura Family']
],
'Mission: Yozakura Family',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/vpjari/respect_taiyo_asano_mission_yozakura_family/

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

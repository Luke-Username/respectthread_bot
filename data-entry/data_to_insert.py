"""
# This script is used to enter new characters into the database when a respect thread is written of them.
# New respect threads are found at this link: https://www.reddit.com/r/respectthreads/new/
# An example of how to enter a new character is as follows.

id = get_rt_id(cur, 'Respect Dr. Evil (Austin Powers)', 'https://www.reddit.com/r/respectthreads/comments/1my1b8x/respect_dr_evil_austin_powers/')
add_data(['Dr\.? Evil'],
'Dr. Evil',
False,
False,
[
    ['Austin Powers']
],
'Austin Powers',
'{' + '{}'.format(id) + '}'
)
#

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
            # Turn the name into a string acceptable for PostgreSQL (no idea if this is correct. can't be bothered to do proper testing.)
            #formatted_name_list.append(name.replace('\\', '\\\\'))
            pass

    formatted_version_list = []
    for version in version_list:
        version_array_string = '{'
        for regex in version:
            if not is_valid_regex(regex):
                return
            else:
                #version_array_string += '"{}",'.format(regex.replace('\\', '\\\\'))
                pass

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

update_respectthread(cur, 17371, 'Respect Altair (Re:Creators anime)', 'https://www.reddit.com/r/respectthreads/comments/1qsaq1t/respect_altair_recreators_anime/')

########################################

id = get_rt_id(cur, 'Respect Lesla-Lar (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1qpqgmm/respect_leslalar_dc_comics_postflashpoint/')
add_data(['Lesla-Lar'],
'Lesla-Lar',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lesla-Lar'],
'Lesla-Lar',
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

id = get_rt_id(cur, 'Respect Queen Clea (DC Comics, Absolute Universe)', 'https://www.reddit.com/r/respectthreads/comments/1qs7cz0/respect_queen_clea_dc_comics_absolute_universe/')
add_data(['Queen Clea'],
'Queen Clea',
False,
False,
[
    ['Absolute Universe']
],
'Absolute Universe',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Cobra Bubbles (Lilo & Stitch)', 'https://www.reddit.com/r/respectthreads/comments/1qpxtbt/respect_cobra_bubbles_lilo_stitch/')
add_data(['Cobra Bubbles'],
'Cobra Bubbles',
False,
False,
[
    ['Lilo (and|&) Stitch']
],
'Lilo & Stitch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Sonic (Sonic and the Blade of Courage)', 'https://www.reddit.com/r/respectthreads/comments/1qqstww/respect_sonic_sonic_and_the_blade_of_courage/')
add_data(['Sonic'],
'Sonic',
False,
False,
[
    ['Sonic and the Blade of Courage']
],
'Sonic and the Blade of Courage',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yuuta (Sonic and the Blade of Courage)', 'https://www.reddit.com/r/respectthreads/comments/1qqvj6e/respect_yuuta_sonic_and_the_blade_of_courage/')
add_data(['Yuuta'],
'Yuuta',
False,
False,
[
    ['Sonic and the Blade of Courage']
],
'Sonic and the Blade of Courage',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yura (Kagurabachi)', 'https://www.reddit.com/r/respectthreads/comments/1qshpbk/respect_yura_kagurabachi/')
add_data(['Yura'],
'Yura',
False,
False,
[
    ['Kagurabachi']
],
'Kagurabachi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dracula (Buffyverse)', 'https://www.reddit.com/r/respectthreads/comments/1qsik8p/respect_dracula_buffyverse/')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Buffy the Vampire Slayer'], ['\(Buffy\)'], ['Buffyverse'], ['BTVS'], ['Dracula ?\(Buffy\)'], ['Dracula from Buffy(verse)?']
],
'Buffy the Vampire Slayer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Scarlet El Vandimion (May I Ask For One Final Thing?) [Manga/Anime]', 'https://www.reddit.com/r/respectthreads/comments/1qspspx/respect_scarlet_el_vandimion_may_i_ask_for_one/')
add_data(['Scarlet El Vandimion'],
'Scarlet El Vandimion',
False,
True,
[
    ['May I Ask For One Final Thing']
],
'May I Ask For One Final Thing?',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Sentinels (Marvel, Earth-TRN1300 [X-Men Origins: Wolverine Tie-In Game])', 'https://www.reddit.com/r/respectthreads/comments/1qsyib2/respect_the_sentinels_marvel_earthtrn1300_xmen/')
add_data(['Sentinels'],
'Sentinels',
False,
False,
[
    ['TRN1300']
],
'TRN1300',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Stray Cat (Stray)', 'https://www.reddit.com/r/respectthreads/comments/1qt6i4g/respect_the_stray_cat_stray/')
add_data(['Stray Cat'],
'Stray Cat',
False,
False,
[
    ['\(Stray\)']
],
'Stray',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Cat from Stray'],
'Cat from Stray',
False,
False,
[
    ['\(Stray\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Titans (VERSUS)', 'https://www.reddit.com/r/respectthreads/comments/1qu3fym/respect_the_titans_versus/')
add_data(['Titans'],
'Titans',
False,
False,
[
    ['Titans ?\(VERSUS\)']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pakkya (VERSUS)', 'https://www.reddit.com/r/respectthreads/comments/1qui7um/respect_pakkya_versus/')
add_data(['Pakkya'],
'Pakkya',
False,
False,
[
    ['Pakkya ?\(VERSUS\)']
],
'VERSUS',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect X-Virus (X-Virus)', 'https://www.reddit.com/r/respectthreads/comments/1quauxe/respect_xvirus_xvirus/')
add_data(['X-Virus'],
'X-Virus',
False,
False,
[
    ['Creepypasta']
],
'Creepypasta',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nick Wilde (Zootopia)', 'https://www.reddit.com/r/respectthreads/comments/1quqfi2/respect_nick_wilde_zootopia/')
add_data(['Nick Wilde'],
'Nick Wilde',
False,
True,
[
    ['Zootopia']
],
'Zootopia',
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

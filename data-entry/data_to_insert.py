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

update_respectthread(cur, 9276, 'Respect Karma Abyss (I Can Go Adventuring by Myself, Mom!: The Son Raised by the Strongest Overprotective Dragon-Mom)', 'https://www.reddit.com/r/respectthreads/comments/1pmve52/respect_karma_abyss_i_can_go_adventuring_by/')

########################################

add_data(['Dutch'],
'Dutch',
False,
False,
[
    ['Dutch ?\(Predator\)'], ["Dutch''?s? Team", 'Predator'], ['Dutch in.*Predator']
],
'Predator',
'{16762}'
)
#https://www.reddit.com/r/whowouldwin/comments/hp029j/john_rambo_rambo_vs_dutch_predator/
#https://www.reddit.com/r/whowouldwin/comments/1m7k58w/rambo_first_blood_vs_dutch_predator_in_a_guerilla/
#https://www.reddit.com/r/whowouldwin/comments/1dhy9iv/dutchs_team_predator_is_placed_in_a_wrong_horror/
#https://www.reddit.com/r/whowouldwin/comments/1hts1sf/the_following_characters_replace_dutch_in/


########################################

add_data(['Ice(-| )?man'],
'Iceman',
False,
False,
[
    ['Richard Kuklinski']
],
'Richard Kuklinski',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/1pm3pux/anton_chigurh_vs_the_iceman_movie_psychopath_vs/nu03slr/?context=3


########################################

add_data(['Asha'],
'Asha',
False,
False,
[
    ['Mirabel', 'Moana']
],
'Wish',
'{25869}'
)
#https://www.reddit.com/r/whowouldwin/comments/1plnf05/mirabel_moana_merida_asha_and_rapunzel_debate/nttyml8/?context=3

add_data(['Belle'],
'Belle',
False,
False,
[
    ['Ariel', 'Cinderella']
],
'Beauty and the Beast',
'{26010}'
)
#https://www.reddit.com/r/whowouldwin/comments/1plnf05/mirabel_moana_merida_asha_and_rapunzel_debate/nttyml8/?context=3

add_data(['Mirabel'],
'Mirabel',
False,
False,
[
    ['Merida', 'Moana']
],
'Encanto',
'{21201}'
)
#https://www.reddit.com/r/whowouldwin/comments/1plnf05/mirabel_moana_merida_asha_and_rapunzel_debate/nttyml8/?context=3

########################################

id = get_rt_id(cur, 'Respect Team Deus Ex Machina (Character Scramble)', 'https://www.reddit.com/r/respectthreads/comments/1pkscv1/respect_team_deus_ex_machina_character_scramble/')
add_data(['Deus Ex Machina'],
'Deus Ex Machina',
True,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect X (Pokemon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1pksd1v/respect_x_pokemon_adventures/')
add_data(['X'],
'X',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yvonna Gabena (Pokemon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1pksd4m/respect_yvonna_gabena_pokemon_adventures/')
add_data(['Y'],
'Y',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Yvonna Gabena'],
'Yvonna Gabena',
False,
True,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nona Ewin (WITCHRIV)', 'https://www.reddit.com/r/respectthreads/comments/1plcrup/respect_nona_ewin_witchriv/')
add_data(['Nona Ewin'],
'Nona Ewin',
False,
False,
[
    ['WITCHRIV']
],
'WITCHRIV',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marisa Rossetti (Street Fighter)', 'https://www.reddit.com/r/respectthreads/comments/1plw7xg/respect_marisa_rossetti_street_fighter/')
add_data(['Marisa Rossetti'],
'Marisa Rossetti',
False,
True,
[
    ['Street Fighter']
],
'Street Fighter',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Karen Aijo (Revue Starlight)', 'https://www.reddit.com/r/respectthreads/comments/1pm0n8l/respect_karen_aijo_revue_starlight/')
add_data(['Karen Aijo'],
'Karen Aijo',
False,
False,
[
    ['Revue Starlight']
],
'Revue Starlight',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Hikari Kagura (Revue Starlight)', 'https://www.reddit.com/r/respectthreads/comments/1pm0n8r/respect_hikari_kagura_revue_starlight/')
add_data(['Hikari Kagura'],
'Hikari Kagura',
False,
False,
[
    ['Revue Starlight']
],
'Revue Starlight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Captain Scarlet (Captain Scarlet and the Mysterons)', 'https://www.reddit.com/r/respectthreads/comments/1pme8xd/respect_captain_scarlet_captain_scarlet_and_the/')
add_data(['Captain Scarlet'],
'Captain Scarlet',
False,
False,
[
    ['Captain Scarlet and the Mysterons']
],
'Captain Scarlet and the Mysterons',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Connor of Daventry (King''s Quest: Mask of Eternity)", 'https://www.reddit.com/r/respectthreads/comments/1pme8y4/respect_connor_of_daventry_kings_quest_mask_of/')
add_data(['Connor'],
'Connor',
False,
False,
[
    ["King''?s Quest"]
],
"King''s Quest",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kamen Rider (Shin Kamen Rider)', 'https://www.reddit.com/r/respectthreads/comments/1pmjz9p/respect_kamen_rider_shin_kamen_rider/')
add_data(['Kamen Rider'],
'Kamen Rider',
False,
False,
[
    ['Shin Kamen Rider']
],
'Shin Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Takeshi Hongo'],
'Takeshi Hongo',
False,
False,
[
    ['Shin Kamen Rider']
],
'Shin Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kamen Rider No. 2 (Shin Kamen Rider)', 'https://www.reddit.com/r/respectthreads/comments/1pmjzb1/respect_kamen_rider_no_2_shin_kamen_rider/')
add_data(['Kamen Rider No\.? 2'],
'Kamen Rider No. 2',
False,
False,
[
    ['Shin Kamen Rider']
],
'Shin Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kamen Rider No. 0 (Shin Kamen Rider)', 'https://www.reddit.com/r/respectthreads/comments/1pmjzcg/respect_kamen_rider_no_0_shin_kamen_rider/')
add_data(['Kamen Rider No. 0'],
'Kamen Rider No. 0',
False,
False,
[
    ['Shin Kamen Rider']
],
'Shin Kamen Rider',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Beast (Angel)', 'https://www.reddit.com/r/respectthreads/comments/1pmowix/respect_the_beast_angel/')
add_data(['The Beast'],
'The Beast',
False,
False,
[
    ['The Beast ?\(Angel\)']
],
'Angel',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect SCP 352, Baba Yaga (SCP Foundation)', 'https://www.reddit.com/r/respectthreads/comments/1pmowjz/respect_scp_352_baba_yaga_scp_foundation/')
add_data(['SCP ?(-| )? ?352'],
'SCP-352',
False,
True,
[
    ['Baba Yaga']
],
'',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect SCP 3783, Baba Yaga''s Cottage (SCP Foundation)", 'https://www.reddit.com/r/respectthreads/comments/1pmowln/respect_scp_3783_baba_yagas_cottage_scp_foundation/')
add_data(['SCP ?(-| )? ?3783'],
'SCP-3783',
False,
True,
[
    ["Baba Yaga''?s Cottage"]
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Travis Bickle (Taxi Driver)', 'https://www.reddit.com/r/respectthreads/comments/1pmq3sq/respect_travis_bickle_taxi_driver/')
add_data(['Travis Bickle'],
'Travis Bickle',
False,
True,
[
    ['Taxi Driver']
],
'Taxi Driver',
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

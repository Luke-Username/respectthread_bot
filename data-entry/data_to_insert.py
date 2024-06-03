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

update_respectthread(cur, 3286, 'Respect Son Gohan (Dragon Ball [Manga])', 'https://redd.it/1d5ekjm')
update_respectthread(cur, 17336, 'Respect Titanus Mosura, aka Mothra (MonsterVerse)', 'https://redd.it/1d6j2g6')

########################################

add_data(['Perry'],
'Perry',
False,
False,
[
    ['Doofenshmirtz']
],
'Phineas and Ferb',
'{17636}'
)
#https://www.reddit.com/r/whowouldwin/comments/1d5ecdr/perry_and_doofenshmirtz_work_together_to_stop_the/l6kup8o/?context=3

########################################

id = get_rt_id(cur, 'Respect Betelgeuse! (Beetlejuice)', 'https://redd.it/dpou13')
add_data(['Betelgeuse'],
'Betelgeuse',
False,
False,
[
    ['Beetlejuice']
],
'Beetlejuice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1d5l50f/pennywise_1990s_it_vs_beetlejuice/l6m265z/?context=3

########################################

id = get_rt_id(cur, 'Respect the Justice League (Justice League vs Godzilla vs Kong)', 'https://redd.it/1d50z6d')
add_data(['Justice League'],
'Justice League',
False,
False,
[
    ['Justice League vs Godzilla vs Kong'], ['Godzilla vs Justice League vs Kong']
],
'Justice League vs Godzilla vs Kong',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d50z6d/respect_the_justice_league_justice_league_vs/

########################################

id = get_rt_id(cur, 'Respect Kong (Justice League vs Godzilla vs Kong)', 'https://redd.it/1d5fl8p')
add_data(['Kong'],
'Kong',
False,
False,
[
    ['Justice League vs Godzilla vs Kong'], ['Godzilla vs Justice League vs Kong']
],
'Justice League vs Godzilla vs Kong',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5fl8p/respect_kong_justice_league_vs_godzilla_vs_kong/

########################################

id = get_rt_id(cur, 'Respect the MonsterVerse Titans (Justice League vs Godzilla vs Kong)', 'https://redd.it/1d5faaq')
add_data(['Titans'],
'Titans',
True,
False,
[
    ['Justice League vs Godzilla vs Kong'], ['Godzilla vs Justice League vs Kong']
],
'Justice League vs Godzilla vs Kong',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5faaq/respect_the_monsterverse_titans_justice_league_vs/

########################################

id = get_rt_id(cur, 'Respect the Forest Devil (Predator: The Pride at Nghasa) [Dark Horse Comics]', 'https://redd.it/1d5dy83')
add_data(['Forest Devil'],
'Forest Devil',
False,
False,
[
    ['Pride at Nghasa']
],
'Predator: The Pride at Nghasa',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5dy83/respect_the_forest_devil_predator_the_pride_at/

########################################

id = get_rt_id(cur, 'Respect the Four-Armed Predator (Predators: Surviving Life)', 'https://redd.it/1d5erps')
add_data(['Four(-| )Armed Predator'],
'Four-Armed Predator',
False,
True,
[
    ['Surviving Life']
],
'Predators: Surviving Life',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5erps/respect_the_fourarmed_predator_predators/

########################################

id = get_rt_id(cur, 'Respect Smash Mason (Aliens: Hive Wars)', 'https://redd.it/1d5ghgm')
add_data(['Smash Mason'],
'Smash Mason',
False,
False,
[
    ['Aliens|Hive Wars']
],
'Aliens: Hive Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5ghgm/respect_smash_mason_aliens_hive_wars/

########################################

id = get_rt_id(cur, 'Respect Gold (Pokemon Adventures)', 'https://redd.it/1d5kihh')
add_data(['Gold'],
'Gold',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5kihh/respect_gold_pokemon_adventures/

########################################

id = get_rt_id(cur, 'Respect Agatha (Pokemon Anime)', 'https://redd.it/1d75rwu')
add_data(['Agatha'],
'Agatha',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d75rwu/respect_agatha_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Team Rocket Officer Tyson (Pokemon Anime)', 'https://redd.it/1d74mry')
add_data(['Tyson'],
'Tyson',
False,
False,
[
    ['Tyson ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d74mry/respect_team_rocket_officer_tyson_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Kiyo (Pokemon Anime)', 'https://redd.it/1d6d02p')
add_data(['Kiyo'],
'Kiyo',
False,
False,
[
    ['Kiyo ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6d02p/respect_kiyo_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Claire Kent, alias Super-Sister! (DC Comics, Pre-Crisis)', 'https://redd.it/1d5mls8')
add_data(['Claire Kent'],
'Claire Kent',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Super-Sister'],
'Super-Sister',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5mls8/respect_claire_kent_alias_supersister_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Speedrunner Link (Terminalmontage)', 'https://redd.it/1d5r1yy')
add_data(['Speedrunner Link'],
'Speedrunner Link',
False,
True,
[
    ['Something ?Series'], ['Terminal ?Montage']
],
'Something Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d5r1yy/respect_speedrunner_link_terminalmontage/

########################################

id = get_rt_id(cur, 'Respect Mother Russia! (Kick Ass [Movies])', 'https://redd.it/1d6dq91')
add_data(['Mother Russia'],
'Mother Russia',
False,
False,
[
    ['Kick(-| )?Ass']
],
'Kick-Ass',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6dq91/respect_mother_russia_kick_ass_movies/

########################################

id = get_rt_id(cur, 'Respect Wammawink (Centaurworld)', 'https://redd.it/1d6hjac')
add_data(['Wammawink'],
'Wammawink',
False,
True,
[
    ['Centaurworld']
],
'Centaurworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6hjac/respect_wammawink_centaurworld/

########################################

id = get_rt_id(cur, 'Respect The Fox (Tunic)', 'https://redd.it/1d6hjc1')
add_data(['The Fox'],
'The Fox',
False,
False,
[
    ['Tunic']
],
'Tunic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6hjc1/respect_the_fox_tunic/

########################################

id = get_rt_id(cur, 'Respect Taboo (Wereworld)', 'https://redd.it/1d6l8au')
add_data(['Taboo'],
'Taboo',
False,
False,
[
    ['Wereworld']
],
'Wereworld',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6l8au/respect_taboo_wereworld/

########################################

id = get_rt_id(cur, 'Respect Ghost Godzilla (Kaiju War Chronicles Multimedia #11)', 'https://redd.it/1d6pu2p')
add_data(['Ghost Godzilla'],
'Ghost Godzilla',
False,
False,
[
    ['Kaiju War Chronicles Multimedia']
],
'Kaiju War Chronicles Multimedia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d6pu2p/respect_ghost_godzilla_kaiju_war_chronicles/

########################################

id = get_rt_id(cur, "Respect Jennifer Check (Jennifer''s Body)", 'https://redd.it/1d77rjk')
add_data(['Jennifer Check'],
'Jennifer Check',
False,
False,
[
    ["Jennifer''s Body"]
],
"Jennifer''s Body",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d77rjk/respect_jennifer_check_jennifers_body/

add_data(['Jennifer'],
'Jennifer',
False,
False,
[
    ["Jennifer ?\(Jennifer''s Body"]
],
"Jennifer''s Body",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1d77rjk/respect_jennifer_check_jennifers_body/

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

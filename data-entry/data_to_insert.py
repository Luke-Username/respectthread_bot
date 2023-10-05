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

update_respectthread(cur, 5610, 'Respect Henry Stickmin (Henry Stickmin Series)', 'https://redd.it/16vtf8y')
update_respectthread(cur, 13058, 'Respect Ellie Rose (Henry Stickmin Series)', 'https://redd.it/170k741')
update_respectthread(cur, 13320, 'Respect The Center for Chaos Containment (Henry Stickmin Series)', 'https://redd.it/170k84b')
update_respectthread(cur, 13057, 'Respect Charles Calvin (Henry Stickmin Series)', 'https://redd.it/1701av9')
update_respectthread(cur, 13319, 'Respect Right Hand Man (Henry Stickmin Series)', 'https://redd.it/1701aae')
update_respectthread(cur, 6211, 'Respect Slender Man! (Victor Surge)', 'https://redd.it/16wrjv8')
update_respectthread(cur, 324, 'Respect Mace Windu (Star Wars Canon)', 'https://redd.it/16yisty')

########################################

add_data(['Slender(-| )?man'],
'Slenderman',
False,
True,
[
    ['Victor Surge']
],
'',
'{6211}'
)
#

########################################

add_data(['Alastor( "Mad(-| )?Eye")? Moody'],
'Alastor Moody',
False,
True,
[
    ['Harry Potter']
],
'Harry Potter',
'{5822}'
)
#https://www.reddit.com/r/whowouldwin/comments/16yx0p6/samus_aran_metroid_vs_alastor_madeye_moody_harry/k3btn0w/?context=3

########################################

add_data(['Beatles'],
'Beatles',
False,
False,
[
    ['John','Paul','George','Ringo']
],
'The Beatles',
'{23623}'
)
#https://www.reddit.com/r/whowouldwin/comments/16xeif5/how_many_beatles_would_it_take_to_beat_goku/k32i2vv/?context=3

########################################

id = get_rt_id(cur, "Respect Godzilla (Godzilla vs Mighty Morphin'' Power Rangers)", 'https://redd.it/16vznwe')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ["Godzilla vs\.? (Mighty Morphin(''|g)? )?Power Rangers"]
],
"Godzilla vs Mighty Morphin'' Power Rangers",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vznwe/respect_godzilla_godzilla_vs_mighty_morphin_power/

########################################

id = get_rt_id(cur, "Respect the Mighty Morphin'' Power Rangers! (Godzilla vs. The Mighty Morphin' Power Rangers)", 'https://redd.it/16vznzz')
add_data(['Power Rangers'],
'Power Rangers',
True,
False,
[
    ["Godzilla vs\.? (Mighty Morphin(''|g)? )?Power Rangers"]
],
"Godzilla vs Mighty Morphin'' Power Rangers",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vznzz/respect_the_mighty_morphin_power_rangers_godzilla/

########################################

id = get_rt_id(cur, "Respect Gigan! (Godzilla vs. The Mighty Morphin'' Power Rangers)", 'https://redd.it/16vzoyf')
add_data(['Gigan'],
'Gigan',
False,
False,
[
    ["Godzilla vs\.? (Mighty Morphin(''|g)? )?Power Rangers"]
],
"Godzilla vs Mighty Morphin'' Power Rangers",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vzoyf/respect_gigan_godzilla_vs_the_mighty_morphin/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model NIL: the Black King (Marvel, Earth-616)', 'https://redd.it/16vzoyf')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model NIL'], ['Black King']
],
'Black King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Angel! (Tower of God)', 'https://redd.it/16wdpfi')
add_data(['Angel'],
'Angel',
False,
False,
[
    ['Tower of God']
],
'Tower of God',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wdpfi/respect_angel_tower_of_god/

########################################

id = get_rt_id(cur, 'Respect Billie Lurk! (Dishonored)', 'https://redd.it/16wf29n')
add_data(['Billie Lurk'],
'Billie Lurk',
False,
True,
[
    ['Dishonou?red']
],
'Dishonored',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wf29n/respect_billie_lurk_dishonored/

########################################

id = get_rt_id(cur, 'Respect Malikai (Soulfire)', 'https://redd.it/16wf4c4')
add_data(['Malikai'],
'Malikai',
False,
False,
[
    ['Soulfire']
],
'Soulfire',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wf4c4/respect_malikai_soulfire/

########################################

id = get_rt_id(cur, 'Respect Sombra (Overwatch)', 'https://redd.it/16wo722')
add_data(['Sombra'],
'Sombra',
False,
False,
[
    ['Overwatch'], ['Talon'], ['OW']
],
'Overwatch',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wo722/respect_sombra_overwatch/

########################################

id = get_rt_id(cur, 'Respect the Staircases ! (Search and Rescue Woods)', 'https://redd.it/16wrkp6')
add_data(['Stairs'],
'Stairs',
False,
False,
[
    ['Search and Rescue Woods']
],
'Search and Rescue Woods',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wrkp6/respect_the_staircases_search_and_rescue_woods/

add_data(['Staircases?'],
'Staircases',
False,
False,
[
    ['Search and Rescue Woods']
],
'Search and Rescue Woods',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wrkp6/respect_the_staircases_search_and_rescue_woods/

########################################

id = get_rt_id(cur, 'Respect Varan (Godzilla, Composite)', 'https://redd.it/16wvvey')
add_data(['Varan'],
'Varan',
False,
False,
[
    ['Godzilla']
],
'Godzilla',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16wvvey/respect_varan_godzilla_composite/

########################################

id = get_rt_id(cur, 'Respect the Mummies (Hammer Horror)', 'https://redd.it/16x1khn')
add_data(['Mummies'],
'Mummies',
True,
False,
[
    ['Hammer (Horror|Version)']
],
'Hammer Horror',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16x1khn/respect_the_mummies_hammer_horror/

########################################

id = get_rt_id(cur, 'Respect Lord Ruthven (The Vampyre)', 'https://redd.it/16x5iyc')
add_data(['Lord Ruthven'],
'Lord Ruthven',
False,
True,
[
    ['The Vampyre']
],
'The Vampyre',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-165, The Creeping, Hungry Sands of Tule (SCP Foundation)', 'https://redd.it/16x61sb')
add_data(['SCP ?(-| )? ?165'],
'SCP-165',
False,
True,
[
    ['Hungry Sands of Tule']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Raven (DC, Post-Flashpoint)', 'https://redd.it/16x7cb3')
add_data(['Raven'],
'Raven',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16x7cb3/respect_raven_dc_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect Scarab! (Adventure Time)', 'https://redd.it/16xzs1m')
add_data(['Scarab'],
'Scarab',
False,
False,
[
    ['Adventure Time']
],
'Adventure Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16xzs1m/respect_scarab_adventure_time/

########################################

id = get_rt_id(cur, 'Respect Siren Head! (Trevor Henderson Mythos)', 'https://redd.it/16yeyd8')
add_data(['Siren Head'],
'Siren Head',
False,
True,
[
    ['Trevor Henderson']
],
'Trevor Henderson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16yeyd8/respect_siren_head_trevor_henderson_mythos/

########################################

id = get_rt_id(cur, 'Respect the Cassowary (MatromX)', 'https://redd.it/16yims3')
add_data(['Cassowary'],
'Cassowary',
False,
False,
[
    ['MatromX']
],
'MatromX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16yims3/respect_the_cassowary_matromx/

########################################

id = get_rt_id(cur, 'Respect the Anaconda (MatromX)', 'https://redd.it/16yiujj')
add_data(['Anaconda'],
'Anaconda',
False,
False,
[
    ['MatromX']
],
'MatromX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16yiujj/respect_the_anaconda_matromx/

########################################

id = get_rt_id(cur, 'Respect the Pteranodon (MatromX)', 'https://redd.it/170qktb')
add_data(['Pteranodon'],
'Pteranodon',
False,
False,
[
    ['MatromX']
],
'MatromX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/170qktb/respect_the_pteranodon_matromx/

########################################

id = get_rt_id(cur, 'Respect the Harpy Eagle (MatromX)', 'https://redd.it/170qu2b')
add_data(['Harpy Eagle'],
'Harpy Eagle',
False,
False,
[
    ['MatromX']
],
'MatromX',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/170qu2b/respect_the_harpy_eagle_matromx/

########################################

id = get_rt_id(cur, "Respect Ash''s Incineroar (Pokemon Anime)", 'https://redd.it/16zn39z')
add_data(['Incineroar'],
'Incineroar',
False,
False,
[
    ['Ash']
],
'Ash',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16zn39z/respect_ashs_incineroar_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect \"Ash''s\" Larvitar (Pokemon Anime)", 'https://redd.it/170hmv2')
add_data(['Larvitar'],
'Larvitar',
False,
False,
[
    ['Ash']
],
'Ash',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/170hmv2/respect_ashs_larvitar_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Dracula (Dracula: Dead and Loving It)', 'https://redd.it/16zw8g4')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Dead and Loving It']
],
'Dead and Loving It',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16zw8g4/respect_dracula_dracula_dead_and_loving_it/

########################################

id = get_rt_id(cur, 'Respect the Haunted Gigan Suit (The haunted gigan final wars suit)', 'https://redd.it/1705xb9')
add_data(['Haunted Gigan( Final Wars)? Suit'],
'Haunted Gigan Suit',
False,
True,
[
    ['Final Wars']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1705xb9/respect_the_haunted_gigan_suit_the_haunted_gigan/

########################################

id = get_rt_id(cur, 'Respect Xipe Totec (The Valdevia Canon)', 'https://redd.it/17060kd')
add_data(['Xipe Totec'],
'Xipe Totec',
False,
True,
[
    ['Valdevia'], ['Eduardo Vald(é|e)s(-| )Hevia']
],
'The Valdevia',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17060kd/respect_xipe_totec_the_valdevia_canon/

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

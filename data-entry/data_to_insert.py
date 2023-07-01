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

update_respectthread(cur, 4682, 'Respect Legosi (Beastars)', 'https://redd.it/djfbik')
update_respectthread(cur, 12060, 'Respect Tserriednich Hui Guo Rou! (Hunter X Hunter)', 'https://redd.it/14kek75')
update_respectthread(cur, 1604, 'Respect James Jesse, The Trickster! (DC Comics, Pre-Flashpoint)', 'https://redd.it/14kmtvh')
update_respectthread(cur, 21540, 'Respect Amalthea: The Last Unicorn', 'https://redd.it/68thok')
update_respectthread(cur, 91, 'Respect Sportacus! (LazyTown)', 'https://redd.it/14m5cuz')
update_respectthread(cur, 90, 'Respect Robbie Rotten! (LazyTown)', 'https://redd.it/9akbw5')
update_respectthread(cur, 1599, 'Respect Mick Rory, Heat Wave! (DC Comics, Pre-Flashpoint)', 'https://redd.it/14n1knb')

########################################

add_data(['Insomniac Spide(r(-| )?Man|y)'],
'Insomniac Spider-Man',
False,
True,
[
    ['1048']
],
'',
'{15258}'
)
#https://www.reddit.com/r/whowouldwin/comments/14k3jwi/avatar_aang_vs_insomnic_spidey/

########################################

add_data(['Hancock'],
'Hancock',
False,
False,
[
    ['vs Hancock']
],
'',
'{457}'
)
#https://www.reddit.com/r/whowouldwin/comments/14ksm71/zohan_dont_mess_with_zohan_vs_hancock/

########################################

id = get_rt_id(cur, 'Respect Akko Kagari (Little Witch Academia: Chamber of Time)', 'https://redd.it/14jtwy7')
add_data(['Akko'],
'Akko',
False,
False,
[
    ['Chamber of Time']
],
'Little Witch Academia: Chamber of Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14jtwy7/respect_akko_kagari_little_witch_academia_chamber/

########################################

id = get_rt_id(cur, 'Respect Rooper Nitani (Star Wars Canon)', 'https://redd.it/14jxxd6')
add_data(['Rooper Nitani'],
'Rooper Nitani',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14jxxd6/respect_rooper_nitani_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Keeve Trennis (Star Wars Canon)', 'https://redd.it/14lt4wy')
add_data(['Keeve Trennis'],
'Keeve Trennis',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14lt4wy/respect_keeve_trennis_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Kurumi Tokisaki! (Date A Live [Anime Series])', 'https://redd.it/14kbas0')
add_data(['Kurumi'],
'Kurumi',
False,
False,
[
    ['Date A Live'], ['Tokisaki']
],
'Date A Live',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14kbas0/respect_kurumi_tokisaki_date_a_live_anime_series/

########################################

id = get_rt_id(cur, 'Respect Chōji Akimichi (Naruto)', 'https://redd.it/14kpuk1')
add_data(['Ch(ō|o)ji'],
'Chōji',
False,
False,
[
    ['Naruto'], ['Akimichi'], ['Konoha']
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Suburb Slasher (SCP Foundation)', 'https://redd.it/14kvep1')
add_data(['Suburb Slasher'],
'Suburb Slasher',
False,
True,
[
    ['SCP']
],
'SCP',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14kvep1/respect_the_suburb_slasher_scp_foundation/

add_data(['SCP ?(-| )? ?5733 ?(-| )? ?1'],
'SCP-5733-1',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14kvep1/respect_the_suburb_slasher_scp_foundation/

add_data(['SCP ?(-| )? ?6733 ?(-| )? ?1'],
'SCP-6733-1',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14kvep1/respect_the_suburb_slasher_scp_foundation/


########################################

id = get_rt_id(cur, "Respect Misty''s Clauncher (Pokemon Anime)", 'https://redd.it/14l9sma')
add_data(['Clauncher'],
'Clauncher',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14l9sma/respect_mistys_clauncher_pokemon_anime/


########################################

id = get_rt_id(cur, 'Respect Cujo (Cujo)', 'https://redd.it/14lce7j')
add_data(['Cujo'],
'Cujo',
False,
False,
[
    ['Cujo ?\(Cujo\)'], ['Stephen Kings?'], ['movie'], ['Dogs?'], ['Cujo vs'], ['Pit ?bulls?'], ['Jason Voorhees'], ['Gr(e|a)y Wolf']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14lce7j/respect_cujo_cujo/

########################################

id = get_rt_id(cur, 'Respect Tari! (Meta Runner)', 'https://redd.it/14ljvae')
add_data(['Tari'],
'Tari',
False,
False,
[
    ['Meta Runner']
],
'Meta Runner',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ljvae/respect_tari_meta_runner/

########################################

id = get_rt_id(cur, 'Respect Meg McCaffrey! (The Trials of Apollo)', 'https://redd.it/14m10kj')
add_data(['Meg McCaffrey'],
'Meg McCaffrey',
False,
True,
[
    ['Percy Jackson'], ['Riordan(-| )?(verse)?'], ['Trials of Apollo']
],
'Percy Jackson',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14m10kj/respect_meg_mccaffrey_the_trials_of_apollo/

########################################

id = get_rt_id(cur, 'Respect: Spider-Carnage (Marvel Animated Universe)', 'https://redd.it/14m1xwp')
add_data(['Spider(-| )?Carnage'],
'Spider-Carnage',
False,
False,
[
    ['Animated']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14m1xwp/respect_spidercarnage_marvel_animated_universe/

########################################

id = get_rt_id(cur, 'Respect The Joker (Mortal Kombat)', 'https://redd.it/14m542n')
add_data(['Joker'],
'Joker',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14m542n/respect_the_joker_mortal_kombat/

########################################

add_data(['Black Widow'],
'Black Widow',
False,
False,
[
    ['vs Black Widow', 'Batman']
],
'616',
'{1989}'
)
#https://www.reddit.com/r/whowouldwin/comments/14mxtlt/cammy_white_vs_black_widow_at_night/

########################################

id = get_rt_id(cur, 'Respect Diluc (Genshin Impact)', 'https://redd.it/14ncj73')
add_data(['Diluc'],
'Diluc',
False,
True,
[
    ['Genshin']
],
'Genshin Impact',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ncj73/respect_diluc_genshin_impact/

########################################

id = get_rt_id(cur, 'Respect the Aliens! (Pixels)', 'https://redd.it/14nktey')
add_data(['Aliens'],
'Aliens',
False,
False,
[
    ['Pixels']
],
'Pixels',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14nktey/respect_the_aliens_pixels/


########################################

id = get_rt_id(cur, 'Respect Plok! (Plok!)', 'https://redd.it/14nkz5v')
add_data(['Plok'],
'Plok',
False,
True,
[
    ['Plok ?\(Plok\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14nktey/respect_the_aliens_pixels/

########################################

id = get_rt_id(cur, 'Respect Snowguard (Marvel 616)', 'https://redd.it/14nyb3n')
add_data(['Snowguard'],
'Snowguard',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14nyb3n/respect_snowguard_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Penelope Spectra (Danny Phantom)', 'https://redd.it/14nyb4j')
add_data(['Penelope Spectra'],
'Penelope Spectra',
False,
True,
[
    ['Danny Phantom']
],
'Danny Phantom',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14nyb4j/respect_penelope_spectra_danny_phantom/

########################################

id = get_rt_id(cur, 'Respect Batman (Batman Unlimited)', 'https://redd.it/14nyb5n')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Batman Unlimited']
],
'Batman Unlimited',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14nyb5n/respect_batman_batman_unlimited/

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

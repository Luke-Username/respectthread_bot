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

update_respectthread(cur, 557, 'Respect Miho (Sin City) [Movies]', 'https://redd.it/129p955')

########################################

add_data(['Static'],
'Static',
False,
False,
[
    ['Static ?\(Static Shock\)']
],
'DCAU',
'{771}'
)
#https://www.reddit.com/r/whowouldwin/comments/qh37kd/who_would_win_gambit_or_static_shock/

add_data(['Static Shock'],
'Static Shock',
False,
False,
[
    ['animated series']
],
'DCAU',
'{771}'
)
#https://www.reddit.com/r/whowouldwin/comments/qh37kd/who_would_win_gambit_or_static_shock/

########################################

add_data(['Shazam'],
'Shazam',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{22688}'
)
#https://www.reddit.com/r/whowouldwin/comments/1280rhv/what_if_shazam_post_crisis_was_in_one_piece/jeiykv8/?context=3

########################################

id = get_rt_id(cur, "Respect Larry (Telltale''s The Walking Dead Game)", 'https://redd.it/128ck6x')
add_data(['Larry'],
'Larry',
False,
False,
[
    ['Wa(lk|kl)ing Dead']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128ck6x/respect_larry_telltales_the_walking_dead_game/

########################################

id = get_rt_id(cur, 'Respect The Gamers (The Gamers: Dorkness Rising)', 'https://redd.it/128e1r8')
add_data(['Gamers'],
'Gamers',
True,
False,
[
    ['Dorkness Rising']
],
'The Gamers: Dorkness Rising',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128e1r8/respect_the_gamers_the_gamers_dorkness_rising/

########################################

id = get_rt_id(cur, 'Respect Giorno Giovanna (What if Giorno ONLY Made Pitbulls and Babies?)', 'https://redd.it/128iaag')
add_data(['Giorno'],
'Giorno Giovanna',
False,
False,
[
    ['Pitbulls and Babies']
],
'What if Giorno ONLY Made Pitbulls and Babies?',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128iaag/respect_giorno_giovanna_what_if_giorno_only_made/

########################################

id = get_rt_id(cur, "Respect Garnet (Garnet''s Universe)", 'https://redd.it/128juhf')
add_data(['Garnet'],
'Garnet',
False,
False,
[
    ["Garnet''s Universe"]
],
"Garnet''s Universe",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128juhf/respect_garnet_garnets_universe/

########################################

id = get_rt_id(cur, 'Respect Davoth, the Dark Lord (Doom Eternal)', 'https://redd.it/128k1gu')
add_data(['Davoth'],
'Davoth',
False,
True,
[
    ['DOOM']
],
'DOOM',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128k1gu/respect_davoth_the_dark_lord_doom_eternal/

########################################

id = get_rt_id(cur, 'Respect SCP 6959 (SCP Foundation)', 'https://redd.it/128l2z1')
add_data(['SCP ?(-| )? ?6959'],
'SCP-6959',
False,
True,
[
    ['Cirno']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128l2z1/respect_scp_6959_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect Jerri Blank (Strangers with Candy)', 'https://redd.it/128mcr6')
add_data(['Jerri Blank'],
'Jerri Blank',
False,
True,
[
    ['Strangers with Candy']
],
'Strangers with Candy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128mcr6/respect_jerri_blank_strangers_with_candy/

########################################

id = get_rt_id(cur, 'Respect Hammy! (Over The Hedge Newspaper Comic Strip)', 'https://redd.it/128qesj')
add_data(['Hammy'],
'Hammy',
False,
False,
[
    ['Over The Hedge']
],
'Over The Hedge',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qesj/respect_hammy_over_the_hedge_newspaper_comic_strip/

########################################

id = get_rt_id(cur, 'Respect The 17 Trillion Wasps! (The Adventures of 17 Trillion Wasps)', 'https://redd.it/128qh5l')
add_data(['17 Trillion Wasps'],
'17 Trillion Wasps',
False,
True,
[
    ['The Adventures of 17 Trillion Wasps']
],
'The Adventures of 17 Trillion Wasps',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qh5l/respect_the_17_trillion_wasps_the_adventures_of/

########################################

id = get_rt_id(cur, 'Respect Superhand! (Rooster Teeth Animated Adventures)', 'https://redd.it/128qhwp')
add_data(['Superhand'],
'Superhand',
False,
True,
[
    ['Rooster ?Teeth']
],
'Rooster Teeth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qhwp/respect_superhand_rooster_teeth_animated/

########################################

id = get_rt_id(cur, 'Respect Captain Hammer and Weather Woman! (The Backyardigans)', 'https://redd.it/128qjb1')
add_data(['Captain Hammer'],
'Captain Hammer',
False,
False,
[
    ['Backyardigans']
],
'Backyardigans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qjb1/respect_captain_hammer_and_weather_woman_the/

add_data(['Weather Woman'],
'Weather Woman',
False,
False,
[
    ['Backyardigans']
],
'Backyardigans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qjb1/respect_captain_hammer_and_weather_woman_the/

########################################

id = get_rt_id(cur, 'Respect Dr. Shrinky and Yucky Man! (The Backyardigans)', 'https://redd.it/128qk5n')
add_data(['Dr\.? Shrinky'],
'Dr. Shrinky',
False,
True,
[
    ['Backyardigans']
],
'Backyardigans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qjb1/respect_captain_hammer_and_weather_woman_the/

add_data(['Yucky Man'],
'Yucky Man',
False,
False,
[
    ['Backyardigans']
],
'Backyardigans',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128qk5n/respect_dr_shrinky_and_yucky_man_the_backyardigans/

########################################

id = get_rt_id(cur, 'Respect Chumbot! (Spongebob Squarepants)', 'https://redd.it/128qkss')
add_data(['Chumbot'],
'Chumbot',
False,
True,
[
    ['Spongebob']
],
'Spongebob',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Spraymond the Skunk! (Nickelodeon Clickamajigs: Spraymond the Skunk)', 'https://redd.it/128sgdd')
add_data(['Spraymond the Skunk'],
'Spraymond the Skunk',
False,
True,
[
    ['Nickelodeon Clickamajigs']
],
'Nickelodeon Clickamajigs',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128sgdd/respect_spraymond_the_skunk_nickelodeon/

########################################

id = get_rt_id(cur, 'Respect Zote the Mighty, Invincible, Fearless, Sensual, Mysterious, Enchanting, Vigorous, Diligent, Overwhelming, Gorgeous, Passionate, Terrifying, Beautiful, and Powerful (Hollow Knight)', 'https://redd.it/128x8p0')
add_data(['Zote the Mighty'],
'Zote the Mighty',
False,
True,
[
    ['Hollow Knight']
],
'Hollow Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128x8p0/respect_zote_the_mighty_invincible_fearless/

add_data(['Zote'],
'Zote',
False,
False,
[
    ['Hollow Knight']
],
'Hollow Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/128x8p0/respect_zote_the_mighty_invincible_fearless/

########################################

id = get_rt_id(cur, 'Respect Emily (Until Dawn)', 'https://redd.it/12962vl')
add_data(['Emily'],
'Emily',
False,
False,
[
    ['Until Dawn']
],
'Until Dawn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12962vl/respect_emily_until_dawn/

########################################

id = get_rt_id(cur, 'Respect Chuck Liddell (Duralast Commercials)', 'https://redd.it/129fz0z')
add_data(['Chuck Liddell'],
'Chuck Liddell',
False,
False,
[
    ['Duralast'], ['Commercials?']
],
'Duralast Commercials',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Demitri Maximoff (Night Warriors: Darkstalkers'' Revenge) (the anime OVA)", 'https://redd.it/129ib6i')
add_data(['Demitri Maximoff'],
'Demitri Maximoff',
False,
True,
[
    ['Darkstalkers']
],
'Darkstalkers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129ib6i/respect_demitri_maximoff_night_warriors/

########################################

id = get_rt_id(cur, 'Respect Garfield / Garfielf (Fist of the B0rf star)', 'https://redd.it/129iwc1')
add_data(['Garfield'],
'Garfield',
False,
False,
[
    ['Fist of the B0rf star']
],
'Fist of the B0rf star',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129iwc1/respect_garfield_garfielf_fist_of_the_b0rf_star/

add_data(['Garfielf'],
'Garfielf',
False,
False,
[
    ['Fist of the B0rf star']
],
'Fist of the B0rf star',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129iwc1/respect_garfield_garfielf_fist_of_the_b0rf_star/

########################################

id = get_rt_id(cur, 'Respect the Doomed (DC Comics, Post Flashpoint)', 'https://redd.it/129m41h')
add_data(['Doomed'],
'Doomed',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point', 'Reiser']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129m41h/respect_the_doomed_dc_comics_post_flashpoint/

########################################

id = get_rt_id(cur, 'Respect Captain Nemo (The League of Extraordinary Gentlemen) [Movie]', 'https://redd.it/129p92m')
add_data(['Captain Nemo'],
'Captain Nemo',
False,
False,
[
    ['League of Extraordinary Gentlemen']
],
'The League of Extraordinary Gentlemen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129p92m/respect_captain_nemo_the_league_of_extraordinary/

########################################

id = get_rt_id(cur, 'Respect Leatherface! (Mortal Kombat)', 'https://redd.it/129sodu')
add_data(['Leatherface'],
'Leatherface',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/129sodu/respect_leatherface_mortal_kombat/

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

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
            formatted_name_list.append(name.replace('\\', '\\\\'))
            #formatted_name_list.append(name)

    formatted_version_list = []
    for version in version_list:
        version_array_string = '{'
        for regex in version:
            if not is_valid_regex(regex):
                return
            else:
                # Note: Replacing \\ with \\\\ is needed so Postgres can pick up that a \ is supposed to be there
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

update_respectthread(cur, 1596, 'Respect Leonard Snart/Captain Cold (DC Comics, Post Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rbuhcy/respect_leonard_snartcaptain_cold_dc_comics_post/')
update_respectthread(cur, 4597, 'Respect Toriko! (Toriko)', 'https://www.reddit.com/r/respectthreads/comments/1rdbrxh/respect_toriko_toriko/')
update_respectthread(cur, 2276, 'Respect the Shocker! (Marvel Comics, Earth-616)', 'https://www.reddit.com/r/respectthreads/comments/1redzrh/respect_the_shocker_marvel_comics_earth616/')
update_respectthread(cur, 1079, 'Respect Jenny Wakeman/XJ-9 (My Life As A Teenage Robot)', 'https://www.reddit.com/r/respectthreads/comments/1re4jpt/respect_jenny_wakemanxj9_my_life_as_a_teenage/')

########################################

id = get_rt_id(cur, 'Respect Bowser (DEATH BATTLE)', 'https://www.reddit.com/r/respectthreads/comments/1rbt7hb/respect_bowser_death_battle/')
add_data(['Bowser'],
'Bowser',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Team Galactic! (Pokémon Adventures)', 'https://www.reddit.com/r/respectthreads/comments/1rccga3/respect_team_galactic_pok%C3%A9mon_adventures/')
add_data(['Team Galactic'],
'Team Galactic',
True,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cipher (Honkai: Star Rail)', 'https://www.reddit.com/r/respectthreads/comments/1rci9c9/respect_cipher_honkai_star_rail/')
add_data(['Cipher'],
'Cipher',
False,
False,
[
    ['Honkai', 'Star Rail']
],
'Honkai: Star Rail',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/1mxhq9m/the_chrysos_heirs_honkai_star_rail_vs_the_round/

########################################

id = get_rt_id(cur, 'Respect Schmidt and Jenko (21 Jump Street)', 'https://www.reddit.com/r/respectthreads/comments/1rckd58/respect_schmidt_and_jenko_21_jump_street/')
add_data(['Schmidt'],
'Schmidt',
False,
False,
[
    ['(21|22) Jump ?Street']
],
'21 Jump Street',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Jenko'],
'Jenko',
False,
False,
[
    ['(21|22) Jump ?Street']
],
'21 Jump Street',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Schmidt and Jenko'],
'Schmidt and Jenko',
True,
True,
[
    ['(21|22) Jump ?Street']
],
'21 Jump Street',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect The Skeletons! (The Skeleton Dance)', 'https://www.reddit.com/r/respectthreads/comments/1rcmz8a/respect_the_skeletons_the_skeleton_dance/')
add_data(['Skeletons'],
'Skeletons',
False,
False,
[
    ['The Skeleton Dance']
],
'The Skeleton Dance',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kei the Dragon (Belle: The Dragon and the Freckled Princess)', 'https://www.reddit.com/r/respectthreads/comments/1rcolva/respect_kei_the_dragon_belle_the_dragon_and_the/')
add_data(['Kei'],
'Kei',
False,
False,
[
    ['Dragon and the Freckled Princess']
],
'Belle: The Dragon and the Freckled Princess',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Suzu Naito, aka Belle (Belle: The Dragon and the Freckled Princess)', 'https://www.reddit.com/r/respectthreads/comments/1rcor6o/respect_suzu_naito_aka_belle_belle_the_dragon_and/')
add_data(['Belle'],
'Belle',
False,
False,
[
    ['Dragon and the Freckled Princess']
],
'Belle: The Dragon and the Freckled Princess',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Suzu Naito, aka Belle (Belle: The Dragon and the Freckled Princess)', 'https://www.reddit.com/r/respectthreads/comments/1rcor6o/respect_suzu_naito_aka_belle_belle_the_dragon_and/')
add_data(['Belle'],
'Belle',
False,
False,
[
    ['Dragon and the Freckled Princess']
],
'Belle: The Dragon and the Freckled Princess',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Ghouls! (World of Darkness)', 'https://www.reddit.com/r/respectthreads/comments/1rcrn82/respect_the_ghouls_world_of_darkness/')
add_data(['Ghouls'],
'Ghouls',
False,
False,
[
    ['World of Darkness']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Unnamed Chaos Insurgency Soldier in the SCP Tale Power', 'https://www.reddit.com/r/respectthreads/comments/1rcudan/respect_the_unnamed_chaos_insurgency_soldier_in/')
add_data(['Chaos Insurgency Soldier'],
'Chaos Insurgency Soldier',
False,
False,
[
    ['Power', 'SCP']
],
'SCP Power',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect David Speed (Super Fuzz)', 'https://www.reddit.com/r/respectthreads/comments/1rcv4a6/respect_david_speed_super_fuzz/')
add_data(['David Speed'],
'David Speed',
False,
False,
[
    ['Super Fuzz']
],
'Super Fuzz',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lee and Carter (Rush Hour)', 'https://www.reddit.com/r/respectthreads/comments/1rdgmd8/respect_lee_and_carter_rush_hour/')
add_data(['(Inspector )?Lee (and|&) (Detective )?Carter|(Detective )?Carter (and|&) (Inspector )?Lee'],
'Lee and Carter',
True,
False,
[
    ['Rush Hour']
],
'Rush Hour',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lee'],
'Lee',
False,
False,
[
    ['Lee.*Rush Hour'], ['Lee.*Jackie Chan']
],
'Rush Hour',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Carter'],
'Carter',
False,
False,
[
    ['Carter.*Rush Hour']
],
'Rush Hour',
'{' + '{}'.format(id) + '}'
)
#

#https://www.reddit.com/r/whowouldwin/comments/haeusj/bad_boys_vs_rush_hour/
#https://www.reddit.com/r/whowouldwin/comments/opjoph/wayne_from_letterkenny_vs_detective_inspector_lee/
#https://www.reddit.com/r/whowouldwin/comments/1heqe0v/lee_carter_rush_hour_vs_mike_marcus_bad_boys/
#https://www.reddit.com/r/whowouldwin/comments/1pr3dyy/agents_k_and_j_vs_mike_lowrey_and_marcus_burnett/
#https://www.reddit.com/r/whowouldwin/comments/1qtu8rs/could_any_of_these_cops_succeed_in_the_speed/
#https://www.reddit.com/r/whowouldwin/comments/oglsvd/lee_and_carter_rush_hour_vs_john_wick/
#https://www.reddit.com/r/whowouldwin/comments/cd4t13/john_wick_carter_and_lee_rush_hour_movies_vs_rama/
#https://www.reddit.com/r/whowouldwin/comments/50qbu6/gotham_gets_a_new_squad_of_elite_police_officers/
#https://www.reddit.com/r/whowouldwin/comments/1kzl8cu/detective_lees_dad_or_agent_carters_dad_rush_hour/
#https://www.reddit.com/r/whowouldwin/comments/tzeg99/leerush_hour_vs_4six_underground/
#https://www.reddit.com/r/whowouldwin/comments/kq892v/martin_riggs_lethal_weapon_vs_axel_foley_beverly/

########################################

id = get_rt_id(cur, 'Respect Tango and Cash (Tango and Cash)', 'https://www.reddit.com/r/respectthreads/comments/1rdpmwa/respect_tango_and_cash_tango_and_cash/')
add_data(['Tango (&|and) Cash'],
'Tango & Cash',
True,
True,
[
    ['Tango (&|and) Cash ?\(Tango & Cash\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Ray(mond)? Tango'],
'Ray Tango',
False,
False,
[
    ['Cash']
],
'Tango & Cash',
'{' + '{}'.format(id) + '}'
)
#


add_data(['Ga(br|rb)iel Cash'],
'Gabriel Cash',
False,
False,
[
    ['Tango']
],
'Tango & Cash',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Agent K! (Men in Black)', 'https://www.reddit.com/r/respectthreads/comments/1rdpv67/respect_agent_k_men_in_black/')
add_data(['Agent K'],
'Agent K',
False,
False,
[
    ['Men in Black']
],
'Men in Black',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Agent K'],
'Agent K',
False,
False,
[
    ['Men in Black'], ['MIB']
],
'Men in Black',
'{' + '{}'.format(id) + '}'
)
#

add_data(['K'],
'K',
False,
False,
[
    ['Men in Black'], ['MIB', 'J']
],
'Men in Black',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Long John Silver! (Treasure Planet)', 'https://www.reddit.com/r/respectthreads/comments/1rdswwv/respect_long_john_silver_treasure_planet/')
add_data(['John Silver'],
'John Silver',
False,
False,
[
    ['Treasure Planet']
],
'Treasure Planet',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Frederick von Frankenstein/Riot (DC Comics, Post Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1rdw87j/respect_frederick_von_frankensteinriot_dc_comics/')
add_data(['Frederick von Frankenstein'],
'Frederick von Frankenstein',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Frederick von Frankenstein'],
'Frederick von Frankenstein',
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

id = get_rt_id(cur, 'Respect Zatanna (DC Comics, Absolute Universe)', 'https://www.reddit.com/r/respectthreads/comments/1remwof/respect_zatanna_dc_comics_absolute_universe/')
add_data(['Zatanna'],
'Zatanna',
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

id = get_rt_id(cur, 'Respect Giganta (DC Comics, Absolute Universe)', 'https://www.reddit.com/r/respectthreads/comments/1remxgu/respect_giganta_dc_comics_absolute_universe/')
add_data(['Giganta'],
'Giganta',
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

id = get_rt_id(cur, 'Respect Sherlock Holmes (Sherlock Holmes in the 22nd Century)', 'https://www.reddit.com/r/respectthreads/comments/1re9gr2/respect_sherlock_holmes_sherlock_holmes_in_the/')
add_data(['Sherlock'],
'Sherlock Holmes',
False,
False,
[
    ['Sherlock Holmes in the 22nd Century']
],
'Sherlock Holmes in the 22nd Century',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Watson (Sherlock Holmes in the 22nd Century)', 'https://www.reddit.com/r/respectthreads/comments/1re9guz/respect_watson_sherlock_holmes_in_the_22nd_century/')
add_data(['Watson'],
'Watson',
False,
False,
[
    ['Sherlock Holmes in the 22nd Century']
],
'Sherlock Holmes in the 22nd Century',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Echo Leader (Rainbow 6: Patriots)', 'https://www.reddit.com/r/respectthreads/comments/1recunu/respect_echo_leader_rainbow_6_patriots/')
add_data(['Echo Leader'],
'Echo Leader',
False,
False,
[
    ['Rainbow 6:? Patriots']
],
'Rainbow 6: Patriots',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect the ED-209 (Robocop)', 'https://www.reddit.com/r/respectthreads/comments/1ref5mj/respect_the_ed209_robocop/')
add_data(['ED(-| )?209'],
'ED-209',
False,
False,
[
    ['RoboCop']
],
'RoboCop',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The ED-209 (Robocop Rogue City)', 'https://www.reddit.com/r/respectthreads/comments/1ref4po/respect_the_ed209_robocop_rogue_city/')
add_data(['ED(-| )?209'],
'ED-209',
False,
False,
[
    ['Rogue City']
],
'RoboCop: Rogue City',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Sunstreaker (Transformers, IDW Comics [2005])', 'https://www.reddit.com/r/respectthreads/comments/1reefvw/respect_sunstreaker_transformers_idw_comics_2005/')
add_data(['Sunstreaker'],
'Sunstreaker',
False,
False,
[
    ['Transformers', 'IDW']
],
'Transformers IDW',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nathan Drake (UNCHARTED - Live Action Fan Film)', 'https://www.reddit.com/r/respectthreads/comments/1reftwt/respect_nathan_drake_uncharted_live_action_fan/')
add_data(['Nathan Drake'],
'Nathan Drake',
False,
False,
[
    ['Uncharted', 'Fan Film']
],
'Uncharted Fan Film',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alex DeLarge (A Clockwork Orange)', 'https://www.reddit.com/r/respectthreads/comments/1reftyy/respect_alex_delarge_a_clockwork_orange/')
add_data(['Alex DeLarge'],
'Alex DeLarge',
False,
True,
[
    ['Clockwork Orange']
],
'A Clockwork Orange',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Alex'],
'Alex',
False,
False,
[
    ['Clockwork Orange']
],
'A Clockwork Orange',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cohen the Barbarian (Discworld)', 'https://www.reddit.com/r/respectthreads/comments/1relepk/respect_cohen_the_barbarian_discworld/')
add_data(['Cohen the Barbarian'],
'Cohen the Barbarian',
False,
True,
[
    ['Disc ?world']
],
'Discworld',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Cohen'],
'Cohen',
False,
False,
[
    ['Disc ?world']
],
'Discworld',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Omar little (The wire)', 'https://www.reddit.com/r/respectthreads/comments/1rf2rwa/respect_omar_little_the_wire/')
add_data(['Omar little'],
'Omar little',
False,
False,
[
    ['The wire']
],
'The wire',
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

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
update_respectthread(cur, 5766, 'Respect Butler (Artemis Fowl)', 'https://www.reddit.com/r/respectthreads/comments/1rg6ohq/respect_butler_artemis_fowl/')
update_respectthread(cur, 20535, 'Respect Hal Jordan! (Green Lantern (2011))', 'https://www.reddit.com/r/respectthreads/comments/1rgc0g1/respect_hal_jordan_green_lantern_2011/')
update_respectthread(cur, 364, 'Respect Shin Hayata and Ultraman (Ultraman)', 'https://www.reddit.com/r/respectthreads/comments/1rgz5aj/respect_shin_hayata_and_ultraman_ultraman/')
update_respectthread(cur, 5355, 'Respect Joker (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr06n/respect_joker_persona_5/')
update_respectthread(cur, 5358, 'Respect Ryuji Sakamoto (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr1ca/respect_ryuji_sakamoto_persona_5/')
update_respectthread(cur, 5354, 'Respect Goro Akechi (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr1sw/respect_goro_akechi_persona_5/')
update_respectthread(cur, 5353, 'Respect Ann Takamaki (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr39f/respect_ann_takamaki_persona_5/')
update_respectthread(cur, 5359, 'Respect Yusuke Kitagawa (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr6t6/respect_yusuke_kitagawa_persona_5/')
update_respectthread(cur, 5357, 'Respect Morgana (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr7jj/respect_morgana_persona_5/')
update_respectthread(cur, 11133, 'Respect Kasumi Yoshizawa (Persona 5 Royal)', 'https://www.reddit.com/r/respectthreads/comments/1rhr9m2/respect_kasumi_yoshizawa_persona_5_royal/')
update_respectthread(cur, 5356, 'Respect Makoto Niijima (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhrb8e/respect_makoto_niijima_persona_5/')
update_respectthread(cur, 14895, 'Respect Haru Okumura (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhrk61/respect_haru_okumura_persona_5/')

########################################

id = get_rt_id(cur, 'Respect Futaba Sakura (Persona 5)', 'https://www.reddit.com/r/respectthreads/comments/1rhr0sn/respect_futaba_sakura_persona_5/')
add_data(['Futaba Sakura'],
'Futaba Sakura',
False,
True,
[
    ['Persona']
],
'Persona',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Futaba'],
'Futaba',
False,
False,
[
    ['Persona']
],
'Persona',
'{' + '{}'.format(id) + '}'
)
#

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

id = get_rt_id(cur, 'Respect Inspector Beth Lestrade (Sherlock Holmes in the 22nd Century)', 'https://www.reddit.com/r/respectthreads/comments/1rgast4/respect_inspector_beth_lestrade_sherlock_holmes/')
add_data(['Beth Lestrade'],
'Beth Lestrade',
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

id = get_rt_id(cur, 'Respect Ultra Magnus (Transformers, IDW Comics [2005])', 'https://www.reddit.com/r/respectthreads/comments/1rhkwyo/respect_ultra_magnus_transformers_idw_comics_2005/')
add_data(['Ultra Magnus'],
'Ultra Magnus',
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

id = get_rt_id(cur, 'Respect Bruce Wayne, Bat-Man (Batman: Gotham by Gaslight, Earth 19)', 'https://www.reddit.com/r/respectthreads/comments/1rf9xp0/respect_bruce_wayne_batman_batman_gotham_by/')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Gotham by Gaslight']
],
'Gotham by Gaslight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Brian Savage, the Scalphunter (DC Comics, Pre-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rfdcs0/respect_brian_savage_the_scalphunter_dc_comics/')
add_data(['Scalphunter'],
'Scalphunter',
False,
False,
[
    ['Pre(-| )?Flashpoint']
],
'Pre-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Scalphunter'],
'Scalphunter',
False,
False,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Larfleeze, the Orange Lantern (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rh1d5f/respect_larfleeze_the_orange_lantern_dc_comics/')
add_data(['Larfleeze'],
'Larfleeze',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Joe Chill (DC Comics)', 'https://www.reddit.com/r/respectthreads/comments/1rfr4q5/respect_joe_chill_dc_comics/')
add_data(['Joe Chill'],
'Joe Chill',
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

id = get_rt_id(cur, "Respect Batman! (DC''s Tomorrowverse)", 'https://www.reddit.com/r/respectthreads/comments/1rfl69l/respect_batman_dcs_tomorrowverse/')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Tomorrowverse']
],
'Tomorrowverse',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Batman! (DC Animated Movie Universe)', 'https://www.reddit.com/r/respectthreads/comments/1rfl3zm/respect_batman_dc_animated_movie_universe/')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['DC Animated (Film|Movie) Universe'], ['DCA(F|M)U'], ['DC Animated Movies?']
],
'DC Animated Movie Universe',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nicholas Scratch! (Marvel, 616)', 'https://www.reddit.com/r/respectthreads/comments/1rffmcv/respect_nicholas_scratch_marvel_616/')
add_data(['Nicholas Scratch'],
'Nicholas Scratch',
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

id = get_rt_id(cur, 'Respect The Crimson Paw! (The Bad Guys)', 'https://www.reddit.com/r/respectthreads/comments/1rff6xl/respect_the_crimson_paw_the_bad_guys/')
add_data(['Crimson Paw'],
'Crimson Paw',
False,
False,
[
    ['Bad Guys']
],
'The Bad Guys',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Alicia Varney (World of Darkness)', 'https://www.reddit.com/r/respectthreads/comments/1rfuelg/respect_alicia_varney_world_of_darkness/')
add_data(['Alicia Varney'],
'Alicia Varney',
False,
False,
[
    ['World of Darkness'], ['WOD']
],
'World of Darkness',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Artemis Fowl! (Artemis Fowl)', 'https://www.reddit.com/r/respectthreads/comments/1rg20i1/respect_artemis_fowl_artemis_fowl/')
add_data(['Artemis Fowl'],
'Artemis Fowl',
False,
True,
[
    ['Artemis Fowl ?\(Artemis Fowl\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Giovanni (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rhn8zh/respect_giovanni_pokemon_anime/')
add_data(['Giovanni'],
'Giovanni',
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

id = get_rt_id(cur, 'Respect Cilan (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rg5jq5/respect_cilan_pokemon_anime/')
add_data(['Artemis Cilan'],
'Cilan',
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

id = get_rt_id(cur, "Respect Cilan''s Pansage (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rg5jqk/respect_cilans_pansage_pokemon_anime/')
add_data(['Pansage'],
'Pansage',
False,
False,
[
    ['Cilan']
],
'Cilan',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Cilan''s Crustle (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rg5jrw/respect_cilans_crustle_pokemon_anime/')
add_data(['Crustle'],
'Crustle',
False,
False,
[
    ['Cilan']
],
'Cilan',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Dwebble'],
'Dwebble',
False,
False,
[
    ['Cilan']
],
'Cilan',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, "Respect Cilan''s Stunfisk (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rg5jsk/respect_cilans_stunfisk_pokemon_anime/')
add_data(['Stunfisk'],
'Stunfisk',
False,
False,
[
    ['Cilan']
],
'Cilan',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Quagsire (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rg6b1w/respect_quagsire_pokemon_anime/')
add_data(['Quagsire'],
'Quagsire',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Wooper'],
'Wooper',
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

id = get_rt_id(cur, 'Respect John Spartan (Demolition Man)', 'https://www.reddit.com/r/respectthreads/comments/1rg690d/respect_john_spartan_demolition_man/')
add_data(['John Spartan'],
'John Spartan',
False,
False,
[
    ['Demolition Man']
],
'Demolition Man',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Corlis Rath (Star Wars, Canon)', 'https://www.reddit.com/r/respectthreads/comments/1rgau2e/respect_corlis_rath_star_wars_canon/')
add_data(['Corlis Rath'],
'Corlis Rath',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Unnamed Beasts (Flight)', 'https://www.reddit.com/r/respectthreads/comments/1rggogz/respect_the_unnamed_beasts_flight/')
add_data(['Unnamed Beasts'],
'Unnamed Beasts',
False,
False,
[
    ['Flight']
],
'Flight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Shaun Riley (IDW Shaun Of The Dead)', 'https://www.reddit.com/r/respectthreads/comments/1rggv7q/respect_shaun_riley_idw_shaun_of_the_dead/')
add_data(['Shaun'],
'Shaun',
False,
False,
[
    ['Shaun Of The Dead', 'IDW']
],
'IDW Shaun Of The Dead',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Smiling Dead! (The Gaslight District)', 'https://www.reddit.com/r/respectthreads/comments/1rgtq9x/respect_the_smiling_dead_the_gaslight_district/')
add_data(['Smiling Dead'],
'Smiling Dead',
True,
False,
[
    ['Gaslight District']
],
'The Gaslight District',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cain, Robocop 2 (Robocop 2)', 'https://www.reddit.com/r/respectthreads/comments/1rh37h5/respect_cain_robocop_2_robocop_2/')
add_data(['Cain'],
'Cain',
False,
False,
[
    ['RoboCop 2'], ['Cain.*RoboCop']
],
'RoboCop',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Robo(-| )?Cain'],
'Robo Cain',
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

id = get_rt_id(cur, 'Respect The Old Man, Robocop 2 (Robocop Rogue City)', 'https://www.reddit.com/r/respectthreads/comments/1rh520c/respect_the_old_man_robocop_2_robocop_rogue_city/')
add_data(['Old Man'],
'Old Man',
False,
False,
[
    ['RoboCop', 'Rogue City']
],
'RoboCop: Rogue City',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Joker (Character Scramble Season 19)', 'https://www.reddit.com/r/respectthreads/comments/1rh3haa/respect_joker_character_scramble_season_19/')
add_data(['Joker'],
'Joker',
False,
False,
[
    ['Character Scramble']
],
'Character Scramble',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Francine Nebulon (Lloyd in Space)', 'https://www.reddit.com/r/respectthreads/comments/1rh563t/respect_francine_nebulon_lloyd_in_space/')
add_data(['Francine Nebulon'],
'Francine Nebulon',
False,
True,
[
    ['Lloyd in Space']
],
'Lloyd in Space',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ben Richards (The Running Man) [1987]', 'https://www.reddit.com/r/respectthreads/comments/1rh669f/respect_ben_richards_the_running_man_1987/')
add_data(['Ben Richards'],
'Ben Richards',
False,
False,
[
    ['Running Man', '1987']
],
'The Running Man, 1987',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Mike and Marcus (Bad Boys)', 'https://www.reddit.com/r/respectthreads/comments/1rh6kg1/respect_mike_and_marcus_bad_boys/')
add_data(['Mike (and|&) Marcus|Marcus (and|&) Mike'],
'Mike and Marcus',
True,
False,
[
    ['Bad Boys']
],
'Bad Boys',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Mike Lowrey'],
'Mike Lowrey',
False,
False,
[
    ['Bad Boys']
],
'Bad Boys',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Marcus Burnett'],
'Marcus Burnett',
False,
False,
[
    ['Bad Boys']
],
'Bad Boys',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Suzie Dickson and Jon Johnson (Sex Criminals)', 'https://www.reddit.com/r/respectthreads/comments/1rhi0yu/respect_suzie_dickson_and_jon_johnson_sex/')
add_data(['Suzie Dickson'],
'Suzie Dickson',
False,
False,
[
    ['Sex Criminals']
],
'Sex Criminals',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Jon Johnson'],
'Jon Johnson',
False,
False,
[
    ['Sex Criminals']
],
'Sex Criminals',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Bosko (Looney Tunes)', 'https://www.reddit.com/r/respectthreads/comments/1rh927t/respect_bosko_looney_tunes/')
add_data(['Bosko'],
'Bosko',
False,
False,
[
    ['Looney Tunes']
],
'Looney Tunes',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Wonderland! (Alice''s Adventures in Wonderland)", 'https://www.reddit.com/r/respectthreads/comments/1rhib4x/respect_wonderland_alices_adventures_in_wonderland/')
add_data(['Wonderland'],
'Wonderland',
True,
False,
[
    ["Alice", 'Red Queen']
],
"Alice''s Adventures in Wonderland",
'{' + '{}'.format(id) + '}'
)
#

add_data(['Cheshire Cat'],
'Cheshire Cat',
False,
False,
[
    ['Wonderland']
],
"Alice''s Adventures in Wonderland",
'{' + '{}'.format(id) + '}'
)
#


add_data(['Alice'],
'Alice',
False,
False,
[
    ['Alice ?\((Alice in )?Wonderland\)']
],
"Alice''s Adventures in Wonderland",
'{' + '{}'.format(id) + '}'
)
#


add_data(['Queen of Hearts'],
'Queen of Hearts',
False,
False,
[
    ['Wonderland']
],
"Alice''s Adventures in Wonderland",
'{' + '{}'.format(id) + '}'
)
#

#https://www.reddit.com/r/whowouldwin/comments/1bawe58/dorothy_oz_vs_alice_wonderland/
#https://www.reddit.com/r/whowouldwin/comments/10z42bz/chaos_king_deltarune_vs_queen_of_hearts_alice_in/
#https://www.reddit.com/r/whowouldwin/comments/1hh6bxu/oz_narnia_terabithia_wonderland_whoville_and/

########################################

id = get_rt_id(cur, 'Respect Diamondback (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/1rhmb9h/respect_diamondback_marvel_cinematic_universe/')
add_data(['Diamondback'],
'Diamondback',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Akemura Soga (Kagurabachi)', 'https://www.reddit.com/r/respectthreads/comments/1rhnbf1/respect_akemura_soga_kagurabachi/')
add_data(['Akemura Soga'],
'Akemura Soga',
False,
True,
[
    ['Kagurabachi']
],
'Kagurabachi',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Seiichi Samura (Kagurabachi)', 'https://www.reddit.com/r/respectthreads/comments/1rhupn6/respect_seiichi_samura_kagurabachi/')
add_data(['Seiichi Samura'],
'Seiichi Samura',
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

id = get_rt_id(cur, "Respect Sherlock Holmes (Frogware''s Sherlock Holmes)", 'https://www.reddit.com/r/respectthreads/comments/1rhrkgj/respect_sherlock_holmes_frogwares_sherlock_holmes/')
add_data(['Sherlock'],
'Sherlock Holmes',
False,
False,
[
    ['Frogware']
],
'Frogware',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Bulk and Skull (Power Rangers)', 'https://www.reddit.com/r/respectthreads/comments/1rhrkyw/respect_bulk_and_skull_power_rangers/')
add_data(['Bulk and Skull'],
'Bulk and Skull',
True,
False,
[
    ['Power ?Rangers?'], ['MMPR']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect The Trunk Monkey (Advertisements)', 'https://www.reddit.com/r/respectthreads/comments/1rhry2v/respect_the_trunk_monkey_advertisements/')
add_data(['Trunk Monkey'],
'Trunk Monkey',
False,
False,
[
    ['Ad(vertisement)?s']
],
'Advertisements',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Grand Fisher (Bleach)', 'https://www.reddit.com/r/respectthreads/comments/1rhubsf/respect_grand_fisher_bleach/')
add_data(['Grand Fisher'],
'Grand Fisher',
False,
False,
[
    ['Bleach']
],
'Bleach',
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

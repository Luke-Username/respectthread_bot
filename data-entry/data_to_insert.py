"""
# This script is used to enter new characters into the database when a respect thread is written of them.
# New respect threads are found at this link: https://www.reddit.com/r/respectthreads/new/
# An example of how to enter a new character is as follows.

id = get_rt_id(cur, "Respect Sully (Monsters, Inc.)", "https://redd.it/d2kwip")
add_data(["Sully"],
"Sully",
False,
False,
[
'{"Monsters,? Inc"}'
],
"Monsters, Inc.",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/d2kwip/respect_sully_monsters_inc/

# The following function call is an example of how to update the database when a respect thread is reposted.
# Refer to the CSV of respect threads to find the correct ID.
# Take the title and URL from the post itself.
update_respectthread(cur, 1189, "Respect Beowulf (2007 Film)", "https://redd.it/dspz5z")
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
full_version_names = []
rt_id_arrays = []
num_chars = []

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

def add_data(name_list, default_name, is_team, is_default, version_list, full_version_name, rt_id_array):
    # Check if the names are valid regular expressions
    for name in name_list:    
        try:
            re.compile(name)
        except re.error:
            print("WARNING: {} is not a valid regular expression!".format(name))
            return

    name_lists.append(name_list)
    default_names.append(default_name)
    is_team_list.append(is_team)
    is_default_list.append(is_default)
    version_lists.append(version_list)
    full_version_names.append(full_version_name)
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

update_respectthread(cur, 2014, "Respect Franklin Hall, Graviton (Marvel, Earth-616)", "https://redd.it/ou5af2")
update_respectthread(cur, 1970, "Respect the Destroyer [Asgardian] (Marvel, Earth-616)", "https://redd.it/ou5ahm")
update_respectthread(cur, 15420, "Respect Gwen Stacy, Ghost-Spider, Gwenom (Marvel, Earth-65)", "https://redd.it/ou5mts")
update_respectthread(cur, 13154, "Respect Quetzalcoatl, the Winged Serpent! (Fate)", "https://redd.it/ou98ye")
update_respectthread(cur, 690, "Respect Prisoner 775/Chamalien (Ben 10)", "https://redd.it/ouk5bp")
update_respectthread(cur, 3371, "Respect Tian Kui (Feng Shen Ji)", "https://redd.it/oyimnk")
update_respectthread(cur, 2537, "Respect Ultimate Reed Richards, The Maker (Marvel, 1610)", "https://redd.it/p0sybs")
update_respectthread(cur, 1374, "Respect Goffu (Cartoon Hooligans)", "https://redd.it/p17560")
update_respectthread(cur, 14812, "Respect Altera, the Scourge of God! (Fate)", "https://redd.it/p1eyzr")
update_respectthread(cur, 233, "Respect the Avengers (Marvel Cinematic Universe)", "https://redd.it/p3px68")
update_respectthread(cur, 674, "Respect Blitzwolfer (Ben 10)", "https://redd.it/p4ulvi")
update_respectthread(cur, 13140, "Respect Harley Quinn (DC Extended Universe)", "https://redd.it/pbbmtk")
update_respectthread(cur, 5487, "Respect Heihachi Mishima (Tekken)", "https://redd.it/pdeswd")
update_respectthread(cur, 679, "Respect Ditto (Ben 10 Classic)", "https://redd.it/pdwjmz")
update_respectthread(cur, 5683, 'Respect Razputin "Raz" Aquato! (Psychonauts)', "https://redd.it/pdzd3p")
update_respectthread(cur, 5613, "Respect Jacket! (Hotline Miami)", "https://redd.it/pdzjg9")
update_respectthread(cur, 3933, "Respect Shota Aizawa, Eraser Head! (My Hero Academia)", "https://redd.it/pecp0f")
update_respectthread(cur, 669, "Respect Alien X! (Ben 10 Classic)", "https://redd.it/pfvdrd")

########################################

add_data(["Gwenom"],
"Gwenom",
False,
True,
[
'{"65"}'
],
"65",
'{15420}'
)
#https://www.reddit.com/r/respectthreads/comments/ou5mts/respect_gwen_stacy_ghostspider_gwenom_marvel/

add_data(["Ghost(-| )?Spider"],
"Ghost-Spider",
False,
True,
[
'{"65"}'
],
"65",
'{15420}'
)
#https://www.reddit.com/r/respectthreads/comments/ou5mts/respect_gwen_stacy_ghostspider_gwenom_marvel/

########################################

id = get_rt_id(cur, "Respect Captain Carter (Marvel Cinematic Universe: What If...?)", "https://redd.it/p3gume")
add_data(["Captain Carter"],
"Captain Carter",
False,
True,
[
'{"Marvel Cinematic Universe"}', '{"MCU"}', '{"What if"}'
],
"MCU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3gume/respect_captain_carter_marvel_cinematic_universe/

########################################

id = get_rt_id(cur, "Respect Steve Rogers, the Hydra Stomper (Marvel Cinematic Universe, What If?)", "https://redd.it/p31sm8")
add_data(["Hydra Stomper"],
"Hydra Stomper",
False,
True,
[
'{"Marvel Cinematic Universe"}', '{"MCU"}', '{"What if"}'
],
"MCU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p31sm8/respect_steve_rogers_the_hydra_stomper_marvel/

########################################

id = get_rt_id(cur, "Respect Redwing! (Marvel 616)", "https://redd.it/pe6qb4")
add_data(["Redwing"],
"Redwing",
False,
False,
[
r'{"Redwing ?\\(Marvel"}', '{"616"}', '{"Krypto"}'
],
"616",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pe6qb4/respect_redwing_marvel_616/

########################################

id = get_rt_id(cur, "Respect Bill Foster [Goliath/Black Goliath/Giant-Man] (Marvel, Earth-616)", "https://redd.it/pcz4oe")
add_data(["Bill Foster"],
"Bill Foster",
False,
False,
[
'{"Marvel"}', '{"616"}', '{"Goliath"}', '{"Giant(-| )?Man"}'
],
"616",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pcz4oe/respect_bill_foster_goliathblack_goliathgiantman/

add_data(["Black Goliath"],
"Black Goliath",
False,
False,
[
'{"Marvel"}', '{"616"}', '{"Bill Foster"}'
],
"616",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pcz4oe/respect_bill_foster_goliathblack_goliathgiantman/

########################################

id = get_rt_id(cur, "Respect Combo Man (Marvel, 616)", "https://redd.it/ouminh")
add_data(["Combo Man"],
"Combo Man",
False,
True,
[
'{"Marvel"}', '{"616"}'
],
"616",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ouminh/respect_combo_man_marvel_616/

########################################

id = get_rt_id(cur, "Respect BB! (Fate)", "https://redd.it/pf890d")
add_data(["BB"],
"BB",
False,
False,
[
'{"Fate"}',
'{"CCC"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf890d/respect_bb_fate/

########################################

id = get_rt_id(cur, "Respect Charlemagne, the Wandering Knight! (Fate/EXTELLA LINK)", "https://redd.it/p4mg1s")
add_data(["Charlemagne"],
"Charlemagne",
False,
False,
[
'{"Fate"}',
'{"EXTELLA LINK"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4mg1s/respect_charlemagne_the_wandering_knight/

########################################

id = get_rt_id(cur, "Respect Thomas Edison! (Fate)", "https://redd.it/p4c5bg")
add_data(["Thomas Edison"],
"Thomas Edison",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4c5bg/respect_thomas_edison_fate/

########################################

id = get_rt_id(cur, "Respect Fionn mac Cumhaill! (Fate)", "https://redd.it/p3ajx2")
add_data(["Fionn mac Cumhaill"],
"Fionn mac Cumhaill",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3ajx2/respect_fionn_mac_cumhaill_fate/

########################################

id = get_rt_id(cur, "Respect Nikola Tesla! (Fate)", "https://redd.it/p1s3ii")
add_data(["Nikola Tesla"],
"Nikola Tesla",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p1s3ii/respect_nikola_tesla_fate/

########################################

id = get_rt_id(cur, "Respect James Moriarty, the Napoleon of Crime! (Fate)", "https://redd.it/owvu8x")
add_data(["Moriarty"],
"Moriarty",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/owvu8x/respect_james_moriarty_the_napoleon_of_crime_fate/

########################################

id = get_rt_id(cur, "Respect Waver Velvet/Lord El-Melloi II! (Fate)", "https://redd.it/ovk3fd")
add_data(["Waver Velvet"],
"Waver Velvet",
False,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovk3fd/respect_waver_velvetlord_elmelloi_ii_fate/

########################################

id = get_rt_id(cur, "Respect Gray, the Gravekeeper! (Fate)", "https://redd.it/ouybqj")
add_data(["Gr(a|e)y"],
"Gray",
False,
False,
[
r'{"Gr(e|a)y ?\\(Fate"}',
r'{"Gr(e|a)y ?\\(F/?GO"}',
'{"gravekeeper"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ouybqj/respect_gray_the_gravekeeper_fate/

########################################

id = get_rt_id(cur, "Respect Ishtar, Queen of the Heavens! (Fate)", "https://redd.it/oubxkr")
add_data(["Ishtar"],
"Ishtar",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oubxkr/respect_ishtar_queen_of_the_heavens_fate/

########################################

id = get_rt_id(cur, "Respect Hessian Lobo, the Avenger of Shinjuku! (Fate)", "https://redd.it/oucwpc")
add_data(["Hessian Lobo"],
"Hessian Lobo",
False,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oucwpc/respect_hessian_lobo_the_avenger_of_shinjuku_fate/


########################################

id = get_rt_id(cur, "Respect Saint Martha, the Dragonslayer! (Fate)", "https://redd.it/ouenpd")
add_data([r"S(ain)?t\\.? Martha"],
"Saint Martha",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}',
'{"Servents?"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ouenpd/respect_saint_martha_the_dragonslayer_fate/

########################################

id = get_rt_id(cur, "Respect Titan (Invincible)", "https://redd.it/ouebxj")
add_data(["Titan"],
"Titan",
False,
False,
[
r'{"Titan ?\\(Invincible"}'
],
"Invincible",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ouebxj/respect_titan_invincible/

########################################

id = get_rt_id(cur, "Respect Gwen Tennyson (Ben 10 Classic)", "https://redd.it/pf6tp6")
add_data(["Gwen"],
"Gwen",
False,
False,
[
'{"Ben|Kevin"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf6tp6/respect_gwen_tennyson_ben_10_classic/

add_data(["Gwen Tennyson"],
"Gwen Tennyson",
False,
True,
[
'{"Ben|Kevin"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf6tp6/respect_gwen_tennyson_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Upchuck! (Ben 10 Classic)", "https://redd.it/petm2l")
add_data(["Upchuck"],
"Upchuck",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/petm2l/respect_upchuck_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Jetray! (Ben 10 Classic)", "https://redd.it/peliub")
add_data(["Jetray"],
"Jetray",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/peliub/respect_jetray_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Chromastone! (Ben 10 Classic)", "https://redd.it/pdapts")
add_data(["Chromastone"],
"Chromastone",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdapts/respect_chromastone_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Spidermonkey! (Ben 10 Classic)", "https://redd.it/pdw706")
add_data(["Spider(-| )?monkey"],
"Spidermonkey",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdw706/respect_spidermonkey_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Swampfire! (Ben 10 Classic)", "https://redd.it/pculwd")
add_data(["Swamp ?fire"],
"Swampfire",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pculwd/respect_swampfire_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Water Hazard (Ben 10 Classic)", "https://redd.it/pdbsx2")
add_data(["Water Hazard"],
"Water Hazard",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdbsx2/respect_water_hazard_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Kevin Levin! (Ben 10 Classic)", "https://redd.it/pdejw6")
add_data(["Kevin"],
"Kevin",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}', '{"Levin"}', '{"Ultimate Kevin"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdejw6/respect_kevin_levin_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Lodestar (Ben 10 Classic)", "https://redd.it/p3nk1j")
add_data(["Lodestar"],
"Lodestar",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3nk1j/respect_lodestar_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Goop! (Ben 10 Classic)", "https://redd.it/pd15vt")
add_data(["Goop"],
"Goop",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pd15vt/respect_goop_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect George Washington (Ben 10)", "https://redd.it/oxshmq")
add_data(["George Washington"],
"George Washington",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oxshmq/respect_george_washington_ben_10/

########################################

id = get_rt_id(cur, "Respect Feedback (Ben 10)", "https://redd.it/p1q3hu")
add_data(["Feedback"],
"Feedback",
False,
False,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p1q3hu/respect_feedback_ben_10/

########################################

id = get_rt_id(cur, "Respect Aggregor! (Ben 10)", "https://redd.it/owpl0t")
add_data(["Aggregor"],
"Aggregor",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/owpl0t/respect_aggregor_ben_10/

########################################

id = get_rt_id(cur, "Respect Terraspin (Ben 10)", "https://redd.it/owjw9j")
add_data(["Terraspin"],
"Terraspin",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/owjw9j/respect_terraspin_ben_10/

########################################

id = get_rt_id(cur, "Respect Crashhopper (Ben 10)", "https://redd.it/ovszhz")
add_data(["Crashhopper"],
"Crashhopper",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#

########################################

id = get_rt_id(cur, "Respect Armodrillo! (Ben 10)", "https://redd.it/ovh7go")
add_data(["Armodrillo"],
"Armodrillo",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovh7go/respect_armodrillo_ben_10/

########################################

id = get_rt_id(cur, "Respect Ampfibian! (Ben 10)", "https://redd.it/ov9ci2")
add_data(["Ampfibian"],
"Ampfibian",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ov9ci2/respect_ampfibian_ben_10/

########################################

id = get_rt_id(cur, "Respect Gravattack (Ben 10)", "https://redd.it/ov67g0")
add_data(["Gravattack"],
"Gravattack",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ov67g0/respect_gravattack_ben_10/

########################################

id = get_rt_id(cur, "Respect Eatle (Ben 10)", "https://redd.it/ouj74n")
add_data(["Eatle"],
"Eatle",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ouj74n/respect_eatle_ben_10/

########################################

id = get_rt_id(cur, "Respect Tetrax! (Ben 10 Classic)", "https://redd.it/oupbx1")
add_data(["Tetrax"],
"Tetrax",
False,
True,
[
'{"Ben (10|Ten(nyson)?)"}', '{"(Omn|Ulti)itrix"}'
],
"Ben 10",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oupbx1/respect_tetrax_ben_10_classic/

########################################

id = get_rt_id(cur, "Respect Marrow (Dreamwalker)", "https://redd.it/oum2xl")
add_data(["Marrow"],
"Marrow",
False,
False,
[
'{"Dreamwalker"}'
],
"Dreamwalker",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oum2xl/respect_marrow_dreamwalker/

########################################

id = get_rt_id(cur, "Respect Leo/Kamen Rider Psyga (Kamen Rider Faiz)!", "https://redd.it/p6hlzb")
add_data(["Kamen Rider Psyga"],
"Kamen Rider Psyga",
False,
True,
[
'{"Faiz"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6hlzb/respect_leokamen_rider_psyga_kamen_rider_faiz/

########################################

id = get_rt_id(cur, "Respect Yuji Kiba/The Horse Orphnoch (Kamen Rider Faiz)!", "https://redd.it/p6hkyy")
add_data(["Kamen Rider Orga"],
"Kamen Rider Orga",
False,
True,
[
'{"Faiz"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6hkyy/respect_yuji_kibathe_horse_orphnoch_kamen_rider/

add_data(["Horse Orphnoch"],
"Horse Orphnoch",
False,
True,
[
'{"Faiz"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6hkyy/respect_yuji_kibathe_horse_orphnoch_kamen_rider/

########################################

id = get_rt_id(cur, "Respect Kamen Rider Delta (Kamen Rider Faiz)!", "https://redd.it/p6hgwq")
add_data(["Kamen Rider Delta"],
"Kamen Rider Delta",
False,
True,
[
'{"Faiz"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6hgwq/respect_kamen_rider_delta_kamen_rider_faiz/

########################################

id = get_rt_id(cur, "Respect Masato Kusaka/Kamen Rider Kaixa (Kamen Rider Faiz)!", "https://redd.it/p6hdp0")
add_data(["Kamen Rider Kaixa"],
"Kamen Rider Kaixa",
False,
True,
[
'{"Faiz"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6hdp0/respect_masato_kusakakamen_rider_kaixa_kamen/

########################################

id = get_rt_id(cur, "Respect Takumi Inui, aka (Kamen Rider Faiz)!", "https://redd.it/p4dgq9")
add_data(["Kamen Rider Faiz"],
"Kamen Rider Faiz",
False,
True,
[
'{"555"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4dgq9/respect_takumi_inui_aka_kamen_rider_faiz/

add_data(["Takumi Inui"],
"Takumi Inui",
False,
True,
[
'{"555"}', '{"Kamen Rider"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4dgq9/respect_takumi_inui_aka_kamen_rider_faiz/

########################################

id = get_rt_id(cur, "Respect Ryusei Sakuta, Kamen Rider Meteor (Kamen Rider Fourze)", "https://redd.it/owev3h")
add_data(["Kamen Rider Meteor"],
"Kamen Rider Meteor",
False,
True,
[
'{"Kamen Rider Fourze"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/owev3h/respect_ryusei_sakuta_kamen_rider_meteor_kamen/

########################################

id = get_rt_id(cur, "Respect Gentaro Kisaragi, Kamen Rider Fourze (Kamen Rider Fourze)", "https://redd.it/ovq7ar")
add_data(["Kamen Rider Fourze"],
"Kamen Rider Fourze",
False,
True,
[
'{"Gentaro Kisaragi"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovq7ar/respect_gentaro_kisaragi_kamen_rider_fourze_kamen/

########################################

id = get_rt_id(cur, "Respect Mitsuaki Gamou, the Sagittarius Zodiarts (Kamen Rider Fourze)", "https://redd.it/oxbvq8")
add_data(["Mitsuaki Gamou"],
"Mitsuaki Gamou",
False,
True,
[
'{"Kamen Rider"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oxbvq8/respect_mitsuaki_gamou_the_sagittarius_zodiarts/

########################################

id = get_rt_id(cur, "Respect Kou Tatsugami, the Leo Zodiarts (Kamen Rider Fourze)", "https://redd.it/ox2eff")
add_data(["Kou Tatsugami"],
"Kou Tatsugami",
False,
True,
[
'{"Kamen Rider"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ox2eff/respect_kou_tatsugami_the_leo_zodiarts_kamen/

########################################

id = get_rt_id(cur, "Respect Natsuji Kijima, the Pegasus / Cancer Zodiarts (Kamen Rider Fourze)", "https://redd.it/ov9v74")
add_data(["Natsuji Kijima"],
"Natsuji Kijima",
False,
True,
[
'{"Kamen Rider"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ov9v74/respect_natsuji_kijima_the_pegasus_cancer/

add_data(["Cancer Zodiarts"],
"Cancer Zodiarts",
False,
True,
[
'{"Kamen Rider"}'
],
"Kamen Rider",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ov9v74/respect_natsuji_kijima_the_pegasus_cancer/

########################################

id = get_rt_id(cur, "Respect Agito (Origin: Spirits of the Past)", "https://redd.it/ove3kp")
add_data(["Agito"],
"Agito",
False,
False,
[
'{"Origins?"}', '{"Spirits of the Past"}'
],
"Origin: Spirits of the Past",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ove3kp/respect_agito_origin_spirits_of_the_past/

########################################

id = get_rt_id(cur, "Respect Flamie Speeddraw! (Rokka no Yuusha) (anime)", "https://redd.it/ovmpol")
add_data(["Flamie Speeddraw"],
"Flamie Speeddraw",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmpol/respect_flamie_speeddraw_rokka_no_yuusha_anime/

########################################

id = get_rt_id(cur, "Respect Nachetanya Loei Piena Augustra! (Rokka no Yuusha) (anime)", "https://redd.it/ovmsa4")
add_data(["Nachetan(i|y)a Loei Piena Augustra"],
"Nashetania Loei Piena Augustra",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmsa4/respect_nachetanya_loei_piena_augustra_rokka_no/

########################################

id = get_rt_id(cur, "Respect Goldov Auora! (Rokka no Yuusha) (anime)", "https://redd.it/ovmslx")
add_data(["Goldo(f|v) Auora"],
"Goldof Auora",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmslx/respect_goldov_auora_rokka_no_yuusha_anime/

########################################

id = get_rt_id(cur, "Respect Chamot Rosso! (Rokka no Yuusha) (anime)", "https://redd.it/ovmsxw")
add_data(["Chamot? Rosso"],
"Chamo Rosso",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmsxw/respect_chamot_rosso_rokka_no_yuusha_anime/

########################################

id = get_rt_id(cur, "Respect Hans Humpty! (Rokka no Yuusha) (anime)", "https://redd.it/ovmtcb")
add_data(["Hans Humpty"],
"Hans Humpty",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmtcb/respect_hans_humpty_rokka_no_yuusha_anime/

########################################

id = get_rt_id(cur, "Respect Maura Chester! (Rokka no Yuusha) (anime)", "https://redd.it/ovmtke")
add_data(["M(o|au)ra Chester"],
"Mora Chester",
False,
True,
[
'{"Rokka"}'
],
"Rokka: Braves of the Six Flowers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovmtke/respect_maura_chester_rokka_no_yuusha_anime/

########################################

id = get_rt_id(cur, "Respect Superman! (Superman: Brainiac Attacks)", "https://redd.it/ozq5wz")
add_data(["Super(-| )?man"],
"Superman",
False,
False,
[
'{"Superman:? Brai?niac Attacks"}', r'{"Super(-| )?man ?\\(Brai?niac Attacks"}'
],
"Superman: Brainiac Attacks",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozq5wz/respect_superman_superman_brainiac_attacks/

########################################

id = get_rt_id(cur, "Respect Brainiac (Superman: Brainiac Attacks)", "https://redd.it/ovpr9w")
add_data(["Brai?niac"],
"Brainiac",
False,
False,
[
'{"Superman:? Brainiac Attacks"}'
],
"Superman: Brainiac Attacks",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovpr9w/respect_brainiac_superman_brainiac_attacks/

########################################

id = get_rt_id(cur, "Respect Blinx (Blinx: The Time Sweeper)", "https://redd.it/ovrotg")
add_data(["Blinx"],
"Blinx",
False,
True,
[
'{"Time Sweeper"}'
],
"Blinx: The Time Sweeper",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovrotg/respect_blinx_blinx_the_time_sweeper/

########################################

id = get_rt_id(cur, "Respect Siegfried (The Nibelungenlied)", "https://redd.it/ovsh75")
add_data(["Siegfried"],
"Siegfried",
False,
False,
[
'{"Nibelungenlied"}',
'{"myth?(ical|olog(y|ical))?"}'
],
"The Nibelungenlied",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovsh75/respect_siegfried_the_nibelungenlied/

add_data(["Sigurd"],
"Sigurd",
False,
False,
[
'{"Nibelungenlied"}',
'{"myth?(ical|olog(y|ical))?"}'
],
"The Nibelungenlied",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovsh75/respect_siegfried_the_nibelungenlied/

add_data(["Sigurd"],
"Sigurd",
False,
False,
[
'{"Fate"}'
],
"Fate",
'{}'
)
#

add_data(["Siegfried"],
"Siegfried",
False,
False,
[
'{"Fate"}'
],
"Fate",
'{}'
)
#

########################################

id = get_rt_id(cur, "Respect Tommy Oliver (Bat in the Sun)", "https://redd.it/ovtdbn")
add_data(["Tommy Oliver"],
"Tommy Oliver",
False,
False,
[
'{"Bat ?in ?the ?Sun"}'
],
"Bat in the Sun",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovtdbn/respect_tommy_oliver_bat_in_the_sun/

add_data(["Green Ranger"],
"Green Ranger",
False,
False,
[
'{"Bat ?in ?the ?Sun"}'
],
"Bat in the Sun",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovtdbn/respect_tommy_oliver_bat_in_the_sun/

########################################

id = get_rt_id(cur, "Respect Zeb Orrelios (Star Wars Canon)", "https://redd.it/pey81q")
add_data(["Orrelios"],
"Zeb Orrelios",
False,
True,
[
'{"S(tar )?Wars"}'
],
"Star Wars",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pey81q/respect_zeb_orrelios_star_wars_canon/

########################################

id = get_rt_id(cur, "Respect Quinlan Vos (Star Wars) [Legends]", "https://redd.it/ovyuxg")
add_data(["Quinlan Vos"],
"Quinlan Vos",
False,
True,
[
'{"S(tar )?Wars"}', '{"Legends?"}'
],
"Star Wars",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ovyuxg/respect_quinlan_vos_star_wars_legends/

########################################

id = get_rt_id(cur, "Respect Mech Cadet Yu and Buddy (Mech Cadet Yu)", "https://redd.it/owfsal")
add_data(["Mech Cadet Yu"],
"Mech Cadet Yu",
False,
True,
[
'{"Buddy"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/owfsal/respect_mech_cadet_yu_and_buddy_mech_cadet_yu/

########################################

id = get_rt_id(cur, "Respect Grant Morrison (Dc Post-Crisis)", "https://redd.it/p49mea")
add_data(["Grant Morrison"],
"Grant Morrison",
False,
True,
[
'{"Posts?(-| )?C(risis)?"}', '{"PC"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p49mea/respect_grant_morrison_dc_postcrisis/

########################################

id = get_rt_id(cur, "Respect Harvey Dent, Two-Face (DC Comics, New 52)", "https://redd.it/pft8ca")
add_data(["Two(-| )?Face"],
"Two-Face",
False,
False,
[
'{"New(-| )?52"}', '{"Nu?-?52"}', '{"Post(-| )52"}', '{"Prime(-| )Earth"}', '{"Rebirth"}'
],
"New 52",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pft8ca/respect_harvey_dent_twoface_dc_comics_new_52/

add_data(["Two(-| )?Face"],
"Two-Face",
False,
True,
[
r'{"(\\(|\\[)DC( Comics)?(\\)|\\])"}', '{"Two(-| )?Face vs"}', r'{"vs\\. Two(-| )?Face"}',
'{"Bat(-| )?man"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pft8ca/respect_harvey_dent_twoface_dc_comics_new_52/


########################################

id = get_rt_id(cur, "Respect Mongal (Dc Post-Crisis)", "https://redd.it/p3rkln")
add_data(["Mongal"],
"Mongal",
False,
False,
[
'{"Posts?(-| )?C(risis)?"}', '{"PC"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3rkln/respect_mongal_dc_postcrisis/

add_data(["Mongal"],
"Mongal",
False,
True,
[
r'{"(\\(|\\[)DC( Comics)?(\\)|\\])"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3rkln/respect_mongal_dc_postcrisis/

add_data(["Mongal"],
"Mongal",
False,
False,
[
'{"Suicide Squad"}', '{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}'
],
"DCEU",
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/p3rkln/respect_mongal_dc_postcrisis/

########################################

id = get_rt_id(cur, "Respect The Hemo-Goblin (Dc Post-Crisis)", "https://redd.it/p30cst")
add_data(["Hemo(-| )?Goblin"],
"Hemo-Goblin",
False,
True,
[
'{"DC"}', '{"Posts?(-| )?C(risis)?"}', '{"PC"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p30cst/respect_the_hemogoblin_dc_postcrisis/

########################################

id = get_rt_id(cur, "Respect Weasel (Dc-Post Crisis)", "https://redd.it/p4tyn2")
add_data(["Weasel"],
"Weasel",
False,
False,
[
r'{"Weasel ?\\(Posts?(-| )?C(risis)?"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4tyn2/respect_weasel_dcpost_crisis/

add_data(["Weasel"],
"Weasel",
False,
False,
[
r'{"Weasel ?\\(DC"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4tyn2/respect_weasel_dcpost_crisis/
 
########################################

id = get_rt_id(cur, "Respect Hat (DC, Post Crisis)", "https://redd.it/p1qx8b")
add_data(["Hat"],
"Hat",
False,
False,
[
r'{"Hat ?\\(DC"}', r'{"Hat ?\\(Posts?(-| )?C(risis)?"}',
'{"Manchester Black"}', '{"The Elite"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p1qx8b/respect_hat_dc_post_crisis/

########################################

id = get_rt_id(cur, "Respect Javelin! (DC Comics Post-Crisis)", "https://redd.it/oy9f35")
add_data(["Javelin"],
"Javelin",
False,
False,
[
r'{"Javelin ?\\(DC"}', r'{"Javelin ?\\(Posts?(-| )?C(risis)?"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#

########################################

id = get_rt_id(cur, "Respect Bloodsport! (DC Comics Post-Crisis)", "https://redd.it/ozjtz3")
add_data(["Bloodsport"],
"Bloodsport",
False,
False,
[
r'{"Bloodsport ?\\(DC"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozjtz3/respect_bloodsport_dc_comics_postcrisis/

add_data(["Bloodsport"],
"Bloodsport",
False,
False,
[
r'{"Bloodsport ?\\(Posts?(-| )?C(risis)?"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozjtz3/respect_bloodsport_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, "Respect Motherbox (DC Pre-Flashpoint)", "https://redd.it/oxk0jv")
add_data(["Mother ?Box(es)?"],
"Mother Box",
False,
True,
[
r'{"(\\(|\\[)DC( Comics)?(\\)|\\])"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oxk0jv/respect_motherbox_dc_preflashpoint/

add_data(["Mother ?Box(es)?"],
"Mother Box",
False,
False,
[
'{"Pre(-| )?Flashpoint"}'
],
"Pre-Flashpoint",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oxk0jv/respect_motherbox_dc_preflashpoint/

add_data(["Mother ?Box(es)?"],
"Mother Box",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', '{"Snyder"}'
],
"DCEU",
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/oxk0jv/respect_motherbox_dc_preflashpoint/

add_data(["Steppenwolf"],
"Steppenwolf",
False,
False,
[
'{"Snyder"}'
],
"DCEU",
'{128}'
)
#https://www.reddit.com/r/respectthreads/comments/oxk0jv/respect_motherbox_dc_preflashpoint/

########################################

id = get_rt_id(cur, "Respect Blackguard (Dc Post-Crisis)", "https://redd.it/p5fxih")
add_data(["Blackguard"],
"Blackguard",
False,
False,
[
r'{"(\\(|\\[)DC( Comics)?(\\)|\\])"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

add_data(["Blackguard"],
"Blackguard",
False,
False,
[
'{"PC"}', '{"Earth(-| )(1|One)"}', '{"Posts?(-| )?C(risis)?"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5fxih/respect_blackguard_dc_postcrisis/

########################################

id = get_rt_id(cur, "Respect Savant (DC Comics, Post-Crisis)", "https://redd.it/p683tv")
add_data(["Savant"],
"Savant",
False,
False,
[
r'{"Savant ?\\(DC"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

add_data(["Savant"],
"Savant",
False,
False,
[
'{"PC"}', '{"Earth(-| )(1|One)"}', '{"Posts?(-| )?C(risis)?"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

add_data(["Savant"],
"Savant",
False,
False,
[
'{"Pre(-| )?Crisis"}', '{"Silver(-| )?Age"}', '{"Earth(-| )(1|One)"}'
],
"Pre-Crisis",
'{}'
)
#

########################################

id = get_rt_id(cur, "Respect Ratcatcher (DC Comics, Post-Crisis)", "https://redd.it/p5erbp")
add_data(["Ratcatcher"],
"Ratcatcher",
False,
True,
[
r'{"(\\(|\\[)DC( Comics)?(\\)|\\])"}'
],
"DC",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

add_data(["Ratcatcher"],
"Ratcatcher",
False,
False,
[
'{"PC"}', '{"Earth(-| )(1|One)"}', '{"Posts?(-| )?C(risis)?"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

add_data(["Ratcatcher"],
"Ratcatcher",
False,
False,
[
'{"Pre(-| )?Crisis"}', '{"Silver(-| )?Age"}', '{"Earth(-| )(1|One)"}'
],
"Pre-Crisis",
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/p5erbp/respect_ratcatcher_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, "Respect Starro the Conqueror (DCEU)", "https://redd.it/p8rb3e")
add_data(["Starro"],
"Starro",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}',
'{"Suicide Squad"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8rb3e/respect_starro_the_conqueror_dceu/

########################################

add_data(["Harley Quinn?"],
"Harley Quinn",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}',
'{"Suicide Squad"}'
],
"DCEU",
'{13140}'
)
#https://www.reddit.com/r/respectthreads/comments/pbbmtk/respect_harley_quinn_dc_extended_universe/

########################################

id = get_rt_id(cur, "Respect Ratcatcher 2 (DCEU)", "https://redd.it/p2uoy6")
add_data(["Ratcatcher (2|II)"],
"Ratcatcher 2",
False,
True,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', '{"Suicide Squad"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p2uoy6/respect_ratcatcher_2_dceu/

########################################

id = get_rt_id(cur, "Respect Polka-Dot Man (DCEU)", "https://redd.it/p2uldn")
add_data(["Polka(-| )Dot Man"],
"Polka Dot Man",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', '{"Suicide Squad"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p2uldn/respect_polkadot_man_dceu/

########################################

id = get_rt_id(cur, "Respect King Shark (DCEU)", "https://redd.it/ozbbgp")
add_data(["King Shark"],
"King Shark",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', '{"Suicide Squad"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozbbgp/respect_king_shark_dceu/

########################################

id = get_rt_id(cur, "Respect Bloodsport (DCEU)", "https://redd.it/ozmbjz")
add_data(["Bloodsport"],
"Bloodsport",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', '{"Suicide Squad"}',
'{"Idris Elba"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozmbjz/respect_bloodsport_dceu/

########################################

id = get_rt_id(cur, "Respect Peacemaker (DCEU)", "https://redd.it/ozmbil")
add_data(["Peace ?maker"],
"Peacemaker",
False,
False,
[
'{"DC Extended Universe"}', '{"DC ?(E|C)U"}', '{"DC Cinematic Universe"}', r'{"Peace ?maker ?\\((The )?Suicide Squad"}',
'{"John Cena"}'
],
"DCEU",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ozmbil/respect_peacemaker_dceu/

add_data(["Peace ?maker"],
"Peacemaker",
False,
False,
[
'{"Suicide Squad", "comics?"}', r'{"Peace ?maker ?\\(D\\.?C"}'
],
"DC",
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/ozmbil/respect_peacemaker_dceu/

########################################

id = get_rt_id(cur, "Respect Black Panther (Stars and Stripes Comics)", "https://redd.it/oyhkqp")
add_data(["Black Panther"],
"Black Panther",
False,
False,
[
'{"Stars (and|&) Stripes"}'
],
"Stars and Stripes",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oyhkqp/respect_black_panther_stars_and_stripes_comics/

########################################

id = get_rt_id(cur, "Respect Kaido (One Piece)", "https://redd.it/oyl7oz")
add_data(["Kaido"],
"Kaido",
False,
True,
[
'{"One ?Piece?"}'
],
"One Piece",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oyl7oz/respect_kaido_one_piece/

########################################

id = get_rt_id(cur, "Respect Captain Hero (Drawn Together)", "https://redd.it/oyjena")
add_data(["Captain Hero"],
"Captain Hero",
False,
True,
[
'{"Drawn Together"}'
],
"Drawn Together",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oyjena/respect_captain_hero_drawn_together/

########################################

id = get_rt_id(cur, "Respect Sparkster (Rocket Knight Adventures)", "https://redd.it/oypki6")
add_data(["Sparkster"],
"Sparkster",
False,
True,
[
'{"Rocket Knight Adventures"}'
],
"Rocket Knight Adventures",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/oypki6/respect_sparkster_rocket_knight_adventures/

########################################

id = get_rt_id(cur, "Respect The Fantastic Four (Fantastic Four 1967)", "https://redd.it/p0i04u")
add_data(["Fantastic Four"],
"Fantastic Four",
True,
False,
[
'{"1967"}'
],
"1967",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0i04u/respect_the_fantastic_four_fantastic_four_1967/

########################################

id = get_rt_id(cur, "Respect Reed Richards, The Dark Raider (Earth-944)", "https://redd.it/p0i1w4")
add_data(["Reed Richards"],
"Reed Richards",
False,
False,
[
'{"Dark Raider"}', '{"944"}'
],
"944",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0i1w4/respect_reed_richards_the_dark_raider_earth944/

########################################

id = get_rt_id(cur, "Respect Rambo! (First Blood)", "https://redd.it/p0ix2a")
add_data(["Rambo"],
"Rambo",
False,
False,
[
'{"Morrell"}'
],
"David Morrell",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0ix2a/respect_rambo_first_blood/

########################################

id = get_rt_id(cur, "Respect Rambo! (Mortal Kombat)", "https://redd.it/p0j3yw")
add_data(["Rambo"],
"Rambo",
False,
False,
[
'{"Mortal Kombat"}'
],
"Mortal Kombat",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0j3yw/respect_rambo_mortal_kombat/

########################################

id = get_rt_id(cur, "Respect Rambo! (Blackthorne Publishing)", "https://redd.it/p0j930")
add_data(["Rambo"],
"Rambo",
False,
False,
[
'{"Blackthorne"}'
],
"Blackthorne Publishing",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0j930/respect_rambo_blackthorne_publishing/

########################################

id = get_rt_id(cur, "Respect Peter Parker/The Masked Spider (Masked Spider)", "https://redd.it/p0otgd")
add_data(["Masked Spider"],
"Masked Spider",
False,
True,
[
'{"Cartoon ?Hooligans"}'
],
"CartoonHooligans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p0otgd/respect_peter_parkerthe_masked_spider_masked/

########################################

id = get_rt_id(cur, "Respect Super Thor (Cartoon Hooligans)", "https://redd.it/p176ka")
add_data(["Super ?Thor"],
"Super Thor",
False,
False,
[
'{"Cartoon ?Hooligans"}',
'{"Goffu"}'
],
"CartoonHooligans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p176ka/respect_super_thor_cartoon_hooligans/

########################################

id = get_rt_id(cur, "Respect Desiree! (Danny Phantom)", "https://redd.it/p14g8z")
add_data(["Desiree"],
"Desiree",
False,
False,
[
'{"Danny Phantom"}'
],
"Danny Phantom",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p14g8z/respect_desiree_danny_phantom/

########################################

id = get_rt_id(cur, "Respect Gavan Type-G (Space Sheriff Gavan)", "https://redd.it/p150xm")
add_data(["Gavan Type(-| )G"],
"Gavan Type-G",
False,
True,
[
'{"Space Sheriff Gavan"}'
],
"Space Sheriff Gavan",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p150xm/respect_gavan_typeg_space_sheriff_gavan/

########################################

id = get_rt_id(cur, "Respect Sloth (The Goonies)", "https://redd.it/p1sq53")
add_data(["Sloth"],
"Sloth",
False,
False,
[
'{"Goonies"}'
],
"The Goonies",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p1sq53/respect_sloth_the_goonies/

########################################

id = get_rt_id(cur, "Respect Yellow (Character Scramble)", "https://redd.it/p2asq0")
add_data(["Yellow"],
"Yellow",
False,
False,
[
'{"Character Scramble"}'
],
"Character Scramble",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p2asq0/respect_yellow_character_scramble/

########################################

id = get_rt_id(cur, "Respect Hermes Conrad (Character Scramble)", "https://redd.it/p1u6aa")
add_data(["Hermes Conrad"],
"Hermes Conrad",
False,
False,
[
'{"Character Scramble"}'
],
"Character Scramble",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p1u6aa/respect_hermes_conrad_character_scramble/

########################################

id = get_rt_id(cur, "Respect Takayuki Yagami (Judgment)", "https://redd.it/p236za")
add_data(["Takayuki Yagami"],
"Takayuki Yagami",
False,
True,
[
'{"Judgment"}',
'{"Yakuza"}'
],
"Yakuza",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p236za/respect_takayuki_yagami_judgment/

########################################

id = get_rt_id(cur, "Respect Pegasus Koga (Saint Seiya: Omega)", "https://redd.it/pbq6xl")
add_data(["Pegasus K(ō|o)u?ga"],
"Pegasus Kōga",
False,
True,
[
'{"Seiya"}'
],
"Saint Seiya",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pbq6xl/respect_pegasus_koga_saint_seiya_omega/

########################################

id = get_rt_id(cur, "Respect Pegasus Tenma (Saint Seiya: the Lost Canvas)", "https://redd.it/p3dirj")
add_data(["Pegasus Tenma"],
"Pegasus Tenma",
False,
True,
[
'{"Seiya"}'
],
"Saint Seiya",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p3dirj/respect_pegasus_tenma_saint_seiya_the_lost_canvas/

########################################

id = get_rt_id(cur, "Respect Super Brainz! (Plants vs Zombies)", "https://redd.it/p42sya")
add_data(["Super Brainz"],
"Super Brainz",
False,
True,
[
'{"Plants", "Zombies"}', '{"PvZ"}', '{"Garden Warfare"}'
],
"Plants vs. Zombies",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p42sya/respect_super_brainz_plants_vs_zombies/

########################################

id = get_rt_id(cur, "Respect the Chosen Ones (Class of the Titans)", "https://redd.it/p4821g")
add_data(["Chosen Ones"],
"Chosen Ones",
True,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p4821g/respect_the_chosen_ones_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Jay (Class of the Titans)", "https://redd.it/p482vt")
add_data(["Jay"],
"Jay",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p482vt/respect_jay_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Atlanta (Class of the Titans)", "https://redd.it/p483k3")
add_data(["Atlanta"],
"Atlanta",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p483k3/respect_atlanta_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Herry (Class of the Titans)", "https://redd.it/p484f9")
add_data(["Herry"],
"Herry",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p484f9/respect_herry_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Archie (Class of the Titans)", "https://redd.it/p48550")
add_data(["Archie"],
"Archie",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p48550/respect_archie_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Theresa (Class of the Titans)", "https://redd.it/p485jf")
add_data(["Theresa"],
"Theresa",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p485jf/respect_theresa_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Odie (Class of the Titans)", "https://redd.it/p485y5")
add_data(["Odie"],
"Odie",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p485y5/respect_odie_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Neil (Class of the Titans)", "https://redd.it/p486i0")
add_data(["Neil"],
"Neil",
False,
False,
[
'{"Class of the Titans"}'
],
"Class of the Titans",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p486i0/respect_neil_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Cooler (Dragon Ball Franchise)", "https://redd.it/p54983")
add_data(["Cooler"],
"Cooler",
False,
False,
[
'{"squadron"}', '{"Dragon ?Ball"}', '{"DB(Z|S)?"}'
'{"Metal?( |-)?Cooler"}', '{"Fr(e|i)eza"}', '{"Gete Star"}', '{"Salza"}'
],
"Dragon Ball",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p54983/respect_cooler_dragon_ball_franchise/

########################################

id = get_rt_id(cur, "Respect Mima (Touhou)", "https://redd.it/p7el9u")
add_data(["Mima"],
"Mima",
False,
False,
[
'{"Touhou"}'
],
"Touhou",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7el9u/respect_mima_touhou/

########################################

id = get_rt_id(cur, "Respect Yumemi Okazaki (Touhou))", "https://redd.it/p5emwv")
add_data(["Yumemi Okazaki"],
"Yumemi Okazaki",
False,
False,
[
'{"Touhou"}'
],
"Touhou",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p5emwv/respect_yumemi_okazaki_touhou/

########################################

id = get_rt_id(cur, "Respect Manfred von Wreckerstein (The Thing (1979))", "https://redd.it/p6b0tr")
add_data(["Manfred von Wreckerstein"],
"Manfred von Wreckerstein",
False,
True,
[
'{"Thing"}'
],
"The Thing, 1979",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6b0tr/respect_manfred_von_wreckerstein_the_thing_1979/

########################################

id = get_rt_id(cur, "Respect Wallace & Gromit (Wallace & Gromit)", "https://redd.it/p6owat")
add_data(["Gromit"],
"Wallace and Gromit",
False,
True,
[
'{"Wallace"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p6owat/respect_wallace_gromit_wallace_gromit/

########################################

id = get_rt_id(cur, "Respect Xena (Xena: Warrior Princess)", "https://redd.it/pgium0")
add_data(["Xena"],
"Xena",
False,
True,
[
'{"Warrior Princess"}',
'{"chakram"}'
],
"Xena: Warrior Princess",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pgium0/respect_xena_xena_warrior_princess/

########################################

id = get_rt_id(cur, "Respect Virgil (Xena: Warrior Princess)", "https://redd.it/p76u04")
add_data(["Virgil"],
"Virgil",
False,
False,
[
'{"Xena"}', '{"Warrior Princess"}'
],
"Xena: Warrior Princess",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p76u04/respect_virgil_xena_warrior_princess/

########################################

id = get_rt_id(cur, "Respect Gabrielle (Xena: Warrior Princess)", "https://redd.it/ph9lck")
add_data(["Gabrielle"],
"Gabrielle",
False,
False,
[
'{"Xena"}', '{"Warrior Princess"}'
],
"Xena: Warrior Princess",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ph9lck/respect_gabrielle_xena_warrior_princess/

########################################

id = get_rt_id(cur, "Respect Donquixote Rosinante (One Piece)", "https://redd.it/p76yy7")
add_data(["Rosinante"],
"Rosinante",
False,
False,
[
'{"One ?Piece?"}', '{"Don ?quixote"}'
],
"One Piece",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p76yy7/respect_donquixote_rosinante_one_piece/

########################################

id = get_rt_id(cur, "Respect the Cursed Camera (Goosebumps)", "https://redd.it/p7hyoi")
add_data(["Camera"],
"Camera",
False,
False,
[
'{"Goosebumps"}', '{"Say Cheese and Die"}'
],
"Goosebumps",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7hyoi/respect_the_cursed_camera_goosebumps/

########################################

id = get_rt_id(cur, "Respect Shadow the Hedgehog! (Sonic X)", "https://redd.it/p8ygue")
add_data(["Shadow"],
"Shadow",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8ygue/respect_shadow_the_hedgehog_sonic_x/

########################################

id = get_rt_id(cur, "Respect Sonic the Hedgehog! (Sonic X)", "https://redd.it/p9k7sn")
add_data(["Sonic"],
"Sonic",
False,
False,
[
r'{"Sonic ?\\(Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9k7sn/respect_sonic_the_hedgehog_sonic_x/

add_data(["Sonic the Hedgehog"],
"Sonic the Hedgehog",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9k7sn/respect_sonic_the_hedgehog_sonic_x/

########################################

id = get_rt_id(cur, "Respect Emerl (Sonic X)", "https://redd.it/p9042i")
add_data(["Emerl"],
"Emerl",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9042i/respect_emerl_sonic_x/

########################################

id = get_rt_id(cur, "Respect Sam Speed! (Sonic X)", "https://redd.it/p8cer0")
add_data(["Sam Speed"],
"Sam Speed",
False,
True,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8cer0/respect_sam_speed_sonic_x/

########################################

id = get_rt_id(cur, "Respect Tails! (Sonic X)", "https://redd.it/p8by5i")
add_data(["Tails"],
"Tails",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8by5i/respect_tails_sonic_x/

########################################

id = get_rt_id(cur, "Respect Knuckles the Echidna! (Sonic X)", "https://redd.it/p7mper")
add_data(["Knuckles"],
"Knuckles",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7mper/respect_knuckles_the_echidna_sonic_x/

########################################

id = get_rt_id(cur, "Respect Amy Rose! (Sonic X)", "https://redd.it/p7n1mf")
add_data(["Amy Rose"],
"Amy Rose",
False,
False,
[
'{"Sonic X"}'
],
"Sonic X",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7n1mf/respect_amy_rose_sonic_x/

########################################

id = get_rt_id(cur, "Respect Benjy Grimm a.k.a. The Thing (The Thing (1979 Cartoon))", "https://redd.it/p7olf0")
add_data(["The Thing"],
"The Thing",
False,
False,
[
r'{"The Thing ?\\(1979"}'
],
"1979",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7olf0/respect_benjy_grimm_aka_the_thing_the_thing_1979/

########################################

id = get_rt_id(cur, "Respect Sonic the Hedgehog! (Tails Gets Trolled)", "https://redd.it/p7xmfa")
add_data(["Sonic"],
"Sonic",
False,
False,
[
'{"Tails Gets Trolled"}'
],
"Tails Gets Trolled",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p7xmfa/respect_sonic_the_hedgehog_tails_gets_trolled/

########################################

id = get_rt_id(cur, "Respect Psycho Goreman (Psycho Goreman)", "https://redd.it/p859rm")
add_data(["Psycho Goreman"],
"Psycho Goreman",
False,
True,
[
'{"PG"}'
],
"",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p859rm/respect_psycho_goreman_psycho_goreman/

########################################

id = get_rt_id(cur, "Respect Chipp Zanuff! (Guilty Gear)", "https://redd.it/p9m1vb")
add_data(["Chipp"],
"Chipp",
False,
False,
[
'{"Guilty Gear"}', '{"Zanuff"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9m1vb/respect_chipp_zanuff_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Nagoriyuki! (Guilty Gear)", "https://redd.it/p9m3px")
add_data(["Nagoriyuki"],
"Nagoriyuki",
False,
True,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9m3px/respect_nagoriyuki_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Potemkin! (Guilty Gear)", "https://redd.it/p9m33y")
add_data(["Potemkin"],
"Potemkin",
False,
False,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9m33y/respect_potemkin_guilty_gear/

########################################

id = get_rt_id(cur, "Respect I-No! (Guilty Gear)", "https://redd.it/p9m2qb")
add_data(["I-No"],
"I-No",
False,
True,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9m2qb/respect_ino_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Slayer! (Guilty Gear)", "https://redd.it/p8gxgo")
add_data(["Slayer"],
"Slayer",
False,
False,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8gxgo/respect_slayer_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Answer! (Guilty Gear)", "https://redd.it/p8gzi7")
add_data(["Answer"],
"Answer",
False,
False,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8gzi7/respect_answer_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Baiken! (Guilty Gear)", "https://redd.it/p8gy3r")
add_data(["Baiken"],
"Baiken",
False,
True,
[
'{"Guilty Gear"}'
],
"Guilty Gear",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8gy3r/respect_baiken_guilty_gear/

########################################

id = get_rt_id(cur, "Respect Prettz (Final Fantasy: Legend of the Crystals)", "https://redd.it/p8icb9")
add_data(["Prettz"],
"Prettz",
False,
False,
[
'{"Final Fantasy"}'
],
"Final Fantasy",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8icb9/respect_prettz_final_fantasy_legend_of_the/

########################################

id = get_rt_id(cur, "Respect Stetch Atelier (Dungeons & Artifacts)", "https://redd.it/p8q7yf")
add_data(["Stetch Atelier"],
"Stetch Atelier",
False,
True,
[
'{"Dungeons (&|and) Artifacts"}'
],
"Dungeons & Artifacts",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p8q7yf/respect_stetch_atelier_dungeons_artifacts/

########################################

id = get_rt_id(cur, "Respect The Saint of Killers (Preacher)", "https://redd.it/p94fwy")
add_data(["Saint of Killers"],
"Saint of Killers",
False,
True,
[
'{"Preacher"}'
],
"Preacher",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p94fwy/respect_the_saint_of_killers_preacher/

########################################

id = get_rt_id(cur, "Respect Xanthe Rumpole! (RWBY)", "https://redd.it/pd7eyb")
add_data(["Xanthe Rumpole"],
"Xanthe Rumpole",
False,
True,
[
'{"RWBY"}'
],
"RWBY",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pd7eyb/respect_xanthe_rumpole_rwby/

########################################

id = get_rt_id(cur, "Respect Tock! (RWBY)", "https://redd.it/p9co85")
add_data(["Tock"],
"Tock",
False,
False,
[
'{"RWBY"}'
],
"RWBY",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/p9co85/respect_tock_rwby/

########################################

id = get_rt_id(cur, "Respect The Shredder (Teenage Mutant Ninja Turtles 90s live-action film)", "https://redd.it/pam63d")
add_data(["Shredder"],
"Shredder",
False,
False,
[
'{"1990"}'
],
"TMNT, 1990",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pam63d/respect_the_shredder_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, "Respect the Teenage Mutant Ninja Turtles (Teenage Mutant Ninja Turtles 90s live action film)", "https://redd.it/pba88o")
add_data(["Ninja Turtles?"],
"Teenage Mutant Ninja Turtles",
True,
False,
[
'{"1990"}'
],
"1990",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pba88o/respect_the_teenage_mutant_ninja_turtles_teenage/

########################################

id = get_rt_id(cur, "Respect Kaoru Shiba/Princess ShinkenRed (Samurai Sentai Shinkenger)", "https://redd.it/penx8x")
add_data(["Princess ShinkenRed"],
"Princess ShinkenRed",
False,
True,
[
'{"Samurai Sentai Shinkenger"}'
],
"Samurai Sentai Shinkenger",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/penx8x/respect_kaoru_shibaprincess_shinkenred_samurai/

add_data(["Kaoru Shiba"],
"Kaoru Shiba",
False,
True,
[
'{"Samurai Sentai Shinkenger"}'
],
"Samurai Sentai Shinkenger",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/penx8x/respect_kaoru_shibaprincess_shinkenred_samurai/

########################################

id = get_rt_id(cur, "Respect Juzo Fuwa (Samurai Sentai Shinkenger)", "https://redd.it/papm06")
add_data(["Juzo Fuwa"],
"Juzo Fuwa",
False,
True,
[
'{"Samurai Sentai Shinkenger"}'
],
"Samurai Sentai Shinkenger",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/papm06/respect_juzo_fuwa_samurai_sentai_shinkenger/

########################################

id = get_rt_id(cur, "Respect the Wu-Tang Clan! (Wu-Tang: Shaolin Style)", "https://redd.it/pazq4c")
add_data(["Wu(-| )?Tang Clan"],
"Wu-Tang Clan",
True,
False,
[
'{"Shaolin Style"}'
],
"Wu-Tang: Shaolin Style",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pazq4c/respect_the_wutang_clan_wutang_shaolin_style/

########################################

id = get_rt_id(cur, "Respect Sergei (Mother Russia Bleeds)", "https://redd.it/pb8ua0")
add_data(["Sergei"],
"Sergei",
False,
False,
[
'{"Mother Russia Bleeds"}'
],
"Mother Russia Bleeds",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pb8ua0/respect_sergei_mother_russia_bleeds/

########################################

id = get_rt_id(cur, "Respect Andrew Detmer (Chronicle)", "https://redd.it/pbat71")
add_data(["Andrew"],
"Andrew",
False,
False,
[
'{"Chronicles?"}', '{"Detmer"}'
],
"Chronicle",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pbat71/respect_andrew_detmer_chronicle/

########################################

id = get_rt_id(cur, "Respect Dosu Kinuta! (Naruto) [Manga]", "https://redd.it/pbc2ex")
add_data(["Dosu"],
"Dosu",
False,
False,
[
'{"Naruto"}', '{"Kinuta"}', '{"Team Dosu"}'
],
"Naruto",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pbc2ex/respect_dosu_kinuta_naruto_manga/

########################################

id = get_rt_id(cur, "Respect Professor Poopypants! (Captain Underpants)", "https://redd.it/pcq988")
add_data(["Poopypants"],
"Poopypants",
False,
False,
[
'{"Professor"}', '{"Underpants"}'
],
"Captain Underpants",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pcq988/respect_professor_poopypants_captain_underpants/

########################################

id = get_rt_id(cur, "Respect The Egg Beater Mech (Archie Sonic, Pre-Genesis Wave)", "https://redd.it/pdgpfn")
add_data(["Egg Beater"],
"Egg Beater",
False,
False,
[
'{"Archie"}'
],
"Archie Comics",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdgpfn/respect_the_egg_beater_mech_archie_sonic/

########################################

id = get_rt_id(cur, "Respect Cornelius (Planet of the Apes/Green Lantern)", "https://redd.it/pdoofu")
add_data(["Cornelius"],
"Cornelius",
False,
False,
[
'{"Green Lantern"}'
],
"Green Lantern",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdoofu/respect_cornelius_planet_of_the_apesgreen_lantern/

########################################

id = get_rt_id(cur, "Respect Tetsutetsu Tetsutetsu! (My Hero Academia)", "https://redd.it/pdpbqn")
add_data(["Tetsutetsu"],
"Tetsutetsu Tetsutetsu",
False,
True,
[
'{"My Hero Academia"}', r'{"\\(My Hero\\)"}', '{"(M|BN?)HA"}', '{"Boku no Hero"}'
],
"My Hero Academia",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdpbqn/respect_tetsutetsu_tetsutetsu_my_hero_academia/

########################################

id = get_rt_id(cur, "Respect Marco! (Animorphs)", "https://redd.it/pdrarq")
add_data(["Marco"],
"Marco",
False,
False,
[
'{"Animorphs?"}'
],
"Animorphs",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pdrarq/respect_marco_animorphs/

########################################

id = get_rt_id(cur, "Respect Wonder Woman (Joss Whedon''s unused script)", "https://redd.it/pgxfcc")
add_data(["Wonder ?Woman"],
"Wonder Woman",
False,
False,
[
'{"Whedon"}'
],
"Joss Whedon",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pgxfcc/respect_wonder_woman_joss_whedons_unused_script/

########################################

id = get_rt_id(cur, "Respect Batman (Tom Mankiewicz''s The Batman, unused script)", "https://redd.it/pf6585")
add_data(["Bat(-| )?man"],
"Batman",
False,
False,
[
'{"Mankiewicz"}'
],
"Tom Mankiewicz",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf6585/respect_batman_tom_mankiewiczs_the_batman_unused/

########################################

id = get_rt_id(cur, "Respect Batman (Fortnite)", "https://redd.it/pe31rn")
add_data(["Bat(-| )?man"],
"Batman",
False,
False,
[
'{"Fortnite"}'
],
"Fortnite",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pe31rn/respect_batman_fortnite/

########################################

id = get_rt_id(cur, "Respect The Janitor (Willy''s Wonderland)", "https://redd.it/pf8c8p")
add_data(["Janitor"],
"Janitor",
False,
False,
[
'{"Willy(''|’)s Wonderland"}'
],
"Willy''s Wonderland",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf8c8p/respect_the_janitor_willys_wonderland/

add_data(["Nicolas Cage"],
"Nicolas Cage",
False,
False,
[
'{"Willy(''|’)s Wonderland"}'
],
"Willy''s Wonderland",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pf8c8p/respect_the_janitor_willys_wonderland/

########################################

id = get_rt_id(cur, "Respect Meggy Spletzer! (SMG4 Bloopers)", "https://redd.it/pfmp63")
add_data(["Meggy Spletzer"],
"Meggy Spletzer",
False,
True,
[
'{"SMG4 Bloopers"}'
],
"SMG4 Bloopers",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pfmp63/respect_meggy_spletzer_smg4_bloopers/

########################################

id = get_rt_id(cur, 'Respect Atsuko "Akko" Kagari! (Little Witch Academia [TV Series])', "https://redd.it/pg2cm1")
add_data(["Atsuko"],
"Atsuko",
False,
False,
[
'{"Little Witch Academia"}',
'{"Kagari"}',
'{"Luna Nova"}'
],
"Little Witch Academia",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pg2cm1/respect_atsuko_akko_kagari_little_witch_academia/

add_data(["Akko"],
"Akko",
False,
False,
[
'{"Little Witch Academia"}',
'{"Kagari"}',
'{"Izuku"}',
'{"Luna Nova"}'
],
"Little Witch Academia",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/pg2cm1/respect_atsuko_akko_kagari_little_witch_academia/

########################################

id = get_rt_id(cur, "Respect Honō (Pokemon Mystery Dungeon: Blazing Exploration Team)", "https://redd.it/ph2uwo")
add_data(["Hon(ō|o)"],
"Honō",
False,
False,
[
'{"Mystery Dungeon"}'
],
"Pokémon Mystery Dungeon",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ph2uwo/respect_hon%C5%8D_pokemon_mystery_dungeon_blazing/

########################################

id = get_rt_id(cur, "Respect Totodile (Pokemon Mystery Dungeon: Blazing Exploration Team)", "https://redd.it/ph2uya")
add_data(["Totodile"],
"Totodile",
False,
False,
[
'{"Mystery Dungeon"}'
],
"Pokémon Mystery Dungeon",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ph2uya/respect_totodile_pokemon_mystery_dungeon_blazing/

########################################

id = get_rt_id(cur, "Respect Death! (My Name is Death)", "https://redd.it/ph7lv1")
add_data(["Death"],
"Death",
False,
False,
[
'{"My Name is Death"}'
],
"My Name is Death",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/ph7lv1/respect_death_my_name_is_death/

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
                
def insert_character(cur, default_name, version_list, is_default, rt_id_array, full_version_name):
    rows_inserted = 0
    query = "INSERT INTO character (default_name, version, is_default, rt_id_array, full_version_name) VALUES "
    for version in version_list:
        cur.execute("SELECT COUNT(*) FROM character WHERE default_name='{}' AND version='{}';".format(default_name, version))
        num_results = cur.fetchone()
        if num_results[0] == 0:
            query += "('{}', '{}', {}, '{}', '{}'),".format(default_name, version, is_default, rt_id_array, full_version_name)
            rows_inserted += 1
    
    if rows_inserted != 0:
        query = query.rstrip(",") + ";"
        cur.execute(query)
        print("Successfully inserted {} into TABLE character ({} rows)".format(default_name, rows_inserted))

for i in range(len(num_chars)):
    insert_character_name(cur, name_lists[i], default_names[i], is_team_list[i])
    insert_character(cur, default_names[i], version_lists[i], is_default_list[i], rt_id_arrays[i], full_version_names[i])

con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

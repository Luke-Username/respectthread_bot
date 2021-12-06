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
'{"Monsters,? Inc"}'
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

def add_data(name_list, default_name, is_team, is_default, version_list, displayed_version_name, rt_id_array):
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

update_respectthread(cur, 5384, 'Respect Doctor Ivo "Eggman" Robotnik (Sonic the Hedgehog)', "https://redd.it/r66ur6")
update_respectthread(cur, 6470, "Respect Chandra Nalaar! (Magic: The Gathering)", "https://redd.it/r6k9eo")
update_respectthread(cur, 6483, "Respect Sorin Markov! (Magic: The Gathering)", "https://redd.it/r78tr8")
update_respectthread(cur, 15938, 'Respect Candyman (Candyman)', 'https://redd.it/r82hhf')
update_respectthread(cur, 183, 'Respect Godzilla (Millennium Era)', 'https://redd.it/r9f8e5')

########################################

id = get_rt_id(cur, 'Respect Big the Cat! (Sonic the Hedgehog)', 'https://redd.it/r8xl3u')
add_data(['Big the Cat'],
'Big the Cat',
False,
True,
[
'{"Sonic"}'
],
'Sonic the Hedgehog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8xl3u/respect_big_the_cat_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, "Respect Emerl! (Sonic the Hedgehog)", "https://redd.it/r6tgpd")
add_data(["Emerl"],
"Emerl",
False,
True,
[
'{"Sonic"}'
],
"Sonic the Hedgehog",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6tgpd/respect_emerl_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, "Respect G-merl! (Sonic the Hedgehog)", "https://redd.it/r60k6y")
add_data(["G(-|e)merl"],
"G-merl",
False,
True,
[
'{"Sonic"}'
],
"Sonic the Hedgehog",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r60k6y/respect_gmerl_sonic_the_hedgehog/

########################################

id = get_rt_id(cur, "Respect Sir Bedivere! (Fate)", "https://redd.it/r7qzu3")
add_data(["Bedivere"],
"Bedivere",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}',
'{"Serv(a|e)nts?"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r7qzu3/respect_sir_bedivere_fate/

########################################

id = get_rt_id(cur, "Respect Shuten-Douji! (Fate)", "https://redd.it/r7b0j1")
add_data(["Shuten(-| )D(ō|o)u?ji"],
"Shuten-Dōji",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}',
'{"Serv(a|e)nts?"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r7b0j1/respect_shutendouji_fate/

########################################

id = get_rt_id(cur, "Respect Minamoto-no-Raikou! (Fate)", "https://redd.it/r6xake")
add_data(["Minamoto(-| )no(-| )Raikou?"],
"Minamoto-no-Raikou",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6xake/respect_minamotonoraikou_fate/

########################################

id = get_rt_id(cur, "Respect Kiyohime! (Fate)", "https://redd.it/r62v0k")
add_data(["Kiyohime"],
"Kiyohime",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r62v0k/respect_kiyohime_fate/

########################################

id = get_rt_id(cur, "Respect Lu Bu! (Fate)", "https://redd.it/r62krj")
add_data(["Lu Bu"],
"Lu Bu",
False,
False,
[
r'{"Lu Bu ?\\(Fate"}', '{"Fate/EXTRA"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r62krj/respect_lu_bu_fate/

########################################

id = get_rt_id(cur, "Respect Tamamo-no-Mae, the Fox Priestess of Peerless Beauty! (Fate)", "https://redd.it/r5wo7m")
add_data(["Tamamo(-| )no(-| )Mae"],
"Tamamo-no-Mae",
False,
False,
[
'{"Fate"}', '{"Extra"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5wo7m/respect_tamamonomae_the_fox_priestess_of_peerless/

########################################

id = get_rt_id(cur, "Respect Vlad the Impaler! (Fate)", "https://redd.it/r5ojg5")
add_data(["Vlad"],
"Vlad",
False,
False,
[
r'{"?\\(Fate"}',
'{"Lancer|Berserker"}',
'{"Apoc(rypha)?"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5ojg5/respect_vlad_the_impaler_fate/

########################################

id = get_rt_id(cur, "Respect Sherlock Holmes! (Fate)", "https://redd.it/r61sob")
add_data(["Sherlock"],
"Sherlock Holmes",
False,
False,
[
r'{"Sherlock( Holmes)? ?\\(Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r61sob/respect_sherlock_holmes_fate/

########################################

id = get_rt_id(cur, "Respect Sir Gawain, the Knight of the Sun! (Fate)", "https://redd.it/r53m49")
add_data(["Gawain"],
"Gawain",
False,
False,
[
'{"Fate"}', '{"Saber"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Nero Claudius, the Emperor of Roses! (Fate)", "https://redd.it/r4xpvs")
add_data(["Nero"],
"Nero",
False,
False,
[
r'{"Nero( Claudius)? ?\\(Fate"}',
'{"Fate", "Extra"}', '{"Saber"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r4xpvs/respect_nero_claudius_the_emperor_of_roses_fate/

########################################

id = get_rt_id(cur, "Respect Leonardo da Vinci! (Fate)", "https://redd.it/r3rgxj")
add_data(["Da Vinci"],
"Leonardo da Vinci",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F(ate )?/?GO"}'
],
"Fate",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r3rgxj/respect_leonardo_da_vinci_fate/

########################################

id = get_rt_id(cur, "Respect Fei Wangfang, The Tiger''s Vessel! (Kengan Omega)", "https://redd.it/r69xnd")
add_data(["Fei Wangfang"],
"Fei Wangfang",
False,
False,
[
'{"Kengan(verse)?"}'
],
"Kengan Asura",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r69xnd/respect_fei_wangfang_the_tigers_vessel_kengan/

########################################

id = get_rt_id(cur, 'Respect Yumigahama Hikaru, "The Traitor Fang" (Kengan Omega)', "https://redd.it/r3u5eg")
add_data(["Yumigahama Hikaru"],
"Yumigahama Hikaru",
False,
False,
[
'{"Kengan(verse)?"}'
],
"Kengan Asura",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r3u5eg/respect_yumigahama_hikaru_the_traitor_fang_kengan/

########################################

id = get_rt_id(cur, "Respect the Swamp Thing (Swamp Thing, 2019 series)", "https://redd.it/r466mi")
add_data(["Swamp Thing"],
"Swamp Thing",
False,
False,
[
'{"2019"}'
],
"2019",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r466mi/respect_the_swamp_thing_swamp_thing_2019_series/

########################################

id = get_rt_id(cur, "Respect Al Bundy (Married... with Children: 2099)", "https://redd.it/r4aj5g")
add_data(["Al Bundy"],
"Al Bundy",
False,
False,
[
'{"2099"}'
],
"Married... with Children: 2099",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r4aj5g/respect_al_bundy_married_with_children_2099/

########################################

id = get_rt_id(cur, 'Respect Lady Deadpool (Earth-3010)', 'https://redd.it/r8qila')
add_data(['Lady Deadpool'],
'Lady Deadpool',
False,
True,
[
'{"3010"}'
],
'3010',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8qila/respect_lady_deadpool_earth3010/

########################################

id = get_rt_id(cur, "Respect The Whiz Kid (Marvel-616)", "https://redd.it/r6a8oz")
add_data(["Whiz Kid"],
"Whiz Kid",
False,
False,
[
'{"Marvel"}', '{"616"}'
],
"616",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6a8oz/respect_the_whiz_kid_marvel616/

########################################

id = get_rt_id(cur, "Respect Monet (Marvel, 616)", "https://redd.it/r4fxhb")
add_data(["Monet"],
"Monet",
False,
False,
[
'{"M"}',
'{"Marvel"}', '{"616"}'
],
"616",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r4fxhb/respect_monet_marvel_616/

########################################

id = get_rt_id(cur, "Respect General Ross, The Hulk (Earth-523000)", "https://redd.it/r5tok5")
add_data(["(General|Thunderbolt) Ross"],
"General Ross",
False,
False,
[
'{"523000"}'
],
"523000",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5tok5/respect_general_ross_the_hulk_earth523000/

########################################

id = get_rt_id(cur, "Respect Ashtaroth (Nemesis Saga book 5: Project Legion)", "https://redd.it/r4l8qe")
add_data(["Ashtaroth"],
"Ashtaroth",
False,
False,
[
'{"Nemesis Saga"}',
'{"Project Legion"}'
],
"Nemesis Saga",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r4l8qe/respect_ashtaroth_nemesis_saga_book_5_project/

########################################

id = get_rt_id(cur, 'Respect Tom Ward (Wardstone Chronicles)', 'https://redd.it/r8sj2c')
add_data(['Tom Ward'],
'Tom Ward',
False,
True,
[
'{"Wardstone Chronicles"}', '{"Last Apprentice"}'
],
'Wardstone Chronicles',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8sj2c/respect_tom_ward_wardstone_chronicles/

########################################

id = get_rt_id(cur, "Respect Alice Deane (Wardstone Chronicles)", "https://redd.it/r6hvvi")
add_data(["Alice Deane"],
"Alice Deane",
False,
True,
[
'{"Wardstone Chronicles"}'
],
"Wardstone Chronicles",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6hvvi/respect_alice_deane_wardstone_chronicles/

########################################

id = get_rt_id(cur, "Respect Slither (Wardstone Chronicles)", "https://redd.it/r4ylp0")
add_data(["Slither"],
"Slither",
False,
False,
[
'{"Wardstone Chronicles"}'
],
"Wardstone Chronicles",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r4ylp0/respect_slither_wardstone_chronicles/

########################################

id = get_rt_id(cur, "Respect Grimalkin (Wardstone Chronicles)", "https://redd.it/r5ly9d")
add_data(["Grimalkin"],
"Grimalkin",
False,
False,
[
'{"Wardstone Chronicles"}',
'{"Dark Assassin"}'
],
"Wardstone Chronicles",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5ly9d/respect_grimalkin_wardstone_chronicles/

########################################

id = get_rt_id(cur, "Respect Marisa Kirisame (Touhou)", "https://redd.it/r5qi72")
add_data(["Marisa"],
"Marisa",
False,
False,
[
'{"Touhou"}'
],
"Touhou",
'{' + '{}, 20388'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5qi72/respect_marisa_kirisame_touhou/

########################################

id = get_rt_id(cur, "Respect Lord Van Bloot (Chaotic)", "https://redd.it/r5d8ni")
add_data(["Lord Van Bloot"],
"Lord Van Bloot",
False,
False,
[
'{"Chaotic"}'
],
"Chaotic",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5d8ni/respect_lord_van_bloot_chaotic/

########################################

id = get_rt_id(cur, "Respect Black [...And I Show You How Deep The Rabbit Hole Goes]", "https://redd.it/r5eyu0")
add_data(["Black"],
"Black",
False,
False,
[
'{"And I Show You How Deep The Rabbit Hole Goes"}'
],
"...And I Show You How Deep The Rabbit Hole Goes",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5eyu0/respect_black_and_i_show_you_how_deep_the_rabbit/

########################################

id = get_rt_id(cur, "Respect Izumu Niounomiya (Zaregoto Series)", "https://redd.it/r5gvb3")
add_data(["Izumu Niounomiya"],
"Izumu Niounomiya",
False,
True,
[
'{"Zaregoto"}'
],
"Zaregoto",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5gvb3/respect_izumu_niounomiya_zaregoto_series/

########################################

id = get_rt_id(cur, 'Respect SCP-1915, Status Quo (SCP Foundation)', 'https://redd.it/r9ruf5')
add_data(['SCP(-| )?1915'],
'SCP-1915',
False,
True,
[
'{"SCP Foundation"}'
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect SCP-004, "The 12 Rusty Keys and the Door" (SCP Foundation)', "https://redd.it/r5jtjx")
add_data(['SCP(-| )?004'],
'SCP-004',
False,
True,
[
'{"SCP Foundation"}'
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5jtjx/respect_scp004_the_12_rusty_keys_and_the_door_scp/

########################################

id = get_rt_id(cur, "RESPECT THE GREEN DEATH! (Green Death series)", "https://redd.it/r5uz9f")
add_data(["Green Death"],
"Green Death",
False,
False,
[
'{"Green Death series"}'
],
"",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5uz9f/respect_the_green_death_green_death_series/

########################################

id = get_rt_id(cur, "Respect the Amogus Kid (Among Us Ruined my Life Copypastas)", "https://redd.it/r5z1wd")
add_data(["Amon?g ?Us"],
"Among Us",
False,
False,
[
'{"Among Us Ruined my Life"}'
],
"Among Us Ruined my Life",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r5z1wd/respect_the_amogus_kid_among_us_ruined_my_life/

########################################

id = get_rt_id(cur, "Respect Kang the Conqueror (Avengers: Earth''s Mightiest Heroes)", "https://redd.it/r61exp")
add_data(["Kang the Conqueror"],
"Kang the Conqueror",
False,
False,
[
"{\"Earth''s Mightiest Heroes\"}", '{"Avengers:? Earths? Mightiest Heroes"}', '{"Avengers:? Earth\'\'s Mightiest Heroes"}', '{"EMH"}'
],
"Earth''s Mightiest Heroes",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r61exp/respect_kang_the_conqueror_avengers_earths/

########################################

id = get_rt_id(cur, "Respect Drusilla (Buffyverse)", "https://redd.it/r6e7wa")
add_data(["Drusilla"],
"Drusilla",
False,
True,
[
'{"Buffy(verse)?"}'
],
"Buffy the Vampire Slayer",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6e7wa/respect_drusilla_buffyverse/

########################################

id = get_rt_id(cur, "Respect Eddie Collins, aka ShadowHawk! (Image Comics)", "https://redd.it/r6gtme")
add_data(["ShadowHawk"],
"ShadowHawk",
False,
True,
[
'{"Image"}'
],
"Image Comics",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6gtme/respect_eddie_collins_aka_shadowhawk_image_comics/

########################################

id = get_rt_id(cur, "Respect Black Tyrannosaurus (Dinosaur King)", "https://redd.it/r6ho5s")
add_data(["Black (T\\.?(-| )Rex|Tyrannosaurus)"],
"Black Tyrannosaurus",
False,
True,
[
'{"Dinosaur King"}'
],
"Dinosaur King",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6ho5s/respect_black_tyrannosaurus_dinosaur_king/

########################################

id = get_rt_id(cur, 'Respect Alexander Gallen (Baki)', 'https://redd.it/r9jmrw')
add_data(['Alexander Gallen'],
'Alexander Gallen',
False,
True,
[
'{"Baki"}'
],
'Baki the Grappler',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r9jmrw/respect_alexander_gallen_baki/

########################################

id = get_rt_id(cur, "Respect Jun Guevaru (Baki)", "https://redd.it/r6icwv")
add_data(["Jun Guevaru"],
"Jun Guevaru",
False,
True,
[
'{"Baki"}'
],
"Baki the Grappler",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6icwv/respect_jun_guevaru_baki/

########################################

id = get_rt_id(cur, "Respect Amarendra Baahubali (Baahubali)", "https://redd.it/r6kzo9")
add_data(["Amarendra"],
"Amarendra",
False,
False,
[
'{"Baahubali"}'
],
"Baahubali",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6kzo9/respect_amarendra_baahubali_baahubali/

########################################

id = get_rt_id(cur, "Respect Shiva / Mahendra Baahubali (Baahubali)", "https://redd.it/r6l3j5")
add_data(["Mahendra"],
"Mahendra",
False,
False,
[
'{"Baahubali"}'
],
"Baahubali",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6l3j5/respect_shiva_mahendra_baahubali_baahubali/

add_data(["Shiva"],
"Shiva",
False,
False,
[
'{"Baahubali"}'
],
"Baahubali",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6l3j5/respect_shiva_mahendra_baahubali_baahubali/

########################################

id = get_rt_id(cur, 'Respect Joseph "Fumi" Joestar (Jojo''s Bizarre Adventure: Jojolion)', "https://redd.it/r6pbge")
add_data(["Fumi"],
"Fumi",
False,
False,
[
'{"Jojo(lion)?"}'
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6pbge/respect_joseph_fumi_joestar_jojos_bizarre/

########################################

id = get_rt_id(cur, 'Respect The Praetorian (Super Crooks)', 'https://redd.it/r6vy7p')
add_data(['Praetorian'],
'Praetorian',
False,
False,
[
'{"Super Crooks"}'
],
'Super Crooks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r6vy7p/respect_the_praetorian_super_crooks/

########################################

id = get_rt_id(cur, 'Respect Android 21 (Dragon Ball FighterZ)', 'https://redd.it/r78alf')
add_data(['Android 21'],
'Android 21',
False,
True,
[
'{"Dragon ?Ball"}', '{"DB(FZ)?"}', '{"Fighters? ?Z"}'
],
'Dragon Ball FighterZ',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r78alf/respect_android_21_dragon_ball_fighterz/

########################################

id = get_rt_id(cur, 'Respect Hell Fighter 17 (Dragon Ball GT)', 'https://redd.it/r7ddb8')
add_data(['Hell Fighter 17'],
'Hell Fighter 17',
False,
True,
[
'{"Dragon ?Ball"}', '{"DB(GT)?"}'
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r7ddb8/respect_hell_fighter_17_dragon_ball_gt/

########################################

id = get_rt_id(cur, 'Respect Super 17 (Dragon Ball GT)', 'https://redd.it/r7dfpm')
add_data(['Super 17'],
'Super 17',
False,
True,
[
'{"Dragon ?Ball"}', '{"DB(GT)?"}'
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r7dfpm/respect_super_17_dragon_ball_gt/

########################################

id = get_rt_id(cur, 'Respect Kakarot Kent (Dragon Ball DC)', 'https://redd.it/r7zmxa')
add_data(['Kakarot Kent'],
'Kakarot Kent',
False,
True,
[
'{"Dragon Ball DC"}'
],
'Dragon Ball DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r7zmxa/respect_kakarot_kent_dragon_ball_dc/

########################################

id = get_rt_id(cur, 'Respect Vegeta (Dragon Ball DC)', 'https://redd.it/r8wmkh')
add_data(['Vegeta'],
'Vegeta',
False,
False,
[
'{"Dragon Ball DC"}'
],
'Dragon Ball DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8wmkh/respect_vegeta_dragon_ball_dc/

########################################

id = get_rt_id(cur, 'Respect Archangel Avacyn! (Magic: The Gathering)', 'https://redd.it/r821ur')
add_data(['Avacyn'],
'Avacyn',
False,
True,
[
'{"Magic:? The Gathering"}', '{"M:?TG"}'
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r821ur/respect_archangel_avacyn_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Tartarus! (DC Earth-8)', 'https://redd.it/r8j87t')
add_data(['Tartarus'],
'Tartarus',
False,
False,
[
'{"Earth(-| )8"}'
],
'Earth-8',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8j87t/respect_tartarus_dc_earth8/

########################################

id = get_rt_id(cur, 'Respect Superman (Superman: Flyby Unused Script)', 'https://redd.it/r8prch')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
'{"Superman:? Flyby"}', r'{"J\\.?J\\.? Abrams"}'
],
'Superman: Flyby',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8prch/respect_superman_superman_flyby_unused_script/

########################################

id = get_rt_id(cur, "Respect ''Lightning Bolt'' Zolt! (Legend of Korra)", 'https://redd.it/r8zwro')
add_data(['Zolt'],
'Zolt',
False,
False,
[
'{"Avatar"}', '{"Korra"}', '{"Lightning Bolt"}'
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r8zwro/respect_lightning_bolt_zolt_legend_of_korra/

########################################

id = get_rt_id(cur, 'Respect Exdeath! (Final Fantasy)', 'https://redd.it/r97v3n')
add_data(['Exdeath'],
'Exdeath',
False,
True,
[
'{"Final Fantasy"}'
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r97v3n/respect_exdeath_final_fantasy/

########################################

id = get_rt_id(cur, 'Respect Koopa (DEATH BATTLE!)', 'https://redd.it/r9syxr')
add_data(['Koopa'],
'Koopa',
False,
False,
[
'{"DEATH BATTLE"}'
],
'DEATH BATTLE',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/r9syxr/respect_koopa_death_battle/

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

con.commit()
print("Committed")

# Close the cursor and connection
cur.close()
con.close()

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

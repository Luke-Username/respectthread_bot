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
'{' + r'{id}' +'}'
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

update_respectthread(cur, 5248, "Respect Raiden (Metal Gear)", "https://redd.it/qs9njr")
update_respectthread(cur, 5245, "Respect Jetstream Sam (Metal Gear Rising: Revengeance)", "https://redd.it/qsz2jc")
update_respectthread(cur, 1725, "Respect Ragman (DC Comics, New 52)", "https://redd.it/qtel6v")
update_respectthread(cur, 2802, "Respect Marko! (Saga)", "https://redd.it/qw3s36")
update_respectthread(cur, 2803, "Respect The Will! (Saga)", "https://redd.it/qw3s4i")
update_respectthread(cur, 1872, "Respect Static (DC Comics, New 52)", "https://redd.it/qwd1rd")
update_respectthread(cur, 14424, "Respect Asterios! (Fate)", "https://redd.it/qx09n6")
update_respectthread(cur, 2606, "Respect Mega Man! (Archie Comics)", "https://redd.it/qwu3v3")
update_respectthread(cur, 5737, "Respect Reimu Hakurei (Touhou)", "https://redd.it/r0ei4c")
update_respectthread(cur, 12473, 'Respect Carlos Medel, "El Dorado" (Kengan Omega)', "https://redd.it/r1f0p1")

########################################

id = get_rt_id(cur, "Respect Mighty Mom & Dyno Dad! (The Fairly OddParents)", "https://redd.it/qwwkqa")
add_data(["Mighty Mom|Dyno Dad"],
"Mighty Mom and Dyno Dad",
False,
True,
[
'{"Fairly OddParents"}'
],
"Fairly OddParents",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qwwkqa/respect_mighty_mom_dyno_dad_the_fairly_oddparents/

########################################

id = get_rt_id(cur, "Respect Mash Kyrielight! (Fate)", "https://redd.it/r1nntw")
add_data(["Mashu? Kyrielight"],
"Mash Kyrielight",
False,
True,
[
'{"Fate"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r1nntw/respect_mash_kyrielight_fate/

add_data(["Mash"],
"Mash",
False,
False,
[
'{"\\(Fate"}', 
'{"Grande? Order"}', '{"F(ate )?/?GO"}',
'{"Galahad"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r1nntw/respect_mash_kyrielight_fate/

########################################

id = get_rt_id(cur, "Respect Karna, the Hero of Charity! (Fate)", "https://redd.it/qzrhwq")
add_data(["Karna"],
"Karna",
False,
False,
[
'{"Fate"}',
'{"Apoc(rypha)?"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzrhwq/respect_karna_the_hero_of_charity_fate/

########################################

id = get_rt_id(cur, "Respect Lakshmibai! (Fate)", "https://redd.it/r0nnvp")
add_data(["Lakshmibai"],
"Lakshmibai",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r0nnvp/respect_lakshmibai_fate/

########################################

id = get_rt_id(cur, "Respect the Crypters! (Fate)", "https://redd.it/qzehn7")
add_data(["Crypters"],
"Crypters",
True,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzehn7/respect_the_crypters_fate/

########################################

id = get_rt_id(cur, "Respect Billy the Kid! (Fate)", "https://redd.it/qoe1ad")
add_data(["Billy the Kid"],
"Billy the Kid",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qoe1ad/respect_billy_the_kid_fate/

########################################

id = get_rt_id(cur, "Respect Abigail Williams! (Fate)", "https://redd.it/qx33fc")
add_data(["Abigail Williams"],
"Abigail Williams",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qx33fc/respect_abigail_williams_fate/

########################################

id = get_rt_id(cur, "Respect Rama, the King of Kosala! (Fate)", "https://redd.it/qz4h9x")
add_data(["Rama"],
"Rama",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz4h9x/respect_rama_the_king_of_kosala_fate/

########################################

id = get_rt_id(cur, "Respect Scáthach, Queen of the Land of Shadows! (Fate)", "https://redd.it/qz8wrm")
add_data(["Sc(á|a)thach"],
"Scáthach",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}',
'{"Lancer"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz8wrm/respect_sc%C3%A1thach_queen_of_the_land_of_shadows_fate/

########################################

id = get_rt_id(cur, "Respect the Lostbelt Kings! (Fate)", "https://redd.it/qz8ym9")
add_data(["Lostbelt Kings?"],
"Lostbelt Kings",
True,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz8ym9/respect_the_lostbelt_kings_fate/

add_data(["Sc(á|a)thach(-| )Ska(ð|o)i"],
"Scáthach-Skaði",
False,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz8ym9/respect_the_lostbelt_kings_fate/

add_data(["Arjuna Alter"],
"Arjuna Alter",
False,
True,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz8ym9/respect_the_lostbelt_kings_fate/

########################################

id = get_rt_id(cur, "Respect Arjuna, the Endowed Hero! (Fate)", "https://redd.it/qx4vlu")
add_data(["Arjuna"],
"Arjuna",
False,
False,
[
r'{"Arjuna ?\\(Fate"}', r'{"Arjuna ?\\[Fate"}', '{"Archer"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qx4vlu/respect_arjuna_the_endowed_hero_fate/

########################################

id = get_rt_id(cur, "Respect Arash Kamangir! (Fate)", "https://redd.it/qx82g4")
add_data(["Arash"],
"Arash",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qx82g4/respect_arash_kamangir_fate/

########################################

id = get_rt_id(cur, "Respect Xiang Yu! (Fate)", "https://redd.it/qwssde")
add_data(["Xiang Yu"],
"Xiang Yu",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qwssde/respect_xiang_yu_fate/

########################################

id = get_rt_id(cur, "Respect Amakusa Shirou Tokisada! (Fate)", "https://redd.it/qq8y4c")
add_data(["Amakusa Shir(ō|o)u?"],
"Amakusa Shirō",
False,
False,
[
'{"Fate"}',
'{"Apoc(rypha)?"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qq8y4c/respect_amakusa_shirou_tokisada_fate/

########################################

id = get_rt_id(cur, "Respect Napoléon Bonaparte, the Good Fellow of Everlasting Flame! (Fate)", "https://redd.it/qqyh9q")
add_data(["Napol(é|e)on"],
"Napoléon",
False,
False,
[
r'{"Napol(é|e)on ?\\(Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qqyh9q/respect_napol%C3%A9on_bonaparte_the_good_fellow_of/

########################################

id = get_rt_id(cur, "Respect Spartacus! (Fate)", "https://redd.it/qvcd2c")
add_data(["Spartacus"],
"Spartacus",
False,
False,
[
r'{"Spartacus ?\\(Fate"}', r'{"Spartacus ?\\[Fate"}',
'{"Red"}', '{"Servants?"}', '{"Apoc(rypha)?"}', '{"Berserker"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qvcd2c/respect_spartacus_fate/

########################################

id = get_rt_id(cur, "Respect the Phantom of the Opera! (Fate)", "https://redd.it/qrc2yv")
add_data(["Phantom of the Opera"],
"Phantom of the Opera",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrc2yv/respect_the_phantom_of_the_opera_fate/

########################################

id = get_rt_id(cur, "Respect Brynhildr! (Fate)", "https://redd.it/qrc86p")
add_data(["Brynhildr"],
"Brynhildr",
False,
False,
[
'{"Fate"}', '{"Lancer"}'
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrc86p/respect_brynhildr_fate/

########################################

id = get_rt_id(cur, "Respect Marie Antoinette, the White Lily Queen! (Fate)", "https://redd.it/qrysjw")
add_data(["Marie Antoinette"],
"Marie Antoinette",
False,
False,
[
'{"Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrysjw/respect_marie_antoinette_the_white_lily_queen_fate/

########################################

id = get_rt_id(cur, "Respect Francis Drake, the King of Storms! (Fate)", "https://redd.it/qs4ko1")
add_data(["Francis Drake"],
"Francis Drake",
False,
False,
[
'{"Fate", "Extra"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qs4ko1/respect_francis_drake_the_king_of_storms_fate/

########################################

id = get_rt_id(cur, "Respect Geronimo! (Fate)", "https://redd.it/qsv2ms")
add_data(["Geronimo"],
"Geronimo",
False,
False,
[
r'{"Geronimo ?\\(Fate"}',
'{"Grande? Order"}', '{"F/?GO"}'
],
"Fate",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qsv2ms/respect_geronimo_fate/

########################################

id = get_rt_id(cur, "Respect Beowulf, the King of Savagery! (Fate)", "https://redd.it/qoe1sr")
add_data(["Beowulf"],
"Beowulf",
False,
False,
[
r'{"Beowulf ?\\(Fate"}'
],
"Fate",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qoe1sr/respect_beowulf_the_king_of_savagery_fate/

########################################

add_data(["Minato"],
"Minato",
False,
False,
[
'{"Edo"}'
],
"Naruto",
'{20429}'
)
#

########################################

id = get_rt_id(cur, "Respect Jyuzo Fujimaki (Garouden)", "https://redd.it/r0gwep")
add_data(["Jyuzo Fujimaki"],
"Jyuzo Fujimaki",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r0gwep/respect_jyuzo_fujimaki_garouden/

########################################

id = get_rt_id(cur, "Respect Hikoichi Kurama (Garouden)", "https://redd.it/qzoyfh")
add_data(["Hikoichi Kurama"],
"Hikoichi Kurama",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzoyfh/respect_hikoichi_kurama_garouden/

########################################

id = get_rt_id(cur, "Respect Hiroshi Nagata (Garouden)", "https://redd.it/qy8dd8")
add_data(["Hiroshi Nagata"],
"Hiroshi Nagata",
False,
False,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qy8dd8/respect_hiroshi_nagata_garouden/

########################################

id = get_rt_id(cur, "Respect The Great Tatsumi (Garouden)", "https://redd.it/qxilm8")
add_data(["Tatsumi"],
"Tatsumi",
False,
False,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxilm8/respect_the_great_tatsumi_garouden/

########################################

id = get_rt_id(cur, "Respect Tsutomu Himekawa (Garouden)", "https://redd.it/qrv41g")
add_data(["Tsutomu Himekawa"],
"Tsutomu Himekawa",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrv41g/respect_tsutomu_himekawa_garouden/

########################################

id = get_rt_id(cur, "Respect Shozan Matsuo (Garouden)", "https://redd.it/quj547")
add_data(["Shozan Matsuo"],
"Shozan Matsuo",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/quj547/respect_shozan_matsuo_garouden/

########################################

id = get_rt_id(cur, "Respect Juumei Kuga (Garouden)", "https://redd.it/qopq57")
add_data(["Juu?mei Kuga"],
"Juumei Kuga",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qopq57/respect_juumei_kuga_garouden/

########################################

id = get_rt_id(cur, "Respect Jyohei Tsutsumi (Garouden)", "https://redd.it/qpkwy9")
add_data(["Jyohei Tsutsumi"],
"Jyohei Tsutsumi",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qpkwy9/respect_jyohei_tsutsumi_garouden/

########################################

id = get_rt_id(cur, "Respect Alpha (TOME)", "https://redd.it/qoqcp5")
add_data(["Alpha"],
"Alpha",
False,
False,
[
'{"TOME"}'
],
"TOME",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qoqcp5/respect_alpha_tome/

########################################

id = get_rt_id(cur, "Respect Kirbopher (TOME)", "https://redd.it/qq5m80")
add_data(["Kirbopher"],
"Kirbopher",
False,
True,
[
'{"TOME"}'
],
"TOME",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qq5m80/respect_kirbopher_tome/

########################################

id = get_rt_id(cur, "Respect Nylocke (TOME)", "https://redd.it/qqxeop")
add_data(["Nylocke"],
"Nylocke",
False,
True,
[
'{"TOME"}'
],
"TOME",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qqxeop/respect_nylocke_tome/

########################################

id = get_rt_id(cur, "Respect Flamegirl (TOME)", "https://redd.it/qpfjb8")
add_data(["Flamegirl"],
"Flamegirl",
False,
False,
[
'{"TOME"}'
],
"TOME",
'{' + '{}'.format(id) +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qpfjb8/respect_flamegirl_tome/

########################################

id = get_rt_id(cur, "Respect Gamecrazed (TOME)", "https://redd.it/qqxfiq")
add_data(["Gamecrazed"],
"Gamecrazed",
False,
True,
[
'{"TOME"}'
],
"TOME",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qqxfiq/respect_gamecrazed_tome/

########################################

id = get_rt_id(cur, "Respect Zetto (TOME)", "https://redd.it/qrqler")
add_data(["Zetto"],
"Zetto",
False,
False,
[
'{"TOME"}'
],
"TOME",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrqler/respect_zetto_tome/

########################################

id = get_rt_id(cur, "Respect Harvest! (DC Comics)", "https://redd.it/qzvkxr")
add_data(["Harvest"],
"Harvest",
False,
False,
[
r'{"Harvest ?\\(DC"}'
],
"DC",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzvkxr/respect_harvest_dc_comics/

########################################

id = get_rt_id(cur, "Respect 3g4 (Dc Comics, Post Crisis)", "https://redd.it/r1eok9")
add_data(["3g4"],
"3g4",
False,
False,
[
'{"DC"}',
'{"PC"}', '{"Earth(-| )(1|One)"}', '{"Posts?(-| )?C(risis)?"}', '{"New(-| )Earth"}'
],
"Post-Crisis",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r1eok9/respect_3g4_dc_comics_post_crisis/

########################################

id = get_rt_id(cur, "Respect the Reaper (Dc, Post Crisis)", "https://redd.it/qt63qm")
add_data(["Reaper"],
"Reaper",
False,
False,
[
r'{"Reaper ?\\(Posts?(-| )?C(risis)?"}'
],
"Post-Crisis",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qt63qm/respect_the_reaper_dc_post_crisis/

add_data(["Reaper"],
"Reaper",
False,
False,
[
r'{"Reaper ?\\(DC"}', '{"Judson Caspian"}'
],
"DC",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qt63qm/respect_the_reaper_dc_post_crisis/

#Ragman
########################################

id = get_rt_id(cur, "Respect Denny Swan, Solar Superman (New 52/Rebirth)", "https://redd.it/qpco2f")
add_data(["Denny Swan"],
"Denny Swan",
False,
True,
[
'{"New(-| )?52"}', '{"Nu?-?52"}', '{"Prime(-| )Earth"}', '{"Rebirth"}'
],
"New 52 / Rebirth",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qpco2f/respect_denny_swan_solar_superman_new_52rebirth/

########################################

id = get_rt_id(cur, "Respect Yor Forger, the Thorn Princess! (Spy x Family)", "https://redd.it/qpukjk")
add_data(["Yor Forger"],
"Yor Forger",
False,
True,
[
'{"Spy x Family"}'
],
"Spy x Family",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qpukjk/respect_yor_forger_the_thorn_princess_spy_x_family/

########################################

id = get_rt_id(cur, "Respect The Muscle (Batman: The Adventures Continue Season Two)", "https://redd.it/qsecyh")
add_data(["The Muscle"],
"The Muscle",
False,
False,
[
'{"Bat(-| )?man", "Adventures? Continues"}'
],
"DCAU",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qsecyh/respect_the_muscle_batman_the_adventures_continue/

########################################

id = get_rt_id(cur, "Respect Talon (Batman: The Adventures Continue Season Two)", "https://redd.it/qrlt1n")
add_data(["Talon"],
"Talon",
False,
False,
[
'{"Bat(-| )?man", "Adventures? Continues"}'
],
"DCAU",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrlt1n/respect_talon_batman_the_adventures_continue/

########################################

id = get_rt_id(cur, "Respect Mr. Wing (Batman: The Adventures Continue)", "https://redd.it/qq30as")
add_data([r"(Mister|Mr\\.?) Wing"],
"Mister Wing",
False,
False,
[
'{"DC Animated Universe"}',	'{"Animated DC"}', '{"DCAU"}',
'{"Bat(-| )?man", "Adventures? Continues"}'
],
"DCAU",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qq30as/respect_mr_wing_batman_the_adventures_continue/

########################################

id = get_rt_id(cur, "Respect Overman (Justice League Infinity)", "https://redd.it/qqcp0f")
add_data(["Overman"],
"Overman",
False,
False,
[
'{"Justice League Infinity"}', r'{"Overman ?\\(DCAU"}'
],
"DCAU",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qqcp0f/respect_overman_justice_league_infinity/

########################################

id = get_rt_id(cur, "Respect Luz Noceda! (The Owl House)", "https://redd.it/qr5onc")
add_data(["Luz"],
"Luz",
False,
False,
[
'{"Luz Noceda"}', '{"Owl House"}'
],
"The Owl House",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qr5onc/respect_luz_noceda_the_owl_house/

########################################

id = get_rt_id(cur, "Respect Flumpty Bumpty (One Night at Flumpty''s)", "https://redd.it/qrjlwx")
add_data(["Flumpty"],
"Flumpty",
False,
True,
[
'{"One Night"}', '{"Flumpty Bumpty"}'
],
"One Night at Flumpty''s",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrjlwx/respect_flumpty_bumpty_one_night_at_flumptys/

########################################

id = get_rt_id(cur, 'Respect SCP-002, The "Living" Room. (SCP Foundation)', "https://redd.it/r1nlnl")
add_data(["SCP(-| )?002"],
"SCP-002",
False,
True,
[
'{"Living"}'
],
"",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r1nlnl/respect_scp002_the_living_room_scp_foundation/

########################################

id = get_rt_id(cur, "Respect SCP-504, Critical Tomatoes! (SCP Foundation)", "https://redd.it/qrpreh")
add_data(["SCP(-| )?504"],
"SCP-504",
False,
True,
[
'{"Critical Tomatoes?"}'
],
"",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrpreh/respect_scp504_critical_tomatoes_scp_foundation/

########################################

id = get_rt_id(cur, "Respect Erik, the Opera Ghost (The Phantom of the Opera)", "https://redd.it/qrwyr5")
add_data(["Erik"],
"Erik",
False,
False,
[
'{"The (Phantom|Opera)"}'
],
"The Phantom of the Opera",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrwyr5/respect_erik_the_opera_ghost_the_phantom_of_the/

########################################

id = get_rt_id(cur, "Respect Eclipse (The Gifted)", "https://redd.it/qrznth")
add_data(["Eclipse"],
"Eclipse",
False,
False,
[
'{"The Gifted"}'
],
"The Gifted",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qrznth/respect_eclipse_the_gifted/

########################################

id = get_rt_id(cur, "Respect Princess Fiona! (Shrek)", "https://redd.it/qsfql2")
add_data(["Fiona"],
"Fiona",
False,
False,
[
'{"Shrek"}', '{"Princess"}', '{"Tai Lung"}'
],
"Shrek",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qsfql2/respect_princess_fiona_shrek/

########################################

id = get_rt_id(cur, "Respect Chaor (Chaotic)", "https://redd.it/qsize9")
add_data(["Chaor"],
"Chaor",
False,
True,
[
'{"Chaotic"}'
],
"Chaotic",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qsize9/respect_chaor_chaotic/

########################################

id = get_rt_id(cur, "Respect Ginny Weasley! (Harry Potter Books)", "https://redd.it/qsneod")
add_data(["Ginny"],
"Ginny",
False,
True,
[
'{"Weasley"}', '{"Harry"}', '{"Ron"}', '{"Hermione"}'
],
"Harry Potter",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qsneod/respect_ginny_weasley_harry_potter_books/

########################################

id = get_rt_id(cur, "Respect Unnamed Earthbending Champion (The Legend of Korra)", "https://redd.it/quk1lh")
add_data(["Unnamed Champion"],
"Unnamed Champion",
False,
False,
[
'{"Avatar"}', '{"A?TLA"}', '{"(Air|Earth)(-| )bender"}', '{"Aang"}', '{"Korra"}', '{"A?T?LOK"}'
],
"Avatar: TLA",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/quk1lh/respect_unnamed_earthbending_champion_the_legend/

########################################

id = get_rt_id(cur, "Respect Unnamed Earthbending Champion (The Legend of Korra)", "https://redd.it/quk1lh")
add_data(["Unnamed Champion"],
"Unnamed Champion",
False,
False,
[
'{"Avatar"}', '{"A?TLA"}', '{"(Air|Earth)(-| )bender"}', '{"Aang"}', '{"Korra"}', '{"A?T?LOK"}'
],
"Avatar: TLA",
'{' + f'{id}' +'}'
)
#

########################################

id = get_rt_id(cur, "Respect Lucy! (Lucy)", "https://redd.it/qukyku")
add_data(["Lucy"],
"Lucy",
False,
False,
[
r'{"Lucy ?\\(Lucy"}', '{"100"}', '{"2014"}', 
'{"Scarlett Johansen"}'
],
"",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qukyku/respect_lucy_lucy/

########################################

id = get_rt_id(cur, "Respect Field Marshal Tamas (Powder Mage)", "https://redd.it/qvlid9")
add_data(["Tamas"],
"Tamas",
False,
False,
[
'{"Powder Mage"}'
],
"Powder Mage",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qvlid9/respect_field_marshal_tamas_powder_mage/

########################################

id = get_rt_id(cur, "Respect He Dachun! (Scissor Seven)", "https://redd.it/qy8po0")
add_data(["Dachun"],
"Dachun",
False,
False,
[
'{"Scissor Seven"}', '{"(He|Body(-| )?guard) Dachun"}'
],
"Scissor Seven",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qy8po0/respect_he_dachun_scissor_seven/

########################################

id = get_rt_id(cur, "Respect Seven! (Scissor Seven)", "https://redd.it/qvf4hg")
add_data(["Seven"],
"Seven",
False,
False,
[
'{"Scissor Seven"}'
],
"Scissor Seven",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qvf4hg/respect_seven_scissor_seven/

########################################

id = get_rt_id(cur, "Respect Redtooth! (Scissor Seven)", "https://redd.it/qxi5bf")
add_data(["Redtooth"],
"Redtooth",
False,
False,
[
'{"Scissor Seven"}'
],
"Scissor Seven",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxi5bf/respect_redtooth_scissor_seven/

########################################

id = get_rt_id(cur, "Respect Thirteen! (Scissor Seven)", "https://redd.it/qw3wzz")
add_data(["Thirteen"],
"Thirteen",
False,
False,
[
'{"Scissor Seven"}'
],
"Scissor Seven",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qw3wzz/respect_thirteen_scissor_seven/

########################################

id = get_rt_id(cur, "Respect The Prince of Stan! (Scissor Seven)", "https://redd.it/qwb1g4")
add_data(["Prince of Stan"],
"Prince of Stan",
False,
True,
[
'{"Scissor Seven"}'
],
"Scissor Seven",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qwb1g4/respect_the_prince_of_stan_scissor_seven/

########################################

id = get_rt_id(cur, "Respect Prince Robot IV! (Saga)", "https://redd.it/qw3s1j")
add_data(["Prince Robot IV"],
"Prince Robot IV",
False,
True,
[
'{"Saga"}'
],
"Saga",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qw3s1j/respect_prince_robot_iv_saga/

########################################

add_data(["Static"],
"Static",
False,
False,
[
r'{"\\(New 52\\)"}'
],
"New 52",
'{1872}'
)
#https://www.reddit.com/r/respectthreads/comments/qwd1rd/respect_static_dc_comics_new_52/

########################################

id = get_rt_id(cur, "Respect Armaggon! (Teenage Mutant Ninja Turtles) (Archie Comics)", "https://redd.it/qw3svf")
add_data(["Armaggon"],
"Armaggon",
False,
True,
[
'{"Teenaged? Mutant Ninja Turtles?"}', '{"TMNT"}'
],
"TMNT",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qw3svf/respect_armaggon_teenage_mutant_ninja_turtles/

########################################

id = get_rt_id(cur, "Respect Bass! (Archie Comics)", "https://redd.it/qxlut2")
add_data(["Bass"],
"Bass",
False,
False,
[
r'{"Bass ?\\(Archie"}'
],
"Archie Comics",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxlut2/respect_bass_archie_comics/

########################################

id = get_rt_id(cur, "Respect Basil of Baker Street (The Great Mouse Detective)", "https://redd.it/qwz2kj")
add_data(["Basil of Baker Street"],
"Basil of Baker Street",
False,
False,
[
'{"Great Mouse Detective"}'
],
"The Great Mouse Detective",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qwz2kj/respect_basil_of_baker_street_the_great_mouse/

########################################

id = get_rt_id(cur, "Respect The Lake Guardians (Pokemon Anime)", "https://redd.it/qxl8dq")
add_data(["Lake Guardians?"],
"Lake Guardians",
True,
False,
[
'{"Pok(e|é)m(o|a)n"}'
],
"Pokémon",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxl8dq/respect_the_lake_guardians_pokemon_anime/

add_data(["Uxie"],
"Uxie",
False,
True,
[
'{"Pok(e|é)m(o|a)n"}'
],
"Pokémon",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxl8dq/respect_the_lake_guardians_pokemon_anime/

add_data(["Mesprit"],
"Mesprit",
False,
True,
[
'{"Pok(e|é)m(o|a)n"}'
],
"Pokémon",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxl8dq/respect_the_lake_guardians_pokemon_anime/

add_data(["Azelf"],
"Azelf",
False,
True,
[
'{"Pok(e|é)m(o|a)n"}'
],
"Pokémon",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qxl8dq/respect_the_lake_guardians_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect "The Other" Tokita Niko (Kengan Omega/Asura)', "https://redd.it/qyny1h")
add_data(["Tokita Niko"],
"Tokita Niko",
False,
True,
[
'{"Kengan(verse)?"}'
],
"Kengan Asura",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qyny1h/respect_the_other_tokita_niko_kengan_omegaasura/

########################################

id = get_rt_id(cur, "Respect Achilles (Ben Olding Games)", "https://redd.it/qyv07a")
add_data(["Achilles"],
"Achilles",
False,
False,
[
'{"Ben Olding"}'
],
"Ben Olding Games",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qyv07a/respect_achilles_ben_olding_games/

########################################

id = get_rt_id(cur, "Respect Ultron (Marvel Cinematic Universe: What If...?)", "https://redd.it/qyy5yp")
add_data(["Ultron"],
"Ultron",
False,
False,
[
'{"What( |-)if"}'
],
"MCU: What If...?",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qyy5yp/respect_ultron_marvel_cinematic_universe_what_if/

########################################

id = get_rt_id(cur, "Respect the Ultron Singularity (Marvel Earth-14831)", "https://redd.it/qyzve4")
add_data(["Ultron"],
"Ultron",
False,
False,
[
'{"14831"}'
],
"14831",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qyzve4/respect_the_ultron_singularity_marvel_earth14831/

add_data(["Ultron Singularity"],
"Ultron Singularity",
False,
True,
[
'{"14831"}'
],
"14831",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qyzve4/respect_the_ultron_singularity_marvel_earth14831/

########################################

id = get_rt_id(cur, "Respect Linda-085 (Halo)", "https://redd.it/qz1im2")
add_data(["Linda(-| )085"],
"Linda-085",
False,
False,
[
'{"Halo"}'
],
"Halo",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz1im2/respect_linda085_halo/

########################################

id = get_rt_id(cur, "Respect Azog (The Hobbit films)", "https://redd.it/qz1lc9")
add_data(["Azog"],
"Azog",
False,
False,
[
'{"BOTFA"}', '{"Battle of the Five Armies"}' '{"Hobbit (film|movie)s?"}'
],
"The Hobbit, 2014",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz1lc9/respect_azog_the_hobbit_films/

########################################

id = get_rt_id(cur, "Respect the Dimensional Horror (Stellaris)", "https://redd.it/qz1ncd")
add_data(["Dimensional Horror"],
"Dimensional Horror",
False,
True,
[
'{"Stellaris"}'
],
"Stellaris",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz1ncd/respect_the_dimensional_horror_stellaris/

########################################

id = get_rt_id(cur, "Respect Star and Stripe (My Hero Academia)", "https://redd.it/qz31b6")
add_data(["Star and Stripe"],
"Star and Stripe",
False,
False,
[
'{"My Hero"}', r'{"\\(My Hero\\)"}', '{"(M|BN?)HA"}', '{"Boku no Hero"}',
'{"New Order"}'
],
"My Hero Academia",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz31b6/respect_star_and_stripe_my_hero_academia/

add_data(["Stars and Stripes"],
"Stars and Stripes",
False,
False,
[
'{"My Hero"}', r'{"\\(My Hero\\)"}', '{"(M|BN?)HA"}', '{"Boku no Hero"}',
'{"New Order"}'
],
"My Hero Academia",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qz31b6/respect_star_and_stripe_my_hero_academia/

########################################

id = get_rt_id(cur, "Respect Infinity Man (DC Comics, New 52)", "https://redd.it/qzoonx")
add_data(["Infinity Man"],
"Infinity Man",
False,
False,
[
'{"New(-| )?52"}', '{"Nu?-?52"}', '{"Prime(-| )Earth"}'
],
"New 52",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzoonx/respect_infinity_man_dc_comics_new_52/

########################################

id = get_rt_id(cur, "Respect Therizinosaurus (Dinosaur King)", "https://redd.it/qzvqqk")
add_data(["Therizinosaurus"],
"Therizinosaurus",
False,
False,
[
'{"Dinosaur King"}'
],
"Dinosaur King",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/qzvqqk/respect_therizinosaurus_dinosaur_king/

########################################

add_data(["Reimu"],
"Reimu",
False,
True,
[
'{"Touhou"}', '{"Gensokyo"}'
],
"Touhou",
'{5737}'
)
#https://www.reddit.com/r/respectthreads/comments/r0ei4c/respect_reimu_hakurei_touhou/

########################################

id = get_rt_id(cur, "Ogi Zenin (Jujutsu Kaisen)", "https://redd.it/r0jmyg")
add_data(["Ogi Zenin"],
"Ogi Zenin",
False,
True,
[
'{"Jujus?t?s?u Kaisen"}'
],
"Jujutsu Kaisen",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r0jmyg/ogi_zenin_jujutsu_kaisen/

########################################

id = get_rt_id(cur, "Respect the Unnamed Wolf Kretch (Wardstone Chronicles)", "https://redd.it/r0ubrk")
add_data(["Wolf Kretch"],
"Wolf Kretch",
False,
True,
[
'{"Wardstone Chronicles"}'
],
"Wardstone Chronicles",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r0ubrk/respect_the_unnamed_wolf_kretch_wardstone/

########################################

id = get_rt_id(cur, "Respect Natsuo Ishido (Teppu)", "https://redd.it/r1frew")
add_data(["Natsuo Ishid(ō|o)"],
"Natsuo Ishidō",
False,
True,
[
'{"Teppu"}'
],
"Teppu",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r10ex8/respect_natsuo_ishido_teppu/

########################################

id = get_rt_id(cur, "Respect Cronus (Class of the Titans)", "https://redd.it/r14nzo")
add_data(["Cronus"],
"Cronus",
False,
False,
[
'{"Class of the Titans?"}'
],
"Class of the Titans",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r14nzo/respect_cronus_class_of_the_titans/

########################################

id = get_rt_id(cur, "Respect Mega Man! (Mega Man Megamix/Gigamix)", "https://redd.it/r18kg0")
add_data(["Mega ?Man"],
"Mega Man",
False,
False,
[
'{"Mega Man (Megamix|Gigamix)"}'
],
"Mega Man Megamix",
'{' + f'{id}' +'}'
)
#https://www.reddit.com/r/respectthreads/comments/r18kg0/respect_mega_man_mega_man_megamixgigamix/

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

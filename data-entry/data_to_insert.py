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

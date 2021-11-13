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

id = get_rt_id(cur, "Respect Juumei Kuga (Garouden)", "https://redd.it/qopq57")
add_data(["Juu?mei Kuga"],
"Juumei Kuga",
False,
True,
[
'{"Gar(ō|o)u?den"}'
],
"Garōden",
'{' + '{}'.format(id) +'}'
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

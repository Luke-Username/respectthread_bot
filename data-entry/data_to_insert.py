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

update_respectthread(cur, 23014, 'Respect Death (Darksiders)', 'https://redd.it/102lglw')
update_respectthread(cur, 6122, 'Respect Beowulf! (Beowulf)', 'https://redd.it/103ka0i')
update_respectthread(cur, 6481, 'Respect Ral Zarek! (Magic: The Gathering)', 'https://redd.it/104ctnk')

########################################

id = get_rt_id(cur, 'Respect Togera (War of the Monsters)', 'https://redd.it/100nyzk')
add_data(['Togera'],
'Togera',
False,
False,
[
    ['War of the Monsters']
],
'War of the Monsters',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100nyzk/respect_togera_war_of_the_monsters/

########################################

id = get_rt_id(cur, 'Respect the Ape (A*P*E)', 'https://redd.it/100nzab')
add_data(['Ape'],
'Ape',
False,
False,
[
    ['A\*P\*E']
],
'A*P*E',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100nzab/respect_the_ape_ape/

########################################

id = get_rt_id(cur, 'Respect Nanoha Takamachi (Mahou Shoujo Lyrical Nanoha Movie Canon)', 'https://redd.it/100tgxh')
add_data(['Nanoha Takamachi'],
'Nanoha Takamachi',
False,
True,
[
    ['Mahou Shoujo Lyrical Nanoha'], ['MSLN']
],
'Mahou Shoujo Lyrical Nanoha',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100tgxh/respect_nanoha_takamachi_mahou_shoujo_lyrical/

########################################

id = get_rt_id(cur, 'Respect: Ravage! (Marvel, Earth-616)', 'https://redd.it/100wy3k')
add_data(['Ravage'],
'Ravage',
False,
False,
[
    ['Ravage ?\(616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100wy3k/respect_ravage_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect: Flux! (Marvel, Earth-616)', 'https://redd.it/102k728')
add_data(['Flux'],
'Flux',
False,
False,
[
    ['Flux ?\(616'], ['Benjamin Tibbets', '616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/100wy3k/respect_ravage_marvel_earth616/

########################################

id = get_rt_id(cur, 'Respect Fred Dukes, the Blob (Marvel, 616)', 'https://redd.it/104ueo0')
add_data(['Blob'],
'Blob',
False,
False,
[
    ['Blob ?\(616'], ['Fred Dukes'],
    ['Blob ?\(Marvel( Comics)?\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/104ueo0/respect_fred_dukes_the_blob_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 53: the Squirrel Girlbuster (Marvel, Earth-616)', 'https://redd.it/101rniz')
add_data(['Squirrel Girl ?buster'],
'Squirrel Girlbuster',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/101rniz/respect_iron_man_model_53_the_squirrel_girlbuster/

########################################

id = get_rt_id(cur, 'Respect Squirrelpool (Marvel, 616)', 'https://redd.it/10386ma')
add_data(['Squirrelpool'],
'Squirrelpool',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10386ma/respect_squirrelpool_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Dazzler (Marvel Comics, Earth-616)', 'https://redd.it/106q1t3')
add_data(['Dazzler'],
'Dazzler',
False,
False,
[
    ['616'],
    ['Black Canary', 'Banshee'], ['Jubilee', 'Fireworks?'],
    ['Dazzler vs', 'Black Canary'], ['Black Bolt', 'Sound'],
    ['Jubilee', 'X(-| )?Men']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Captain Barbossa (Pirates of the Caribbean)', 'https://redd.it/1019yk8')
add_data(['Barbossa'],
'Barbossa',
False,
False,
[
    ['Pirates? of the Caribbean'], ['POTC'], ['Captain Barbossa']
],
'Pirates of the Caribbean',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1019yk8/respect_captain_barbossa_pirates_of_the_caribbean/

########################################

id = get_rt_id(cur, 'Respect the Potion (Death Becomes Her)', 'https://redd.it/101fri4')
add_data(['Potion'],
'Potion',
False,
False,
[
    ['Death Becomes Her']
],
'Death Becomes Her',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/101fri4/respect_the_potion_death_becomes_her/

########################################

id = get_rt_id(cur, "Respect Smokin'' Joe Rudeboy! (Tom Cardy)", 'https://redd.it/101kehw')
add_data(["Smokin'' Joe Rudeboy"],
"Smokin'' Joe Rudeboy",
False,
False,
[
    ['Tom Cardy']
],
'Tom Cardy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/101kehw/respect_smokin_joe_rudeboy_tom_cardy/

########################################

id = get_rt_id(cur, 'Respect Klarion the Witch Boy (Young Justice)', 'https://redd.it/101ocee')
add_data(['Klarion'],
'Klarion',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/101ocee/respect_klarion_the_witch_boy_young_justice/

########################################

id = get_rt_id(cur, 'Respect Rebecca! (Cyberpunk: Edgerunners)', 'https://redd.it/101u155')
add_data(['Rebecca'],
'Rebecca',
False,
False,
[
    ['Cyberpunk'], ['Edgerunners']
],
'Cyberpunk',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/101u155/respect_rebecca_cyberpunk_edgerunners/

########################################

id = get_rt_id(cur, 'Respect Rin Kaenbyou (Touhou)', 'https://redd.it/102859k')
add_data(['Rin Kaenbyou'],
'Rin Kaenbyou',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/102859k/respect_rin_kaenbyou_touhou/

########################################

id = get_rt_id(cur, 'Respect Satori Komeiji (Touhou)', 'https://redd.it/1046zat')
add_data(['Satori Komeiji'],
'Satori Komeiji',
False,
True,
[
    ['Touhou']
],
'Touhou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1046zat/respect_satori_komeiji_touhou/

########################################

id = get_rt_id(cur, 'Respect Lightray (DC, New 52/Rebirth)', 'https://redd.it/102g1r3')
add_data(['Lightray'],
'Lightray',
False,
False,
[
    ['DC cosmic'], ['New Gods?']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/102g1r3/respect_lightray_dc_new_52rebirth/

add_data(['Lightray'],
'Lightray',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/102g1r3/respect_lightray_dc_new_52rebirth/

########################################

id = get_rt_id(cur, 'Respect Icon! (Milestone / DC Comics, Post-Crisis)', 'https://redd.it/103ffl0')
add_data(['Icon'],
'Icon',
False,
False,
[
    ['Icon ?\(DC( Comics)?\)'], ['Milestone', 'DC'], ['Milestone Comics?']
],
'DC Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103ffl0/respect_icon_milestone_dc_comics_postcrisis/

add_data(['Icon'],
'Icon',
False,
False,
[
    ['Icon ?\(Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103ffl0/respect_icon_milestone_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Mitchell Shelley, The Resurrection Man! (DC Comics, Post-Crisis)', 'https://redd.it/106c2dn')
add_data(['Resurrection Man'],
'Resurrection Man',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103ffl0/respect_icon_milestone_dc_comics_postcrisis/

add_data(['Resurrection Man'],
'Resurrection Man',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/106c2dn/respect_mitchell_shelley_the_resurrection_man_dc/

########################################

id = get_rt_id(cur, 'Respect Plastique! (DC Comics, Futures End)', 'https://redd.it/103fhqg')
add_data(['Plastique'],
'Plastique',
False,
False,
[
    ['Futures End']
],
'Futures End',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103fhqg/respect_plastique_dc_comics_futures_end/

########################################

id = get_rt_id(cur, 'Respect the Battle Pope! (Battle Pope)', 'https://redd.it/103eork')
add_data(['Battle Pope'],
'Battle Pope',
False,
True,
[
    ['Battle Pope ?\(Battle Pope']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103eork/respect_the_battle_pope_battle_pope/

########################################

id = get_rt_id(cur, 'Respect Consul N (Xenoblade Chronicles 3)', 'https://redd.it/103yfln')
add_data(['Consul N'],
'Consul N',
False,
True,
[
    ['Xenoblade']
],
'Xenoblade',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/103yfln/respect_consul_n_xenoblade_chronicles_3/

########################################

id = get_rt_id(cur, 'Respect Zira! (My Girlfriend is an Orc Warlord)', 'https://redd.it/104boz5')
add_data(['Zira'],
'Zira',
False,
False,
[
    ['Girlfriend is an Orc Warlord']
],
'My Girlfriend is an Orc Warlord',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/104boz5/respect_zira_my_girlfriend_is_an_orc_warlord/

########################################

id = get_rt_id(cur, 'Respect Rakdos! (Magic: The Gathering)', 'https://redd.it/106p35p')
add_data(['Rakdos'],
'Rakdos',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/106p35p/respect_rakdos_magic_the_gathering/

########################################

id = get_rt_id(cur, "Respect: Utopian! (Jupiter''s Legacy)", 'https://redd.it/10513tm')
add_data(['Utopian'],
'Utopian',
False,
False,
[
    ["Jupiter''?s Legacy"], ['Utopian vs|vs\.? Utopian', 'Omni(-| )?Man|Hancock|Homelander'], ['vs\. The Utopian']
],
"Jupiter''s Legacy",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10513tm/respect_utopian_jupiters_legacy/

########################################

id = get_rt_id(cur, 'Respect Touma Kamiyama, aka (Kamen Rider Saber)!', 'https://redd.it/10579c8')
add_data(['Kamen Rider Saber'],
'Kamen Rider Saber',
False,
True,
[
    ['Touma Kamiyama']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/10579c8/respect_touma_kamiyama_aka_kamen_rider_saber/

########################################

id = get_rt_id(cur, 'Respect Art the Clown (Terrifier)', 'https://redd.it/105ontx')
add_data(['Art the Clown'],
'Art the Clown',
False,
True,
[
    ['Terrifier']
],
'Terrifier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/105ontx/respect_art_the_clown_terrifier/

########################################

id = get_rt_id(cur, 'Respect Suguru Geto! (Jujutsu Kaisen)', 'https://redd.it/105sdja')
add_data(['Suguru Geto|Geto Suguru'],
'Suguru Geto',
False,
True,
[
    ['Jujus?t?s?u Kaisen']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/105sdja/respect_suguru_geto_jujutsu_kaisen/

########################################

id = get_rt_id(cur, 'Respect Lucas Kane (Fahrenheit/Indigo Prophecy)', 'https://redd.it/106n0uz')
add_data(['Lucas Kane'],
'Lucas Kane',
False,
True,
[
    ['Fahrenheit'], ['Indigo Prophecy']
],
'Fahrenheit/Indigo Prophecy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/106n0uz/respect_lucas_kane_fahrenheitindigo_prophecy/

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

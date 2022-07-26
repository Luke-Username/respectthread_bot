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

update_respectthread(cur, 3555, "Respect Hol Horse (Jojo''s Bizarre Adventure)", 'https://redd.it/w5sg04')
update_respectthread(cur, 13270, 'Respect Rem (Re:Zero, Anime)', 'https://redd.it/w7omg7')
update_respectthread(cur, 6469, 'Respect Arlinn Kord (Magic the Gathering)', 'https://redd.it/w8887d')

########################################

add_data(['Dante'],
'Dante',
False,
False,
[
    ["Dante ?\(Dante''?s Inferno"]
],
'Dante''?s Inferno',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/w7hopv/dante_dantes_inferno_runs_a_gauntlet/ihjqiye/?context=3

########################################

add_data(['Aizawa'],
'Aizawa',
False,
False,
[
    ['Squid Girl']
],
'Squid Girl',
'{}'
)
#

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['Multiverse of Madness']
],
'MCU',
'{270}'
)
#https://www.reddit.com/r/whowouldwin/comments/w77z3u/multiverse_of_madness_wanda_vs_thanos/ihio5ka/?context=3

add_data(['Thanos'],
'Thanos',
False,
False,
[
    ['Multiverse of Madness']
],
'MCU',
'{263}'
)
#https://www.reddit.com/r/whowouldwin/comments/w77z3u/multiverse_of_madness_wanda_vs_thanos/ihio5ka/?context=3

########################################

add_data(['Darcy'],
'Darcy',
False,
False,
[
    ['Amphibia']
],
'Amphibia',
'{22028}'
)
#https://www.reddit.com/r/whowouldwin/comments/w6bhuz/darcy_with_all_of_her_weapons_amphibia_vs/ihdmy9b/?context=3

########################################
id = get_rt_id(cur, 'Respect Finn (One Punch Finn)', 'https://redd.it/w5ncb0')
add_data(['One Punch Finn'],
'One Punch Finn',
False,
False,
[
    ['QYTvLX0NZog']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w5ncb0/respect_finn_one_punch_finn/

########################################
id = get_rt_id(cur, 'Respect William Adams (Tenkaichi)', 'https://redd.it/w5rfof')
add_data(['William Adams'],
'William Adams',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w5rfof/respect_william_adams_tenkaichi/

########################################
id = get_rt_id(cur, 'Respect Yagyu Munenori (Tenkaichi)', 'https://redd.it/w5rg7b')
add_data(['Yagyu Munenori'],
'Yagyu Munenori',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w5rg7b/respect_yagyu_munenori_tenkaichi/

########################################

id = get_rt_id(cur, 'Respect Mr. Justice (FIGHTERS)', 'https://redd.it/w64ap4')
add_data(['M(iste)?r\.? Justice'],
'Mr. Justice',
False,
False,
[
    ['FIGHTERS']
],
'FIGHTERS',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w64ap4/respect_mr_justice_fighters/

########################################

id = get_rt_id(cur, "Respect Michael Malloy (Sam O''Nella Academy)", 'https://redd.it/w66hmf')
add_data(['Michael Malloy'],
'Michael Malloy',
False,
False,
[
    ['kuYylDsN6KQ'], ['Sam.*Nella']
],
"Sam O''Nella Academy",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w66hmf/respect_michael_malloy_sam_onella_academy/

########################################

id = get_rt_id(cur, 'Respect Makunouchi Ippo! (Hajime no Ippo)', 'https://redd.it/w6atvc')
add_data(['Ippo'],
'Ippo',
False,
False,
[
    ['Makunouchi'], ['Ippo.*Hajime no Ippo'], ['HNI']
],
'Hajime no Ippo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6atvc/respect_makunouchi_ippo_hajime_no_ippo/

########################################

id = get_rt_id(cur, 'Respect Bea! (Pokemon Anime | Pokemon Journeys)', 'https://redd.it/w6bml6')
add_data(['Bea'],
'Bea',
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

id = get_rt_id(cur, "Respect Josuke Higashikata (Crazy Diamond''s Demonic Heartbreak)", 'https://redd.it/w6e6cb')
add_data(['Josuke Higashikata'],
'Josuke Higashikata',
False,
False,
[
    ["Crazy Diamond''s Demonic Heartbreak"]
],
"Crazy Diamond''s Demonic Heartbreak",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6e6cb/respect_josuke_higashikata_crazy_diamonds_demonic/

########################################

id = get_rt_id(cur, "Respect Hol Horse (Crazy Diamond''s Demonic Heartbreak)", 'https://redd.it/w6e6nw')
add_data(['Hol Horse'],
'Hol Horse',
False,
False,
[
    ["Crazy Diamond''s Demonic Heartbreak"]
],
"Crazy Diamond''s Demonic Heartbreak",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6e6nw/respect_hol_horse_crazy_diamonds_demonic/

########################################

id = get_rt_id(cur, 'Respect Fuuko Izumo! (Undead Unluck)', 'https://redd.it/w6ijor')
add_data(['Fuuko Izumo'],
'Fuuko Izumo',
False,
True,
[
    ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6ijor/respect_fuuko_izumo_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Ban, DekaRed (Tokusou Sentai Dekaranger)', 'https://redd.it/w6t2hn')
add_data(['DekaRed'],
'DekaRed',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6t2hn/respect_ban_dekared_tokusou_sentai_dekaranger/

########################################

id = get_rt_id(cur, 'Respect Hoji, DekaBlue (Tokusou Sentai Dekaranger)', 'https://redd.it/w6t2rs')
add_data(['DekaBlue'],
'DekaBlue',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6t2rs/respect_hoji_dekablue_tokusou_sentai_dekaranger/


########################################

id = get_rt_id(cur, 'Respect Sen-chan, DekaGreen (Tokusou Sentai Dekaranger)', 'https://redd.it/w7m15d')
add_data(['DekaGreen'],
'DekaGreen',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w7m15d/respect_senchan_dekagreen_tokusou_sentai/

########################################

id = get_rt_id(cur, 'Respect the Dekaranger Robo (Tokusou Sentai Dekaranger)', 'https://redd.it/w7m208')
add_data(['Dekaranger Robo'],
'Dekaranger Robo',
False,
True,
[
    ['Tokusou Sentai Dekaranger']
],
'Tokusou Sentai Dekaranger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w7m208/respect_the_dekaranger_robo_tokusou_sentai/

########################################

id = get_rt_id(cur, 'Respect Tena Sorimura, The Phantom Solitaire (Dead Mount Death Play)', 'https://redd.it/w6tbyy')
add_data(['Tena Sorimura'],
'Tena Sorimura',
False,
True,
[
    ['Dead Mount Death Play']
],
'Dead Mount Death Play',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6tbyy/respect_tena_sorimura_the_phantom_solitaire_dead/

########################################

id = get_rt_id(cur, 'Respect Hunter! (Five Kingdoms)', 'https://redd.it/w6zjw6')
add_data(['Hunter'],
'Hunter',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w6zjw6/respect_hunter_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect SCP-4128, Action Comics #1 (SCP Foundation)', 'https://redd.it/w715ov')
add_data(['SCP ?(-| )? ?4128'],
'SCP-4128',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w715ov/respect_scp4128_action_comics_1_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect SCP-6599 (SCP Foundation)', 'https://redd.it/w7es0o')
add_data(['SCP ?(-| )? ?6599'],
'SCP-6599',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w7es0o/respect_scp6599_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect the Knights of the Cross (The Dresden Files)', 'https://redd.it/w7ze40')
add_data(['Knights of the Cross'],
'Knights of the Cross',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w7ze40/respect_the_knights_of_the_cross_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect Doctor Cockroach! (Monsters vs. Aliens)', 'https://redd.it/w80yqv')
add_data(['D(octo)?r\.? Cockroach'],
'Doctor Cockroach',
False,
True,
[
    ['Monsters vs?\.? Aliens']
],
'Monsters vs. Aliens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w80yqv/respect_doctor_cockroach_monsters_vs_aliens/

########################################

id = get_rt_id(cur, 'Respect Giovanni Potage (Epithet Erased)', 'https://redd.it/w83uga')
add_data(['Giovanni Potage'],
'Giovanni Potage',
False,
True,
[
    ['Epithet Erased']
],
'Epithet Erased',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/w83uga/respect_giovanni_potage_epithet_erased/

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

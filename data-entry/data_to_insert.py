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

update_respectthread(cur, 5380, 'Respect Inspector Carmelita Fox (Sly Cooper)', 'https://redd.it/tj9sz8')
update_respectthread(cur, 5378, 'Respect Clockwerk (Sly Cooper)', 'https://redd.it/tj9teu')
update_respectthread(cur, 14814, 'Respect Enkidu, the Chain of the Heavens! (Fate)', 'https://redd.it/tjohjx')
update_respectthread(cur, 5379, 'Respect the Cooper Gang (Sly Cooper)', 'https://redd.it/tk19mc')

########################################

add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Tom', 'Tobey', 'Andrew']
],
'Live-Action',
'{302,113,261}'
)
#https://www.reddit.com/r/whowouldwin/comments/tjafk0/quiet_place_monster_vs_xenomorph/

########################################

add_data(['Electro'],
'Electro',
False,
False,
[
    ['No Way Home'], ['NWH']
],
'The Amazing Spider-Man',
'{110}'
)
#https://www.reddit.com/r/whowouldwin/comments/tkeec3/electro_spiderman_no_way_home_vs_ozai_avatar_the/

########################################

add_data(['Mr\.? ?Fahrenheit'],
'Mr. Fahrenheit',
False,
False,
[
    ['Freddie Mercury'], ['stop me Now']
],
'',
'{6428}'
)
#https://www.reddit.com/r/whowouldwin/comments/nvevek/who_is_the_strongest_character_dont_stop_me_now/

########################################

id = get_rt_id(cur, 'Respect Sakura! (Udon Comics Street Fighter)', 'https://redd.it/tja9n3')
add_data(['Sakura Kasugano'],
'Sakura Kasugano',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tja9n3/respect_sakura_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Dhalsim! (Udon Comics Street Fighter)', 'https://redd.it/tjzquv')
add_data(['Dhalsim'],
'Dhalsim',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjzquv/respect_dhalsim_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Blanka! (Udon Comics Street Fighter)', 'https://redd.it/tk0ac6')
add_data(['Blanka'],
'Blanka',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk0ac6/respect_blanka_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Lee (Enter the Dragon)', 'https://redd.it/tjadaw')
add_data(['Lee'],
'Lee',
False,
False,
[
    ['Enter the Dragon']
],
'Enter the Dragon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjadaw/respect_lee_enter_the_dragon/

########################################

id = get_rt_id(cur, 'Respect Master Wei (Avatar: The Legend of Aang Videogame)', 'https://redd.it/tjnlw5')
add_data(['Master Wei'],
'Master Wei',
False,
False,
[
    ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjnlw5/respect_master_wei_avatar_the_legend_of_aang/

########################################

id = get_rt_id(cur, 'Respect The Overconfident Fire Nation Soldier (Avatar: The Last Airbender)', 'https://redd.it/tk3co2')
add_data(['Overconfident Fire Nation Soldier'],
'Overconfident Fire Nation Soldier',
False,
True,
[
    ['Avatar'], ['A?TLA']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk3co2/respect_the_overconfident_fire_nation_soldier/

########################################

id = get_rt_id(cur, 'Respect Jester Karture! (Fate/Strange Fake)', 'https://redd.it/tjokhf')
add_data(['Jester Karture'],
'Jester Karture',
False,
True,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjokhf/respect_jester_karture_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect True Assassin! (Fate/Strange Fake)', 'https://redd.it/tjolma')
add_data(['True Assassin'],
'True Assassin',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjolma/respect_true_assassin_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect True Berserker! (Fate/Strange Fake)', 'https://redd.it/tjome5')
add_data(['True Berserker'],
'True Berserker',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjome5/respect_true_berserker_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect True Rider! (Fate/Strange Fake)', 'https://redd.it/tjon3h')
add_data(['True Rider'],
'True Rider',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjon3h/respect_true_rider_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect True Caster! (Fate/Strange Fake)', 'https://redd.it/tjonuo')
add_data(['True Caster'],
'True Caster',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjonuo/respect_true_caster_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Fake Rider! (Fate/Strange Fake)', 'https://redd.it/tjookf')
add_data(['Fake Rider'],
'Fake Rider',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjookf/respect_fake_rider_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Fake Assassin! (Fate/Strange Fake)', 'https://redd.it/tjoqd3')
add_data(['Fake Assassin'],
'Fake Assassin',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjoqd3/respect_fake_assassin_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Fake Caster! (Fate/Strange Fake)', 'https://redd.it/tjpdnm')
add_data(['Fake Caster'],
'Fake Caster',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjpdnm/respect_fake_caster_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect True Archer! (Fate/Strange Fake)', 'https://redd.it/tk5y0h')
add_data(['True Archer'],
'True Archer',
False,
False,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk5y0h/respect_true_archer_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Hansa Cervantes! (Fate/Strange Fake)', 'https://redd.it/tk7q7v')
add_data(['Hansa Cervantes'],
'Hansa Cervantes',
False,
True,
[
    ['Strange Fake']
],
'Fate/Strange Fake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk7q7v/respect_hansa_cervantes_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Illyasviel von Einzbern! (Fate)', 'https://redd.it/tjpkje')
add_data(['Illya'],
'Illya',
False,
False,
[
    ['Fate'], ['F/?SN'], ['F/?KL']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjpkje/respect_illyasviel_von_einzbern_fate/

add_data(['Illya(sviel)( von)? Einzbern'],
'Illyasviel von Einzbern',
False,
True,
[
    ['Fate'], ['F/?SN'], ['F/?KL']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tjpkje/respect_illyasviel_von_einzbern_fate/

########################################

id = get_rt_id(cur, 'Respect Chloe von Einzbern! (Fate)', 'https://redd.it/tk678m')
add_data(['Chloe'],
'Chloe',
False,
False,
[
    ['Illya(sviel)']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk678m/respect_chloe_von_einzbern_fate/

add_data(['Chloe von Einzbern'],
'Chloe von Einzbern',
False,
False,
[
    ['Illya(sviel)']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk678m/respect_chloe_von_einzbern_fate/

########################################

id = get_rt_id(cur, 'Respect Bazett Fraga McRemitz! (Fate)', 'https://redd.it/tk7rt0')
add_data(['Bazett'],
'Bazett',
False,
False,
[
    ['Fate'], ['Bazett Fraga McRemitz'], ['Holy Grail'], ['Serv(a|e)nts?']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk7rt0/respect_bazett_fraga_mcremitz_fate/

########################################

id = get_rt_id(cur, 'Respect Penelope (Sly Cooper)', 'https://redd.it/tk198u')
add_data(['Penelope'],
'Penelope',
False,
False,
[
    ['Sly']
],
'Sly Cooper',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk198u/respect_penelope_sly_cooper/

########################################

id = get_rt_id(cur, 'Respect Vegeta (Dragon Ball AF, Young Jijii)', 'https://redd.it/tk41uw')
add_data(['Vegeta'],
'Vegeta',
False,
False,
[
    ['Dragon Ball AF']
],
'Dragon Ball AF',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk41uw/respect_vegeta_dragon_ball_af_young_jijii/

########################################

id = get_rt_id(cur, 'Respect Anderson Robotics! (SCP Foundation)', 'https://redd.it/tk675l')
add_data(['Anderson Robotics'],
'Anderson Robotics',
False,
False,
[
    ['SCP']
],
'SCP',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tk675l/respect_anderson_robotics_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect SCP-3008 (SCP Foundation)', 'https://redd.it/tkjoam')
add_data(['SCP ?(-| )? ?3008'],
'SCP-3008',
False,
False,
[
    ['SCP']
],
'SCP',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tkjoam/respect_scp3008_scp_foundation/

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

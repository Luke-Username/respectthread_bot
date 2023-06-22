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

update_respectthread(cur, 4935, 'Respect Captain Harlock [Space Pirate Captain Harlock]', 'https://redd.it/14b2li5')
update_respectthread(cur, 5618, "Respect Heaven Ascension DIO (JoJo''s Bizarre Adventure: Eyes of Heaven)", 'https://redd.it/14bquia')
update_respectthread(cur, 2496, 'Respect the Mangog (Marvel, Earth-616)', 'https://redd.it/14ej1yc')

########################################

add_data(['Kaneki'],
'Kaneki',
False,
False,
[
    ['Tokyo', 'Ghouls?']
],
'Tokyo Ghoul',
'{4964}'
)
#https://www.reddit.com/r/whowouldwin/comments/14bk515/james_heller_discovers_ghouls_in_tokyo_can_he/jog1wu4/?context=3

########################################

add_data(['Guts'],
'Guts',
False,
False,
[
    ['Griffith'], ['Berserker Armor']
],
'Berserk',
'{3076}'
)
#https://www.reddit.com/r/whowouldwin/comments/14do84n/berserker_armor_guts_and_griffith_takes_a_walk_in/joqqbq0/?context=3

########################################

id = get_rt_id(cur, 'Respect SCP-5683 (SCP Foundation)', 'https://redd.it/14axboy')
add_data(['SCP ?(-| )? ?5683'],
'SCP-5683',
False,
True,
[
    ['SCP Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14axboy/respect_scp5683_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect SCP-082, "Fernand" the Cannibal (SCP Foundation)', 'https://redd.it/14c31qo')
add_data(['SCP ?(-| )? ?082'],
'SCP-082',
False,
True,
[
    ['Fernand']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14c31qo/respect_scp082_fernand_the_cannibal_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect SCP-4264 (SCP Foundation)', 'https://redd.it/14erbiz')
add_data(['SCP ?(-| )? ?4264'],
'SCP-4264',
False,
True,
[
    ['Lesson Plans']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14c31qo/respect_scp082_fernand_the_cannibal_scp_foundation/

########################################

id = get_rt_id(cur, 'Respect the Hulk (Hulk, 2003 Video Game Tie-in)', 'https://redd.it/14aw32s')
add_data(['Hulk'],
'Hulk',
False,
False,
[
    ['2003', 'Tie(-| )in', 'games?']
],
'2003, Tie-in game',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Peter Parker, Octo-Spider (Marvel Animated Universe)', 'https://redd.it/14axxwf')
add_data(['Octo(-| )Spider'],
'Octo-Spider',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14axxwf/respect_peter_parker_octospider_marvel_animated/

########################################

id = get_rt_id(cur, 'Respect: Peter Parker, Six-Armed Spider-Man (Marvel Animated Universe)', 'https://redd.it/14bqymb')
add_data(['Six(-| )?Armed Spider(-| )?Man'],
'Six-Armed Spider-Man',
False,
False,
[
    ['Marvel Animated Universe']
],
'Marvel Animated Universe',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14bqymb/respect_peter_parker_sixarmed_spiderman_marvel/

########################################

id = get_rt_id(cur, 'Respect the Inquisitor (Star Wars: Visions - The Bandits of Golak)', 'https://redd.it/14bd71w')
add_data(['The Inquisitor'],
'The Inquisitor',
False,
False,
[
    ['Bandits of Golak']
],
'Star Wars: Visions - The Bandits of Golak',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14axxwf/respect_peter_parker_octospider_marvel_animated/

########################################

id = get_rt_id(cur, 'Respect Yaddle (Star Wars Canon)', 'https://redd.it/14berkm')
add_data(['Yaddle'],
'Yaddle',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14berkm/respect_yaddle_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Ochi of Bestoon (Star Wars Canon)', 'https://redd.it/14cv3k2')
add_data(['Ochi of Bestoon'],
'Ochi of Bestoon',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14cv3k2/respect_ochi_of_bestoon_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Dagan Gera (Star Wars Canon)', 'https://redd.it/14d527g')
add_data(['Dagan Gera'],
'Dagan Gera',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14d527g/respect_dagan_gera_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Enya Keen (Star Wars Canon)', 'https://redd.it/14fr1zq')
add_data(['Enya Keen'],
'Enya Keen',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14fr1zq/respect_enya_keen_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Arkoff (Star Wars Canon)', 'https://redd.it/14fnfd0')
add_data(['Arkoff'],
'Arkoff',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14fnfd0/respect_arkoff_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Kaj Savaros (Star Wars Legends)', 'https://redd.it/14ez0p7')
add_data(['Kaj Savaros'],
'Kaj Savaros',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ez0p7/respect_kaj_savaros_star_wars_legends/

########################################

id = get_rt_id(cur, 'Respect Sav Malagán (Star Wars Canon)', 'https://redd.it/14etzg1')
add_data(['Sav(ina)?( Besatrix)? Malag(á|a)n'],
'Sav Malagán',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14etzg1/respect_sav_malag%C3%A1n_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Oliviah Zeveron (Star Wars Canon)', 'https://redd.it/14ergct')
add_data(['Oliviah Zeveron'],
'Oliviah Zeveron',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ergct/respect_oliviah_zeveron_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Matthea Cathley (Star Wars Canon)', 'https://redd.it/14enxdg')
add_data(['Matthea Cathley'],
'Matthea Cathley',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14enxdg/respect_matthea_cathley_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Vildar Mac (Star Wars Canon)', 'https://redd.it/14dvxak')
add_data(['Vildar Mac'],
'Vildar Mac',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14dvxak/respect_vildar_mac_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Sula Badani (Star Wars Canon)', 'https://redd.it/14dqwt2')
add_data(['Sula Badani'],
'Sula Badani',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14dqwt2/respect_sula_badani_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Kureha Shinogi (Grappler Baki)', 'https://redd.it/14c4jef')
add_data(['Kureha Shinogi'],
'Kureha Shinogi',
False,
True,
[
    ['Baki(verse)?']
],
'Baki',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14c4jef/respect_kureha_shinogi_grappler_baki/

########################################

id = get_rt_id(cur, 'Respect The Big Guy (Big Guy and Rusty the Boy Robot)', 'https://redd.it/14ddy7n')
add_data(['Big Guy'],
'Big Guy',
False,
False,
[
    ['Big Guy and Rusty']
],
'Big Guy and Rusty the Boy Robot',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ddy7n/respect_the_big_guy_big_guy_and_rusty_the_boy/

########################################

id = get_rt_id(cur, 'Respect Roger Goshaw, the Agent Orange (Marvel, 616)', 'https://redd.it/14eky26')
add_data(['Roger Goshaw'],
'Roger Goshaw',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14eky26/respect_roger_goshaw_the_agent_orange_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Thia Escardos! (Fate/Strange Fake)', 'https://redd.it/14ehc3h')
add_data(['Thia Escardos'],
'Thia Escardos',
False,
True,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14ehc3h/respect_thia_escardos_fatestrange_fake/

########################################

id = get_rt_id(cur, 'Respect Ain & Binz (One Piece)', 'https://redd.it/14dyxyy')
add_data(['Ain (&|and) Binz'],
'Ain & Binz',
True,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14dyxyy/respect_ain_binz_one_piece/

########################################

id = get_rt_id(cur, 'Respect Showa Godzilla (Slick)', 'https://redd.it/14epq53')
add_data(['Showa Godzilla'],
'Showa Godzilla',
False,
False,
[
    ['Slick']
],
'Slick',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/14epq53/respect_showa_godzilla_slick/

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

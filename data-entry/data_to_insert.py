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

update_respectthread(cur, 6252, 'Respect Gilgamesh, the King of Heroes! (Fate)', 'https://redd.it/trgl81')
update_respectthread(cur, 3950, 'Respect Itachi Uchiha! (Naruto)', 'https://redd.it/tt3h7t')

########################################

add_data(['Rex'],
'Rex',
False,
False,
[
    ['Dog N....']
],
'Dog Nigga',
'{7531}'
)
#https://www.reddit.com/r/respectthreads/comments/lem62k/respect_dog_nigga_dog_nigga/

########################################

add_data(['Ghost'],
'Ghost',
False,
False,
[
    ['Ghost ?\\(MCU']
],
'MCU',
'{6502}'
)
#https://www.reddit.com/r/whowouldwin/comments/tryjpt/tai_lung_kung_fu_panda_vs_captain_america_mcu/i2p2cx1/?context=3

########################################

add_data(['Teen Titans'],
'Teen Titans',
False,
False,
[
    ['Teen Titans.*CN'], ['CN.*Teen Titans']
],
'Teen Titans',
'{977}'
)
#https://www.reddit.com/r/whowouldwin/comments/ts1a7e/knd_kids_next_door_vs_teen_titans_cn/i2oubh5/?context=3

########################################

add_data(['Bloodshot'],
'Bloodshot',
False,
False,
[
    ['Bloodshot ?\\(Bloodshot']
],
'2020',
'{10806}'
)
#https://www.reddit.com/r/whowouldwin/comments/ts1a7e/knd_kids_next_door_vs_teen_titans_cn/i2oubh5/?context=3
#https://www.reddit.com/r/whowouldwin/comments/ts5138/bloodshot_bloodshot_vs_wolverine_fox_xmen/i2perdc/?context=3

########################################

add_data(['Simon the Digger'],
'Simon the Digger',
False,
True,
[
    ['Gurren Lagann']
],
'Gurren Lagann',
'{4573}'
)
#https://www.reddit.com/r/whowouldwin/comments/tsgv44/simon_the_digger_vs_white_lantern_kyle_rayner/i2r92cs/?context=3

########################################

id = get_rt_id(cur, "Respect Dorshe, the Queen''s Shield! (Ranking of Kings)", 'https://redd.it/tra18s')
add_data(['Dorshe'],
'Dorshe',
False,
False,
[
    ['Ranking of Kings'], ['Ousama Ranking']
],
'Ranking of Kings',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tra18s/respect_dorshe_the_queens_shield_ranking_of_kings/

########################################

id = get_rt_id(cur, 'Respect Bojji! (Ousama Ranking)', 'https://redd.it/tt2hb1')
add_data(['Bojji'],
'Bojji',
False,
False,
[
    ['Ranking of Kings'], ['Ousama Ranking']
],
'Ranking of Kings',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tt2hb1/respect_bojji_ousama_ranking/

########################################

id = get_rt_id(cur, 'Respect Miyu Edelfelt! (Fate)', 'https://redd.it/trflwc')
add_data(['Miyu Edelfelt'],
'Miyu Edelfelt',
False,
True,
[
    ['Fate'], ['Kaleid']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trflwc/respect_miyu_edelfelt_fate/

########################################

id = get_rt_id(cur, 'Respect U-Olga Marie Animusphere, the Foreign God and Seventh Beast of Humanity! (Fate)', 'https://redd.it/trfn9y')
add_data(['U-Olga'],
'U-Olga',
False,
True,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfn9y/respect_uolga_marie_animusphere_the_foreign_god/

########################################

id = get_rt_id(cur, 'Respect Captain Nemo! (Fate)', 'https://redd.it/trfo25')
add_data(['Captain Nemo'],
'Captain Nemo',
False,
False,
[
    ['Fate'], ['Grande? Order'], ['F(ate )?/?GO']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfo25/respect_captain_nemo_fate/

########################################

id = get_rt_id(cur, 'Respect Ashiya Douman! (Fate)', 'https://redd.it/trfp8r')
add_data(['Ashiya D(ō|o)u?man'],
'Ashiya Dōman',
False,
False,
[
    ['Fate']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfp8r/respect_ashiya_douman_fate/

########################################

id = get_rt_id(cur, 'Respect the Dioscuri! (Fate)', 'https://redd.it/trfpzu')
add_data(['Dioscuri'],
'Dioscuri',
False,
False,
[
    ['Fate'], ['Grande? Order']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfpzu/respect_the_dioscuri_fate/

########################################

id = get_rt_id(cur, 'Respect Ivan the Terrible, the Thunderous Emperor! (Fate)', 'https://redd.it/trfqxt')
add_data(['Ivan the Terrible'],
'Ivan the Terrible',
False,
False,
[
    ['Fate'], ['Grande? Order']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfqxt/respect_ivan_the_terrible_the_thunderous_emperor/

########################################

id = get_rt_id(cur, 'Respect Scathach-Skadi! (Fate)', 'https://redd.it/trfrlm')
add_data(['Scathach(-| )Skadi'],
'Scathach-Skadi',
False,
True,
[
    ['Fate'], ['Grande? Order']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfrlm/respect_scathachskadi_fate/

########################################

id = get_rt_id(cur, 'Respect Qin Shi Huang Di, the Son of Heaven! (Fate)', 'https://redd.it/trfs6o')
add_data(['Qin Shi Huang'],
'Qin Shi Huang',
False,
False,
[
    ['Fate'], ['Grande? Order']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trfs6o/respect_qin_shi_huang_di_the_son_of_heaven_fate/

########################################

id = get_rt_id(cur, 'Respect Zeus, the King of the Gods! (Fate)', 'https://redd.it/trftkr')
add_data(['Zeus'],
'Zeus',
False,
False,
[
    ['Zeus.*Grande? Order']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/trftkr/respect_zeus_the_king_of_the_gods_fate/

########################################

id = get_rt_id(cur, 'Respect Zeus, the King of the Gods! (Fate)', 'https://redd.it/trftkr')
add_data(['Princess Bean'],
'Princess Bean',
False,
False,
[
    ['Disenchantment']
],
'Disenchantment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ts3uf4/respect_princess_bean_disenchantment/

add_data(['Bean'],
'Bean',
False,
False,
[
    ['Disenchantment']
],
'Disenchantment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ts3uf4/respect_princess_bean_disenchantment/

add_data(['Tiabeanie'],
'Tiabeanie',
False,
True,
[
    ['Disenchantment']
],
'Disenchantment',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ts3uf4/respect_princess_bean_disenchantment/


########################################

id = get_rt_id(cur, 'Respect Makoto! (Udon Comics Street Fighter)', 'https://redd.it/ts6eda')
add_data(['Makoto'],
'Makoto',
False,
False,
[
    ['Street Fighter', 'UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ts6eda/respect_makoto_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Ryu! (Street Fighter Comics)', 'https://redd.it/ttk9na')
add_data(['Ryu'],
'Ryu',
False,
False,
[
    ['Street Fighter Comics']
],
'Street Fighter Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/ttk9na/respect_ryu_street_fighter_comics/

########################################

id = get_rt_id(cur, 'Respect Rainbow Mika! (Udon Comics Street Fighter)', 'https://redd.it/tt08su')
add_data(['Rainbow Mika'],
'Rainbow Mika',
False,
False,
[
    ['UDON']
],
'UDON',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tt08su/respect_rainbow_mika_udon_comics_street_fighter/

########################################

id = get_rt_id(cur, 'Respect Alternate World Ash, Dawn, Goh, and Chloe (Pokemon Anime)', 'https://redd.it/tsaeae')
add_data(['Alternate World Ash'],
'Alternate World Ash',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tsaeae/respect_alternate_world_ash_dawn_goh_and_chloe/

########################################

id = get_rt_id(cur, 'Respect Alternate World Team Rocket (Pokemon Anime)', 'https://redd.it/tsaebb')
add_data(['Alternate World Team Rocket'],
'Alternate World Team Rocket',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tsaebb/respect_alternate_world_team_rocket_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Lara Croft! (Lara Croft: Tomb Raider)', 'https://redd.it/tse2cz')
add_data(['Lara Croft'],
'Lara Croft',
False,
False,
[
    ['2001'], ['Lara Croft: Tomb Raider']
],
'Lara Croft: Tomb Raider',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tse2cz/respect_lara_croft_lara_croft_tomb_raider/

########################################

id = get_rt_id(cur, "Respect Thunder McQueen and his stand, Highway to Hell (JoJo''s Bizarre Adventure)", 'https://redd.it/tsfz85')
add_data(['Thunder McQueen'],
'Thunder McQueen',
False,
True,
[
    ['Jojos?(verse)?'], ['JJBA']
],
'Jojo''s Bizarre Adventure',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Thundarr the Barbarian! (Thundarr the Barbarian)', 'https://redd.it/tsx3jv')
add_data(['Thundarr the Barbarian'],
'Thundarr the Barbarian',
False,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tsx3jv/respect_thundarr_the_barbarian_thundarr_the/

########################################

id = get_rt_id(cur, 'Respect Man Ray! (Spongebob Squarepants)', 'https://redd.it/tt37jd')
add_data(['Man(-| )?Ray'],
'Man Ray',
False,
False,
[
    ['SpongeBob'], ['Patrick'], ['Mermaid Man'], ['Barnacle Boy']
],
'SpongeBob',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tt37jd/respect_man_ray_spongebob_squarepants/

########################################

id = get_rt_id(cur, 'Respect Devil Ray (DC New 52/Rebirth)', 'https://redd.it/tt39rz')
add_data(['Devil Ray'],
'Devil Ray',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tt39rz/respect_devil_ray_dc_new_52rebirth/

########################################

id = get_rt_id(cur, 'Respect Molly Hernandez (Runaways/Marvel Cinematic Universe)', 'https://redd.it/tt886e')
add_data(['Molly Hernandez'],
'Molly Hernandez',
False,
False,
[
    ['Runaways'], ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tt886e/respect_molly_hernandez_runawaysmarvel_cinematic/

########################################

id = get_rt_id(cur, 'Respect Shirou Emiya! (Illyaverse)', 'https://redd.it/tthy2f')
add_data(['Shirou'],
'Emiya Shirou',
False,
False,
[
    ['Illyaverse']
],
'Illyaverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/tthy2f/respect_shirou_emiya_illyaverse/

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

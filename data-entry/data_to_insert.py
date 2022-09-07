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

update_respectthread(cur, 2272, 'Respect Adrian Toomes, the Vulture! (Marvel, Earth-616)', 'https://redd.it/x547gi')

########################################

add_data(['Mob'],
'Mob',
False,
False,
[
    ['Mob.*Mob Psycho 100']
],
'Mob Psycho 100',
'{3906,3905}'
)
#https://www.reddit.com/r/whowouldwin/comments/x3vo8t/mob_from_mob_psycho_100_vs_saiki_kusuo_from_saikik/

########################################

add_data(['Bane'],
'Bane',
False,
False,
[
    ['Bane.*Venom']
],
'DC',
'{1529,1530}'
)
#https://www.reddit.com/r/whowouldwin/comments/x70clo/who_would_win_captain_america_or_bane/in9tkt3/?context=3

########################################

add_data(['Predator'],
'Predator',
False,
False,
[
    ['Xenomorphs?']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/x4pk6r/thanos_vs_horror_characters/imwln9z/?context=3

add_data(['Predators'],
'Predators',
False,
False,
[
    ['Xenomorphs?']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/x4pk6r/thanos_vs_horror_characters/imwln9z/?context=3

########################################

add_data(['Luban'],
'Luban',
False,
False,
[
    ['Leprechaun']
],
'Leprechaun film series',
'{9214}'
)
#

########################################

id = get_rt_id(cur, "Respect Red (Genndy Tartakovsky''s Primal)", 'https://redd.it/x2tj7n')
add_data(['Red'],
'Red',
False,
False,
[
    ['Primal', 'Tartakovskys?']
],
'Primal',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2tj7n/respect_red_genndy_tartakovskys_primal/

########################################

id = get_rt_id(cur, 'Respect Crazy Jane (DC, Post-Crisis)', 'https://redd.it/x2vo6s')
add_data(['Crazy Jane'],
'Crazy Jane',
False,
True,
[
    ['Doom Patrol'], ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2vo6s/respect_crazy_jane_dc_postcrisis/

add_data(['Crazy Jane'],
'Crazy Jane',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2vo6s/respect_crazy_jane_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect the Lord God (Pearl of Great Price)', 'https://redd.it/x2w7cd')
add_data(['God'],
'God',
False,
False,
[
    ['Pearl of Great Price']
],
'Pearl of Great Price',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2w7cd/respect_the_lord_god_pearl_of_great_price/

########################################

id = get_rt_id(cur, 'Respect Captain Falcon (DEATH BATTLE!)', 'https://redd.it/x2wqc1')
add_data(['Ca?pt(ain)?\.? Falcon'],
'Captain Falcon',
False,
False,
[
    ['DEATH BATTLE']
],
'DEATH BATTLE!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x2wqc1/respect_captain_falcon_death_battle/

########################################

id = get_rt_id(cur, 'Respect Spider-Man! (Spider-Man: The Animated Series 1994)', 'https://redd.it/s5f4c4')
add_data(['Spider(-| )?Mans?'],
'Spider-Man',
False,
False,
[
    ['Animated', '1994'], ['Spider(-| )?Man:? The Animated Series']
],
'Spider-Man: The Animated Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Davriel Cane (Magic: The Gathering)', 'https://redd.it/x3olht')
add_data(['Davriel Cane'],
'Davriel Cane',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x3olht/respect_davriel_cane_magic_the_gathering/

########################################

id = get_rt_id(cur, 'Respect Tlano, The Batman of Zur-En-Arrh (DC, Pre-Crisis)', 'https://redd.it/x41kbh')
add_data(['Tlano'],
'Tlano',
False,
False,
[
    ['Pre(-| )?Crisis'], ['Batman of Zur(-| )En(-| )Arrh']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x41kbh/respect_tlano_the_batman_of_zurenarrh_dc_precrisis/

########################################

id = get_rt_id(cur, 'Respect Roron Corobb (Star Wars Legends)', 'https://redd.it/x4ay0q')
add_data(['Roron Corobb'],
'Roron Corobb',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Foul Moudama (Star Wars Legends)', 'https://redd.it/x52v7n')
add_data(['Foul Moudama'],
'Foul Moudama',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x52v7n/respect_foul_moudama_star_wars_legends/

########################################

id = get_rt_id(cur, 'Respect the Illuminati (Marvel Cinematic Universe, Earth-838)', 'https://redd.it/x4mlxv')
add_data(['Illuminati'],
'Illuminati',
True,
False,
[
    ['Marvel Cinematic Universe'], ['MCU'], ['838'], ['DS:? ?MOM'], ['Multiverse of Madness']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kirk Langstrom, the Man-Bat! (DC, Post-Crisis)', 'https://redd.it/x547ez')
add_data(['Man(-| )?Bat'],
'Man-Bat',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x547ez/respect_kirk_langstrom_the_manbat_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Stegosaurus (Dinosaur King)', 'https://redd.it/x5ece6')
add_data(['Stegosaurus'],
'Stegosaurus',
False,
False,
[
    ['Dinosaur King']
],
'Dinosaur King',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Feral Predator (Prey)', 'https://redd.it/x5nnz1')
add_data(['Feral Predator'],
'Feral Predator',
False,
True,
[
    ['Prey']
],
'Prey',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x5nnz1/respect_the_feral_predator_prey/

########################################

id = get_rt_id(cur, 'Respect Naru (Prey)', 'https://redd.it/x5nou2')
add_data(['Naru'],
'Naru',
False,
False,
[
    ['Prey']
],
'Prey',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x5nou2/respect_naru_prey/

########################################

id = get_rt_id(cur, 'Respect Kefka! (Final Fantasy)', 'https://redd.it/x5t27t')
add_data(['Kefka'],
'Kefka',
False,
True,
[
    ['Final Fantasy'], ['FF'], ['FF\d\d?']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x5t27t/respect_kefka_final_fantasy/

########################################

id = get_rt_id(cur, 'Respect Neru (Camprul: The Prul Campaign)', 'https://redd.it/x5z4g0')
add_data(['Neru'],
'Neru',
False,
False,
[
    ['Camprul'], ['Prul Campaign']
],
'Camprul: The Prul Campaign',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x5z4g0/respect_neru_camprul_the_prul_campaign/

########################################

id = get_rt_id(cur, 'Respect Aril Leewings (Camprul: The Prul Campaign)', 'https://redd.it/x6kh4m')
add_data(['Ari Leewings'],
'Ari Leewings',
False,
True,
[
    ['Camprul'], ['Prul Campaign']
],
'Camprul: The Prul Campaign',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6kh4m/respect_aril_leewings_camprul_the_prul_campaign/

########################################

id = get_rt_id(cur, 'Respect Munchy (Road to Radcon)', 'https://redd.it/x63mcc')
add_data(['Munchy'],
'Munchy',
False,
False,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x63mcc/respect_munchy_road_to_radcon/

########################################

id = get_rt_id(cur, 'Respect Brad Garlinghouse (Road to Radcon)', 'https://redd.it/x63mrk')
add_data(['Brad Garlinghouse'],
'Brad Garlinghouse',
False,
False,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x63mrk/respect_brad_garlinghouse_road_to_radcon/

########################################

id = get_rt_id(cur, 'Respect Ben Saint (Road to Radcon)', 'https://redd.it/x63n7w')
add_data(['Ben Saint'],
'Ben Saint',
False,
True,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jacked Pumpk (Road to Radcon)', 'https://redd.it/x63nmz')
add_data(['Jacked Pumpk'],
'Jacked Pumpk',
False,
False,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x63nmz/respect_jacked_pumpk_road_to_radcon/

########################################

id = get_rt_id(cur, 'Respect Digibro (Road to Radcon)', 'https://redd.it/x63o20')
add_data(['Digibro'],
'Digibro',
False,
True,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x63o20/respect_digibro_road_to_radcon/

########################################

id = get_rt_id(cur, 'Respect Tom (Road to Radcon)', 'https://redd.it/x63ocd')
add_data(['Tom'],
'Tom',
False,
False,
[
    ['Road to Radcon']
],
'Road to Radcon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x63ocd/respect_tom_road_to_radcon/

########################################

id = get_rt_id(cur, 'Respect The Bombers: Genthru, Sub, and Bara (Hunter x Hunter)', 'https://redd.it/x64dhq')
add_data(['Genthru'],
'Genthru',
False,
False,
[
    ['Hunter ?(x ?)?Hunter'], ['HxH']
],
'Hunter x Hunter',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x64dhq/respect_the_bombers_genthru_sub_and_bara_hunter_x/

########################################

id = get_rt_id(cur, 'Respect Big Al (Walking With Dinosaurs)', 'https://redd.it/x6cd00')
add_data(['Big Al'],
'Big Al',
False,
False,
[
    ['Walking With Dinosaurs']
],
'Walking With Dinosaurs',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6cd00/respect_big_al_walking_with_dinosaurs/

########################################

id = get_rt_id(cur, 'Respect Aquaman (Orin, Young Justice)', 'https://redd.it/x6hkgc')
add_data(['Aqua(-| )?man'],
'Aquaman',
False,
False,
[
    ['Aqua(-| )?man ?\(Young Justice'], ['Aqua(-| )?man from Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6hkgc/respect_aquaman_orin_young_justice/

########################################

id = get_rt_id(cur, 'Respect Grail, The Daughter of Darkseid (DC, New 52/Rebirth)', 'https://redd.it/x6ksce')
add_data(['Grail'],
'Grail',
False,
False,
[
    ['Grail ?\(DC'], ['Darkseid', 'DC']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6ksce/respect_grail_the_daughter_of_darkseid_dc_new/

add_data(['Grail'],
'Grail',
False,
False,
[
    ['Grail.*New 52'], ['Grail ?\(Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6ksce/respect_grail_the_daughter_of_darkseid_dc_new/

########################################

id = get_rt_id(cur, 'Respect Vampire Batman (Batman: The Brave and the Bold)', 'https://redd.it/x6rott')
add_data(['Vampire Batman'],
'Vampire Batman',
False,
False,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6rott/respect_vampire_batman_batman_the_brave_and_the/

########################################

id = get_rt_id(cur, 'Respect Bat Monolith! (Batman: The Brave and the Bold)', 'https://redd.it/x7u1b1')
add_data(['Bat(-| )Monolith'],
'Bat Monolith',
False,
True,
[
    ['Brave (and|&) the Bold']
],
'The Brave and the Bold',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7u1b1/respect_bat_monolith_batman_the_brave_and_the_bold/

########################################

id = get_rt_id(cur, 'Respect the Warrior Lady (Yu-Gi-Oh! Card Game)', 'https://redd.it/x6x5lt')
add_data(['Warrior Lady'],
'Warrior Lady',
False,
False,
[
    ['Warrior Lady of the Wasteland'], ['Yu(-| )?Gi(-| )?Oh']
],
'Yu-Gi-Oh!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6x5lt/respect_the_warrior_lady_yugioh_card_game/

########################################

id = get_rt_id(cur, 'Respect Galactus (Fortnite)', 'https://redd.it/x6zhjf')
add_data(['Galactus'],
'Galactus',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6zhjf/respect_galactus_fortnite/

########################################

id = get_rt_id(cur, 'Respect the Scientist (Fortnite)', 'https://redd.it/x7jedc')
add_data(['The Scientist'],
'The Scientist',
False,
False,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7jedc/respect_the_scientist_fortnite/

########################################

id = get_rt_id(cur, 'Respect Meowscles! (Fortnite)', 'https://redd.it/x7hupg')
add_data(['Meowscles'],
'Meowscles',
False,
True,
[
    ['Fortnite']
],
'Fortnite',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7hupg/respect_meowscles_fortnite/

########################################

id = get_rt_id(cur, 'Respect: Thor Odinson! (Ultimate Avengers)', 'https://redd.it/x6sxyg')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['Ultimate Avengers']
],
'Ultimate Avengers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6sxyg/respect_thor_odinson_ultimate_avengers/

########################################

id = get_rt_id(cur, 'Respect Bio-Ship (Young Justice)', 'https://redd.it/x6ztvd')
add_data(['Bio-Ship'],
'Bio-Ship',
False,
False,
[
    ['Young Justice']
],
'Young Justice',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x6ztvd/respect_bioship_young_justice/

########################################

id = get_rt_id(cur, 'Respect Malcolm Merlyn (DC, Post-Crisis)', 'https://redd.it/x7chbs')
add_data(['Merlyn'],
'Merlyn',
False,
False,
[
    ['Posts?(-| )?C(risis)?']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7chbs/respect_malcolm_merlyn_dc_postcrisis/

add_data(['Merlyn'],
'Merlyn',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7chbs/respect_malcolm_merlyn_dc_postcrisis/

add_data(['Malcolm Merlyn'],
'Malcolm Merlyn',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7chbs/respect_malcolm_merlyn_dc_postcrisis/

add_data(['Malcolm Merlyn'],
'Malcolm Merlyn',
False,
False,
[
    ['(Fl)?arrow(-| )?verse'], ['(DC)?CW'], ['DC ?TV']
],
'CW Arrowverse',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/x7chbs/respect_malcolm_merlyn_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect George Dyke, The Gorilla Boss of Gotham City (DC, Pre-Crisis)', 'https://redd.it/x7q3je')
add_data(['George Dyke'],
'George Dyke',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7q3je/respect_george_dyke_the_gorilla_boss_of_gotham/

########################################

id = get_rt_id(cur, 'Respect The Grapplers! (Marvel 616)', 'https://redd.it/x7jm5d')
add_data(['The Grapplers'],
'The Grapplers',
True,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7jm5d/respect_the_grapplers_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Pulsemon (Digimon Project)', 'https://redd.it/x7v8x0')
add_data(['Pulsemon'],
'Pulsemon',
False,
False,
[
    ['Digimon Project']
],
'Digimon Project',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7v8x0/respect_pulsemon_digimon_project/

########################################

id = get_rt_id(cur, 'Respect RizeGreymon (Digimon Project)', 'https://redd.it/x7v8yu')
add_data(['RizeGreymon'],
'RizeGreymon',
False,
False,
[
    ['Digimon Project']
],
'Digimon Project',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/x7v8yu/respect_rizegreymon_digimon_project/

########################################

id = get_rt_id(cur, 'Respect BlackWarGreymon (Digimon Project)', 'https://redd.it/x7vdna')
add_data(['BlackWarGreymon'],
'BlackWarGreymon',
False,
False,
[
    ['Digimon Project']
],
'Digimon Project',
'{' + '{}'.format(id) + '}'
)
#

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

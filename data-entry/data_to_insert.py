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

update_respectthread(cur, 23150, 'Respect Nagi Tahira (Tank Chair)', 'https://redd.it/11xvbwl')

########################################

add_data(['Hanayama'],
'Hanayama',
False,
False,
[
    ['Baki']
],
'Baki',
'{7413}'
)
#https://www.reddit.com/r/whowouldwin/comments/11wizj1/fatgum_mha_vs_hanayama_baki/jcy4v0a/?context=3

########################################

add_data(['Doc Oc'],
'Doc Oc',
False,
True,
[
    ['616']
],
'616',
'{2267}'
)
#https://www.reddit.com/r/whowouldwin/comments/11wigg4/who_wins_this_fight_cyclops_vs_sinister_six/jd0jgzi/?context=3


########################################

add_data(['Electro'],
'Electro',
False,
False,
[
    ['Sinister Six']
],
'616',
'{2268}'
)
#https://www.reddit.com/r/whowouldwin/comments/11wigg4/who_wins_this_fight_cyclops_vs_sinister_six/jd0jgzi/?context=3

########################################

add_data(['Cyclops'],
'Cyclops',
False,
False,
[
    ['Sinister Six'], ['X-Mansion']
],
'616',
'{2354}'
)
#

########################################

add_data(['Wanda'],
'Wanda',
False,
False,
[
    ['Wanda ?\( ?MOM ?\)']
],
'MCU',
'{270}'
)
#https://www.reddit.com/r/whowouldwin/comments/11xaf4p/could_jesusthe_holy_bible_convince_wanda_mom_to/jd240xe/?context=3

########################################

id = get_rt_id(cur, 'Respect Granolah (Dragon Ball Super)', 'https://redd.it/11tv732')
add_data(['Granolah'],
'Granolah',
False,
True,
[
    ['Dragon ?Ball'], ['DB(Z|S)']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11tv732/respect_granolah_dragon_ball_super/

########################################

id = get_rt_id(cur, 'Respect Batman (Scooby Doo)', 'https://redd.it/11tw3ps')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Scooby(-| )?Doo']
],
'Scooby-Doo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11tw3ps/respect_batman_scooby_doo/

########################################

id = get_rt_id(cur, 'Respect Pukin! (Magical Girl Raising Project)', 'https://redd.it/11ubu77')
add_data(['Pukin'],
'Pukin',
False,
False,
[
    ['Magical Girl Raising Project'], ['Mahou Shoujo Ikusei Keikaku']
],
'Magical Girl Raising Project',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ubu77/respect_pukin_magical_girl_raising_project/

########################################

id = get_rt_id(cur, 'Respect Menma Uzumaki! (Road to Ninja: Naruto the Movie)', 'https://redd.it/11ubxkt')
add_data(['Menma Uzu?maki'],
'Menma Uzumaki',
False,
True,
[
    ['Naruto']
],
'Naruto',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ubxkt/respect_menma_uzumaki_road_to_ninja_naruto_the/

########################################

id = get_rt_id(cur, 'Respect Minos Prime (Ultrakill)', 'https://redd.it/11v3tbg')
add_data(['Minos Prime'],
'Minos Prime',
False,
True,
[
    ['ULTRAKILL']
],
'ULTRAKILL',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11v3tbg/respect_minos_prime_ultrakill/

########################################

id = get_rt_id(cur, 'Respect Chaos! (Primal Rage)', 'https://redd.it/11vahle')
add_data(['Chaos'],
'Chaos',
False,
False,
[
    ['Primal Rage']
],
'Primal Rage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11vahle/respect_chaos_primal_rage/

########################################

id = get_rt_id(cur, 'Respect Jon (Fist of the B0rf Star)', 'https://redd.it/11vhvx6')
add_data(['Jon'],
'Jon',
False,
False,
[
    ['Fist of the B(0|o)rf Star']
],
'Fist of the B0rf Star',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11vhvx6/respect_jon_fist_of_the_b0rf_star/

########################################

id = get_rt_id(cur, 'Respect Calvin and Hobbs (Fist of the B0rf Star)', 'https://redd.it/120vgro')
add_data(['Calvin (and|&) Hobbes'],
'Calvin and Hobbes',
False,
True,
[
    ['Fist of the B(0|o)rf Star']
],
'Fist of the B0rf Star',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120vgro/respect_calvin_and_hobbs_fist_of_the_b0rf_star/

########################################

id = get_rt_id(cur, 'Respect Flandre Scarlet (minusT Animations)', 'https://redd.it/11vkvmb')
add_data(['Flandre Scarlet'],
'Flandre Scarlet',
False,
False,
[
    ['minusT']
],
'minusT',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11vkvmb/respect_flandre_scarlet_minust_animations/

########################################

id = get_rt_id(cur, 'Respect krypto the Superdog (Krypto the Superdog)', 'https://redd.it/11vnbmx')
add_data(['Krypto the Superdog'],
'Krypto the Superdog',
False,
False,
[
    ['2005']
],
'2005',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11vnbmx/respect_krypto_the_superdog_krypto_the_superdog/

########################################

id = get_rt_id(cur, 'Kurozumi Orochi (One Piece)', 'https://redd.it/11wxta2')
add_data(['Kurozumi Orochi'],
'Kurozumi Orochi',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11wxta2/kurozumi_orochi_one_piece/

########################################

id = get_rt_id(cur, 'Respect Leo (One Piece)', 'https://redd.it/11vs91b')
add_data(['Leo'],
'Leo',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11vs91b/respect_leo_one_piece/

########################################

id = get_rt_id(cur, 'Respect the Godzilla Family (Godzilla Neo)', 'https://redd.it/11wkhnt')
add_data(['Godzilla Family'],
'Godzilla Family',
True,
False,
[
    ['Godzilla Neo']
],
'Godzilla Neo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11wkhnt/respect_the_godzilla_family_godzilla_neo/

########################################

id = get_rt_id(cur, 'Respect Crystal (Pokemon Adventures)', 'https://redd.it/11wlx92')
add_data(['Crystal'],
'Crystal',
False,
False,
[
    ['Pok(e|é)m(o|a)n Adventures']
],
'Pokémon Adventures',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11wlx92/respect_crystal_pokemon_adventures/

########################################

id = get_rt_id(cur, 'Respect the Gorillaz (Gorillaz)', 'https://redd.it/11wt8vr')
add_data(['Gorillaz'],
'Gorillaz',
True,
True,
[
    ['\(Gorillaz\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11wt8vr/respect_the_gorillaz_gorillaz/

########################################

id = get_rt_id(cur, "Respect the Ninja Megazord (Mighty Morphin'' Power Rangers)", 'https://redd.it/11xczc9')
add_data(['Ninja Megazord'],
'Ninja Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11xczc9/respect_the_ninja_megazord_mighty_morphin_power/

########################################

id = get_rt_id(cur, "Respect the Shogun Megazord (Mighty Morphin'' Power Rangers)", 'https://redd.it/11xd11y')
add_data(['Shogun Megazord'],
'Shogun Megazord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11xd11y/respect_the_shogun_megazord_mighty_morphin_power/

########################################

id = get_rt_id(cur, 'Respect Hero (Hero)', 'https://redd.it/11xfafy')
add_data(['Hero'],
'Hero',
False,
False,
[
    ['Dom Fera']
],
'Dom Fera',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11xfafy/respect_hero_hero/

########################################

id = get_rt_id(cur, 'Respect Volcano (Hero)', 'https://redd.it/11xfbhn')
add_data(['Volcano'],
'Volcano',
False,
False,
[
    ['Dom Fera']
],
'Dom Fera',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11xfbhn/respect_volcano_hero/

########################################

id = get_rt_id(cur, 'Respect Beck! (The Rundown)', 'https://redd.it/11xgea3')
add_data(['Beck'],
'Beck',
False,
False,
[
    ['The Rundown']
],
'The Rundown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11xgea3/respect_beck_the_rundown/

########################################

add_data(['Nagi Tahira'],
'Nagi Tahira',
False,
True,
[
    ['Tank Chair']
],
'Tank Chair',
'{23150}'
)
#https://www.reddit.com/r/respectthreads/comments/11xvbwl/respect_nagi_tahira_tank_chair/

########################################

id = get_rt_id(cur, 'Respect Asajj Ventress (Star Wars Canon)', 'https://redd.it/11y1czy')
add_data(['Asajj Ventress'],
'Asajj Ventress',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11y1czy/respect_asajj_ventress_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Jason Voorhees! (Mortal Kombat)', 'https://redd.it/11ylgh1')
add_data(['Jason Voo?rhee?s'],
'Jason Voorhees',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11ylgh1/respect_jason_voorhees_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect Robocop! (Mortal Kombat)', 'https://redd.it/120xtwz')
add_data(['Robocop'],
'Robocop',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120xtwz/respect_robocop_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect Edward Elric! (Fullmetal Alchemist (PS2 Trilogy))', 'https://redd.it/11yrtbt')
add_data(['Edward Elric'],
'Edward Elric',
False,
False,
[
    ['PS2']
],
'PS2',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11yrtbt/respect_edward_elric_fullmetal_alchemist_ps2/

########################################

id = get_rt_id(cur, 'Respect Berzerker! (BRZRKR)', 'https://redd.it/11yyywb')
add_data(['Berzerker'],
'Berzerker',
False,
False,
[
    ['BRZRKR']
],
'BRZRKR',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11yyywb/respect_berzerker_brzrkr/

########################################

id = get_rt_id(cur, 'Respect Oniguma (To your eternity)', 'https://redd.it/11zbm9o')
add_data(['Oniguma'],
'Oniguma',
False,
True,
[
    ['To Your Eternity']
],
'To Your Eternity',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11zbm9o/respect_oniguma_to_your_eternity/

########################################

id = get_rt_id(cur, 'Respect Reimu (The Power of Terry)', 'https://redd.it/11zfogy')
add_data(['Reimu'],
'Reimu',
False,
False,
[
    ['The Power of Terry']
],
'The Power of Terry',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11zfogy/respect_reimu_the_power_of_terry/

########################################

id = get_rt_id(cur, 'Respect Balalaika! (Black Lagoon (Anime))', 'https://redd.it/11zwqsu')
add_data(['Balalaika'],
'Balalaika',
False,
False,
[
    ['Black Lagoon']
],
'Black Lagoon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11zwqsu/respect_balalaika_black_lagoon_anime/

########################################

id = get_rt_id(cur, 'Respect Black Widow [Claire Voyant] (Marvel 616)', 'https://redd.it/11zxh39')
add_data(['Claire Voyant'],
'Claire Voyant',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/11zxh39/respect_black_widow_claire_voyant_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Rune (Malibu Comics/Marvel)', 'https://redd.it/120qgu9')
add_data(['Rune'],
'Rune',
False,
False,
[
    ['Malibu']
],
'Malibu Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120qgu9/respect_rune_malibu_comicsmarvel/

########################################

id = get_rt_id(cur, 'Respect Elaine Mallory! (The Dresden Files)', 'https://redd.it/120kuop')
add_data(['Elaine Mallory'],
'Elaine Mallory',
False,
True,
[
    ['Dresden( Files|verse)']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120kuop/respect_elaine_mallory_the_dresden_files/

add_data(['Elaine'],
'Elaine',
False,
False,
[
    ['Dresden']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120kuop/respect_elaine_mallory_the_dresden_files/

########################################

id = get_rt_id(cur, 'Respect: Slime Superman, aka the Thing from 40 000 AD! (Pre-Crisis DC Comics)', 'https://redd.it/120sc1g')
add_data(['Slime Superman'],
'Slime Superman',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120sc1g/respect_slime_superman_aka_the_thing_from_40_000/

########################################

id = get_rt_id(cur, 'Respect Odin! (Norse Mythology)', 'https://redd.it/120xd39')
add_data(['Odin'],
'Odin',
False,
False,
[
    ['Nor(se|dic) Mythology'], ['\(myth?(ical|olog(y|ical))\)'], ['myth?(ical|olog(y|ical)) Battle']
],
'Norse Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/120xd39/respect_odin_norse_mythology/

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

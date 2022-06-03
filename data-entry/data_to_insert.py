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

update_respectthread(cur, 1450, 'Respect Christian Brutal Sniper! (TF2 Freaks)', 'https://redd.it/v25fsz')
update_respectthread(cur, 5604, 'Respect Niko Bellic (Grand Theft Auto)', 'https://redd.it/v2xtva')

########################################

add_data(['Spider(-| )?Men'],
'Spider-Men',
True,
False,
[
    ['Tobey|M(a|c)guire', 'Andrew|Garfield', 'Tom|Holland']
],
'Live-Action',
'{302,113,261}'
)
#https://www.reddit.com/r/whowouldwin/comments/v262h5/morbius_movie_vs_spidermen_movies/iar6i70/?context=3

########################################

add_data(['Z(-| )Fighters'],
'Z-Fighters',
True,
True,
[
    ['Dragon Ball'], ['DB(Z|S)?']
],
'Dragon Ball',
'{3288, 3286, 3313, 3306, 9352, 12062, 9349}'
)
#https://www.reddit.com/r/whowouldwin/comments/v24kty/present_zamasu_vs_zfighters/iaqae1g/?context=3

########################################

add_data(['Lucifer Morningstar'],
'Lucifer Morningstar',
False,
False,
[
    ['Lucifer Morningstar ?\(TV']
],
'Lucifer 2018',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/v2jwiw/lucifer_morningstar_tv_vs_cain_supernatural/iasqv4g/?context=3

########################################

id = get_rt_id(cur, 'Respect Livewire (DCAU)', 'https://redd.it/v1f8xf')
add_data(['Livewire'],
'Livewire',
False,
False,
[
    ['DC Animated Universe'], ['DCAU'], ['Timmverse'], ['Animated DC']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v1f8xf/respect_livewire_dcau/

########################################

id = get_rt_id(cur, 'Respect the Silver Surfer (Silver Surfer)', 'https://redd.it/v1o1i9')
add_data(['Silver Surfer'],
'Silver Surfer',
False,
False,
[
    ['Propane'], ['1998', 'TV|Show']
],
'1998',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v1o1i9/respect_the_silver_surfer_silver_surfer/

########################################

id = get_rt_id(cur, 'Respect Doc Morbius (Marvel Earth-31913)', 'https://redd.it/v1qnzc')
add_data(['Morbio?us'],
'Morbius',
False,
False,
[
    ['31913']
],
'31913',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v1qnzc/respect_doc_morbius_marvel_earth31913/

########################################

id = get_rt_id(cur, 'Respect Rui and the Spider Family (Demon Slayer: Kimetsu no Yaiba)', 'https://redd.it/v20hai')
add_data(['Rui'],
'Rui',
False,
False,
[
    ['Demon ?Slayer'], ['Kimetsu no Yaiba'], ['KnY']
],
'Demon Slayer',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v20hai/respect_rui_and_the_spider_family_demon_slayer/

########################################

id = get_rt_id(cur, 'Respect Yuga Khan (DC, Post-Crisis)', 'https://redd.it/v24l1w')
add_data(['Yuga Khan'],
'Yuga Khan',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v24l1w/respect_yuga_khan_dc_postcrisis/

add_data(['Yuga Khan'],
'Yuga Khan',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/v24l1w/respect_yuga_khan_dc_postcrisis/

add_data(['Yuga Khan'],
'Yuga Khan',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v24l1w/respect_yuga_khan_dc_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Subject B-0 (DC, New 52)', 'https://redd.it/v26m3l')
add_data(['Subject B-0'],
'Subject B-0',
False,
True,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v26m3l/respect_subject_b0_dc_new_52/

########################################

id = get_rt_id(cur, 'Respect Adam Strange! (DC Post-Flashpoint)', 'https://redd.it/v2fs1j')
add_data(['Adam Strange'],
'Adam Strange',
False,
False,
[
    ['(Post(-| ))?Flash(-| )?point']
],
'Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v24l1w/respect_yuga_khan_dc_postcrisis/

add_data(['Adam Strange'],
'Adam Strange',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52 / Rebirth',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/v24l1w/respect_yuga_khan_dc_postcrisis/

add_data(['Adam Strange'],
'Adam Strange',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2fs1j/respect_adam_strange_dc_postflashpoint/

########################################

id = get_rt_id(cur, 'Respect Kuraudo Kurashiki, "The Sword Eater" (Rakudai Kishi no Calvary).', 'https://redd.it/v2781g')
add_data(['Kuraudo Kurashiki'],
'Kuraudo Kurashiki',
False,
True,
[
    ['Chivalry of a Failed Knight'], ['Rakudai']
],
'Chivalry of a Failed Knight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2781g/respect_kuraudo_kurashiki_the_sword_eater_rakudai/

########################################

id = get_rt_id(cur, 'Respect Ran Sabiura! (Murcielago)', 'https://redd.it/v2a0h2')
add_data(['Ran Sabiura'],
'Ran Sabiura',
False,
True,
[
    ['Murci(é|e)lago']
],
'Murciélago',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2a0h2/respect_ran_sabiura_murcielago/

########################################

id = get_rt_id(cur, '[NSFW] Respect Kuroko Koumori! (Murcielago)', 'https://redd.it/v2a3c2')
add_data(['Kuroko Koumori'],
'Kuroko Koumori',
False,
True,
[
    ['Murci(é|e)lago']
],
'Murciélago',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2a3c2/nsfw_respect_kuroko_koumori_murcielago/

########################################

id = get_rt_id(cur, 'Respect Rinko Asagi! (Murcielago)', 'https://redd.it/v2a4i7')
add_data(['Rinko Asagi'],
'Rinko Asagi',
False,
True,
[
    ['Murci(é|e)lago']
],
'Murciélago',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2a4i7/respect_rinko_asagi_murcielago/

########################################

id = get_rt_id(cur, 'Respect SCP-896 (SCP Foundation)', 'https://redd.it/v2cyyv')
add_data(['SCP ?(-| )? ?896'],
'SCP-896',
False,
True,
[
    ['Foundation']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2cyyv/respect_scp896_scp_foundation/

########################################

id = get_rt_id(cur, "Respect Nathan ''Rad'' Spencer (Bionic Commando)", 'https://redd.it/v2ec4w')
add_data(['Spencer'],
'Spencer',
False,
False,
[
    ['Bionic Commando']
],
'Bionic Commando',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2ec4w/respect_nathan_rad_spencer_bionic_commando/

########################################

id = get_rt_id(cur, 'Respect Ghazghkull Mag Uruk Thraka (Warhammer 40k)', 'https://redd.it/v2uqp2')
add_data(['Ghazghkull'],
'Ghazghkull',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v2uqp2/respect_ghazghkull_mag_uruk_thraka_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Himeno! (Chainsaw Man)', 'https://redd.it/v397jc')
add_data(['Himeno'],
'Himeno',
False,
False,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v397jc/respect_himeno_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Tomoe Gozen, the Witch of Might! (The War of Greedy Witches)', 'https://redd.it/v3fo5q')
add_data(['Tomoe Gozen'],
'Tomoe Gozen',
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3fo5q/respect_tomoe_gozen_the_witch_of_might_the_war_of/

########################################

id = get_rt_id(cur, 'Respect Elizabeth Bathory, the Witch of Blood! (The War of Greedy Witches)', 'https://redd.it/v3fp16')
add_data(['Elizabeth Bathory'],
'Elizabeth Bathory',
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3fp16/respect_elizabeth_bathory_the_witch_of_blood_the/

########################################

id = get_rt_id(cur, "Respect Jeanne D''Arc, the Witch of Nothing! (The War of Greedy Witches)", 'https://redd.it/v3jnzx')
add_data(["Jeanne d''Arc"],
"Jeanne d''Arc",
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3jnzx/respect_jeanne_darc_the_witch_of_nothing_the_war/

########################################

id = get_rt_id(cur, 'Respect Wu Zetian, the Witch of Supremacy! (The War of Greedy Witches)', 'https://redd.it/v3jolv')
add_data(['Wu Zetian'],
'Wu Zetian',
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3jolv/respect_wu_zetian_the_witch_of_supremacy_the_war/

########################################

id = get_rt_id(cur, 'Respect Cleopatra VII, the Witch of Love! (The War of Greedy Witches)', 'https://redd.it/v3lfjn')
add_data(['Cleopatra'],
'Cleopatra',
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3lfjn/respect_cleopatra_vii_the_witch_of_love_the_war/

########################################

id = get_rt_id(cur, 'Respect Himiko, the Witch of Demons! (The War of Greedy Witches)', 'https://redd.it/v3lflg')
add_data(['Himiko'],
'Himiko',
False,
False,
[
    ['Majo Taisen'], ['War of Greedy Witches']
],
'The War of Greedy Witches',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/v3lflg/respect_himiko_the_witch_of_demons_the_war_of/

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

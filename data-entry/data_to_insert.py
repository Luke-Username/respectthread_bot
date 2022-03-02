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

update_respectthread(cur, 5497, 'Respect The Terrarian! (Terraria)', 'https://redd.it/t3t8sp')
update_respectthread(cur, 251, 'Respect Loki (Marvel Cinematic Universe)', 'https://redd.it/t3waun')

########################################

id = get_rt_id(cur, 'Respect Ulik, King of the Trolls (Complete Respect Thread)', 'https://comicvine.gamespot.com/forums/gen-discussion-1/respect-ulik-king-of-the-trolls-complete-respect-t-2073168/')
add_data(['Ulik'],
'Ulik',
False,
True,
[
    ['616'], ['Marvel Comics?']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/t49fjq/iron_man_vs_ulik/

########################################

id = get_rt_id(cur, 'Respect Agamotto, The All Seeing (Marvel, 616)', 'https://redd.it/t4zn9h')
add_data(['Agamotto'],
'Agamotto',
False,
True,
[
    ['616'], ['Comics?']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4zn9h/respect_agamotto_the_all_seeing_marvel_616/

add_data(['Agamotto'],
'Agamotto',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{}'
)
#https://www.reddit.com/r/respectthreads/comments/t4zn9h/respect_agamotto_the_all_seeing_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Medusa, the Black Serpent! (Fate)', 'https://redd.it/t38bys')
add_data(['Medusa'],
'Medusa',
False,
False,
[
    ['Medusa ?\(Fate'], ['Rider']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t38bys/respect_medusa_the_black_serpent_fate/

########################################

id = get_rt_id(cur, 'Respect Hassan of the Cursed Arm! (Fate)', 'https://redd.it/t3zihw')
add_data(['Medusa'],
'Medusa',
False,
False,
[
    ['Cursed Arms?']
],
'Cursed Arm',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3zihw/respect_hassan_of_the_cursed_arm_fate/

########################################

id = get_rt_id(cur, 'Respect Silent Hill (Silent Hill)', 'https://redd.it/t3bbro')
add_data(['Silent Hill'],
'Silent Hill',
True,
True,
[
    ['default']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3bbro/respect_silent_hill_silent_hill/

########################################

id = get_rt_id(cur, 'Respect Redcloak (Order of the Stick)', 'https://redd.it/t3cbps')
add_data(['Redcloak'],
'Redcloak',
False,
False,
[
    ['Order of the Stick']
],
'Order of the Stick',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3cbps/respect_redcloak_order_of_the_stick/

########################################

id = get_rt_id(cur, 'RESPECT Hakoda (Avatar: The Last Airbender)', 'https://redd.it/t3h3gc')
add_data(['Hakoda'],
'Hakoda',
False,
True,
[
    ['Avatar'], ['Bend(er|ing)']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3h3gc/respect_hakoda_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'RESPECT Master Yu (Avatar: The Last Airbender)', 'https://redd.it/t3h89d')
add_data(['Master Yu'],
'Master Yu',
False,
False,
[
    ['Avatar'], ['A?TLA'], ['Bend(er|ing)']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3h89d/respect_master_yu_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'Respect Emperor Mateus! (Final Fantasy II)', 'https://redd.it/t3zp5b')
add_data(['Emperor Mateus'],
'Emperor Mateus',
False,
True,
[
    ['Final Fantasy'], ['FF(II|2)']
],
'Final Fantasy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3hau8/respect_huu_avatar_the_last_airbender/

########################################

id = get_rt_id(cur, 'Respect Susan Murphy, Ginormica! (Monsters vs. Aliens)', 'https://redd.it/t3ztyh')
add_data(['Ginormica'],
'Ginormica',
False,
True,
[
    ['Monsters vs?\.? Aliens']
],
'Monsters vs. Aliens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3ztyh/respect_susan_murphy_ginormica_monsters_vs_aliens/

add_data(['Susan'],
'Susan',
False,
False,
[
    ['Monsters vs?\.? Aliens']
],
'Monsters vs. Aliens',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t3ztyh/respect_susan_murphy_ginormica_monsters_vs_aliens/

########################################

id = get_rt_id(cur, 'Respect Imhotep (The Mummy, 1932)', 'https://redd.it/t458ge')
add_data(['Imhotep'],
'Imhotep',
False,
False,
[
    ['1932']
],
'The Mummy, 1932',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t458ge/respect_imhotep_the_mummy_1932/

########################################

id = get_rt_id(cur, 'Respect Princess Ahmanet (The Mummy, 2017)', 'https://redd.it/t458hh')
add_data(['Ahmanet'],
'Ahmanet',
False,
False,
[
    ['2017'], ['The Mummy']
],
'The Mummy',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t458hh/respect_princess_ahmanet_the_mummy_2017/

########################################

id = get_rt_id(cur, 'Respect Rachel Woodruff! (Beynders)', 'https://redd.it/t472r1')
add_data(['Rachel'],
'Rachel',
False,
False,
[
    ['Rachel Woodruff'], ['Beyonders']
],
'Beyonders',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t472r1/respect_rachel_woodruff_beynders/

########################################

id = get_rt_id(cur, 'Respect Tanya Spears, Power Girl (Dc, New 52/Rebirth)', 'https://redd.it/t48gsf')
add_data(['Tanya Spears'],
'Tanya Spears',
False,
True,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Rebirth']
],
'New 52 / Rebirth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t48gsf/respect_tanya_spears_power_girl_dc_new_52rebirth/

########################################

id = get_rt_id(cur, 'Respect Gligarman and Gligirl (Pokemon Anime)', 'https://redd.it/t4fewr')
add_data(['Gligarman'],
'Gligarman',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4fewr/respect_gligarman_and_gligirl_pokemon_anime/

add_data(['Gligirl'],
'Gligirl',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4fewr/respect_gligarman_and_gligirl_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Leonardo (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t4hsdw')
add_data(['Leonardo'],
'Leonardo',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4hsdw/respect_leonardo_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect Raphael (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t4hsfh')
add_data(['Raphael'],
'Raphael',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4hsdw/respect_leonardo_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect Donatello (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t4hsgf')
add_data(['Donatello'],
'Donatello',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4hsdw/respect_leonardo_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect Michelangelo (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t4hshj')
add_data(['Michelangelo'],
'Michelangelo',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4hsdw/respect_leonardo_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect the Teenage Mutant Ninja Turtles (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t54lra')
add_data(['Ninja Turtles?'],
'Teenage Mutant Ninja Turtles',
False,
False,
[
    ['2012']
],
'2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t54lra/respect_the_teenage_mutant_ninja_turtles_teenage/

########################################

id = get_rt_id(cur, 'Respect Splinter (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t54ls7')
add_data(['Splinter'],
'Splinter',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t54ls7/respect_splinter_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect Shredder (Teenage Mutant Ninja Turtles 2012)', 'https://redd.it/t54lti')
add_data(['Shredder'],
'Shredder',
False,
False,
[
    ['Teenaged? Mutant Ninja Turtles?', '2012'], ['TMNT', '2012']
],
'TMNT 2012',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t54lti/respect_shredder_teenage_mutant_ninja_turtles_2012/

########################################

id = get_rt_id(cur, 'Respect the Red Dart Machine (Red Dart)', 'https://redd.it/t4ql3n')
add_data(['Red Dart Machine'],
'Red Dart Machine',
False,
True,
[
    ['vending']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t4ql3n/respect_the_red_dart_machine_red_dart/

########################################

id = get_rt_id(cur, 'Respect Alternate Calliope, The Muse of Space! (Homestuck)', 'https://redd.it/t545vm')
add_data(['Alternate Calliope'],
'Alternate Calliope',
False,
True,
[
    ['Homestuck']
],
'Homestuck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/t545vm/respect_alternate_calliope_the_muse_of_space/

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

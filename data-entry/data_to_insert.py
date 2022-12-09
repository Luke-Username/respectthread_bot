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

update_respectthread(cur, 4719, 'Respect Spike Spiegel! (Cowboy Bebop)', 'https://redd.it/ze2m4w')
update_respectthread(cur, 5942, 'Respect SCP-777-J, Darkblade (SCP Foundation)', 'https://redd.it/zgj6vu')

########################################

add_data(['Rudolph'],
'Rudolph',
False,
False,
[
    ['Frosty'], ['Composite Rudolph']
],
'Rankin/Bass',
'{1229}'
)
#https://www.reddit.com/r/whowouldwin/comments/ze87ka/rudolph_vs_frosty_christmas/iz4vwku/?context=3

add_data(['Rudolph the Red(-| )?Nosed? Reindeer'],
'Rudolph the Red-Nosed Reindeer',
False,
True,
[
    ['Frosty'], ['Composite Rudolph']
],
'Rankin/Bass',
'{1229}'
)
#https://www.reddit.com/r/whowouldwin/comments/ze87ka/rudolph_vs_frosty_christmas/iz4vwku/?context=3

########################################

id = get_rt_id(cur, 'Respect Phoenix Wright (Marvel vs. Capcom)', 'https://redd.it/zdx9bj')
add_data(['Phoenix Wright'],
'Phoenix Wright',
False,
False,
[
    ['Marvel', 'Capcom']
],
'Marvel vs. Capcom',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zdx9bj/respect_phoenix_wright_marvel_vs_capcom/

########################################

id = get_rt_id(cur, 'Respect Cut Man (Ruby-Spears Mega Man)', 'https://redd.it/zeaoih')
add_data(['Cut Man'],
'Cut Man',
False,
False,
[
    ['Ruby(-| )Spears']
],
'Ruby-Spears',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zeaoih/respect_cut_man_rubyspears_mega_man/

########################################

id = get_rt_id(cur, 'Respect Guts Man (Ruby-Spears Mega Man)', 'https://redd.it/zeaok9')
add_data(['Guts Man'],
'Guts Man',
False,
False,
[
    ['Ruby(-| )Spears']
],
'Ruby-Spears',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zeaok9/respect_guts_man_rubyspears_mega_man/

########################################

id = get_rt_id(cur, 'Respect Mega Man (The Megas)', 'https://redd.it/zeatml')
add_data(['Mega ?Man'],
'Mega Man',
False,
False,
[
    ['The Megas']
],
'The Megas',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zeatml/respect_mega_man_the_megas/

########################################

id = get_rt_id(cur, 'Respect Block Man (Mega Man)', 'https://redd.it/zeos8w')
add_data(['Block Man'],
'Block Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zeos8w/respect_block_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Cut Man! (Mega Man)', 'https://redd.it/zfmpcw')
add_data(['Cut Man'],
'Cut Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zfmpcw/respect_cut_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Acid Man (Mega Man)', 'https://redd.it/zerqyl')
add_data(['Acid Man'],
'Acid Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zerqyl/respect_acid_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect Blast Man (Mega Man)', 'https://redd.it/zes74m')
add_data(['Blast Man'],
'Blast Man',
False,
False,
[
    ['Mega ?Man']
],
'Mega Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zes74m/respect_blast_man_mega_man/

########################################

id = get_rt_id(cur, 'Respect The Son of Sparda, Dante (Devil May Cry Comics)', 'https://redd.it/zedgur')
add_data(['Dante'],
'Dante',
False,
False,
[
    ['Devil May Cry Comics'], ['Dreamwave']
],
'Devil May Cry Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zedgur/respect_the_son_of_sparda_dante_devil_may_cry/

########################################

id = get_rt_id(cur, 'Respect Fami! (Chainsaw Man)', 'https://redd.it/zel1jj')
add_data(['Fami'],
'Fami',
False,
False,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zel1jj/respect_fami_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect Liquid Snake (Metal Gear Solid)', 'https://redd.it/zeyr7l')
add_data(['Liquid Snake'],
'Liquid Snake',
False,
True,
[
    ['Metal ?Gear'], ['MGS(\d|\w+)?'], ['MGS?\d']
],
'Metal Gear',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zeyr7l/respect_liquid_snake_metal_gear_solid/

########################################

id = get_rt_id(cur, 'Respect Zheng Shi-Hua, Sister Hammer (Marvel, 616)', 'https://redd.it/zf3opz')
add_data(['Zheng Shi(-| )Hua'],
'Zheng Shi-Hua',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zf3opz/respect_zheng_shihua_sister_hammer_marvel_616/

add_data(['Sister Hammer'],
'Sister Hammer',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zf3opz/respect_zheng_shihua_sister_hammer_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Mecha-Noctowl (Pokemon Anime)', 'https://redd.it/zf4hox')
add_data(['Mecha(-| )Noctowl'],
'Mecha-Noctowl',
False,
True,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zf4hox/respect_mechanoctowl_pokemon_anime/

########################################

id = get_rt_id(cur, 'Respect Kotton (Ayashimon)', 'https://redd.it/zffs53')
add_data(['Kotton'],
'Kotton',
False,
False,
[
    ['Ayashimon']
],
'Ayashimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zffs53/respect_kotton_ayashimon/

########################################

id = get_rt_id(cur, 'Respect Maruo Kaido (Ayashimon)', 'https://redd.it/zfmck1')
add_data(['Maruo Kaido'],
'Maruo Kaido',
False,
True,
[
    ['Ayashimon']
],
'Ayashimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zfmck1/respect_maruo_kaido_ayashimon/

########################################

id = get_rt_id(cur, 'Respect Doppo Akari (Ayashimon)', 'https://redd.it/zflu14')
add_data(['Doppo Akari'],
'Doppo Akari',
False,
True,
[
    ['Ayashimon']
],
'Ayashimon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zflu14/respect_doppo_akari_ayashimon/

########################################

add_data(['Juju Toobootie'],
'Juju Toobootie',
False,
True,
[
    ['Everything Everywhere All At Once']
],
'Everything Everywhere All At Once',
'{22369}'
)
#https://www.reddit.com/r/whowouldwin/comments/zgett8/juju_toobootie_everything_everywhere_all_at_once/izgoat2/?context=3

########################################

id = get_rt_id(cur, 'Respect: Shield Captain Valerian (Warhammer 40k)', 'https://redd.it/zfpjeg')
add_data(['Shield(-| )Captain Valerian'],
'Shield-Captain Valerian',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zfpjeg/respect_shield_captain_valerian_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Fumio Kirisaki! (Saitama Chainsaw Shoujo)', 'https://redd.it/zfwx1t')
add_data(['Fumio Kirisaki'],
'Fumio Kirisaki',
False,
True,
[
    ['Saitama Chainsaw Shoujo']
],
'Saitama Chainsaw Shoujo',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zfwx1t/respect_fumio_kirisaki_saitama_chainsaw_shoujo/

########################################

id = get_rt_id(cur, 'Respect John Abar (Abar, The First Black Superman)', 'https://redd.it/zfx3po')
add_data(['Abar'],
'Abar',
False,
False,
[
    ['Black Superman']
],
'The First Black Superman',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zfx3po/respect_john_abar_abar_the_first_black_superman/

########################################

id = get_rt_id(cur, 'Respect: Marvel Man! (Pre-Crisis DC Comics)', 'https://redd.it/zgbbvb')
add_data(['Marvel Man'],
'Marvel Man',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zgbbvb/respect_marvel_man_precrisis_dc_comics/

########################################

id = get_rt_id(cur, 'Respect Captain Torrents (Pirates of the Caribbean: The Adventures of Jack Sparrow)', 'https://redd.it/zgemfi')
add_data(['Captain Torrents'],
'Captain Torrents',
False,
False,
[
    ['Pirates? of the Caribbean', 'Adventures of Jack Sparrow'], ['POTC', 'Adventures of Jack Sparrow']
],
'Pirates of the Caribbean: The Adventures of Jack Sparrow',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/zgemfi/respect_captain_torrents_pirates_of_the_caribbean/

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

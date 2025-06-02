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

update_respectthread(cur, 5905, 'Respect Percy Jackson (Percy Jackson & the Olympians) Updated Version', 'https://redd.it/1kwtha1')
update_respectthread(cur, 4880, 'Respect Kumada (Oyaji)', 'https://redd.it/1kxmd68')
update_respectthread(cur, 25819, 'Respect Longan Dragon Cookie (CookieRun: Ovenbreak)', 'https://redd.it/1kzzrmq')

########################################

add_data(['Conner Kent'],
'Conner Kent',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth']
],
'New 52',
'{7633}'
)
#

add_data(['Conner Kent'],
'Conner Kent',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{7633}'
)
#https://www.reddit.com/r/whowouldwin/comments/1l05rr5/which_marvel_dc_characters_would_win_their/mvapqat/?context=3

########################################

add_data(['Mera'],
'Mera',
False,
False,
[
    ['Mera.*New(-| )?52']
],
'New 52',
'{1491}'
)
#

add_data(['Mera'],
'Mera',
False,
False,
[
    ['Mera ?\(DC( Comics)?\)'], ['Mera ?\[DC( Comics)?\]']
],
'DC',
'{1491}'
)
#

########################################

id = get_rt_id(cur, 'Respect Charlie, Sgt. Gorilla (DC,Pre-Crisis)', 'https://redd.it/1l01454')
add_data(['Sgt\.? Gorilla'],
'Sgt. Gorilla',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Sgt\.? Gorilla'],
'Sgt. Gorilla',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Gay Ghost (DC Comics, Pre-Flashpoint)', 'https://redd.it/1l0n1i2')
add_data(['Gay Ghost'],
'Gay Ghost',
False,
False,
[
    ['Pre(-| )?Flashpoint']
],
'Pre-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Gay Ghost'],
'Gay Ghost',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l0n1i2/respect_the_gay_ghost_dc_comics_preflashpoint/

########################################

id = get_rt_id(cur, 'Respect Monsieur Mallah (DC Comics, Post-Crisis)', 'https://redd.it/1l0oa3d')
add_data(['Monsieur Mallah'],
'Monsieur Mallah',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Monsieur Mallah'],
'Monsieur Mallah',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Brain (DC Comics, Post-Crisis)', 'https://redd.it/1l0oa5y')
add_data(['Brain'],
'Brain',
False,
False,
[
    ['Brain ?\(Posts?(-| )?C(risis)?\)'], ['Brain ?\(New(-| )Earth\)']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Brain'],
'Brain',
False,
False,
[
    ['Brain ?\(DC( Comics)?\)'], ['Brain ?\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l0oa5y/respect_the_brain_dc_comics_postcrisis/

########################################

id = get_rt_id(cur, 'Respect Spider Jerusalem (Transmetropolitan)', 'https://redd.it/1kvv8gb')
add_data(['Spider Jerusalem'],
'Spider Jerusalem',
False,
True,
[
    ['Transmetropolitan']
],
'Transmetropolitan',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kvv8gb/respect_spider_jerusalem_transmetropolitan/

########################################

id = get_rt_id(cur, 'Respect The Mummy (Lot No. 249)', 'https://redd.it/1kvxsy1')
add_data(['Mummy'],
'Mummy',
False,
False,
[
    ['Lot No\.? 249']
],
'Lot No. 249',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gingy (Shrek Tie-In Games)', 'https://redd.it/1kw08nd')
add_data(['Gingy'],
'Gingy',
False,
False,
[
    ['Shrek( Tie(-| )In)? Games']
],
'Shrek Tie-In Games',
'{' + '{}'.format(id) + '}'
)
#

########################################

########################################

id = get_rt_id(cur, "Respect May''s Skitty (Pokemon Anime)", 'https://redd.it/1kw8o94')
add_data(['Skitty'],
'Skitty',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kw8o94/respect_mays_skitty_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect May''s Squirtle (Pokemon Anime)", 'https://redd.it/1kyazia')
add_data(['Squirtle'],
'Squirtle',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kyazia/respect_mays_squirtle_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect May''s Munchlax (Pokemon Anime)", 'https://redd.it/1kwzwp6')
add_data(['Munchlax'],
'Munchlax',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kwzwp6/respect_mays_munchlax_pokemon_anime/

########################################

id = get_rt_id(cur, "Respect May''s Glaceon (Pokemon Anime)", 'https://redd.it/1kxpo73')
add_data(['Glaceon'],
'Glaceon',
False,
False,
[
    ['May']
],
'May',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect May (Pokemon Anime)', 'https://redd.it/1kz3gz8')
add_data(['May'],
'May',
False,
False,
[
    ['May.*\(Pok(e|é)m(o|a)n\)'], ['\[Pok(e|é)m(o|a)n\].*May'], ['May from Pok(e|é)m(o|a)n'], ['Misty', 'Dawn'], ['Ash', 'companion']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Harley (Pokemon Anime)', 'https://redd.it/1l0u3zw')
add_data(['Harley'],
'Harley',
False,
False,
[
    ['Harley ?\(Pok(e|é)m(o|a)n\)']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Invader (The Day the Earth Blew Up)', 'https://redd.it/1kwnpql')
add_data(['Invader'],
'Invader',
False,
False,
[
    ['Day the Earth Blew Up']
],
'The Day the Earth Blew Up',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jeff the Land Shark (Marvel 616)', 'https://redd.it/1kwro1d')
add_data(['Jeff the Land Shark'],
'Jeff the Land Shark',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect "Bill Rizer" and Genbei "Jaguar" Yagyu (Contra)', 'https://redd.it/1kwro3t')
add_data(['Jaguar'],
'Jaguar',
False,
False,
[
    ['Contra']
],
'Contra',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Little Pete (Gone)', 'https://redd.it/1kx4see')
add_data(['Little Pete'],
'Little Pete',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Tom Peaks, Napalm (Gone)', 'https://redd.it/1l09931')
add_data(['Tom Peaks'],
'Tom Peaks',
False,
False,
[
    ['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "You probably shouldn''t respect Not Important! (Hatred)", 'https://redd.it/1kx74il')
add_data(['Not Important'],
'Not Important',
False,
False,
[
    ['Hatred']
],
'Hatred',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kx74il/you_probably_shouldnt_respect_not_important_hatred/


########################################

id = get_rt_id(cur, "Respect Popeye (Genndy''s Cancelled Popeye Movie)", 'https://redd.it/1kxvpgi')
add_data(['Popeye'],
'Popeye',
False,
False,
[
    ['Genndy|Tartakovsky', 'Cancelled']
],
"Genndy''s Cancelled Popeye Movie",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kxvpgi/respect_popeye_genndys_cancelled_popeye_movie/

########################################

id = get_rt_id(cur, 'Respect Dexter Riley (The Medfield Trilogy)', 'https://redd.it/1kyn7ua')
add_data(['Dexter Riley'],
'Dexter Riley',
False,
True,
[
    ['Medfield'], ['Computer Wore Tennis Shoes'], ['Now You See Him'], ['Strongest Man in the World']
],
'Medfield Trilogy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Vegeta (Dragon Ball Daima)', 'https://redd.it/1kyqtmv')
add_data(['Vegeta'],
'Vegeta',
False,
False,
[
    ['Daima']
],
'Dragon Ball Daima',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Goku (Dragon Ball Daima)', 'https://redd.it/1kzg5zz')
add_data(['Goku'],
'Goku',
False,
False,
[
    ['Daima']
],
'Dragon Ball Daima',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Guard Dog (Meet the Guard Dog)', 'https://redd.it/1kyu63y')
add_data(['Guard Dog'],
'Guard Dog',
False,
False,
[
    ['Meet the Guard Dog']
],
'Meet the Guard Dog',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kyu63y/respect_the_guard_dog_meet_the_guard_dog/

########################################

id = get_rt_id(cur, 'Respect Nick and Lever (Nick and Lever)', 'https://redd.it/1kz3kb3')
add_data(['Nick'],
'Nick',
False,
False,
[
    ['Nick (and|&) Lever']
],
'Nick & Lever',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lever'],
'Lever',
False,
False,
[
    ['Nick (and|&) Lever']
],
'Nick & Lever',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Herobrine (HIM)', 'https://redd.it/1kz4ri4')
add_data(['Herobrine'],
'Herobrine',
False,
False,
[
    ['\(HIM\)']
],
'HIM',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Lucius the Eternal (Warhammer 40k)', 'https://redd.it/1kzhgbf')
add_data(['Lucius the Eternal'],
'Lucius the Eternal',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Lucius'],
'Lucius',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kzhgbf/respect_lucius_the_eternal_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Rick Grimes (Rick Grimes 2000) [The Walking Dead]', 'https://redd.it/1kzmg5q')
add_data(['Rick Grimes 2000'],
'Rick Grimes 2000',
False,
True,
[
    ['Wa(lk|kl)ing Dead']
],
'The Walking Dead',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Gryphon (Godzilla Found Footage)', 'https://redd.it/1kzpgu6')
add_data(['Gryphon'],
'Gryphon',
False,
False,
[
    ['Godzilla Found Footage']
],
'Godzilla Found Footage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kzpgu6/respect_the_gryphon_godzilla_found_footage/

########################################

id = get_rt_id(cur, 'Respect Zilla (The Gryphon Godzilla Found Footage)', 'https://redd.it/1kzqg56')
add_data(['Zilla'],
'Zilla',
False,
False,
[
    ['Gryphon', 'Godzilla Found Footage']
],
'Godzilla Found Footage',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1kzpgu6/respect_the_gryphon_godzilla_found_footage/

########################################

id = get_rt_id(cur, 'Millennial Tree Cookie (CookieRun)', 'https://redd.it/1l0puqz')
add_data(['Millennial Tree Cookie'],
'Millennial Tree Cookie',
False,
True,
[
    ['CookieRun']
],
'CookieRun',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1l0puqz/millennial_tree_cookie_cookierun/

########################################

id = get_rt_id(cur, 'Respect Ichi (Ichi the Killer)', 'https://redd.it/1l1gh7o')
add_data(['Ichi'],
'Ichi',
False,
False,
[
    ['Ichi ?\(Ichi the Killer\)'], ['Ichi the Killer', '(Film|Movie) Ichi']
],
'Ichi the Killer',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ssssalbatore! (Rio: Snakes Alive!)', 'https://redd.it/1l1l0oc')
add_data(['Ssssalbatore'],
'Ssssalbatore',
False,
True,
[
    ['Rio']
],
'Rio',
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

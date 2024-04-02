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

########################################

id = get_rt_id(cur, 'Respect Hattori Hanzo (Tenkaichi)', 'https://redd.it/1brimel')
add_data(['Hattori Hanzo'],
'Hattori Hanzo',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1brimel/respect_hattori_hanzo_tenkaichi/

########################################

id = get_rt_id(cur, 'Respect Sasaki Kojiro (Tenkaichi)', 'https://redd.it/1brimrs')
add_data(['Sasaki Kojir(ō|o)u?|Kojir(ō|o)u? Sasaki'],
'Sasaki Kojirō',
False,
False,
[
    ['Tenkaichi']
],
'Tenkaichi',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1brimrs/respect_sasaki_kojiro_tenkaichi/

########################################

id = get_rt_id(cur, 'Respect Super Saiyan 4 Broly (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/1brskqq')
add_data(['Broly'],
'Broly',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1brskqq/respect_super_saiyan_4_broly_hyourinjutsu_dragon/

########################################

id = get_rt_id(cur, 'Respect Baby (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/1bsl6t4')
add_data(['Baby'],
'Baby',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bsl6t4/respect_baby_hyourinjutsu_dragon_ball_what_if/

########################################

id = get_rt_id(cur, 'Respect Goku Black (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/1bsuosi')
add_data(['Goku Black'],
'Goku Black',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bsuosi/respect_goku_black_hyourinjutsu_dragon_ball_what/

########################################

id = get_rt_id(cur, 'Respect Baby Vegito Black (Hyourinjutsu Dragon Ball What If)', 'https://redd.it/1bsup0d')
add_data(['Baby Vegito Black'],
'Baby Vegito Black',
False,
False,
[
    ['Hyourinjutsu']
],
'Hyourinjutsu',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bsup0d/respect_baby_vegito_black_hyourinjutsu_dragon/

########################################

id = get_rt_id(cur, 'Respect Bal, aka Sir Ballister Boldheart (Nimona)', 'https://redd.it/1bsaatz')
add_data(['Ballister'],
'Ballister',
False,
False,
[
    ['Nimona'], ['Ballister Boldheart'], ['BALLiSTAR12']
],
'Nimona',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bsaatz/respect_bal_aka_sir_ballister_boldheart_nimona/

########################################

id = get_rt_id(cur, 'Respect Blue Beetle (DCEU)', 'https://redd.it/1bseb6m')
add_data(['Blue Beetle'],
'Blue Beetle',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bseb6m/respect_blue_beetle_dceu/

########################################

id = get_rt_id(cur, 'Respect OMAC (DCEU)', 'https://redd.it/1bsebh3')
add_data(['OMAC'],
'OMAC',
False,
False,
[
    ['DC Extended Universe'], ['DC ?(E|C)U'], ['DC Cinematic Universe']
],
'DCEU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bsebh3/respect_omac_dceu/

########################################

id = get_rt_id(cur, 'Respect God-Man (Tom the Dancing Bug)', 'https://redd.it/1bt0vw3')
add_data(['God(-| )Man'],
'God-Man',
False,
False,
[
    ['Tom the Dancing Bug'], ['comic']
],
'Tom the Dancing Bug',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt0vw3/respect_godman_tom_the_dancing_bug/

########################################

id = get_rt_id(cur, 'Respect: John Wick! (John Wick AI script)', 'https://redd.it/1bt1odr')
add_data(['John Wick'],
'John Wick',
False,
False,
[
    ['John Wick AI script']
],
'John Wick AI script',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt1odr/respect_john_wick_john_wick_ai_script/

########################################

id = get_rt_id(cur, 'Respect Marty Rantzen (Slaughter High)', 'https://redd.it/1bt1yao')
add_data(['Marty Rantzen'],
'Marty Rantzen',
False,
True,
[
    ['Slaughter High']
],
'Slaughter High',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt1yao/respect_marty_rantzen_slaughter_high/

########################################

id = get_rt_id(cur, 'Respect Kevin and Marcus Copeland (White Chicks)', 'https://redd.it/1bt34o3')
add_data(['Kevin (and|&) Marcus Copeland'],
'Kevin and Marcus Copeland',
True,
True,
[
    ['White Chicks']
],
'White Chicks',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt34o3/respect_kevin_and_marcus_copeland_white_chicks/

add_data(['The White Chicks'],
'The White Chicks',
True,
False,
[
    ['iTk15I5GZsA']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt34o3/respect_kevin_and_marcus_copeland_white_chicks/


########################################

id = get_rt_id(cur, 'Respect "Bocchi" Hitori Gotoh (Bocchi the Rock (Anime))', 'https://redd.it/1bt3kdg')
add_data(['Bocchi'],
'Bocchi',
False,
True,
[
    ['Hitori Gotoh'], ['Bocchi ?\(Bocchi the Rock']
],
'Bocchi the Rock!',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt3kdg/respect_bocchi_hitori_gotoh_bocchi_the_rock_anime/

########################################

id = get_rt_id(cur, 'Respect the Eagles (Birdemic)', 'https://redd.it/1bt51qc')
add_data(['Eagles'],
'Eagles',
False,
False,
[
    ['Birdemic']
],
'Birdemic',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt51qc/respect_the_eagles_birdemic/

########################################

id = get_rt_id(cur, "Respect Harry Mason (Ax ''Em)", 'https://redd.it/1bt51uc')
add_data(['Harry Mason'],
'Harry Mason',
False,
False,
[
    ["Ax ''Em"]
],
"Ax ''Em",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt51uc/respect_harry_mason_ax_em/

########################################

id = get_rt_id(cur, "Respect Squidward''s House! (Spongebob Squarepants)", 'https://redd.it/1bt7tv8')
add_data(["Squidward''s House"],
"Squidward''s House",
False,
True,
[
    ['Spongebob']
],
'Spongebob',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt7tv8/respect_squidwards_house_spongebob_squarepants/

########################################

########################################

id = get_rt_id(cur, 'Respect Forbush Man (Marvel, Earth-665)', 'https://redd.it/1bt9xv3')
add_data(['Forbush Man'],
'Forbush Man',
False,
True,
[
    ['665']
],
'665',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bt9xv3/respect_forbush_man_marvel_earth665/


########################################

id = get_rt_id(cur, 'Respect The Singer (Infinite - Sonic Forces (SiIvaGunner))', 'https://redd.it/1btd1mu')
add_data(['The Singer'],
'The Singer',
False,
False,
[
    ['SiIvaGunner', 'Sonic']
],
'SiIvaGunner',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1btd1mu/respect_the_singer_infinite_sonic_forces/

########################################

id = get_rt_id(cur, 'Respect Octoboss (Image Comics)', 'https://redd.it/1btka2h')
add_data(['Octoboss'],
'Octoboss',
False,
False,
[
    ['Image Comics']
],
'Image Comics',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1btka2h/respect_octoboss_image_comics/

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

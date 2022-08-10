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

update_respectthread(cur, 7606, 'Respect Robin Hood! (Robin Hood 1973)', 'https://redd.it/wk70t8')

########################################

add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['The Doctor.*(Doctor|Dr\.?) ?Who']
],
'Doctor Who',
'{14419, 40, 15401}'
)
#https://www.reddit.com/r/whowouldwin/comments/wicobx/the_doctor_dr_who_vs_mrs_frizzle_the_magic_school/ijany1a/?context=3

########################################

add_data(['Zim'],
'Zim',
False,
False,
[
    ['GIR', 'Alien']
],
'Invader Zim',
'{6526}'
)
#https://www.reddit.com/r/whowouldwin/comments/wkzo1a/goku_vs_superman_vs_zim_alien_fight_swapped/ijq63pl/?context=3

########################################

add_data(['Hancock'],
'Hancock',
False,
False,
[
    ['Hancock ?\(Film']
],
'Hancock',
'{457}'
)
#https://www.reddit.com/r/whowouldwin/comments/wiw3w6/soldier_boy_the_boys_vs_hancock_film/ijdyhue/?context=3

########################################

id = get_rt_id(cur, 'Respect the Ghost Shark (Ghost Shark)', 'https://redd.it/wijdan')
add_data(['Ghost Shark'],
'Ghost Shark',
False,
False,
[
    ['(Film|Movie)s?'], ['Ghost Shark ?\(Ghost Shark']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wijdan/respect_the_ghost_shark_ghost_shark/

########################################

id = get_rt_id(cur, 'Respect Yuichi Sakaki (Neechan Wa Chuunibyou)', 'https://redd.it/wjq4v9')
add_data(['Yuichi Sakak?i'],
'Yuichi Sakaki',
False,
False,
[
    ['Nee(-| )?chan|Chuunibyou']
],
'Neechan Wa Chuunibyou',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wiwqor/respect_yuichi_sakai_neechan_wa_chuunibyou/

########################################

id = get_rt_id(cur, 'Respect Debby (Debby the Corsifa is Emulous; manga)', 'https://redd.it/wj8bps')
add_data(['Debby the Corsifa'],
'Debby the Corsifa',
False,
True,
[
    ['Emulous']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wj8bps/respect_debby_debby_the_corsifa_is_emulous_manga/

########################################

id = get_rt_id(cur, 'Respect Little John! (Robin Hood 1973)', 'https://redd.it/wj8bps')
add_data(['Little John'],
'Little John',
False,
False,
[
    ['Robin Hood', '1973']
],
'Robin Hood, 1973',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Matthias Tannhauser! (Tannhauser Trilogy)', 'https://redd.it/wkeud8')
add_data(['Matthias Tannhauser'],
'Matthias Tannhauser',
False,
True,
[
    ['Trilogy']
],
'Tannhauser',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkeud8/respect_matthias_tannhauser_tannhauser_trilogy/

########################################

id = get_rt_id(cur, 'RESPECT Hundun, Master of Chaos (Legend of Korra Video Game)', 'https://redd.it/wkgy7c')
add_data(['Hundun'],
'Hundun',
False,
False,
[
    ['Korra'], ['A?T?LOK'], ['Avatar']
],
'Avatar: TLA',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkgy7c/respect_hundun_master_of_chaos_legend_of_korra/

########################################

id = get_rt_id(cur, "Respect the Major General Toot-Toot Minimus and the Za-Lord''s Guard (The Dresden Files)", 'https://redd.it/wkhdyp')
add_data(['Toot(-| )Toot'],
'Toot-Toot',
False,
False,
[
    ['Dresden(verse)?']
],
'The Dresden Files',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkhdyp/respect_the_major_general_toottoot_minimus_and/

########################################

id = get_rt_id(cur, 'Respect The Lady in White, Taylor Hebert! (Intuition)', 'https://redd.it/wky5ez')
add_data(['Taylor Hebert'],
'Taylor Hebert',
False,
False,
[
    ['\(Intuition\)']
],
'Intuition',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wky5ez/respect_the_lady_in_white_taylor_hebert_intuition/

########################################

id = get_rt_id(cur, 'Respect Scion! (Intuition)', 'https://redd.it/wkyajc')
add_data(['Scion'],
'Scion',
False,
False,
[
    ['\(Intuition\)']
],
'Intuition',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Gabriel Gray, Mirtis! (Intuition)', 'https://redd.it/wkycm8')
add_data(['Gabriel Gray'],
'Gabriel Gray',
False,
False,
[
    ['\(Intuition\)']
],
'Intuition',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkycm8/respect_gabriel_gray_mirtis_intuition/

########################################

id = get_rt_id(cur, 'Respect Callista! (Five Kingdoms)', 'https://redd.it/wkyxfg')
add_data(['Callista'],
'Callista',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkyxfg/respect_callista_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect the Rogue Knight! (Five Kingdoms)', 'https://redd.it/wkyxgs')
add_data(['Rogue Knight'],
'Rogue Knight',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkyxgs/respect_the_rogue_knight_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Morgassa! (Five Kingdoms)', 'https://redd.it/wkyxhr')
add_data(['Morgassa'],
'Morgassa',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Honor Pemberton! (Five Kingdoms)', 'https://redd.it/wkyxjs')
add_data(['Honor Pemberton'],
'Honor Pemberton',
False,
True,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkyxjs/respect_honor_pemberton_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Trillian! (Five Kingdoms)', 'https://redd.it/wkyxl7')
add_data(['Trillian'],
'Trillian',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Dreadknight! (Five Kingdoms)', 'https://redd.it/wkyxrl')
add_data(['Dreadknight'],
'Dreadknight',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkyxrl/respect_the_dreadknight_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Ramarro! (Five Kingdoms)', 'https://redd.it/wl92ld')
add_data(['Ramarro'],
'Ramarro',
False,
False,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wl92ld/respect_ramarro_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Cole Randolph! (Five Kingdoms)', 'https://redd.it/wl92my')
add_data(['Cole Randolph'],
'Cole Randolph',
False,
True,
[
    ['Five Kingdoms']
],
'Five Kingdoms',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wl92my/respect_cole_randolph_five_kingdoms/

########################################

id = get_rt_id(cur, 'Respect Cadet Dredd (2000AD)', 'https://redd.it/wkzt33')
add_data(['Cadet Dredd'],
'Cadet Dredd',
False,
True,
[
    ['2000 ?AD']
],
'2000 AD',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wkzt33/respect_cadet_dredd_2000ad/

########################################

id = get_rt_id(cur, 'Respect Sir Tristan de Liones (Arthurian Myth)', 'https://redd.it/wl1s5p')
add_data(['Tristan'],
'Tristan',
False,
False,
[
    ['Arthurian']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/wl1s5p/respect_sir_tristan_de_liones_arthurian_myth/

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

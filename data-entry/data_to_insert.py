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

update_respectthread(cur, 14809, 'Respect Satoru Gojo (Jujutsu Kaisen)', 'https://redd.it/16qr5qe')

########################################

add_data(['D4C Love Train'],
'D4C Love Train',
False,
True,
[
    ['Go Beyond'], ['Stands?'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3619}'
)
#https://www.reddit.com/r/whowouldwin/comments/16raey8/which_wins_out_of_the_stands_i_consider_to_be_the/

########################################

add_data(['Soft (&|and) Wet'],
'Soft & Wet',
False,
False,
[
    ['Go Beyond'], ['Stands?'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3628}'
)
#https://www.reddit.com/r/whowouldwin/comments/16raey8/which_wins_out_of_the_stands_i_consider_to_be_the/

########################################

add_data(['Made in Heaven'],
'Made in Heaven',
False,
False,
[
    ['Stands?'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3604}'
)
#https://www.reddit.com/r/respectthreads/comments/64t2af/respect_enrico_pucci_jojos_bizarre_adventure_part/

########################################

add_data(['G\.E\.R'],
'G.E.R.',
False,
False,
[
    ['Stands?'], ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{3591}'
)
#https://www.reddit.com/r/respectthreads/comments/6zy7b0/respect_giorno_giovanna_jojos_bizarre_adventure/

########################################

add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Bat(-| )?mans? ?\(The Batman\)']
],
'The Batman, 2022',
'{22590}'
)
#https://www.reddit.com/r/respectthreads/comments/xd7nvf/respect_batman_the_batman_2022/
#https://www.reddit.com/r/whowouldwin/comments/16umzbb/batman_burtonverse_vs_batman_nolan_vs_batman_the/k2ly75l/?context=3

########################################

add_data(['Wishmaster'],
'Wishmaster',
False,
False,
[
    ['Prismo']
],
"Prismo",
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/16rw7xn/adult_finn_vs_the_star_marceline/k2bliot/?context=3

########################################

id = get_rt_id(cur, 'Respect Latla! (Undead Unluck)', 'https://redd.it/16qh6xy')
add_data(['Latla'],
'Latla',
False,
False,
[
    ['Latla Mirah'], ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Rip! (Undead Unluck)', 'https://redd.it/16qw9lj')
add_data(['Rip'],
'Rip',
False,
False,
[
    ['Rip Tristan'], ['Undead Unluck']
],
'Undead Unluck',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16qw9lj/respect_rip_undead_unluck/

########################################

id = get_rt_id(cur, 'Respect Iron Man Model 1: the Original Armor (Marvel, 616)', 'https://redd.it/16qy7bf')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 1']
],
'Model 1',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16qy7bf/respect_iron_man_model_1_the_original_armor/

########################################

id = get_rt_id(cur, 'Respect The Collector (The Collector)', 'https://redd.it/16qyn39')
add_data(['The Collector'],
'The Collector',
False,
False,
[
    ['The Collector ?\(The Collector'], ['The Collection'], ['Jigsaw']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16qyn39/respect_the_collector_the_collector/

########################################

id = get_rt_id(cur, 'Respect Doctor Stephen Strange (Doctor Strange: The Sorcerer Supreme)', 'https://redd.it/16qynzs')
add_data(['(Doctor|Dr\.?|Stephen) ?Strange'],
'Doctor Strange',
False,
False,
[
    ['Doctor Strange: The Sorcerer Supreme']
],
'Doctor Strange: The Sorcerer Supreme',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16qynzs/respect_doctor_stephen_strange_doctor_strange_the/

########################################

id = get_rt_id(cur, 'Respect Batman (Burtonverse)', 'https://redd.it/16qyox9')
add_data(['Bat(-| )?mans?'],
'Batman',
False,
False,
[
    ['Burtonverse']
],
'Burtonverse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16qyox9/respect_batman_burtonverse/

########################################

id = get_rt_id(cur, 'Respect King Arthur[The 21st Century Guide to Mythology]', 'https://redd.it/16rdnwp')
add_data(['King Arthur'],
'King Arthur',
False,
False,
[
    ['21st Century Guide to Mythology']
],
'The 21st Century Guide to Mythology',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16rdnwp/respect_king_arthurthe_21st_century_guide_to/

########################################

id = get_rt_id(cur, "Respect Ash''s Pidgeot (Pokemon Anime)", 'https://redd.it/16rrivn')
add_data(['Pidgeotto'],
'Pidgeotto',
False,
False,
[
    ['Ash']
],
'Ash',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Pidgeot'],
'Pidgeot',
False,
False,
[
    ['Ash']
],
'Ash',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Superdupont (Superdupont)', 'https://redd.it/16sugk4')
add_data(['Superdupont'],
'Superdupont',
False,
True,
[
    ['Superdupont ?\(Superdupont\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16sugk4/respect_superdupont_superdupont/

########################################

id = get_rt_id(cur, 'Respect Thor Odinson, the Herald of Thunder (Marvel, Earth-616)', 'https://redd.it/16s577z')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['Herald( King)? Thor'], ['Herald of Thunder'], ['Herald of Galactus Thor'], ['Cosmic King Thor']
],
'Herald',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yetrigar (Marvel Comics, Earth-616)', 'https://redd.it/16ssg1u')
add_data(['Yetrigar'],
'Yetrigar',
False,
True,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16ssg1u/respect_yetrigar_marvel_comics_earth616/

########################################

id = get_rt_id(cur, 'Respect Alpha (The killer Sloth from Slotherhouse)', 'https://redd.it/16sz6w0')
add_data(['Alpha'],
'Alpha',
False,
False,
[
    ['Slotherhouse'], ['Killer Sloth']
],
'Slotherhouse',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16sz6w0/respect_alpha_the_killer_sloth_from_slotherhouse/

########################################

id = get_rt_id(cur, "Respect Casey Jones, Ranger X! (Mighty Morphin'' Power Rangers/Teenage Mutant Ninja Turtles)", 'https://redd.it/16tqfra')
add_data(['Casey Jones'],
'Casey Jones',
False,
False,
[
    ['Ranger X']
],
'Ranger X',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16tqfra/respect_casey_jones_ranger_x_mighty_morphin_power/

########################################

id = get_rt_id(cur, 'Respect Darkiplier! (Markiplier Canon)', 'https://redd.it/16u0ajv')
add_data(['Darkiplier'],
'Darkiplier',
False,
True,
[
    ['Markiplier']
],
'Markiplier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16u0ajv/respect_darkiplier_markiplier_canon/

########################################

id = get_rt_id(cur, 'Respect Barbara! (Markiplier Animated – The Legend of Barbara)', 'https://redd.it/16u5gdt')
add_data(['Barbara'],
'Barbara',
False,
False,
[
    ['Markiplier']
],
'Markiplier',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16u5gdt/respect_barbara_markiplier_animated_the_legend_of/

########################################

id = get_rt_id(cur, 'Respect Antisepticeye! (Jacksepticeye Canon)', 'https://redd.it/16umyz7')
add_data(['Antisepticeye'],
'Antisepticeye',
False,
True,
[
    ['Jacksepticeye']
],
'Jacksepticeye',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16umyz7/respect_antisepticeye_jacksepticeye_canon/

########################################

id = get_rt_id(cur, 'Respect Matt Murdock, Daredevil Noir (Marvel, 90214)', 'https://redd.it/16uz0f7')
add_data(['Daredevil Noir'],
'Daredevil Noir',
False,
True,
[
    ['90214']
],
'90214',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16uz0f7/respect_matt_murdock_daredevil_noir_marvel_90214/

########################################

id = get_rt_id(cur, 'Respect Tommy! (Life of Luxury)', 'https://redd.it/16v24pn')
add_data(['Tommy'],
'Tommy',
False,
False,
[
    ['Life of Luxury']
],
'Life of Luxury',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16v24pn/respect_tommy_life_of_luxury/

########################################

id = get_rt_id(cur, 'Respect Fionna and Cake (Adventure Time)', 'https://redd.it/16vdpt6')
add_data(['Fionna'],
'Fionna',
False,
False,
[
    ['Adventure Time'], ['Fionna the Human']
],
'Adventure Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vdpt6/respect_fionna_and_cake_adventure_time/

add_data(['Cake the Cat'],
'Cake the Cat',
False,
True,
[
    ['Adventure Time']
],
'Adventure Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vdpt6/respect_fionna_and_cake_adventure_time/

add_data(['Fionna and Cake'],
'Fionna and Cake',
True,
True,
[
    ['Adventure Time']
],
'Adventure Time',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/16vdpt6/respect_fionna_and_cake_adventure_time/

########################################

id = get_rt_id(cur, 'Ethan Hunt Respect Thread [In progress] ', 'https://comicvine.gamespot.com/forums/gen-discussion-1/ethan-hunt-respect-thread-in-progress-1968660/')
add_data(['Ethan Hunt'],
'Ethan Hunt',
False,
True,
[
    ['Mission:? Impossible']
],
'Mission: Impossible',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/16vlevr/james_bond_replaces_ethan_hunt_in_mission/k2roojy/?context=3

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

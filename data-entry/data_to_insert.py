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

update_respectthread(cur, 3898, 'Respect Zenkichi Hitoyoshi! (Medaka Box)', 'https://redd.it/12aoua3')

########################################

id = get_rt_id(cur, 'Spandam (One Piece)', 'https://redd.it/12a074b')
add_data(['Spandam'],
'Spandam',
False,
True,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12a074b/spandam_one_piece/

########################################

id = get_rt_id(cur, 'Respect Tom (One Piece)', 'https://redd.it/12b4b46')
add_data(['Tom'],
'Tom',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12b4b46/respect_tom_one_piece/

########################################

id = get_rt_id(cur, 'Respect Harry Dresden! (The Dresden Files [TV Series])', 'https://redd.it/12ajpkq')
add_data(['Harry Dresden'],
'Harry Dresden',
False,
False,
[
    ['Dresden Files', 'TV (Shows?|Series)']
],
'The Dresden Files TV Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12ajpkq/respect_harry_dresden_the_dresden_files_tv_series/

########################################

id = get_rt_id(cur, 'Respect Tony Stark, The Iron Monarch of the Earth (Marvel, Earth-42777)', 'https://redd.it/12asu6v')
add_data(['Tony Stark'],
'Iron Man',
False,
False,
[
    ['Iron Monarch'], ['42777']
],
'42777',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12asu6v/respect_tony_stark_the_iron_monarch_of_the_earth/

########################################

id = get_rt_id(cur, 'Respect the Beatles! (Beatles song lyrics)', 'https://redd.it/12auaw0')
add_data(['The Beatles'],
'The Beatles',
False,
True,
[
    ['song lyrics']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12auaw0/respect_the_beatles_beatles_song_lyrics/

########################################

id = get_rt_id(cur, 'Respect Mike Munroe (Until Dawn)', 'https://redd.it/12b3wcm')
add_data(['Mike'],
'Mike',
False,
False,
[
    ['Until Dawn'], ['Mike Munroe']
],
'Until Dawn',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12b3wcm/respect_mike_munroe_until_dawn/

########################################

id = get_rt_id(cur, 'Respect Doomsday (DC Comics, Post Flashpoint)', 'https://redd.it/12bhsie')
add_data(['Doomsday'],
'Doomsday',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12bhsie/respect_doomsday_dc_comics_post_flashpoint/

########################################

id = get_rt_id(cur, 'Respect the Falling Devil! (Chainsaw Man)', 'https://redd.it/12bwgzp')
add_data(['Falling Devil'],
'Falling Devil',
False,
True,
[
    ['Chainsaw(-| )?Man']
],
'Chainsaw Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12bwgzp/respect_the_falling_devil_chainsaw_man/

########################################

id = get_rt_id(cur, 'Respect the White Dragon! (Marvel Comics, 616)', 'https://redd.it/12byo8u')
add_data(['White Dragon'],
'White Dragon',
False,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12byo8u/respect_the_white_dragon_marvel_comics_616/

########################################

id = get_rt_id(cur, "Respect the White Tigerzord (Mighty Morphin'' Power Rangers)", 'https://redd.it/12bz5yj')
add_data(['Tigerzord'],
'Tigerzord',
False,
True,
[
    ['Power Rangers?']
],
'Power Rangers',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12bz5yj/respect_the_white_tigerzord_mighty_morphin_power/

########################################

id = get_rt_id(cur, 'Respect the Transforming Bot! (Xiaolin Showdown)', 'https://redd.it/12c4irj')
add_data(['Transforming Bot'],
'Transforming Bot',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12c4irj/respect_the_transforming_bot_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Robo-Jack Spicers! (Xiaolin Showdown)', 'https://redd.it/12c51hy')
add_data(['Robo(-| )Jack Spicers'],
'Robo-Jack Spicers',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12c51hy/respect_the_robojack_spicers_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect Dude-Bot! (Xiaolin Showdown)', 'https://redd.it/12c5nhk')
add_data(['Dude(-| )Bot'],
'Dude-Bot',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12c5nhk/respect_dudebot_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Chameleon-Bot! (Xiaolin Showdown)', 'https://redd.it/12c60a8')
add_data(['Chameleon(-| )Bot'],
'Chameleon-Bot',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12c60a8/respect_the_chameleonbot_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Golden Tiger Claws! (Xiaolin Showdown)', 'https://redd.it/12ckjc2')
add_data(['Golden Tiger Claws'],
'Golden Tiger Claws',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12ckjc2/respect_the_golden_tiger_claws_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Reversing Mirror! (Xiaolin Showdown)', 'https://redd.it/12cl9x0')
add_data(['Reversing Mirror'],
'Reversing Mirror',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cl9x0/respect_the_reversing_mirror_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Sword of the Storm! (Xiaolin Showdown)', 'https://redd.it/12cpwcj')
add_data(['Sword of the Storm'],
'Sword of the Storm',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cpwcj/respect_the_sword_of_the_storm_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Shroud of Shadows! (Xiaolin Showdown)', 'https://redd.it/12cq93r')
add_data(['Shroud of Shadows'],
'Shroud of Shadows',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cq93r/respect_the_shroud_of_shadows_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Changing Chopsticks! (Xiaolin Showdown)', 'https://redd.it/12cqmd4')
add_data(['Changing Chopsticks'],
'Changing Chopsticks',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cqmd4/respect_the_changing_chopsticks_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Silk Spitter! (Xiaolin Showdown)', 'https://redd.it/12cu69x')
add_data(['Silk Spitter'],
'Silk Spitter',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cu69x/respect_the_silk_spitter_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Mantis Flip Coin! (Xiaolin Showdown)', 'https://redd.it/12dah4n')
add_data(['Mantis Flip Coin'],
'Mantis Flip Coin',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dah4n/respect_the_mantis_flip_coin_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Lotus Twister! (Xiaolin Showdown)', 'https://redd.it/12dapmu')
add_data(['Lotus Twister'],
'Lotus Twister',
False,
True,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dapmu/respect_the_lotus_twister_xiaolin_showdown/

########################################

id = get_rt_id(cur, 'Respect the Monkey Staff! (Xiaolin Showdown)', 'https://redd.it/12db395')
add_data(['Monkey Staff'],
'Monkey Staff',
False,
False,
[
    ['Xiaolin Showdown'], ['Shen Gong Wu']
],
'Xiaolin Showdown',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12db395/respect_the_monkey_staff_xiaolin_showdown/


########################################

id = get_rt_id(cur, 'Respect Armen Ikarus, Amazo (DC, New 52)', 'https://redd.it/12cj1cc')
add_data(['Armen Ikarus'],
'Armen Ikarus',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cj1cc/respect_armen_ikarus_amazo_dc_new_52/

add_data(['Armen Ikarus'],
'Armen Ikarus',
False,
False,
[
    ['New(-| )?52'], ['Nu?-?52'], ['Post(-| )52'], ['Prime(-| )Earth'], ['Rebirth']
],
'New 52',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12cj1cc/respect_armen_ikarus_amazo_dc_new_52/

########################################

id = get_rt_id(cur, 'Respect Joshua Walker, The All American Boy (DC, Post Crisis)', 'https://redd.it/12dkxc0')
add_data(['Joshua Walker'],
'Joshua Walker',
False,
False,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dkxc0/respect_joshua_walker_the_all_american_boy_dc/

add_data(['Joshua Walker'],
'Joshua Walker',
False,
False,
[
    ['PC'], ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dkxc0/respect_joshua_walker_the_all_american_boy_dc/

########################################

id = get_rt_id(cur, "Respect the God of the Hebrews (Dreamworks'' The Prince of Egypt)", 'https://redd.it/12dp7p1')
add_data(['God'],
'God',
False,
False,
[
    ['Prince of Egypt']
],
'The Prince of Egypt',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dp7p1/respect_the_god_of_the_hebrews_dreamworks_the/

add_data(['Moses'],
'Moses',
False,
False,
[
    ['Prince of Egypt']
],
'The Prince of Egypt',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dp7p1/respect_the_god_of_the_hebrews_dreamworks_the/


########################################

id = get_rt_id(cur, "Respect Jesus Christ (Jesus'' Betrayal : What Really Went Down)", 'https://redd.it/12dp83j')
add_data(['Jesus'],
'Jesus',
False,
False,
[
    ["Jesus''? Betrayal", 'What Really Went Down']
],
"Jesus'' Betrayal : What Really Went Down",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dp83j/respect_jesus_christ_jesus_betrayal_what_really/

########################################

id = get_rt_id(cur, 'Respect Spawn! (Mortal Kombat)', 'https://redd.it/12dr0q8')
add_data(['Spawn'],
'Spawn',
False,
False,
[
    ['Mortal Kombat']
],
'Mortal Kombat',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dr0q8/respect_spawn_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect: Generic Adeptus Custodes (Warhammer 40k)', 'https://redd.it/12dv29t')
add_data(['Adeptus Custodes'],
'Adeptus Custodes',
False,
False,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/12dv29t/respect_generic_adeptus_custodes_warhammer_40k/

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

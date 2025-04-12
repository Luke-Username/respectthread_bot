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

update_respectthread(cur, 6658, 'Respect Spinel (Steven Universe)', 'https://redd.it/1jv3sgi')
update_respectthread(cur, 590, 'Respect Gabriel Van Helsing (Van Helsing, 2004)', 'https://redd.it/1jv4u5j')
update_respectthread(cur, 12408, 'Respect En (Dorohedoro)', 'https://redd.it/1jv4w2b')
update_respectthread(cur, 135, 'Respect Dominic Toretto! (The Fast and the Furious)', 'https://redd.it/1jvf5ps')
update_respectthread(cur, 3002, 'Respect Akame! (Akame Ga Kill)', 'https://redd.it/1jvg4ut')
update_respectthread(cur, 1174, 'Respect Miles Morales, Spider-Man! (Spider-Verse)', 'https://redd.it/1jvheyk')
update_respectthread(cur, 1790, 'Respect Superman (DC Comics, Earth-31)', 'https://redd.it/1jxjhc8')
update_respectthread(cur, 276, 'Respect Agent Smith! (The Matrix)', 'https://redd.it/1jx1t7k')


########################################
add_data(['Predator'],
'Predator',
False,
False,
[
	['Predator vs', 'r/predator']
],
'',
'{2799,13507}'
)
#https://www.reddit.com/r/whowouldwin/comments/1jw7y6d/predator_vs_jason/mmgcqf8/?context=3

########################################

id = get_rt_id(cur, 'Respect Iron Man, Model 3 (Marvel, 616)', 'https://redd.it/1jtlr24')
add_data(['I(ro|or)n(-| )?Man'],
'Iron Man',
False,
False,
[
    ['Model 3']
],
'Model 3',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jtlr24/respect_iron_man_model_3_marvel_616/

########################################

id = get_rt_id(cur, 'Respect Gyoro Gyoro! (One-Punch Man)', 'https://redd.it/1jtst2u')
add_data(['Gyoro Gyoro'],
'Gyoro Gyoro',
False,
True,
[
    ['One(-| )Punch Man'], ['OPM']
],
'One Punch Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jtst2u/respect_gyoro_gyoro_onepunch_man/

########################################

id = get_rt_id(cur, 'Respect General Thaddeus "Thunderbolt" Ross, The Red Hulk (Marvel Cinematic Universe)', 'https://redd.it/1jueozf')
add_data(['Red Hulk'],
'Red Hulk',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jueozf/respect_general_thaddeus_thunderbolt_ross_the_red/

########################################

id = get_rt_id(cur, 'Respect Gomah (Dragon Ball Daima)', 'https://redd.it/1juwdqv')
add_data(['Gomah'],
'Gomah',
False,
False,
[
    ['Dragon ?Ball'], ['DB(Z|S)'], ['Daima']
],
'Dragon Ball',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1juwdqv/respect_gomah_dragon_ball_daima/

########################################

id = get_rt_id(cur, 'Respect Miyamoto Iori (Fate/Samurai Remnant)', 'https://redd.it/1jv3pma')
add_data(['Miyamoto Iori'],
'Miyamoto Iori',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Yamato Takeru (Fate/Samurai Remnant)', 'https://redd.it/1jvjarv')
add_data(['Yamato Takeru'],
'Yamato Takeru',
False,
False,
[
    ['Fate'], ['Samurai Remnant']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvjarv/respect_yamato_takeru_fatesamurai_remnant/

########################################

id = get_rt_id(cur, 'Respect Alice Kuonji (Witch on the Holy Night/TYPE-MOON)', 'https://redd.it/1jv98ri')
add_data(['Alice Kuonji'],
'Alice Kuonji',
False,
True,
[
    ['Fate'], ['Witch on the Holy Night'], ['TYPE(-| )MOON'], ['Mah(ō|o)tsukai no Yoru']
],
'Fate',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Black Hand (DC Comics, Post-Crisis)', 'https://redd.it/1jv3wja')
add_data(['Black Hand'],
'Black Hand',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv3wja/respect_black_hand_dc_comics_postcrisis/


########################################

id = get_rt_id(cur, 'Respect Professor Pyg (DC Comics, Post-Flashpoint)', 'https://redd.it/1jv4mev')
add_data(['Professor Pyg'],
'Professor Pyg',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Professor Pyg'],
'Professor Pyg',
False,
True,
[
    ['\(DC( Comics)?\)'], ['\[DC( Comics)?\]'], ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Nimona (Nimona) [Graphic Novel]', 'https://redd.it/1jv4fsh')
id2 = get_rt_id(cur, 'Respect Nimona (Nimona) [Animated Film]', 'https://redd.it/1jv4fxv')
add_data(['Nimona'],
'Nimona',
False,
True,
[
    ['Nimona ?\(Nimona\)'], ['movie Nimona'], ['Nimona ?\(movie'], ['Nimona.*Netflix']
],
'',
'{' + '{}, {}'.format(id, id2) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv4fsh/respect_nimona_nimona_graphic_novel/
#https://www.reddit.com/r/respectthreads/comments/1jv4fxv/respect_nimona_nimona_animated_film/

########################################

id = get_rt_id(cur, "Respect Rick O''Connell (The Mummy Trilogy)", 'https://redd.it/1jv4hvn')
add_data(["Rick O(''| )?Connell"],
"Rick O''Connell",
False,
True,
[
    ['Mummy']
],
'The Mummy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Marvin the Martian (Looney Tunes)', 'https://redd.it/1jv584k')
add_data(['Marvin the Martian'],
'Marvin the Martian',
False,
True,
[
    ['Looney Tunes']
],
'Looney Tunes',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv584k/respect_marvin_the_martian_looney_tunes/

########################################

id = get_rt_id(cur, 'Respect Damian "DJ" Drake Jr (Looney Tunes: Back in Action)', 'https://redd.it/1jvjwks')
add_data(['D\.?J\.? Drake'],
'D.J. Drake',
False,
False,
[
    ['Looney Tunes']
],
'Looney Tunes: Back in Action',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Princess (Slay the Princess)', 'https://redd.it/1jv6tfl')
add_data(['Princess'],
'Princess',
False,
False,
[
    ['Slay the Princess']
],
'Slay the Princess',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv6tfl/respect_the_princess_slay_the_princess/

########################################

id = get_rt_id(cur, 'Respect Cio (Kill Six Billion Demons)', 'https://redd.it/1jv98tn')
add_data(['Cio'],
'Cio',
False,
False,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv98tn/respect_cio_kill_six_billion_demons/

add_data(['Cio(cie)? Cioelle'],
'Ciocie Cioelle',
False,
True,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv98tn/respect_cio_kill_six_billion_demons/

########################################

id = get_rt_id(cur, 'Respect 6 Juggernaut Star Scours the Universe (Kill Six Billion Demons)', 'https://redd.it/1jv98w3')
add_data(['6 Juggernaut Star Scours the Universe'],
'6 Juggernaut Star Scours the Universe',
False,
True,
[
    ['Kill ?(Six|6) ?Billion ?Demons'], ['K(S|6)BD']
],
'Kill Six Billion Demons',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jv98w3/respect_6_juggernaut_star_scours_the_universe/

########################################

id = get_rt_id(cur, 'Respect Misaki Sakimiya (Dead Mount Death Play)', 'https://redd.it/1jva7pc')
add_data(['Misaki Sakimiya'],
'Misaki Sakimiya',
False,
True,
[
    ['Dead Mount Death Play']
],
'Dead Mount Death Play',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jva7pc/respect_misaki_sakimiya_dead_mount_death_play/

########################################

id = get_rt_id(cur, 'Respect Corpse God (Dead Mount Death Play)', 'https://redd.it/1jva8pl')
add_data(['Corpse God'],
'Corpse God',
False,
False,
[
    ['Dead Mount Death Play']
],
'Dead Mount Death Play',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jva8pl/respect_corpse_god_dead_mount_death_play/

########################################

id = get_rt_id(cur, 'Respect Ganondorf (The Legend of Zelda: Tears of the Kingdom)', 'https://redd.it/1jvbu2m')
add_data(['Ganon(dorf)'],
'Ganondorf',
False,
False,
[
    ['Tears of the Kingdom'], ['TOTK']
],
'Tears of the Kingdom',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/

 ########################################

id = get_rt_id(cur, 'Respect Benjamin Gates (National Treasure)', 'https://redd.it/1jvg6jt')
add_data(['Benjamin( Franklin)? Gates'],
'Benjamin Gates',
False,
False,
[
    ['National Treasure']
],
'National Treasure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/

 
 ########################################
 
id = get_rt_id(cur, 'Respect Miles Morales, Spider-Man! (Spider-Verse)', 'https://redd.it/1jvheyk')
add_data(['Benjamin( Franklin)? Gates'],
'Benjamin Gates',
False,
False,
[
    ['National Treasure']
],
'National Treasure',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/

 ########################################
 
id = get_rt_id(cur, "Respect Himmel the Hero! (Frieren: Beyond Journey''s End)", 'https://redd.it/1jvipz7')
add_data(['Himmel'],
'Himmel',
False,
False,
[
    ['Frieren'], ['Himmel the Hero']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################

id = get_rt_id(cur, "Respect Übel (Frieren: Beyond Journey''s End)", 'https://redd.it/1jx2x83')
add_data(['(Ü|U)bel'],
'Übel',
False,
False,
[
    ['Frierens?']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################
id = get_rt_id(cur, "Respect Sein (Frieren: Beyond Journey''s End)", 'https://redd.it/1jxfuff')
add_data(['Sein'],
'Sein',
False,
False,
[
    ['Frierens?']
],
"Frieren: Beyond Journey''s End",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################
 
id = get_rt_id(cur, 'Respect the Twelfth Doctor (Doctor Who)', 'https://redd.it/1jvxpt3')
add_data(['(Twelf|12)th Doctor'],
'Twelfth Doctor',
False,
False,
[
	['(Doctor|Dr\.?) ?Who'], ['Who(ni)?verse']
],
"Doctor Who",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################

id = get_rt_id(cur, 'Respect the Gaiaphage, the Darkness (Gone)', 'https://redd.it/1jwc3sp')
add_data(['Gaiaphage'],
'Gaiaphage',
False,
False,
[
	['Gone']
],
'Gone',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################

id = get_rt_id(cur, "Respect the Prince (Disney''s Cinderella Trilogy)", 'https://redd.it/1jwhvdh')
add_data(['Prince'],
'Prince',
False,
False,
[
	['Prince .*Cinderella']
],
"Disney''s Cinderella",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/

add_data(['Prince Charming'],
'Prince Charming',
False,
False,
[
	['Cinderella']
],
"Disney''s Cinderella",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################

id = get_rt_id(cur, "Respect Anastasia (Disney''s Cinderella Trilogy)", 'https://redd.it/1jwi6yi')
add_data(['Anastasia'],
'Anastasia',
False,
False,
[
	['Disney', 'Cinderella']
],
"Disney''s Cinderella",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################

id = get_rt_id(cur, "Respect Cinderella (Disney''s Cinderella Trilogy)", 'https://redd.it/1jwi73e')
add_data(['Cinderella'],
'Cinderella',
False,
False,
[
	['Disney']
],
'Disney',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################
id = get_rt_id(cur, "Respect the King (Disney''s Cinderella Trilogy)", 'https://redd.it/1jwi8pc')
add_data(['King'],
'King',
False,
False,
[
	["Disney''?s Cinderella"]
],
"Disney''s Cinderella",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/



########################################

id = get_rt_id(cur, 'Respect "That Man," Empty Void! (One-Punch Man [Manga])', 'https://redd.it/1jwi7cz')
add_data(['Empty Void'],
'Empty Void',
False,
False,
[
	['One(-| )Punch Man'], ['OPM']
],
'One Punch Man',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/

########################################
id = get_rt_id(cur, 'Respect Nathan Caine (Novocaine)', 'https://redd.it/1jwn9px')
add_data(['Nathan Caine'],
'Nathan Caine',
False,
False,
[
	['Novocaine']
],
'Novocaine',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


add_data(['Novocaine'],
'Novocaine',
False,
True,
[
	['Nathan']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


########################################
id = get_rt_id(cur, 'Respect Ooube No OO(Joujuu Senjin!! Mushibugyo)', 'https://redd.it/1jxheyl')
add_data(['Ooube No Oo'],
'Ooube No Oo',
False,
False,
[
	['Mushibugy(ō|o)']
],
'Mushibugyō',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1jvbu2m/respect_ganondorf_the_legend_of_zelda_tears_of/


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

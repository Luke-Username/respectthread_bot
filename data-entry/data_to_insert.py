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

update_respectthread(cur, 6142, 'Respect Count Dracula (Dracula, Novel)', 'https://redd.it/17kl1r4')
update_respectthread(cur, 16432, 'Respect Jason Voorhees! (Never Hike Alone)', 'https://redd.it/17ksi4i')

########################################

add_data(['God Gundam'],
'God Gundam',
False,
True,
[
    ['Domon Kasshu']
],
'',
'{3460}'
)
#https://www.reddit.com/r/whowouldwin/comments/17k9sda/how_the_hell_can_a_team_of_op_gundams_take_down/k76ab26/?context=3

########################################

add_data(['Quasimodo'],
'Quasimodo',
False,
False,
[
    ['(DiMeo|Soprano) crime family'], ['Nostradamus']
],
'',
'{}'
)
#https://www.reddit.com/r/whowouldwin/comments/17kdm1m/could_the_dimeo_crime_family_survive_jurassic/k772mhm/?context=3

########################################

id = get_rt_id(cur, 'Respect Michael Badilino, Vengeance! (Marvel Comics, Earth-616)', 'https://redd.it/17jvne5')
add_data(['Vengeance'],
'Vengeance',
False,
False,
[
    ['Michael Badilino', '616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17jvne5/respect_michael_badilino_vengeance_marvel_comics/

########################################

id = get_rt_id(cur, "Respect William Afton (Five Nights at Freddy''s Movie)", 'https://redd.it/17jwqr0')
add_data(['William Afton'],
'William Afton',
False,
False,
[
    ['Five Nights at Fredd(ys?|ies)', '(movie|film)'], ['FNAF\d?', '(movie|film)']
],
'FNAF Movie',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17jwqr0/respect_william_afton_five_nights_at_freddys_movie/

########################################

id = get_rt_id(cur, 'Respect Rorschach (2009 Watchmen Movie)', 'https://redd.it/17k2nu3')
add_data(['Rorschach'],
'Rorschach',
False,
False,
[
    ['Watchmen (movie|film)s?'], ['Watchmen', '2009']
],
'Watchmen, 2009',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17k2nu3/respect_rorschach_2009_watchmen_movie/

########################################

id = get_rt_id(cur, 'Respect Michael Myers (Robot Chicken)', 'https://redd.it/17k2rf5')
add_data(['Mich(ae|ea)l Me?yers'],
'Michael Myers',
False,
False,
[
    ['Robot Chicken']
],
'Robot Chicken',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17k2rf5/respect_michael_myers_robot_chicken/

########################################

id = get_rt_id(cur, 'Respect Monique Dupre (Godzilla: The Series)', 'https://redd.it/17k4fn1')
add_data(['Monique Dupr(é|e)'],
'Monique Dupré',
False,
True,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17k4fn1/respect_monique_dupre_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Nick Tatopoulos (Godzilla: The Series)', 'https://redd.it/17k4u2k')
add_data(['Nick Tatopoulos'],
'Nick Tatopoulos',
False,
False,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect H.E.A.T. (Godzilla: The Series)', 'https://redd.it/17k51qb')
add_data(['H\.E\.A\.T\.?'],
'H.E.A.T.',
False,
False,
[
    ['Godzilla:? The Series']
],
'Godzilla: The Series',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17k51qb/respect_heat_godzilla_the_series/

########################################

id = get_rt_id(cur, 'Respect Tualon Yaluna (Star Wars Canon)', 'https://redd.it/17k6vut')
add_data(['Tualon Yaluna'],
'Tualon Yaluna',
False,
True,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17k6vut/respect_tualon_yaluna_star_wars_canon/

########################################

id = get_rt_id(cur, 'Respect Mystery Inc. (Scooby-Doo, 1998-2001 Movies)', 'https://redd.it/17kfozy')
add_data(['Mystery Inc(orporated)?'],
'Mystery Inc.',
True,
False,
[
    ['Scooby(-| )?Doo', '1998']
],
'Scooby-Doo, 1998',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17kfozy/respect_mystery_inc_scoobydoo_19982001_movies/

########################################

id = get_rt_id(cur, 'Respect Corey Cunningham (Halloween Ends)', 'https://redd.it/17kkql6')
add_data(['Corey Cunningham'],
'Corey Cunningham',
False,
True,
[
    ['Halloween']
],
'Halloween',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17kkql6/respect_corey_cunningham_halloween_ends/

########################################

id = get_rt_id(cur, "Respect the Living Dead (George A. Romero''s Dead series)", 'https://redd.it/17kktev')
add_data(['Night of the Living Dead'],
'Night of the Living Dead',
False,
True,
[
    ['Romero']
],
'',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Dawn of the Dead'],
'Dawn of the Dead',
False,
True,
[
    ['1978']
],
'1978',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Dawn of the Dead'],
'Dawn of the Dead',
False,
False,
[
    ['2004']
],
'2004',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Dredge (Dead by Daylight)', 'https://redd.it/17ko8pz')
add_data(['Dredge'],
'Dredge',
False,
False,
[
    ['Dead by Daylight'], ['DBD']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17ko8pz/respect_the_dredge_dead_by_daylight/

########################################

id = get_rt_id(cur, 'Respect Godzilla (If Godzilla was in Mortal Kombat...)', 'https://redd.it/17kqjma')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['If Godzilla was in Mortal Kombat']
],
'If Godzilla was in Mortal Kombat...',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17kqjma/respect_godzilla_if_godzilla_was_in_mortal_kombat/

########################################

id = get_rt_id(cur, 'Respect The Smile Entity (Smile)', 'https://redd.it/17krcp5')
add_data(['Smile Entity'],
'Smile Entity',
False,
False,
[
    ['The Smile entity']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17krcp5/respect_the_smile_entity_smile/

########################################

id = get_rt_id(cur, "Respect the Mighty Morphin' Turtle Rangers (Mighty Morphin'' Power Rangers/Teenage Mutant Ninja Turtles)", 'https://redd.it/17kuq7n')
add_data(["Mighty Morphing?''? Turtle Rangers"],
"Mighty Morphin'' Turtle Rangers",
True,
True,
[
    ['The Smile entity']
],
"Mighty Morphin'' Power Rangers/Teenage Mutant Ninja Turtles",
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/17kuq7n/respect_the_mighty_morphin_turtle_rangers_mighty/

########################################

id = get_rt_id(cur, 'The Deer (Adventure Time)', 'https://redd.it/17kzsds')
add_data(['The Deer'],
'The Deer',
False,
False,
[
    ['Adventure Time']
],
'Adventure Time',
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

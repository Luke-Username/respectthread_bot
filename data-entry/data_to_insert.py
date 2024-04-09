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

update_respectthread(cur, 22331, 'Respect Mr. Justice, The Number One Ultra (FIGHTERS)', 'https://redd.it/1bwzfou')
update_respectthread(cur, 22284, 'Respect King Rocker, Biggy (FIGHTERS)', 'https://redd.it/1bxr62o')

########################################

id = get_rt_id(cur, "Respect Ravenor''s Rogues Gallery (Warhammer 40k)", 'https://redd.it/1bx2b7s')
add_data(["Ravenor''s Rogues Gallery"],
"Ravenor''s Rogues Gallery",
True,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx2b7s/respect_ravenors_rogues_gallery_warhammer_40k/

add_data(['Toros Revoke'],
'Toros Revoke',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx2b7s/respect_ravenors_rogues_gallery_warhammer_40k/

add_data(['Lucius Worna'],
'Lucius Worna',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx2b7s/respect_ravenors_rogues_gallery_warhammer_40k/

add_data(['Zygmunt Molotch'],
'Zygmunt Molotch',
False,
True,
[
    ['(WH)?40K'], ['Warhammer']
],
'Warhammer 40k',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx2b7s/respect_ravenors_rogues_gallery_warhammer_40k/

########################################

id = get_rt_id(cur, 'Respect Godzilla! (Epic Rap Battles of History)', 'https://redd.it/1bx684e')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx684e/respect_godzilla_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Goku! (Epic Rap Battles of History)', 'https://redd.it/1bx6h7g')
add_data(['Goku'],
'Goku',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx6h7g/respect_goku_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Superman! (Epic Rap Battles of History)', 'https://redd.it/1bx6h85')
add_data(['Super(-| )?man'],
'Superman',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx6h85/respect_superman_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Count Dracula! (Epic Rap Battles of History)', 'https://redd.it/1bx6pqb')
add_data(['Dracula'],
'Dracula',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx6pqb/respect_count_dracula_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Thanos! (Epic Rap Battles of History)', 'https://redd.it/1bx6t0a')
add_data(['Thanos'],
'Thanos',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx6t0a/respect_thanos_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Harry Potter! (Epic Rap Battles of History)', 'https://redd.it/1bx70mz')
add_data(['Harry Potter'],
'Harry Potter',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx70mz/respect_harry_potter_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Luke Skywalker! (Epic Rap Battles of History)', 'https://redd.it/1bx70ql')
add_data(['Luke Skywall?ker'],
'Luke Skywalker',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx70ql/respect_luke_skywalker_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Thor! (Epic Rap Battles of History)', 'https://redd.it/1bx74q1')
add_data(['Thor'],
'Thor',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx74q1/respect_thor_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Darth Vader! (Epic Rap Battles of History)', 'https://redd.it/1bx7a69')
add_data(['Vader'],
'Darth Vader',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Adolf Hitler! (Epic Rap Battles of History)', 'https://redd.it/1bx7f6w')
add_data(['Hitler'],
'Hitler',
False,
False,
[
    ['Epic Rap Battles of History'], ['ERB']
],
'Epic Rap Battles of History',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bx7f6w/respect_adolf_hitler_epic_rap_battles_of_history/

########################################

id = get_rt_id(cur, 'Respect Chappie (Chappie)', 'https://redd.it/1bxg61f')
add_data(['Chappie'],
'Chappie',
False,
True,
[
    ['Chappie "\(Chappie\)']
],
'',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bxg61f/respect_chappie_chappie/

########################################

id = get_rt_id(cur, 'Respect the Panther of the Evil Forest (Arthurian Mythology)', 'https://redd.it/1bxii05')
add_data(['Panther of the Evil Forest'],
'Panther of the Evil Forest',
False,
False,
[
    ['Arthurian']
],
'Arthurian Myth',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bxii05/respect_the_panther_of_the_evil_forest_arthurian/

########################################

id = get_rt_id(cur, 'Respect The Protagonist (Cruelty Squad)', 'https://redd.it/1bybubb')
add_data(['Protagonist'],
'Protagonist',
False,
False,
[
    ['Cruelty Squad']
],
'Cruelty Squad',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bybubb/respect_the_protagonist_cruelty_squad/

add_data(['M\.?T\.? Foxtrot'],
'MT Foxtrot',
False,
False,
[
    ['Cruelty Squad']
],
'Cruelty Squad',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bybubb/respect_the_protagonist_cruelty_squad/

add_data(['Empty Fuck'],
'Empty Fuck',
False,
False,
[
    ['Cruelty Squad']
],
'Cruelty Squad',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bybubb/respect_the_protagonist_cruelty_squad/

add_data(['John Cruelty'],
'John Cruelty',
False,
False,
[
    ['Cruelty Squad']
],
'Cruelty Squad',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bybubb/respect_the_protagonist_cruelty_squad/


########################################

id = get_rt_id(cur, 'Respect Jesus Christ (Ethereal Snake)', 'https://redd.it/1byd63i')
add_data(['Jesus'],
'Jesus',
False,
False,
[
    ['Ethereal Snake']
],
'Ethereal Snake',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1byd63i/respect_jesus_christ_ethereal_snake/

########################################

id = get_rt_id(cur, 'Respect Tokei Grumer (Bakuage Sentai BoonBoomger)', 'https://redd.it/1byzr5x')
add_data(['Tokei Grumer'],
'Tokei Grumer',
False,
True,
[
    ['Bakuage Sentai BoonBoomger']
],
'Bakuage Sentai BoonBoomger',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1byzr5x/respect_tokei_grumer_bakuage_sentai_boonboomger/

########################################

id = get_rt_id(cur, 'Respect the Gyarados Submarine (Pokemon)', 'https://redd.it/1bz41nq')
add_data(['Gyarados Submarine'],
'Gyarados Submarine',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/respectthreads/comments/1bz41nq/respect_the_gyarados_submarine_pokemon/

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

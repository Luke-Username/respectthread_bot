# This Python module contains functions on how the bot is able to 
# analyze text and find matches in its database.
# It starts with the search_characters function looking for matches on character names.

# Modules
import re           # Regular expressions

# Custom modules
import text_processing as tp
from character import Character
from typing import List

respectthread_list = []

def search_characters(title: str, post: str, cur):
    character_list = []
    characters_checked = []
    respectthread_list.clear()
    cur.execute("SELECT * FROM character_name ORDER BY is_team DESC, length(name) DESC;")
    names = cur.fetchall()
    for n in names:
        found_char = False
        name = n[0]
        default_name = n[1]
        if default_name not in characters_checked and post_contains(name, post, cur):
            found_char = True
            char_added = False
            cur.execute("SELECT * FROM character WHERE default_name = '{}' ORDER BY is_default;".format(default_name.replace("'", "''")))
            characters = cur.fetchall()
            for c in characters:
                version = c[1]
                respectthread_ids = c[3]
                verse_name = c[4]
                if check_version_array(version, post, cur):                                                             # Check if the post contains the character's verse-name
                    add_character(name, default_name, verse_name, respectthread_ids, title, post, cur, character_list)
                    char_added = True

            if not char_added:                                                                                          # If the post doesn't mention the character's version,
                for c in characters:                                                                                    # use the default version
                    is_default = c[2]
                    if is_default:
                        add_character(name, default_name, c[4], c[3], title, post, cur, character_list)

        if found_char:                                                                                                  # Prevents redundant character checks
            characters_checked.append(default_name)
    return character_list

def check_version_array(version: List[str], post: str, cur):
    for string in version:
        if not post_contains(string, post, cur):
            return False
    return True

def post_contains(name: str, post: str, cur):
    name_with_bounds = tp.boundary(name)
    regex = re.compile(r"{}".format(name_with_bounds), re.IGNORECASE)
    if re.search(regex, post) is not None:
        name = name.replace("'", "''")
        cur.execute("SELECT COUNT(*) FROM name_conflict WHERE name = '{}';".format(name))
        row_count = cur.fetchone()[0]
        if row_count == 0:
            return True
        else:
            cur.execute("SELECT conflict, first_char FROM name_conflict WHERE name = '{}';".format(name))
            rows = cur.fetchall()
            name_locations = [m.start() for m in re.finditer(regex, post)]
            for n in name_locations:
                non_matches = 0
                for row in rows:
                    conflict = row[0].lower()
                    first_char = n + row[1]
                    last_char = first_char + len(conflict)
                    substring = post[first_char : last_char].lower()
                    if substring != conflict:
                        non_matches += 1
                if non_matches == row_count:
                    return True
    return False

def add_character(name: str, default_name: str, verse_name: str, respectthread_ids: List[int], title: str, post: str, cur, character_list: List[Character]):
    if post_contains(default_name, title, cur):                                                                         # The bot prefers names found in the title
        add_to_reply(default_name, default_name, verse_name, respectthread_ids, character_list, post, cur)              # and prefers the character's "default name"
    elif post_contains(name, title, cur):
        name = tp.extract_match(name, title)
        add_to_reply(name, default_name, verse_name, respectthread_ids, character_list, post, cur)
    elif post_contains(default_name, post, cur):
        add_to_reply(default_name, default_name, verse_name, respectthread_ids, character_list, post, cur)
    else:
        name = tp.extract_match(name, post)
        add_to_reply(name, default_name, verse_name, respectthread_ids, character_list, post, cur)

def add_to_reply(name: str, default_name: str, verse_name: str, respectthread_ids: List[int], character_list: List[Character], post: str, cur):
    included_rts = []
    for id in respectthread_ids:
        if is_rt_in_post(id, post, cur):
            respectthread_list.append(id)
        if id not in respectthread_list:
            respectthread_list.append(id)                                                                               # To prevent linking duplicates
            included_rts.append(id)

    if included_rts:
        character_list.append(Character(name, default_name, verse_name, included_rts))

def is_rt_in_post(id: int, post: str, cur) -> bool:                                                                                       # Check if the post already linked that RT
    cur.execute("SELECT link FROM respectthread WHERE id = {} LIMIT 1;".format(id))
    link = cur.fetchone()[0]
    regex = re.compile(r"https://redd\.it/([a-zA-A0-9]{6})")
    match_shortlink = regex.search(link)
    if match_shortlink is not None:
        post_id = match_shortlink.group(1)
        regex = re.compile(r"\b{}\b".format(post_id))
        if re.search(regex, post) is not None:
            return True
    else:
        regex = re.compile(r"comments/([a-zA-A0-9]{6})")
        match_permalink = regex.search(link)
        if match_permalink is not None:
            post_id = match_permalink.group(1)
            regex = re.compile(r"\b{}\b".format(post_id))
            if re.search(regex, post) is not None:
                return True
    return False

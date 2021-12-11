# This Python module contains functions the main bot uses to analyze post content.

# Modules
import re           # Regular expressions
import unicodedata  # To strip accents

##################################################
# Evaluating for word boundaries
##################################################

# This function checks of a word should have word boundaries \b around it.
# If boundaries are placed where they should not be, 
# the bot might not be able to detect the word it is searching for.
def boundary(word: str) -> str:
    # Exit if the given word is empty
    if word == "":
        print("Given word is empty. Boundary not checked.")
        return word
    
    start_char = re.compile(r"^\w", re.IGNORECASE)
    end_char = re.compile(r"\w$", re.IGNORECASE)

    # This part is to check if the word starts with "("
    i = 1
    in_brackets = "" 
    if word[0] == "(":
        while word[i] != ")" or word[i-1:i+i] == "\)":
            i += 1
        in_brackets = word[1:i]
    pattern_list = in_brackets.split("|")

    # This part is to check if the word ends with ")"
    i = -2
    in_brackets = "" 
    if len(word) >= 2 and word[-1] == ")":
        while word[i] != "(" or word[i-1:i+i] == "\(":
            i -= 1
        in_brackets = word[i+1:-1]
    pattern_list2 = in_brackets.split("|")

    special_chars = ["*", "+", "?"]
    if (word[0] == "(" and valid_patterns_start(pattern_list)) or (word[0] == "[") or (word[0] in special_chars) or (re.search(start_char, word) is not None):
        word = r"\b" + word
    if (word[-1] == ")" and word[-2:] != "\)" and valid_patterns_end(pattern_list2)) or (word[-1] == "]" and word[-2:] != "\]") or (word[-1] in special_chars) or (re.search(end_char, word) is not None):
        word = word + r"\b"

    return word

def valid_patterns_start(strlist) -> bool:
    invalid = ["\\(", "\\["]
    for pattern in invalid:
        if pattern in strlist:
            return False
    return True

def valid_patterns_end(strlist) -> bool:
    invalid = ["\\)", "\\]"]
    for pattern in invalid:
        if pattern in strlist:
            return False
    return True

##################################################
# Evaluating comments for the keyword to summon the bot
##################################################

def get_keyworded_lines_from_comment(comment_body: str, keyword: str) -> str:
    keyworded_comment = ""
    keyword_regex = re.compile(r"(-|\*|\+|\d)? ?{}".format(keyword), re.IGNORECASE)
    
    bodylist = comment_body.split("\n")
    for line in bodylist:
        matches = re.search(keyword_regex, line)
        if matches is not None:
            keyworded_comment += line
    
    return keyworded_comment

##################################################
# Miscellaneous text processing functions
##################################################

# A function to remove accents and diacritics from text.
# This helps simplifiy the search for the bot.
def strip_accents(text: str) -> str:
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3
        #print("NameError")
        pass

    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)

def extract_match(name: str, post: str) -> str:
    regex = re.compile(r"\b{}\b".format(name), re.IGNORECASE)
    matches = re.search(regex, post)
    if matches is not None:
        return matches.group(0)
    else:
        raise TypeError("No pattern matches have been found for the given regex and string.")

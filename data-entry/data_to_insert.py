"""
# This script is used to enter new characters into the database when a respect thread is written of them.
# New respect threads are found at this link: https://www.reddit.com/r/respectthreads/new/
# An example of how to enter a new character is as follows.

id = get_rt_id(cur, 'Respect Dr. Evil (Austin Powers)', 'https://www.reddit.com/r/respectthreads/comments/1my1b8x/respect_dr_evil_austin_powers/')
add_data(['Dr\.? Evil'],
'Dr. Evil',
False,
False,
[
    ['Austin Powers']
],
'Austin Powers',
'{' + '{}'.format(id) + '}'
)
#

# The following function call is an example of how to update the database when a respect thread is reposted.
# Refer to the CSV of respect threads to find the correct ID.
# Take the title and URL from the post itself.
update_respectthread(cur, 2103, 'Respect Paladin (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1rt36du/respect_paladin_marvel_616/')
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
            # Turn the name into a string acceptable for PostgreSQL (no idea if this is correct. can't be bothered to do proper testing.)
            formatted_name_list.append(name.replace('\\', '\\\\'))
            #formatted_name_list.append(name)

    formatted_version_list = []
    for version in version_list:
        version_array_string = '{'
        for regex in version:
            if not is_valid_regex(regex):
                return
            else:
                # Note: Replacing \\ with \\\\ is needed so Postgres can pick up that a \ is supposed to be there
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

update_respectthread(cur, 4773, 'Respect the Valkyria Mako Fujisaki! (Gokukoku no Brynhildr)', 'https://www.reddit.com/r/respectthreads/comments/1rp5y2i/respect_the_valkyria_mako_fujisaki_gokukoku_no/')
update_respectthread(cur, 17529, 'Respect The Hero of Time (The Legend of Zelda: Twilight Princess [Manga])', 'https://www.reddit.com/r/respectthreads/comments/1rpn9k7/respect_the_hero_of_time_the_legend_of_zelda/')
update_respectthread(cur, 2103, 'Respect Paladin (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1rt36du/respect_paladin_marvel_616/')
update_respectthread(cur, 1700, 'Respect Lobo II (DC Comics, Post Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rzk830/respect_lobo_ii_dc_comics_post_flashpoint/')
update_respectthread(cur, 1451, 'Respect The Tick! (Amazon)', 'https://www.reddit.com/r/respectthreads/comments/1s0op41/respect_the_tick_amazon/')

########################################

id = get_rt_id(cur, 'Respect Nando (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rozyz0/respect_nando_pokemon_anime/')
add_data(['Nando'],
'Nando',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Barry (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rsugvf/respect_barry_pokemon_anime/')
add_data(['Barry'],
'Barry',
False,
False,
[
    ['Barry ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Barry''s Empoleon (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rqt6x9/respect_barrys_empoleon_pokemon_anime/')
add_data(['Empoleon'],
'Empoleon',
False,
False,
[
    ['Barry']
],
'Barry',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect James'' Yamask (Pokemon Anime)", 'https://www.reddit.com/r/respectthreads/comments/1rpbjlw/respect_james_yamask_pokemon_anime/')
add_data(['Yamask'],
'Yamask',
False,
False,
[
    ['James']
],
'James',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Ningbo (Jojo''s Bizarre Adventure)", 'https://www.reddit.com/r/respectthreads/comments/1rp95on/respect_ningbo_jojos_bizarre_adventure/')
add_data(['Ningbo'],
'Ningbo',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Maha (One Piece)', 'https://www.reddit.com/r/respectthreads/comments/1rpfcmt/respect_maha_one_piece/')
add_data(['Maha'],
'Maha',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Belo Betty (One Piece)', 'https://www.reddit.com/r/respectthreads/comments/1rpi2wi/respect_belo_betty_one_piece/')
add_data(['Belo Betty'],
'Belo Betty',
False,
False,
[
    ['One ?Piece?']
],
'One Piece',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect King Bulblin (The Legend of Zelda: Twilight Princess [Manga])', 'https://www.reddit.com/r/respectthreads/comments/1rpmefu/respect_king_bulblin_the_legend_of_zelda_twilight/')
add_data(['King Bulblin'],
'King Bulblin',
False,
False,
[
    ['Zelda'], ['Twilight Princess']
],
'The Legend of Zelda',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zant (The Legend of Zelda: Twilight Princess [Manga])', 'https://www.reddit.com/r/respectthreads/comments/1rplzxi/respect_zant_the_legend_of_zelda_twilight/')
add_data(['Zant'],
'Zant',
False,
False,
[
    ['Zelda'], ['Twilight Princess']
],
'The Legend of Zelda',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Flambae (Dispatch)', 'https://www.reddit.com/r/respectthreads/comments/1rq18jg/respect_flambae_dispatch/')
add_data(['Flambae'],
'Flambae',
False,
False,
[
    ['Dispatch(ers?)?']
],
'Dispatch',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The White Wolf(Scary Stories To Tell in the Dark', 'https://www.reddit.com/r/respectthreads/comments/1rqi1u0/respect_the_white_wolfscary_stories_to_tell_in/')
add_data(['White Wolf'],
'White Wolf',
False,
False,
[
    ['Scary Stories To Tell in the Dark']
],
'Scary Stories To Tell in the Dark',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pamela Isley, Poison Ivy (DCAU)', 'https://www.reddit.com/r/respectthreads/comments/1rqulpk/respect_pamela_isley_poison_ivy_dcau/')
add_data(['Poison Ivy'],
'Poison Ivy',
False,
False,
[
    ['DC Animated Universe'], ['DCAU']
],
'DCAU',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Sean Cord (How to Write Fight Scenes like John Wick #johnwick #screenwriting #filmmaking)', 'https://www.reddit.com/r/respectthreads/comments/1rrdvt0/respect_sean_cord_how_to_write_fight_scenes_like/')
add_data(['Sean Cord'],
'Sean Cord',
False,
False,
[
    ['Write Fight Scenes like John Wick']
],
'How to Write Fight Scenes like John Wick',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Hot and Cold (We Were Reincarnated into a World Overrun by Monsters, but it’s No Big Deal!! Because God Gave Us a Mysterious Deck of Cards That Enable Incredible Transformations!! So We’re Going to Work Together to Save This World: The Manga)', 'https://www.reddit.com/r/respectthreads/comments/1rrqbh1/respect_hot_and_cold_we_were_reincarnated_into_a/')
add_data(['Hot and Cold '],
'Hot and Cold ',
True,
False,
[
    ['Reincarnated into a World Overrun by Monsters']
],
'We Were Reincarnated into a World Overrun by Monsters',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Superpower, Eliza Hellbound! (The Power Fantasy)', 'https://www.reddit.com/r/respectthreads/comments/1rs0naf/respect_the_superpower_eliza_hellbound_the_power/')
add_data(['Eliza Hellbound'],
'Eliza Hellbound',
False,
False,
[
    ['The Power Fantasy']
],
'The Power Fantasy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect: Eimin & Uriel, the Apocalypse Twins (Marvel, 616)', 'https://www.reddit.com/r/respectthreads/comments/1s1i7zp/respect_eimin_uriel_the_apocalypse_twins_marvel/')
add_data(['Apocalypse Twins'],
'Apocalypse Twins',
True,
False,
[
    ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Multi-Eternity! Personification of Omniverse, Eighth Sentience of the Cosmos (Marvel, 616)', 'https://www.reddit.com/r/respectthreads/comments/1rsyb46/respect_multieternity_personification_of/')
add_data(['Multi(-| )Eternity'],
'Multi-Eternity',
False,
False,
[
    ['616'], ['Marvel']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Eternity'],
'Eternity',
False,
False,
[
    ['Eternity.*\(Marvel\)', 'Infinity'], ['Eternity ?\(Marvel( Comics)?\)']
],
'616',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/ob1end/justice_league_dark_dc_comics_vs_eternity_marvel/

########################################

id = get_rt_id(cur, "Respect the Fantastic Four (Marvel Comics, 1996''s Heroes Reborn)", 'https://www.reddit.com/r/respectthreads/comments/1s5ya21/respect_the_fantastic_four_marvel_comics_1996s/')
add_data(['Fantastic Four'],
'Fantastic Four',
True,
False,
[
    ['Fantastic Four.*Heroes Reborn']
],
'Heroes Reborn',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect René Rodin, the Mad Thinker (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1s9ecsc/respect_ren%C3%A9_rodin_the_mad_thinker_marvel_comics/')
add_data(['Mad Thinker'],
'Mad Thinker',
False,
False,
[
    ['Marvel'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect René Rodin, the Mad Thinker (Marvel Comics, 616)', 'https://www.reddit.com/r/respectthreads/comments/1s9ecsc/respect_ren%C3%A9_rodin_the_mad_thinker_marvel_comics/')
add_data(['Mad Thinker'],
'Mad Thinker',
False,
False,
[
    ['Marvel'], ['616']
],
'616',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Jeff Hagees, 8-Ball! (Marvel 616)', 'https://www.reddit.com/r/respectthreads/comments/1sa7vwo/respect_jeff_hagees_8ball_marvel_616/')
add_data(['8(-| )Ball'],
'8-Ball',
False,
False,
[
    ['8(-| )Ball ?\(616'], ['Jeff Hagees']
],
'616',
'{' + '{}'.format(id) + '}'
)
#



########################################

id = get_rt_id(cur, 'Respect Happy Hogan (Marvel Cinematic Universe)', 'https://www.reddit.com/r/respectthreads/comments/1s9h2un/respect_happy_hogan_marvel_cinematic_universe/')
add_data(['Happy Hogan'],
'Happy Hogan',
False,
False,
[
    ['Marvel Cinematic Universe'], ['MCU']
],
'MCU',
'{' + '{}'.format(id) + '}'
)
#




########################################

id = get_rt_id(cur, 'Respect Thromnambular! (The Grim Adventures of Billy & Mandy)', 'https://www.reddit.com/r/respectthreads/comments/1rtn9m6/respect_thromnambular_the_grim_adventures_of/')
add_data(['Thromnambular'],
'Thromnambular',
False,
False,
[
    ['Billy (&|and) Mandy']
],
'Billy & Mandy',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zallah Macri and Kevmo Zink (Star Wars Canon)', 'https://www.reddit.com/r/respectthreads/comments/1rtqcze/respect_zallah_macri_and_kevmo_zink_star_wars/')
add_data(['Zallah Macri'],
'Zallah Macri',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Kevmo Zink'],
'Kevmo Zink',
False,
False,
[
    ['S(tar )?Wars']
],
'Star Wars',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Inquisitor (Star Wars: Visions - T0-B1)', 'https://www.reddit.com/r/respectthreads/comments/1s92m5k/respect_the_inquisitor_star_wars_visions_t0b1/')
add_data(['Inquisitor'],
'Inquisitor',
False,
False,
[
    ['S(tar )?Wars:? Visions']
],
'Star Wars: Visions',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Bazuso! (Berserk)', 'https://www.reddit.com/r/respectthreads/comments/1rtu4a1/respect_bazuso_berserk/')
add_data(['Bazuso'],
'Bazuso',
False,
False,
[
    ['Berserk']
],
'Berserk',
'{' + '{}'.format(id) + '}'
)
#


########################################

id = get_rt_id(cur, 'Respect Godzilla (Godzilla and Godzilla Raids Again)', 'https://www.reddit.com/r/respectthreads/comments/1s3aim3/respect_godzilla_godzilla_and_godzilla_raids_again/')
add_data(['Godzilla'],
'Godzilla',
False,
False,
[
    ['Godzilla and Godzilla Raids Again']
],
'Godzilla and Godzilla Raids Again',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Uro! (Jujutsu Kaisen)', 'https://www.reddit.com/r/respectthreads/comments/1s52zdc/respect_uro_jujutsu_kaisen/')
add_data(['Uro'],
'Uro',
False,
False,
[
    ['Jujus?t?s?u Kaisen']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Reggie Star! (Jujutsu Kaisen)', 'https://www.reddit.com/r/respectthreads/comments/1s0qeln/respect_reggie_star_jujutsu_kaisen/')
add_data(['Reggie'],
'Reggie',
False,
False,
[
    ['Jujus?t?s?u Kaisen']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kurourushi (Jujutsu Kaisen)', 'https://www.reddit.com/r/respectthreads/comments/1s52zeo/respect_kurourushi_jujutsu_kaisen/')
add_data(['Kurourushi'],
'Kurourushi',
False,
False,
[
    ['Jujus?t?s?u Kaisen']
],
'Jujutsu Kaisen',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Kuroe Akaishi (Kaiju Girl Caramelise)', 'https://www.reddit.com/r/respectthreads/comments/1s7ed0x/respect_kuroe_akaishi_kaiju_girl_caramelise/')
add_data(['Kuroe Akaishi'],
'Kuroe Akaishi',
False,
False,
[
    ['Kaiju Girl Caramelise']
],
'Kaiju Girl Caramelise',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect General Li Shang! (Mulan 1998)', 'https://www.reddit.com/r/respectthreads/comments/1s7usfm/respect_general_li_shang_mulan_1998/')
add_data(['Li Shang'],
'Li Shang',
False,
False,
[
    ['Mulan', 'Man'], ['Disney'], ['Princes?'], ['1998']
],
"Disney''s Mulan",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect the Snow Queen (Hans Christian Andersen''s The Snow Queen)", 'https://www.reddit.com/r/respectthreads/comments/1s9486i/respect_the_snow_queen_hans_christian_andersens/')
add_data(['Snow Queen'],
'Snow Queen',
False,
False,
[
    ['Hans Christian Andersens?']
],
"Hans Christian Andersen",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Dinosaurus (Invincible)', 'https://www.reddit.com/r/respectthreads/comments/1s9dtcz/respect_dinosaurus_invincible/')
add_data(['Dinosaurus'],
'Dinosaurus',
False,
False,
[
    ['Invincible']
],
'Invincible',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Boulder (Thomas & Friends)', 'https://www.reddit.com/r/respectthreads/comments/1s9e955/respect_boulder_thomas_friends/')
add_data(['Boulder'],
'Boulder',
False,
False,
[
    ['Thomas & Friends'], ['Thomas the Tank Engine']
],
'Thomas & Friends',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect EC Zombies (EC Comics)', 'https://www.reddit.com/r/respectthreads/comments/1ru4r30/respect_ec_zombies_ec_comics/')
add_data(['EC Zombies'],
'EC Zombies',
False,
False,
[
    ['EC Comics']
],
'EC Comics',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Conway (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rueidz/respect_conway_pokemon_anime/')
add_data(['Conway'],
'Conway',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Pokemon Ranger Ben (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rv8siv/respect_pokemon_ranger_ben_pokemon_anime/')
add_data(['Ranger Ben'],
'Ranger Ben',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Meloetta (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rwb6w1/respect_meloetta_pokemon_anime/')
add_data(['Meloetta'],
'Meloetta',
False,
False,
[
    ['Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Cameron (Pokemon Anime)', 'https://www.reddit.com/r/respectthreads/comments/1rwp405/respect_cameron_pokemon_anime/')
add_data(['Cameron'],
'Cameron',
False,
False,
[
    ['Cameron ?\(Pok(e|é)m(o|a)n']
],
'Pokémon',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Little Pale Girl (Terrifier)', 'https://www.reddit.com/r/respectthreads/comments/1rvu18a/respect_the_little_pale_girl_terrifier/')
add_data(['Pale Girl'],
'Pale Girl',
False,
False,
[
    ['Terrifier']
],
'Terrifier',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Film Freak II (DC Comics: New Earth)', 'https://www.reddit.com/r/respectthreads/comments/1rw8niz/respect_film_freak_ii_dc_comics_new_earth/')
add_data(['Film Freak II'],
'Film Freak II',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth'], ['PC']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Film Freak II'],
'Film Freak II',
False,
False,
[
    ['DC Comics']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Titano (DC Comics: Post Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1rzyy2e/respect_titano_dc_comics_post_crisis/')
add_data(['Titano'],
'Titano',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Titano'],
'Titano',
False,
False,
[
    ['Superman Villains?']
],
'DC',
'{' + '{}'.format(id) + '}'
)
#https://www.reddit.com/r/whowouldwin/comments/9ac5c5/superman_villains_vs_reallife_new_york/

########################################

id = get_rt_id(cur, 'Respect Electrocutioner I (DC Comics: Post-Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1rytvo3/respect_electrocutioner_i_dc_comics_postcrisis/')
add_data(['Electrocutioner I'],
'Electrocutioner I',
False,
False,
[
    ['Posts?(-| )?C(risis)?'], ['New(-| )Earth'], ['PC']
],
'Post-Crisis',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect The Matriarch (DC Comics, Post-Flashpoint)', 'https://www.reddit.com/r/respectthreads/comments/1rxmrgp/respect_the_matriarch_dc_comics_postflashpoint/')
add_data(['Matriarch'],
'Matriarch',
False,
False,
[
    ['(Post(-| ))Flash(-| )?point']
],
'Post-Flashpoint',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Zebra-Man (DC Comics: Pre-Crisis)', 'https://www.reddit.com/r/respectthreads/comments/1ry5yai/respect_zebraman_dc_comics_precrisis/')
add_data(['Zebra(-| )Man'],
'Zebra-Man',
False,
False,
[
    ['Pre(-| )?Crisis']
],
'Pre-Crisis',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect The Monkey''s Paw! (The Simpsons)", 'https://www.reddit.com/r/respectthreads/comments/1rwam5x/respect_the_monkeys_paw_the_simpsons/')
add_data(["Monkey''?s Paw"],
"Monkey''s Paw",
False,
False,
[
    ['Simpsons']
],
'The Simpsons',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Key West (Jojo''s Bizarre Adventure)", 'https://www.reddit.com/r/respectthreads/comments/1rxjdse/respect_key_west_jojos_bizarre_adventure/')
add_data(['Key West'],
'Key West',
False,
False,
[
    ['Jojos?(verse)?'], ['JJBA']
],
"Jojo''s Bizarre Adventure",
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Magatsu Kotono-Nushi, The Sovereign of Corpses! (Isekai Ojisan)', 'https://www.reddit.com/r/respectthreads/comments/1ryhhg7/respect_magatsu_kotononushi_the_sovereign_of/')
add_data(['Magatsu Kotono(-| )Nushi'],
'Magatsu Kotono-Nushi',
False,
False,
[
    ['Isekai Ojisan']
],
'Isekai Ojisan',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, "Respect Ocean''s Eleven (Ocean''s Franchise)", 'https://www.reddit.com/r/respectthreads/comments/1rywcm2/respect_oceans_eleven_oceans_franchise/')
add_data(["Ocean''s Eleven"],
"Ocean''s Eleven",
True,
True,
[
    ["Ocean''s Franchise"]
],
'',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect the Doctor (Dead by Daylight)', 'https://www.reddit.com/r/respectthreads/comments/1rz0m37/respect_the_doctor_dead_by_daylight/')
add_data(['The Doctor'],
'The Doctor',
False,
False,
[
    ['Doctor.*(Dead by Daylight|DBD)']
],
'Dead by Daylight',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Garruk Wildspeaker! (Magic: The Gathering)', 'https://www.reddit.com/r/respectthreads/comments/1s0uavl/respect_garruk_wildspeaker_magic_the_gathering/')
add_data(['Garruk Wildspeaker'],
'Garruk Wildspeaker',
False,
True,
[
    ['Magic:? The Gathering'], ['M:?TG'], ['Planeswalk(er)?s?'], ['Neo Walker']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#

add_data(['Garruk'],
'Garruk',
False,
False,
[
    ['Magic:? The Gathering'], ['M:?TG'], ['Planeswalk(er)?s?'], ['Neo Walker'], ['Apex Predator']
],
'Magic: The Gathering',
'{' + '{}'.format(id) + '}'
)
#

########################################

id = get_rt_id(cur, 'Respect Ornate (Image Comics, Massive-Verse)', 'https://www.reddit.com/r/respectthreads/comments/1rzwl4a/respect_ornate_image_comics_massiveverse/')
add_data(['Ornate'],
'Ornate',
False,
False,
[
    ['Massive(-| )Verse']
],
'Massive-Verse',
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

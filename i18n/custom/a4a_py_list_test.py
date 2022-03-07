# -*- coding: utf-8 -*-

# Script used to convert current lists of words to the gettext po format to enable translation

# run with python3 - to keep the utf-8 formatting

import os
import a4a_words

import a4a_py.ca, a4a_py.de, a4a_py.el, a4a_py.en_GB, a4a_py.en_US, a4a_py.es, a4a_py.fr, a4a_py.it, a4a_py.lkt, a4a_py.pl, a4a_py.pt, a4a_py.ru, a4a_py.uk, a4a_py.bg

#lang_list = ['ca', 'de', 'el', 'en_GB', 'en_US', 'es', 'fi', 'fr', 'it', 'lkt', 'pl', 'pt', 'ru', 'sr', 'uk']
#mod_list = [ca, de, el, en_gb, en_us, es, fi, fr, it, lkt, pl, pt, ru, sr, uk]

#lang_list = ['ca', 'de', 'el', 'en_GB', 'en_US', 'es', 'fr', 'it', 'lkt', 'pl', 'pt', 'ru', 'uk', 'bg']
#mod_list = [a4a_py.ca, a4a_py.de, a4a_py.el, a4a_py.en_GB, a4a_py.en_US, a4a_py.es, a4a_py.fr, a4a_py.it, a4a_py.lkt, a4a_py.pl, a4a_py.pt, a4a_py.ru, a4a_py.uk, a4a_py.bg]

lang_list = ['bg']
mod_list = [a4a_py.bg]

lists_str = ["a4a_animals", "a4a_sport", "a4a_body", "a4a_people", "a4a_food", "a4a_clothes_n_accessories", "a4a_actions", "a4a_construction", "a4a_nature", "a4a_jobs", "a4a_fruit_n_veg", "a4a_transport"]



lists_len = len(lists_str)
langs_len = len(lang_list)


# find strings and add to po file
for lang in range(0, langs_len):
    lns = []
    lnso = []
    for i in range(0, lists_len):
        len_orig = len(a4a_words.d[lists_str[i]])
        len_lang = len(mod_list[lang].d[lists_str[i]])
        lns.append("%s: %i" % (lists_str[i], len_lang))
        lnso.append("%s: %i" % (lists_str[i], len_orig))
    print(lang_list[lang])
    print(lnso)
    print(lns)
"""
bg
['a4a_animals: 128', 'a4a_sport: 29', 'a4a_body: 38', 'a4a_people: 29', 'a4a_food: 56', 'a4a_clothes_n_accessories: 45', 'a4a_actions: 80', 'a4a_construction: 37', 'a4a_nature: 19', 'a4a_jobs: 55', 'a4a_fruit_n_veg: 48', 'a4a_transport: 21']
['a4a_animals: 128', 'a4a_sport: 29', 'a4a_body: 38', 'a4a_people: 29', 'a4a_food: 56', 'a4a_clothes_n_accessories: 40', 'a4a_actions: 64', 'a4a_construction: 37', 'a4a_nature: 19', 'a4a_jobs: 51', 'a4a_fruit_n_veg: 48', 'a4a_transport: 21']


d["a4a_clothes_n_accessories"] = ['бижута',   'чорап', 'яке',    'токче', 'петна', 'шорти',  'джоб',   'колие',    'суитчър',    'униформа', 'дъждобран', 'панталони', 'слънчеви очила', 'палто', 'пуловер',  'риза',  'джапанки', 'костюм', 'боди',    'пола',  'цип', 'обувки', 'рубин', 'вратовръзки', 'чехли',    'ръкавици', 'шапка', 'ръкав',  'каскет', 'бански костюм', 'обувка',  'елек', 'очила',   'връзка за обувки', 'кръпка', 'шал',  'ботуш', 'копче',  'рокля', 'кимоно']
d["a4a_clothes_n_accessories"] = ['jewellery', 'sock', 'jacket', 'heel',  'smock', 'shorts', 'pocket', 'necklace', 'sweatshirt', 'uniform',  'raincoat',  'trousers',  'sunglasses',     'coat',  'pullover', 'shirt', 'sandals',  'suit',   'pyjamas', 'skirt', 'zip', 'shoes',  'jewel', 'tie',         'slippers', 'gloves',   'hat',   'sleeve', 'cap',    'swimming suit', 'trainer', 'vest', 'glasses', 'shoelace',         'patch',  'scarf', 'shoe', 'button', 'dress', 'sash', 'shoe sole', 'robe', 'pants', 'kimono', 'overalls']

d["a4a_actions"] = ['лиже', 'вкарва кош', 'проси', 'пада', 'драска',  'докосва', 'мирише', 'вижда', 'изкачва', 'копае', 'вие',  'спи',   'изследват', 'нарисува', 'прегръща', 'учи',   'дреме', 'прави', 'лови',  'ръкува се', 'плаче', 'пее',   'среща', 'продава', 'кълве', 'бие',  'коленичи', 'намира', 'танзуват', 'говори', 'реже', 'чете',  'лае',  'говори', 'играе', 'готви', 'пише',  'удря',  'свири', 'учи',   'оре',  'сънува', 'пуска писмо', 'потапя се', 'слуша',   'мисли', 'дрънкат', 'храни', 'лази',  'пече', 'разлива се', 'къпе се', 'пищи',   'къса', 'плува', 'дърпа', 'яде', 'целува', 'почива', 'излюпва се', 'намига', 'слуша', 'целува', 'играе']
d["a4a_actions"] = ['lick', 'slam',       'beg',   'fell', 'scratch', 'touch',    'sniff', 'see',   'climb',   'dig',   'howl', 'sleep', 'explore',   'draw',     'hug',      'teach', 'nap',   'clay',  'catch', 'clap',      'cry',    'sing', 'meet',  'sell',    'peck',  'beat', 'kneel',    'find',   'dance',    'cough',  'cut',  'think', 'bark', 'speak',  'cheer', 'bake',  'write', 'punch', 'strum', 'study', 'plow', 'dream',  'post',        'dive',      'whisper', 'sob',    'shake',  'feed',  'crawl', 'camp', 'spill',      'clean',   'scream', 'tear', 'float', 'pull',  'ate', 'kiss',    'sit',   'hatch',      'blink',  'hear',  'smooch', 'play', 'wash', 'chat', 'drive', 'drink', 'fly', 'juggle', 'bit', 'sweep', 'look', 'knit', 'lift', 'fetch', 'read', 'croak', 'stare', 'eat']

d["a4a_jobs"] = ['клоун', 'инженер', 'свещеник', 'ветеринар', 'съдия', 'готвач', 'спортист', 'библиотекар', 'жонгльор', 'полицай', 'водопроводчик', 'орден', 'кралица', 'фермер', 'фокусник', 'рицар', 'лекар', 'строителка', 'чистачка', 'учител', 'ловец', 'войник', 'музикант', 'адвокат', 'рибар', 'принцеса', 'пожарникар', 'монахиня', 'пират', 'каубой', 'електротехник', 'медицинска сестра', 'цар', 'политик', 'чиновник', 'дърводелец', 'жокей', 'работник', 'механик', 'пилот', 'актьор', 'готвач', 'студент', 'месар', 'счетоводител', 'принц', 'папа', 'моряк', 'боксьор', 'балерина', 'треньор']
d["a4a_jobs"] = ['clown', 'engineer', 'priest', 'vet', 'judge', 'chef', 'athlete', 'librarian', 'juggler', 'policeman', 'plumber', 'badge', 'queen', 'farmer', 'magician', 'knight', 'doctor', 'bricklayer', 'cleaner', 'teacher', 'hunter', 'soldier', 'musician', 'lawyer', 'fisherman', 'princess', 'fireman', 'nun', 'pirate', 'cowboy', 'electrician', 'nurse', 'king', 'president', 'office worker', 'carpenter', 'jockey', 'worker', 'mechanic', 'pilot', 'actor', 'cook', 'student', 'butcher', 'accountant', 'prince', 'pope', 'sailor', 'boxer', 'ballet dancer', 'coach', 'astronaut', 'painter', 'anaesthesiologist', 'scientist']
"""

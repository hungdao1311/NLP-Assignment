import re 
import os
import sys
import ast
import unicodedata as ud

#relation types
NMOD = 'nmod'
AMOD = 'amod'
NSUBJ = 'nsubj'
DOBJ = 'dobj'
CASE = 'case'

#pos_tags
NOUN = 'noun'
PROPER_NOUN = 'pnoun'
VERB = 'verb'
ID_NOUN = 'idnoun'
TIME = 'time'
PREP = 'prep'
WH_WHICH = 'wh-which'
WH_TIME = 'wh-time'

#relation pattern
PRED = 'PRED'
LSUBJ = 'LSUBJ'
LOBJ = 'LOBJ'

def syllabize(text):
    text = ud.normalize('NFC', text)
    time = "\d+:\d+[Hh][Rr]"
    word = "\w+"
    non_word = "[^\w\s]"
    patterns = []
    patterns.extend([time,non_word, word])
    patterns = "(" + "|".join(patterns) + ")"
    tokens = re.findall(patterns, text, re.UNICODE)    
    return tokens
    
def load_dicts(file_path):
    with open(file_path, encoding="utf8") as fr:
        words = fr.read()
        words = ast.literal_eval(words)
    return words

from tokenizer import *
from utils import * 
from transition import *
class DependencyParser:
    relations_dict = {
        ('xe bus', 'nào'): AMOD,
        ('xe bus', ID_NOUN): AMOD,
        ('đến', 'xe bus'): NSUBJ,
        ('đến', 'thành phố'): DOBJ,
        ('đến', PROPER_NOUN): DOBJ,
        ('thành phố', PROPER_NOUN): NMOD,
        ('đến', 'thời gian'): NMOD,
        ('đến', TIME): NMOD,
        ('xe bus', PROPER_NOUN): NMOD,
        (TIME, 'lúc'): CASE,
        (PROPER_NOUN, 'từ'): CASE
    }
    def __init__(self, tokens, pos_tag):
        self.stack = [('root','root')]
        self.buffer = list(zip(tokens, pos_tag))
        self.arcs = [] 
    
    def __str__(self):
        str_lst = list(map(lambda x: str(x), self.arcs))
        return ','.join(str_lst)

    def parse(self):
        while self.buffer:
            wi = self.stack[-1]
            wj = self.buffer[0]
            search_wi = self.get_search_key(wi)
            search_wj = self.get_search_key(wj)
            child_list = list(map(lambda x: x.child, self.arcs))
            if (search_wj, search_wi) in self.relations_dict and not wi in child_list:
                Transition.left_arc(self, self.relations_dict[search_wj, search_wi], wi, wj)
            elif (search_wi, search_wj) in self.relations_dict:
                Transition.right_arc(self, self.relations_dict[search_wi, search_wj], wi, wj)
            elif wi in child_list:
                Transition.reduce(self)
            else: 
                Transition.shift(self)

    def get_search_key(self, w):
        if w[1] in [ID_NOUN, PROPER_NOUN, TIME]:
            return w[1]
        else: 
            return w[0]


if __name__ == '__main__':
    question = input()
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(question)
    pos_tag = tokenizer.pos_tag(tokens)
    parser = DependencyParser(tokens, pos_tag)
    parser.parse()
    print(parser)

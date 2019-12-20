from dependency_parser import *
from utils import *
class GrammaticalRelation:
    def __init__(self, arcs):
        self.arcs = arcs
        self.var_list = []
        self.variable_dict = load_dicts("variable_dict.txt")
    def get_root(self):
        for arc in self.arcs:
            if arc.type == NSUBJ:
                return arc
    def get_var_name(self, text):
        count = 1
        tmp = text[0].lower() + str(count)
        while tmp in self.var_list:
            count = count + 1
            tmp = text[0] + str(count)
        self.var_list.append(tmp)
        return tmp

    def convert(self, arc):
        if arc.type == NSUBJ:
            return '(s1 PRED ' + self.variable_dict[arc.source.token] + ')(s1 TNS PRES)\n' + '(s1 LSUBJ ' + self.variable_dict[arc.dest.token.lower()] + ')'
        if arc.type == AMOD:
            name_value = arc.dest.token if arc.dest.tag == ID_NOUN else 'WH_WHICH'
            return '(s1 LSUBJ ' + self.variable_dict[arc.source.token] + ')(NAME ' + self.get_var_name(name_value) + ' ' + name_value + ')'
        if arc.type == NMOD:
            if arc.dest.tag == PROPER_NOUN:
                return '(s1 FROM-LOC (NAME ' + self.get_var_name(arc.dest.token) + ' ' + self.variable_dict[arc.dest.token.lower()] + '))'
            else:
                if arc.dest.tag == TIME: 
                    return '(s1 DEST-TIME ' + arc.dest.token + ')'
                else:
                    return '(s1 DEST-TIME ' + arc.dest.tag + ')'
        if arc.type == DOBJ:
            return '(s1 LOBJ (NAME ' + self.get_var_name(arc.dest.token) + ' ' + self.variable_dict[arc.dest.token.lower()] + '))'

    def print_relations(self):
        type_list = [NSUBJ, AMOD, DOBJ, NMOD]
        sorted_arc = sorted(self.arcs, key = lambda x: type_list.index(x.type))
        result = list(map(lambda x: self.convert(x), sorted_arc))
        print('\n'.join(result))

def test():
    question = input()
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(question)
    pos_tag = tokenizer.pos_tag(tokens)
    parser = DependencyParser(tokens, pos_tag)
    parser.parse()
    grammar = GrammaticalRelation(parser.get_shorthand_arcs())
    grammar.print_relations()
test()
from .dependency_parser import *
from .utils import *

class GrammaticalRelation:
    def __init__(self, arcs):
        self.arcs = arcs
        self.var_list = []
        self.variable_dict = load_dicts("variable_dict.txt")
        self.patterns = []
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
            name_value = arc.dest.token if arc.dest.tag == ID_NOUN else self.variable_dict[arc.dest.tag]
            self.patterns.append(Pattern(NAME, self.get_var_name(name_value), name_value))
            return '(s1 LSUBJ ' + self.variable_dict[arc.source.token] + ')(NAME ' + self.get_var_name(name_value) + ' ' + name_value + ')'
        if arc.type == NMOD:
            if arc.dest.tag == PROPER_NOUN:
                self.patterns.append(Pattern(FROM_LOC, 's1', self.variable_dict[arc.dest.token.lower()]))
                return '(s1 FROM-LOC (NAME ' + self.get_var_name(arc.dest.token) + ' ' + self.variable_dict[arc.dest.token.lower()] + '))'
            else:
                if arc.dest.tag == TIME: 
                    animate = arc.dest.token
                    self.patterns.append(Pattern(ARRIVE_TIME, 's1', animate))
                    return '(s1 ARRIVE-TIME ' + animate + ')'
                else:
                    animate = arc.dest.tag
                    self.patterns.append(Pattern(RUN_TIME, 's1', self.variable_dict[animate]))
                    return '(s1 RUNTIME ' + self.variable_dict[animate] + ')'
                
                
        if arc.type == DOBJ:
            self.patterns.append(Pattern(LOBJ, 's1', self.variable_dict[arc.dest.token.lower()]))
            return '(s1 LOBJ (NAME ' + self.get_var_name(arc.dest.token) + ' ' + self.variable_dict[arc.dest.token.lower()] + '))'

    def print_relations(self):
        relation_type = [NSUBJ, AMOD, DOBJ, NMOD]
        pattern_type = [LSUBJ, NAME, LOBJ, FROM_LOC, ARRIVE_TIME, RUN_TIME]
        self.patterns = sorted(self.patterns, key = lambda x: pattern_type.index(x.type))
        self.arcs = sorted(self.arcs, key = lambda x: relation_type.index(x.type))
        result = list(map(lambda x: self.convert(x), self.arcs))
        return '\n'.join(result)

    def print_pattern(self):
        for pattern in self.patterns:
            print(pattern)

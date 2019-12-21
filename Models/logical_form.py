from utils import *
from dependency_parser import *
from grammatical_relation import *
class LogicalForm:
    def __init__(self, patterns):
        self.childs = []
        self.var_list = []
        for pattern in patterns:
            if pattern.animate == "WH_TIME" or pattern.animate == "WH_WHICH":
                self.root = pattern
            self.childs.append(pattern)

    def get_var_name(self, text):
        count = 1
        tmp = text[0].lower() + str(count)
        while tmp in self.var_list:
            count = count + 1
            tmp = text[0] + str(count)
        self.var_list.append(tmp)
        return tmp

    def print_logical_form(self):
        result = ""
        global_var = "b1"
        if self.root.animate == "WH_TIME": 
            result = "THE t1: ("
        else:
            result = "WH b1: ("
        if len(self.childs) > 1:
            result += "& "
        for child in self.childs:
            if child.type == NAME:
                if child.animate == "WH_WHICH":
                    result += "(XEBUS " + global_var + " (NAME ?" + global_var + " " + child.animate + "))"
                else:
                    result += "(XEBUS " + global_var + " (NAME " + global_var + " " + child.animate + "))"
            if child.type == LOBJ:
                result += "(DEST " + global_var + " (NAME " + self.get_var_name(child.animate) + " " + child.animate + "))"
            if child.type == FROM_LOC:
                result += "(FROM-LOC " + global_var + " (NAME " + self.get_var_name(child.animate) + " " + child.animate + "))"
            if child.type == RUN_TIME:
                result += "(RUNTIME " + global_var + " ?t1)"
            if child.type == ARRIVE_TIME:
                result += "(ARRIVE_TIME " + global_var + " " + child.animate + ")"
            
        result += ")"
        print(result)

def get_logical(question):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(question)
    pos_tag = tokenizer.pos_tag(tokens)
    parser = DependencyParser(tokens, pos_tag)
    parser.parse()
    grammar = GrammaticalRelation(parser.get_shorthand_arcs())
    grammar.print_relations()
    logical = LogicalForm(grammar.patterns)
    logical.print_logical_form()
def test():
    questions = ["Xe bus nào đến thành phố Huế lúc 20:00HR", "Thời gian xe bus B3 từ Đà Nẵng đến Huế", "Xe bus nào đến thành phố Hồ Chí Minh"]
    for question in questions:
        get_logical(question)
test()
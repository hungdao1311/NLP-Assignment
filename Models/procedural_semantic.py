from .utils import *
from .logical_form import *
class ProceduralSemantic:
    def __init__(self, predicates):
        self.conditions = {
            ATIME: None,
            DTIME: None,
            RUN_TIME: None,
        }
        self.curr_condition = None
        for predicate in predicates:
            if predicate.operand == "WH_WHICH":
                self.quantifier = PRINT_ALL
            elif predicate.operand == "WH_TIME":
                self.quantifier = FIND_THE
        if self.quantifier == FIND_THE:
            self.conditions[RUN_TIME] = RunTime()
            for predicate in predicates:
                if predicate.pred == DEST:
                    self.conditions[RUN_TIME].dest = predicate.operand
                if predicate.pred == NAME:
                    self.conditions[RUN_TIME].bus = predicate.operand
                if predicate.pred == FROM_LOC:
                    self.conditions[RUN_TIME].dep = predicate.operand
        else:
            self.conditions[ATIME] = ATime()
            for predicate in predicates:
                if predicate.pred == DEST:
                    self.conditions[ATIME].dest = predicate.operand
                if predicate.pred == ARRIVE_TIME:
                    self.conditions[ATIME].time = predicate.operand
    def print_semantic(self):
        result = ""
        if self.quantifier == PRINT_ALL:
            result += "PRINT-ALL ?b "
        else:
            result += "FIND-THE ?t "
        if self.conditions[ATIME]:
            result += "(BUS ?b)" + str(self.conditions[ATIME])
            self.curr_condition = self.conditions[ATIME]
        if self.conditions[DTIME]:
            result += ("BUS ?b") + str(self.conditions[DTIME])
            self.curr_condition = self.conditions[DTIME]
        if self.conditions[RUN_TIME]:
            result += str(self.conditions[RUN_TIME])
            self.curr_condition = self.conditions[RUN_TIME]
        return result

def get_procedural(question):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(question)
    pos_tag = tokenizer.pos_tag(tokens)
    parser = DependencyParser(tokens, pos_tag)
    parser.parse()
    grammar = GrammaticalRelation(parser.get_shorthand_arcs())
    grammar.print_relations()
    logical = LogicalForm(grammar.patterns)
    logical.get_logical_form()
    procedural = ProceduralSemantic(logical.predicates)
    procedural.print_semantic()
def test():
    questions = ["Xe bus nào đến thành phố Huế lúc 20:00HR", "Thời gian xe bus B3 từ Đà Nẵng đến Huế", "Xe bus nào đến thành phố Hồ Chí Minh"]
    for question in questions:
        get_procedural(question)
if __name__ == '__main__':
    test()

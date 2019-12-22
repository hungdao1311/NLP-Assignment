import Models
from Models import *
def write_output(file_path, data):
    f = open(file_path, 'w+')
    for row in data:
        f.write(str(row) + '\n')
        f.write("-----------------------------\n")
    f.close()
    return True

questions = []
with open(r"Input/questions.txt") as input_text:
    for question in input_text:
        questions += [question.strip('\n')]
output_a = []
output_b = []
output_c = []
output_d = []
for question in questions:
    mtokenizer = tokenizer.Tokenizer()
    tokens = mtokenizer.tokenize(question)
    pos_tag = mtokenizer.pos_tag(tokens)
    parser = dependency_parser.DependencyParser(tokens, pos_tag)
    parser.parse()
    grammar = grammatical_relation.GrammaticalRelation(parser.get_shorthand_arcs())
    output_a.append(grammar.print_relations())

    logical = logical_form.LogicalForm(grammar.patterns)
    output_b.append(logical.get_logical_form())

    procedural = procedural_semantic.ProceduralSemantic(logical.predicates)
    output_c.append(procedural.print_semantic())
    mdatabase = database.Database()
    output_d.append(mdatabase.query(procedural.curr_condition))

write_output("Output/output_a.txt", output_a)
write_output("Output/output_b.txt", output_b)
write_output("Output/output_c.txt", output_c)
write_output("Output/output_d.txt", output_d)
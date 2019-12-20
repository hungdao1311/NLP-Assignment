from utils import *
class Tokenizer:
    #set of tags
    def __init__(self, bi_grams_path='bi_grams.txt', tri_grams_path='tri_grams.txt', tags_dict_path='tags_dict.txt'):
        self.bi_grams = load_dicts(bi_grams_path)
        self.tri_grams = load_dicts(tri_grams_path)
        self.tags_dict = load_dicts(tags_dict_path)

    def tokenize(self, text):
        syllabes = syllabize(text)
        syllabes_count = len(syllabes)
        word_list = []
        curr_id = 0
        while curr_id < syllabes_count:
            curr_word = syllabes[curr_id]
            if curr_id >= syllabes_count - 1:
                word_list.append(curr_word)
                break
            pair_word = ' '.join([curr_word.lower(), syllabes[curr_id + 1].lower()])
            if curr_id >= syllabes_count - 2:
                if pair_word in self.bi_grams:
                    word_list.append(pair_word)
                    break
                else:
                    word_list.append(curr_word)
                    word_list.append(syllabes[curr_id+1])
                    break

            triple_word = ' '.join([pair_word, syllabes[curr_id + 2].lower()])
            if triple_word in self.tri_grams:
                word_list.append(triple_word)
                curr_id += 3
            elif pair_word in self.bi_grams:
                word_list.append(pair_word)
                curr_id += 2
            else:
                word_list.append(curr_word)
                curr_id += 1
        return word_list
    
    def pos_tag(self, tokens): 
        tags = []
        time_pattern = re.compile("\d+:\d+[Hh][Rr]")
        for token in tokens:
            if token.lower() in self.tags_dict.keys():
                tags.append(self.tags_dict[token.lower()])
            elif time_pattern.match(token):
                tags.append(TIME)
            else:
                tokens.remove(token)
        return tags

def test(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    print(tokens)
    tags = tokenizer.pos_tag(text)
    print(tags)
if __name__ == '__main__':
    query_string = input()
    test(query_string)


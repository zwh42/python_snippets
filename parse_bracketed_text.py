import re
from collections import OrderedDict

def parse_brackted_text(text, open_token = "{", close_token = "}"):

    regular_expression = "(" + "\\" + open_token + ")|(" + "\\" + close_token + ")|" + ",|" + "[\s]+"
    #print(regular_expression)
    
    token_list = re.split(regular_expression, text)
    #print(token_list)

    token_list = [token for token in token_list if token not in [None, ""]]
    #print("token list: {}".format(token_list))
    
    depth_counter = OrderedDict()
    depth = 0   
    for token in token_list:
        if token == open_token:
            depth += 1
            index = 0
            if depth not in depth_counter:
                depth_counter[depth] = 0
            else:
                depth_counter[depth] += 1
        elif token == close_token:
            depth -= 1
        else:            
            value = float(token)
            temp_name = ""
            extract = list(depth_counter.items())[1:] # remove the out-most "{" order
            for depth, _ in extract:
                temp_name += "[" + str(depth_counter[depth]) + "]"            
            temp_name += "[" + str(index) + "]"            
            index += 1
            
            print(temp_name + " = {}".format(value))


if __name__ == "__main__":
    parse_brackted_text("{{{1, 2}, {3, 4}}}")
    parse_brackted_text("((5, 6, 7), (8, 9))", open_token = "(", close_token = ")")                              
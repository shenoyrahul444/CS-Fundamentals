
import json
import fileinput
""" FOR CONVERTING STRING version of Dictionary to DICTIONARY 

                1> evals(dict_str)
                2> ast.literal_eval(dict_str)        
BEST ->         3> json.loads(dict_str)              <- Problem with Single Inverted commas. But should work for a REGULAR JSON   

"""
d_len = 0
req_len = 0

dict_str = ""

req_ = []
for i, line in enumerate(fileinput.input()):
    if i == 0:
        d_len, req_len = line.split(" ")
        d_len, req_len = int(d_len), int(req_len)
    elif 0 < i <= d_len:
        dict_str += line
    else:
        req_.append(line.replace("\n", ""))

# print(d_len,req_len,dict_str,req_)

result = []
# obj = ast.literal_eval(dict_str)
# obj = eval(dict_str)


obj = json.loads(dict_str)
for reqs in req_:
    layers = reqs.split(".")
    level = obj
    for layer in layers:
        if layer in level:
            level = level[layer]
        else:
            result.append(None)
            layer = None
            break
    if layer:
        result.append(level)

for val in result:
    if val == True:
        print("true")
    elif val == None:
        print("null")
    elif type(val) == str:
        print('"' + val + '"')
    else:
        print(val)






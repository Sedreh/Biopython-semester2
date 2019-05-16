
import json

#json data packet is like python dictionary with a few exceptions. All the keys are strings
# and the values also can be strings. The "load" methods:
# json.loadf(f): allowed us to load json data from a file
#json.loads(s): allowed us to load json data from a strong

# we need to sort the classes in lexicographical order,it means sort in dictionary order.


#For each class, calculate the number of its descendants
tree = json.loads('[{"name": "B", "parents": ["A", "C"]}, '
                  '{"name": "C", "parents": ["A"]},'
                  '{"name": "A", "parents": []},'
                  '{"name": "D", "parents": ["C", "F"]},'
                  '{"name": "E", "parents": ["D"]},'
                  '{"name": "F", "parents": []}]')

d = dict()

for elem in tree:

    if len(elem["parents"]) > 0:
        for p in elem["parents"]:
            if p not in d:
                d[p] = [elem["name"]]
            else:
                d[p].append(elem["name"])

print(d)

elems = [n["name"] for n in tree]
elems.sort()


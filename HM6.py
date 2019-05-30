
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
        for x in elem["parents"]:
            if x not in d:
                d[x] = [elem["name"]] # #a = [1,2], a.append(3)
            else:
                d[x].append(elem["name"])  #difference between extend(adding more than one element) and append(add one element)

print(d)

#sort in lexoicographical(dictionary) order
elems = [n["name"] for n in tree]
elems.sort()

#Given a tree in form of adjacency list we have to calculate the number
# of nodes in the subtree of each node, while calculating the number of
# nodes in the subtree of a particular node that node will also be added
# as a node in subtree hence number of nodes in subtree of leaves is 1.

#Expalnation: First we should calculate value count[s] : the number of
# nodes in subtree of node s. Where subtree contains the node itself and
# all the nodes in the subtree of its children. Thus, we can calculate the
# number of nodes recursively using concept of DFS and DP, where we should
# process each edge only once and count[] value of a children used in calculating
# count[] of its parent expressing the concept of DP(Dynamic programming).


def dfs_tree(d, start):
    viz = dict.fromkeys(elems, False)

    def dfs(node):
        viz[node] = True
        if node in d:
            for ch in d[node]:
                if not viz[ch]:
                    dfs(ch)
    dfs(start)

    return sum(viz.values())

d_values = dict()
for node in elems:
    d_values[node] = dfs_tree(d, node)

print(d_values)
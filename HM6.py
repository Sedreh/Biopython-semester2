

#json data packet is like python dictionary with a few exceptions. All the keys are strings
# and the values also can be strings. The "load" methods:
# json.loadf(f): allowed us to load json data from a file
#json.loads(s): allowed us to load json data from a strong

# we need to sort the classes in lexicographical order,it means sort in dictionary order.


#For each class, calculate the number of its descendants


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

#This homework was more applicable with BFS!


import json

json_data = '''
        [{"name": "B", "parents": ["A", "C"]},
         {"name": "C", "parents": ["A"]},
         {"name": "A", "parents": []},
         {"name": "D", "parents": ["C", "F"]},
         {"name": "E", "parents": ["D"]},
         {"name": "F", "parents": []}]'''


def create_graph(json_data):
    d = dict()
    tree = json.loads(json_data)

    for elem in tree:
        if len(elem["parents"]) > 0:
            for p in elem["parents"]:
                if p not in d:
                    d[p] = [elem["name"]]
                else:
                    d[p].append(elem["name"]) ##difference between extend(adding more than one element) and append(add one element)

    print(d)
    for elem in tree:
        if elem["name"] not in d:
            d[elem["name"]] = []

    d = {x:set(y) for x,y in d.items()}

    return d, sorted(d.keys())

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


graph, nodes = create_graph(json_data)

for node in nodes:
    print('{}: {}'.format(node, len(bfs(graph, node))))




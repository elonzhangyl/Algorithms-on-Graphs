# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:01:00 2018

@author: yz17571
"""

def explore(nodes, x):
    nodes[x]['visited'] = True
    for node in nodes[x]['neighbours']:
        if not nodes[node]['visited']:
            explore(nodes,node)

            
def number_of_components(nodes):
    result = 0
    for node in nodes:
        if not node['visited']:
            result +=1
            explore(nodes, nodes.index(node))
    return result
             


#4 2 1 2 3 2
inputData = input('inputs')
#print(inputData)
data = list(map(int, inputData.split()))#switch string to list
n, m = data[0:2]
data = data[2: ]
edges = list(zip(data[0:2*m:2],data[1:2*m:2]))
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
nodes = list({'visited':False, 'neighbours':neighbours} for neighbours in adj)
print(number_of_components(nodes))
        
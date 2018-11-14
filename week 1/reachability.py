# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:45:24 2018

@author: yz17571
"""

def explore(vertices, x, y):
    vertices[x]['visited'] = True
    if y in vertices[x]['neighbours']:
        return 1
    for u in vertices[x]['neighbours']:
        explore(vertices, u, y)
    return 0

            
             


#4 4 1 2 3 2 4 3 1 4 1 4
inputData = input('inputs')
#print(inputData)
data = list(map(int, inputData.split()))#switch string to list
n, m = data[0:2]
data = data[2: ]
edges = list(zip(data[0:2*m:2],data[1:2*m:2]))
x, y = data[2*m:]
x, y = x-1, y-1
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
vertices = list({'visited':False, 'neighbours':neighbours} for neighbours in adj)
print(explore(vertices,x,y))
    
import math
import json
import os
from Moves import *
#Position/Distance Finder
n = int(input()) #Number Of Nodes
Initial = [i for i in range(1,n+1)]
Distance = []
Number =0
function_list = []
m= int(input())
for i in range(m):
    index = int(input())
    function_list.append(index) 
#BFS
bool_check = {}
Distance.append([Initial])
bool_check[tuple(Initial)] = True
Diameter = 0
nodes = 1
while 1:
    foo = []
    for i in Distance[Diameter]:
        for j in function_list:
            node = i[:]
            execution(node,j)
            if node in bool_check.keys():
                pass
            else:
                foo.append(node)
                bool_check[tuple(node)]=True
                nodes+=1
    Diameter+=1
    if foo == []:
        break
    else:
        Distance.append(foo)
#print(Diameter)
#print(Distance)
#print(nodes)



#Graph
'''
x_axis = [i for i in range(0,Diameter)]
y_axis = [len(i) for i in Distance]
plt.plot(x_axis,y_axis)
plt.show()
'''

#File

Distance_dir ={}

for i,j in enumerate(Distance):
    Distance_dir[i] = j

with open('pravega.txt','w') as file:
    json.dump(Distance_dir,file,indent=4)
                
        




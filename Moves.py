import math
#Functions
#1
def Right_Shift(node,n):
    foo = node[0]
    for i in range(1,n+1):
        node[i%n],foo=foo,node[i%n]
#2
def Left_Shift(node,n):
    foo = node[0]
    for i in range(0,n-1):
        node[i]=node[i+1]
    node[n-1]=foo
#3
def reverse(node,n):
    for i in range(math.ceil((n-1)/2)):
        node[i],node[n-i-1]= node[n-i-1],node[i]
#4
def alt_swap(node,n):
    for i in range(0,n,2):
        if i != n-1:
           node[i],node[i+1] = node[i+1],node[i]
def half_reverse(node,n):
    for i in range(math.floor(n/2)):
        node[i],node[i+math.ceil(n/2)] = node[i+math.ceil(n/2)] , node[i]
#Execution Order
def execution(node,index):
    if index == 1:
       Right_Shift(node,len(node))
    elif index == 2:
       Left_Shift(node,len(node))
    elif index == 3:
        reverse(node,len(node))
    elif index == 4:
        alt_swap(node,len(node))
    elif index == 5:
        half_reverse(node,len(node))
    else:
        pass
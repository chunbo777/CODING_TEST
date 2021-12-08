from collections import defaultdict



def solution(n, vertex):
    final =[]
    vertex.sort()
    parentD = defaultdict(int)
    parentD[1] += 1
    parent = [0]*(n+1)
    for i in range(n+1):
        parent[i] = i
        parentD[i]


    def find_parent(parent, x):
        if parent[x] != x: 
           parentD[x] += parentD[parent[x]]
           return find_parent(parent, parent[x]) 

        return parent[x]

    def union(parent, vertex):
        a, b = vertex
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
            # parentD[b] += (parentD[a]+1)
        elif a == b:
            pass
        else:
            parent[a] = b
            # parentD[a] += (parentD[b]+1)


    for ver in vertex:
        union(parent, ver)
    
    return len([i for i in parentD.values() if i ==  0]) -1



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)
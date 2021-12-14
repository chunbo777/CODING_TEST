# from collections import defaultdict
import copy
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

# def solution(n, vertex):
#     final =[]
#     vertex.sort()
#     parentD = defaultdict(int)
#     parentD[1] += 1
#     parent = [0]*(n+1)
#     for i in range(n+1):
#         parent[i] = i
#         parentD[i]


#     def find_parent(parent, x):
#         if parent[x] != x: 
#            parentD[x] += parentD[parent[x]]
#            return find_parent(parent, parent[x]) 

#         return parent[x]

#     def union(parent, vertex):
#         a, b = vertex
#         a = find_parent(parent, a)
#         b = find_parent(parent, b)
#         if a < b:
#             parent[b] = a
#             # parentD[b] += (parentD[a]+1)
#         elif a == b:
#             pass
#         else:
#             parent[a] = b
#             # parentD[a] += (parentD[b]+1)


#     for ver in vertex:
#         union(parent, ver)
    
#     return len([i for i in parentD.values() if i ==  0]) -1
def solution(n, vertex):
    class Node:
        def __init__(self, key):
            self.key = key
            self.parent = self
            self.rank = 0
        def __str__(self):
            return str(self.key)     
    def makeset(x):
        return Node(x)
    def find(x, find_idx = 0):
        while x.parent != x:
            x = x.parent
            find_idx += 1
        return x, find_idx
    # key_list = []
    def union(ver, keylist):
        x, y = ver
        if x not in [k.key for k in keylist]:
            v = makeset(x)
        else:
            for k in keylist:
                if k.key == x:
                    v = k
                    break
        if y not in [k.key for k in keylist]:
            w = makeset(y)
        else:
            for k in keylist:
                if k.key == y:
                    w = k
                    break
 
        if v.key > w.key:
            v.parent = w
            v.rank += 1
        else:
            w.parent = v
            w.rank += 1
        
        return [v, w]
    key_list = []
    for ver in vertex:
        key_list.extend(union(ver, key_list))
    key_list = list(set(key_list))
    print(key_list)
    # def noding(key, keylist):
    #     if key in keylist:
    #         return Node.up(key)
    #     else:
    #         return Node(key)
# def solution(n, vertex):
#     parent = {}
#     dp ={}
#     def union(a, b,  parent):
#         if a < b:
#             parent[b] = a
#             dp[b] = a
#         else:
#             parent[a] = b
#             dp[a] = b 
#     for ver in vertex:
#         a, b = ver
#         union(a, b,  parent)
     
#     idxs = []
#     parent[1] = None
#     dp[1] = None
#     for x in range(1,n+1):
#         parent = copy.deepcopy(dp)
#         idx = 0
#         while parent[x] != None:
#             idx += 1
#             parent[x] = parent[parent[x]]
#         idxs.append(idx)
#     k = max(idxs)
#     return idxs.count(k)

solution(n, vertex)
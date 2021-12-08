def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = 7, 9

parent = [0]*(v+1)

edges = [(29, 1, 2), (75, 1, 5), (35, 2, 3), (34, 2,6), (7, 3,4), (23,4,6),(13,4,7),(53, 5,6), (25, 6, 7)]
result = 0 

for i in range(1, v+1):
    parent[i]=i
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함 
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
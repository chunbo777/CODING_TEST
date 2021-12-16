
from collections import defaultdict, deque
import numpy as np
def solution(n, computers):
    def zero(array):
        zeros = []
        for i in array:
            z1 = []
            for j in i:
                z1.append(0)
            zeros.append(z1)
        return zeros
    def dfs2(x, y, computers):
        if x<0 or x>=n or y<0 or y>=n:
            return
        if computers[x][y] == 1 or visit[x][y] ==1:
            return
        else:
            visit[x][y]=1
        dfs2(x+1, y, computers)
        dfs2(x-1, y, computers)
        dfs2(x, y-1, computers)
        dfs2(x, y+1, computers)
        return True 
    def bfs(queue, start, visited):
        visited[start] = True
        start += 1
        q = deque([start])
        while True:
            idx = 0
            v = q.popleft()
            for i in queue[v]:
                if i != False and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    visiting[v-1][i] = 1 
                    visiting[i][v-1] = 1
                # elif v-1 == i:
                #     visiting[i][v-1] = 1
            if idx == len(computers)^2:
                break
        return 
    bfsD = defaultdict(list)
    visiting = zero(computers)
    visit = zero(computers)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i!=j:
                bfsD[i].append(j)
            elif i == j:
                visiting[i][j] = 1
                bfsD[i].append(False)
            else:
                bfsD[i].append(False)
    
    queue = deque(bfsD.values())
    queue.appendleft([]) # 더미노드 넣기
    print(bfsD)
    start = 0
    visited = [False]*(n+1)
    
    bfs(queue, start, visited)
    
    cnt = 0
    for i in range(0, n):
        
        for j in range(0, n):
            if dfs2(i,j, computers) == True:
                cnt += 1

    return cnt



n = 3	
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#return =  1
solution(n, computers)
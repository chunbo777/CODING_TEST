"""
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 
컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오."""
"""수도코드
"""
import numpy as np
from collections import defaultdict, deque
def solution(n, computers):
    visited = np.zeros_like(computers)
    visiting = np.zeros_like(computers)
    computers = np.asarray(computers)
    visitD = defaultdict(list)
    def find(x, y):
        if x<0 or x>=n or y<0 or y>=n:
            return
        if computers[x][y] == 1: 
            if x!= y:
                visitD[x].append(y)
                visitD[y].append(x)
        else:
           bfs(x,y)
             
            
            return
        return True
    def dfs2(x, y, computers):
        if x<0 or x>=n or y<0 or y>=n:
            return
        if computers[x][y] == 1 or visited[x][y] ==1:
            return
        else:
            visited[x][y]=1
        dfs2(x+1, y, computers)
        dfs2(x-1, y, computers)
        dfs2(x, y-1, computers)
        dfs2(x, y+1, computers)
        return True 

    def bfs(x, y, start = 0, visitD):
        queue = deque([start])
        visiting[start] = True 
        while queue:
            v = queue.popleft()
            for i in visitD[v]:
                if not visiting[i]:
                    queue.append(i)
                    computers[]
    for i in range(0, n):
        visitD[i].append([]) # 더미 노드 넣어주기 
    for i in range(0, n): 
        stack = []
        for j in range(0, n):
            find(i,j)
    cnt = 0
    for i in range(0, n):
        
        for j in range(0, n):
            if dfs2(i,j, computers) == True:
                cnt += 1

    return cnt+1


    # def find(x, y):
    #     if computers[x][y] == 1: #연결되어 있으면
    #         if x == y:
    #             pass
    #         #1,2 => 2,3으로 이동
    #         else:
    #             x , y = y, x + 1 #y와 x를 스왑 
    #         if x < 0 or x >= n or y < 0 or y >= n or x == y:
    #             return False
    #         else:
    #             find(x, y)
    #     else:
    #         computers[x][y] = 1
    #         computers[y][x] = 1
    #         return 
    # find(0,0)
    
n = 3	
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#return =  2 
solution(n, computers)
# def solution(n, computers):  
#     def zero(array):
#         zeros = []
#         for i in array:
#             z1 = []
#             for j in i:
#                 z1.append(0)
#             zeros.append(z1)
#         return zeros
#     stack = []
#     visit = zero(computers)

#     def bfs(computers, start_i,start_j, stack, visit):
#         while start_j <= n or start_i<= n :
#             while computers[start_i][start_j] != 1: #우측으로만 이동 0의 짝을 찾아서~
#                 start_j += 1
#                 if start_j == n: # 끝에 도달하게 되면
#                     start_j = 0 #좌우값은 초기화
#                     start_i += 1 #행 값을 업뎃
#                 if start_i == n: # 끝에 도달하기 까지 짝이 없다면
#                     return False  #리턴 팔스
#             if start_i == start_j:
#                 visit[start_i][start_j] = 1
#                 start_j+=1
#                 pass
#             else:
                
#                 stack.append(start_i)
#                 stack.append(start_j)
#                 while stack:
#                     v1 = stack.pop()
#                     v2 = stack.pop()
#                     for i, k in enumerate(computers[v1]): #0과 만난 열의 그 행에 대해서
#                         if k == 1 and visit[v2][i] == 0:
#                             computers[v2][i]= 1
#                             visit[v2][i] =1
#                             stack.append(v2)
#                             stack.append(i)
#                         else:
#                             pass
#                 start_j += 1
#     bfs(computers, 0, 0, stack, visit)
from collections import defaultdict
import numpy as np
# def solution(n, computers):
#     visited = np.zeros_like(computers)
#     x = 0
#     y = 0
#     stack = []
#     def dfs(visited, stack,x, y):
#         dfsD = defaultdict(list)
#         visited[x][y] = 1
#         # start = stack[-1]
#         for idx, k in enumerate(computers[x]):
#             # if idx > y :
#             if k == 1 and visited[x][idx] == 0: #연결 되어 있으나 방문하지 않은 경우
#                 stack.append((x, idx)) #시작점, 끝점
#                 dfsD[x].append(idx)
#                 dfsD[idx].append(x)
#                 visited[x][idx] = 1
#                 visited[idx][x] = 1
#                 while stack:
#                     v, w = stack.pop() #시작점 끝점을 빼어서
#                     # if k == w and idx != w:
#                     if idx in dfsD[x] or x in dfsD[idx] and idx!=x: #만약 스택의 (새로운) 끝점이 현재 끝점과 연결되어 있으면 
#                         # stack.append((v, idx)) #끝점과 시작점을 연결 
#                         visited[v][idx] = 1
#                         visited[idx][v] = 1
#                         computers[v][idx] = 1
#                         computers[idx][v] = 1
#                         dfsD[v].append(idx)
#                         dfsD[idx].append(v)
            
#                 dfs(visited, stack, idx, 0)
#             else:
#                 pass
#         return 
#     dfs(visited, stack, x, y)
def solution(n, computers):
    visited = np.zeros_like(computers)
    stack = [(0,0)]

    def bfs(computers, stack):
        while stack:
            x, y = stack.pop() #시작점
            for idx, i in enumerate(computers[x]): #열 중심으로 만나는 값이 있다면 x = 행 idx = 열
                if x!= idx and i == 1 : #자기 자신이 아닌데도 만나는 점이 있다면 
                    if visited[idx][y] == 1: #연결점을 이미 방문했다면 
                        return
                    else:
                        computers[y][idx] = 1 #y = 그 다음의 가야할 곳 그 줄의, 
                        computers[idx][y] = 1
                        visited[idx][y] = 1
                        visited[y][idx]=1
                        stack.append((idx, x)) #그 다음에 가야할 곳 , 연결된 곳 
                else: #자기 자신이라서 만나는 경우
                    visited[idx][y]  =  1
                bfs(computers, stack)
    # for i in n:
    bfs(computers, stack)  
            



        

n = 4
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1,0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#return =  2 
solution(n, computers)
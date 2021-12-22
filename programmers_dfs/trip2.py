i = 0
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	

def bfs(tickets):
    result = []
    visited = [False]*len(tickets)
    visitedD = {}
    result_final = []
    # dep, avl = stack.pop()
    # visited[i]
    stack = bfs_icn(visited)
    # visited[1]=True
    for dep, avl in tickets:
        visitedD[(dep, avl)] = False
    while stack :
        [dep, avl] = stack.pop()
        result.append([dep, avl])
        visitedD[(dep,avl)] = True
        if sum(visited) == 5:
            visited = [False]*len(tickets)
            result_final.append(result)
            break
        for i, [dp, av] in enumerate(tickets):
            if visitedD[(dp, av)]==False and avl == dp:
                stack.append([dp, av])
                # visitedD[(dep,avl)] = False
                
# def bfs_icn(stack, results, visited = [False]*len(tickets)):
def bfs_icn(visited = [False]*len(tickets)):
        for i, [dep, avl] in enumerate(tickets) :
                if dep == "ICN" and visited[i] == False : 
                # if dep == "ICN" and visited[i] == '0' : 
                    # visited.replace(visited[i], '1')
                    visited[i] = True
                    # stack.append([i, tickets[i]])
                    stack.append(tickets[i])
                    break
                   
        if len(stack) == 0: #인천 순회 다 한 경우
            return False
        else:
            return stack
# bfs(tickets)

# def dfs(tickets,result, dep, avl , pointer = 0, visited= [False]*len(tickets)):
#     # 인천 수만큼 인덱스를 잡는 것ㅡ 어ㅈ떨지?
#     if pointer == 0:
#         for [i, [dep, avl]] in bfs_icn(stack, result, visited):
#             visited[i] = True
#             result.extend([dep, avl])
#             dfs(tickets,result, dep, avl, pointer+1, visited)

#     else: 
#         for i, [d, a] in enumerate(tickets):
#             if avl == d and visited[i] == False:
#                 visited[i] = True
#                 result.append(a)
                
#                 if sum(visited) == 5: #모두 방문했을 경우에는
#                     res_all.append(result)
#                     return
#                 dfs(tickets,result, d, a, pointer+1, visited)
#         return


# visited = [False]*len(tickets)
# visited =  "0"*len(tickets)
stack = []
result = []  
res_all = []

# dfs(tickets, result, 0, 0,  visited=[False]*len(tickets))
bfs(tickets)



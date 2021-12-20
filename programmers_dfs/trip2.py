i = 0
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	

# def bfs(tickets):
#     result = []
#     visited = [False]*len(tickets)
#     result_final = []
#     # dep, avl = stack.pop()
#     # visited[i]
#     stack = [['ICN', 'ATL']]
#     visited[1]=True
#     while stack :
#         dep, avl = stack.pop()
#         result.append([dep, avl])
#         if sum(visited) == 5:
#             visited = [False]*len(tickets)
#             result_final.append(result)
#             break
#         for i, [dp, av] in enumerate(tickets):
#             if visited[i]==False and avl == dp:
#                 stack.append([dp, av])
#                 visited[i] = True
def bfs_icn(stack, visited, results):
        for i, [dep, avl] in enumerate(tickets) :
                if dep == "ICN" and visited[i] == False : 
                    visited[i] = True
                    stack.append([i, tickets[i]])
                    
                    # break
        if len(stack) == 0: #인천 순회 다 한 경우
            return False
        else:
            return stack
# bfs(tickets)

def dfs(tickets,result, visited, dep, avl , pointer = 0):
    if pointer == 0:
        for [i, [dep, avl]] in bfs_icn(stack, visited, result):
            visited[i] = True
            result.extend([dep, avl])
            dfs(tickets,result, visited, dep, avl, pointer+1)

    else: 
        for i, [d, a] in enumerate(tickets):
            if avl == d and visited[i] == False:
                visited[i] = True
                result.append(a)
                if sum(visited) == 5: #모두 방문했을 경우에는
                    res_all.append(result)
                    return
                dfs(tickets,result, visited, dep, avl, pointer+1)
                
       
        return


visited = [False]*len(tickets)
stack = []
result = []  
res_all = []

dfs(tickets, result, visited, 0, 0)



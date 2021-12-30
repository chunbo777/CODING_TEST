tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
resall = []
result = tuple()
def bfs(dep, avl, tickets, time = 0, visited = tuple([False])*len(tickets)):
    global result
    if time == 0:
        result_li =list(result) 
        result_li.extend([dep, avl])
        result = tuple(result_li)
        livis = list(visited)
        livis[1] =True
        visited = tuple(livis)

    for i, [d, a] in enumerate(tickets):
        if avl == d and visited[i]==False:
            livis = list(visited)
            livis[i] =True
            visited = tuple(livis)
            result_li =list(result) 
            result_li.append(a)
            result = tuple(result_li)
            print("티켓중:", tickets, "현재방문위치는:", i, [d, a])
            if all(visited):
                resall.append(result)
                # visited[i] = False
                return
            bfs(d, a, tickets, time+1, visited)
        else:
            pass


bfs("ICN", "ATL", tickets)

# #가장 멍청한 방법
# idx = 0
# result = []
# res_all = []
# visitD = {}
# for dep, avl in tickets:
#     visitD[(dep, avl)] = False
# while True:
#     for i, [dep, avl] in enumerate(tickets):
#         if idx == 0:
#             if dep == "ICN":
#                 result.extend([dep, avl])
#                 visitD[(dep, avl)] = True
#                 idx += 1
#                 break
#         else: 
#             if dep == result[-1] and visitD[(dep, avl)]== False:
#                 result.append(avl)
#                 visitD[(dep, avl)] =  True
    
#     if len(result) >= len(tickets) + 1:
#          res_all.append(result)
#          result = []
        
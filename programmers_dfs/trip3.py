tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
resall = []
def bfs(dep, avl, tickets, visit =" ", time = 0, visited =[False]*len(tickets)):
    if time == 0:
        visit = ""
        visited[0] =True
    for i, [d, a] in enumerate(tickets):
        if avl == d and visited[i]==False:
            visit+= " " +a
            visited[i] = True
            if time == 3:
                resall.append(visit)
                visited[i] = False
                return
            bfs(d, a, tickets, visit, time+1, visited)
        else:
            pass


bfs("ICN", "SFO", tickets, visit=" ")

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
        
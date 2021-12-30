from collections import deque
def solution(tickets):
    visited = [False]*len(tickets)
    tickets.sort()
    stack = deque()
    
        
    results = []
    idx =0
    def bfs(stack):
        nonlocal idx
        if idx == 0:
            stack.pop()
            for i, [dep, avl] in enumerate(tickets):
                if dep == "ICN" and avl in [d for d, a in tickets]: #마지막 인천이 아닌 경우에만 
                    visited[i] = True
                    stack.append(tickets[i])
                    results.append("ICN")
                    idx += 1
                    break
        dep, avl = stack.pop()
        results.append(avl)
        for i, [d, a] in enumerate(tickets):
            # if idx <len(tickets)-1:
                # if avl == d and  avl in [d for d, a in tickets] and visited[i]== False :
                if avl == d and visited[i]== False :
                    visited[i] = True
                    stack.append([d,a])
                    idx+=1

                    break
            # else:
            #     if avl == d and visited[i]== False :
            #         visited[i] = True
            #         stack.append([d,a])
            #         idx+=1

            #         break
        return
    stack.append("start")
    while stack:
        bfs(stack)
    

    return results



# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
#return = ["ICN", "JFK", "HND", "IAD"]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["SFO","ZKO"]]	
#return = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
solution(tickets)
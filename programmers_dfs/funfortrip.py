"""주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항

모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 
a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 
알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
["ICN", "JFK", "HND", "IAD"]

[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
입출력 예 설명
예제 #1

["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2

["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다."""


from collections import deque
def solution(tickets):
    visited = [False]* len(tickets)
    stack = deque()
    results = []
    res_all = []
    idx = 0   
 
    def bfs_icn(stack, visited, results):
        nonlocal idx
        # if idx == 0:
        for i, [dep, avl] in enumerate(tickets) :
                if dep == "ICN" and visited[i] == False : 
                    visited[i] = True
                    stack.append(tickets[i])
                    results.append("ICN")
                    # break
        if len(stack) == 0: #인천 순회 다 한 경우
            return False
        else:
            return stack
            # idx += 1

    def bfs(stack, visited, results):
        if len(stack) == 0:
            stack = bfs_icn(stack, visited, results)
            # if stack != False:
            #     pass #인천 스택을 제공     
            # else:
            #     return False
        # if len(stack) == 0:
        #     return results
        while stack:
            dep, avl =  stack.pop()
            results.append(avl)
            if len(results) == len(tickets)+1:
                res_all.append(results)
            for i, [d, a] in enumerate(tickets):
                if avl == d and visited[i]== False :
                    visited[i] = True
                    stack.append([d,a])
                    # return results
                else:
                    if avl !=  d:
                        pass
                    else: # 행선지가 같지만 이미 visit한 경우
                        pass


    
    bfs(stack, visited, results)
        
    return res_all

# from collections import deque

# def solution(tickets):
#     visited = [False]*len(tickets)
#     tickets.sort()
#     stack = deque()
    
        
#     results = []
#     idx =0
#     # def deadend(stack, visited, d, a, i):
#     #     stack2 = stack
#     #     visiting = visited
#     #     stack2.append([d,a])
#     #     visiting[i] = True
#     #     while stack2:
#     #         bfs(stack2)


#     def bfs(stack):
#         nonlocal idx
#         if idx == 0:
#             stack.pop()
#             for i, [dep, avl] in enumerate(tickets):
#                 if dep == "ICN" and avl in [d for d, a in tickets]: #마지막 인천이 아닌 경우에만 
#                     visited[i] = True
#                     stack.append(tickets[i])
#                     results.append("ICN")
#                     idx += 1
                    
#         dep, avl = stack.pop()
#         results.append(avl)
#         for i, [d, a] in enumerate(tickets):
#             if avl == d and visited[i]== False :
#                 visited[i] = True
#                 stack.append([d,a])
#                 idx+=1
#                 # bfs(stack)
#                 # return True
    
#         return
#     stack.append("start")
#     while stack:
#         bfs(stack)
    

#     return results



# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
#return = ["ICN", "JFK", "HND", "IAD"]
#return = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
solution(tickets)
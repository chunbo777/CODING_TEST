import time 
start = time.time()
# import numpy as np
# def solution(n, costs):
#     npcosts = np.array(costs)
#     np.argsort(npcosts)
#     return npcosts
# def solution(n, costs):
#     start = costs[0][2] #시작점
#     final = []
#     cost = []
#     for [st, dp, co] in costs:
#         while co < start:
#             if final != []:
#                 final.pop()
#                 final.pop()
#                 cost.pop()
#             if cost!=[]:
#                 start = cost[-1]
#             else:
#                 start = co
#             final.append(st)
#             final.append(dp)
#             cost.append(co)
#             if (len(final) == 2*(n-1)) and len(set(final)) == n:
#                 break

#             # start = co
#         else :
#             final.append(st)
#             final.append(dp)
#             cost.append(co)

#             start = cost[-1]
#             #여러번 어팬드 되지 않게 해야 함 
#     return sum(cost)

# def solution(n, costs):

    # while len(cost) != n:
    #     for [st, dp, co] in costs:
    #         if cost != []:
    #             while cost[-1] > co:
    #                 final.pop()
    #                 cost.pop()
    #                 if cost == []:
    #                     break
    #                 if len(cost)==n:
    #                     break
                
    #         final.append([st, dp])
    #         cost.append(co)
# n = 5
# # costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# costs = [[2,3,8],[0,2,2],[1,2,5],[1,3,7],[1,3,1],[0,1,1], [0,4,7]]
# solution(n, costs)
# n = 5
# costs = [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]    
     
n = 5
costs = [[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]] 
def mergeSort(a):
    if len(a) > 1: 
        mid = len(a)//2 
        la, ra = a[:mid], a[mid:] 
        mergeSort(la) 
        mergeSort(ra) 
        li, ri, i = 0, 0, 0 
        while li < len(la) and ri < len(ra): 
            if la[li][2] < ra[ri][2]: 
                a[i] = la[li] 
                li += 1 
            else: 
                a[i] = ra[ri] 
                ri += 1 
            i += 1 
        a[i:] = la[li:] if li != len(la) else ra[ri:]
    return a
    

final = []
island = []
cost = []
for [st, dp, co] in mergeSort(costs):
    if st not in final or dp not in final:
        if st not in final and dp not in final:
            island.extend([st,dp])
        final.extend([st, dp])
        cost.append(co)
    if (len(final) == 2*(n-1)) and len(set(final)) == n:
       print(sum(final))
       break

final = [0, 1, 2, 3,3, 4]

# def solution(n, costs):
#     def mergeSort(a):
#         if len(a) > 1: 
#             mid = len(a)//2 
#             la, ra = a[:mid], a[mid:] 
#             mergeSort(la) 
#             mergeSort(ra) 
#             li, ri, i = 0, 0, 0 
#             while li < len(la) and ri < len(ra): 
#                 if la[li][2] < ra[ri][2]: 
#                     a[i] = la[li] 
#                     li += 1 
#                 else: 
#                     a[i] = ra[ri] 
#                     ri += 1 
#                 i += 1 
#             a[i:] = la[li:] if li != len(la) else ra[ri:]
#         return a


#     final = []
#     final_tuple = []
#     st_list = []
#     dp_list = []
#     cost = []
#     # def find(st, dp, st_list, dp_list):
        
#     for [st, dp, co] in mergeSort(costs):
#         # if st not in final or dp not in final:
#         # if st not in final and dp not in final:
#         if st in st_list and dp in dp_list:
#             find(st)
#         st_list.append(st)
#         dp_list.append(dp)
#         final_tuple.append((st, dp))
#         final.extend([st, dp])
#         cost.append(co)
#         # if (len(final) == 2*(n-1)) and len(set(final)) == n:
        #    break
    
#     return sum(cost)
# solution(n, costs)
# end = time.time()
# print(end-start)
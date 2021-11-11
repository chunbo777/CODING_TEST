# answer = 0
# def first_line(route):
#     global answer
#     first_end = route[0][-1]
#     for i, [come, go] in enumerate(route[1:]):
#         if go > first_end :
#             answer+=1
#             first_line(route[i:]) 
#         elif go < first_end :
#             pass
#         # if first_end < come:
#         #     fist_end = go

#     return answer
# def solution(routes):
#     answer = 1
#     sort_route =  sorted(routes, key = lambda x : x[0])
#     return first_line(sort_route)
    # k_list = []
    # for i, [comein, goout] in enumerate(sort_route):
    #     if i == len(sort_route)-1 : 
    #         pass
    #     elif  sort_route[i+1][1] <= goout:
    #         k_list.append((sort_route[i+1][0], sort_route[i+1][1]))
    #     elif goout <  sort_route[i+1][1]:
    #         k_list.append(()) 
    # for k in range(sort_route[0][0], sort_route[-1][-1]):
    #     for i, [comein, goout] in enumerate(sort_route):
    #         if i == len(sort_route)-1:
    #             pass
    #         elif comein <= k <=goout and sort_route[i+1][0]<= k <= sort_route[i+1][1]:
    #             k_list.append(k)
        
    # for i, k in enumerate(k_list):
    #     if i == len(k_list)-1:
    #         pass
    #     elif k_list[i+1] - k != 1:
    #         answer +=1
def solution(routes):
    answer = 0
    pointer = -30001
    sort_route =  sorted(routes, key = lambda x : x[1]) 
    for [st, ed] in sort_route: 
        if pointer <st: 
            answer += 1
            pointer = ed

    return answer
    

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)
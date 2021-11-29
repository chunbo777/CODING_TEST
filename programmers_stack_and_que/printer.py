"""
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

"""
from collections import deque

# def solution(priorities, location):
#     final = deque()
#     temp = deque()
#     pointer = priorities.index(max(priorities)) #시작점
    
#     # while len(final) == len(priorities):
#     while len(temp) != len(priorities): 
#         while len(temp)>0 and temp[-1]<priorities[pointer] :
#             temp.pop()
#         temp.append(priorities[pointer])
#         if pointer >= (len(priorities)-1):        
#             pointer = 0 
#         else:
#             pointer += 1
        

#     temp.append(priorities[i])  
        

#     return temp

def solution_max(priorities, location):
    temp2=[]
    for i, pro in enumerate(priorities):
        temp2.append((pro, "{}".format(i)))
    print(temp2)
    printfor= []
    while len(priorities) != None:
        try:
            max_index =  priorities.index(max([tmp[0] for tmp in temp2]))
            printfor.append(temp2[max_index])
            temp2 = temp2[max_index+1:] + temp2[:max_index] 
            priorities = priorities[max_index+1:] + priorities[:max_index]
        except:
            break
    final_index = [int(v) for k, v in printfor].index(location)
    return final_index + 1
priorities = [2, 1, 3, 2]
priorities = [3, 3, 1, 9, 1, 5, 6]
location = 0
solution_max(priorities, location)
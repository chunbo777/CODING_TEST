from collections import deque, Counter
import collections
import numpy as np
from numpy import random
# 인용 횟수가 많은 것들 부터 정렬함
# 해당 숫자와 pop 거리가 같을 때 까지 pop

def solution(citations):
    que = deque(sorted(citations))
    num = que[-1]
    pop_idx = 0
    while True:
        if que[-1] == num:
            que.pop()
            pop_idx +=1
            if pop_idx >= num:
                break
        try:
            if que[-1]!=num:
                num -=1
        except:
            return pop_idx

    return num

citations = [8,9,9,9,9,9,9]
solution(citations)
# citations = [1, 3, 6, 2, 4, 3, 6, 9, 9, 4, 8, 9, 2, 0, 3, 3, 4, 5, 2, 8, 2, 6, 8, 5, 5, 8, 5, 2, 5, 3]
# citations = list(np.random.choice(10, 30, replace=True))
# solution(citations)

# def solution2(citations):
#      que = sorted(citations, reverse = True)
#      setque = sorted(list(set(que)), reverse= True) 
#      plus = 0
#      for i in setque:
#         idx = i
#         if Counter(que)[i] + plus >= idx:
#             if Counter(que)[i] + plus >= max(range(idx, temp)):
#                 return max(range(idx, temp))
#             else:
#                 return idx
#         temp = idx
#         plus += Counter(que)[i]

# def fast2(citations):
#     visited = [False for _ in range(10)]
#     checkCnt = [[] for _ in range(10)]
#     citations1 = list(map(str, citations))
#     for i in range(10):
#         checkCnt[i] = len([int(v) for v in citations1 if int(v) >= i])
#     for i, v in enumerate(checkCnt):
#         # print(v, i)
#         if i <= int(v):
#             visited[i] = True
#     # print(visited)
#     cnt = 0
#     for i,v in enumerate(visited):
#         if v == True:
#             cnt += 1
#     answer =(cnt-1)
#     return answer
# fast2(citations)
# fast(citations)
# solution(citations)
# solution2(citations)
# while fast2(citations)==solution(citations):
#     print(fast2(citations))
#     print(solution(citations))
#     print(fast2(citations)==solution(citations))
#     print(citations)
#     citations = list(np.random.choice(10, 30, replace=True))
# print(citations)
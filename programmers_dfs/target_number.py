""" n개의 음이 아닌 정수가 있습니다. 
이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다."""
from collections import deque

# def solution(numbers, target):
#     idx =0
#     plus_idx = [False] * len(numbers)
#     minus_idx = [False] * len(numbers)
#     ans = 0
#     plus_stack = []
#     minus_stack = []
    # def dfs(numbers, idx, ans, plus_stack, minus_stack):
        
    #     if plus_idx[idx] == False:
    #         ans += numbers[idx]
    #         plus_stack.append(numbers[idx])
    #         minus_stack.append(numbers[idx])
    #         plus_idx[idx] = True # 방문처리 
    #         idx +=1 
    #         # while idx != len(numbers):
    #         #     return dfs(numbers, idx, ans, plus_stack, minus_stack)
    #     if minus_idx[idx] == False:
    #         ans -= numbers[idx]
    #         plus_stack.append(-numbers[idx])
    #         minus_stack.append(-numbers[idx])
    #         minus_idx[idx] = True
    #         idx += 1
    #         while idx != len(numbers):
    #             return dfs(numbers, idx, ans, plus_stack, minus_stack)
    #         # return dfs(numbers, idx, ans)
            
    # ans_fin = dfs(numbers, idx, ans, plus_stack, minus_stack)

def solution(numbers, target):
    

numbers = [2,3,3,1,2]
target = 1

solution(numbers, target)
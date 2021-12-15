
# def solution(numbers, target):
#     global count
#     value = 0
#     idx = 0 
#     def dfs(idx, value, numbers, target):
#         global count
#         if idx  == len(numbers):
#             if value == target:
#                 count += 1
#             return
        
#         dfs(idx + 1, value + numbers[idx], numbers, target)
#         dfs(idx + 1, value - numbers[idx], numbers, target)
#     dfs(idx, value, numbers, target)
#     return count 
    


def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


count  = 0
numbers = [2,3,3,1,2]
target = 1
solution(numbers, target)

 

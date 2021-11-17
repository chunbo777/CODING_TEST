from itertools import permutations
import numpy as np
from numpy import random
from collections import deque
def innersort(a, b):
    if int(str(a)+str(b)) < int(str(b)+str(a)):
        return True
    else:
        return False 
def solution(numbers):
    stack = deque([])
    numbers = deque(sorted(numbers, key = lambda x: str(x)[0], reverse = True))
    for i, num in enumerate(numbers):
        k_list = deque([])
        idx = 0
        if i == 0:
            stack.append(numbers[0])
        else: 
            while len(stack) > 0 and stack[-1]!= num and innersort(stack[-1], num):
                if idx == 0:
                    k_list = deque([])
                k = stack.pop()
                idx += 1
                k_list.appendleft(k)
            stack.append(num)
            stack.extend(k_list)
    if len(numbers) == sum([i == 0 for i in stack]):
        return "0"
    else:
        return "".join([str(i) for i in stack])
 


    # numbers = sorted(numbers, key = lambda x: str(x)[0] , reverse = True)
    # for i in range(1, len(numbers)):
    #     for j in range(i, 0, -1):
    #         if innersort(numbers[j-1], numbers[j]) == True:
    #              numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    #         else:
    #             pass
    # return "".join([str(i) for i in numbers])



import random # random 메소드 사용을 위해 import

numbers = [979, 97, 978, 81,818,817]


      
def perm(numbers):
    n = len(numbers)
    
    permute =  list(permutations(numbers, n))
    final = []
    for per in permute:
        answer =""
        for p in per:
            answer+=str(p)
        final.append(answer)
    try:
        ans = max(final)
    except:
         ans ="1"
    return ans

import numpy as np
# numbers = [0,0,0,0,0]
# numbers = [521, 32, 165, 128, 182]
anti = []
idx = 0
while idx != 1000000: 
    sol = solution(numbers)
    # print(sol)
    # print(perm(numbers))
    # print(sol == perm(numbers))
    if (sol == perm(numbers)) == False:
        print(numbers)
        anti.append(numbers)
    idx+=1
    numbers = list(np.random.choice(1000, 5, replace=True))
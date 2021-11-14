# def solution(numbers):
#     for i in range(1, len(numbers)):
#         for j in range(i, 0, -1):
#             if str(numbers[j])[0]> str(numbers[j-1])[0]:
#                 numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
#             elif str(numbers[j])==str(numbers[j-1]):
#                 pass
#             elif str(numbers[j])[0]==str(numbers[j-1])[0]:
#                 numbers[j-1], numbers[j] = inner_sort([numbers[j], numbers[j-1]])
#             else:
#                 break
#     return "".join([str(i) for i in numbers])
# def inner_sort(numbers, idx = 1):
    
#     for i in range(1, len(numbers)):
#         for j in range(i, 0, -1):
#             if len(str(numbers[j])) > len(str(numbers[j-1])): #뒷 수가 앞 수보다 자릿수가 크면
#                 if str(numbers[j])[len(str(numbers[j-1]))] > str(numbers[j-1])[len(str(numbers[j-1]))-1] : #자릿수가 많은 애의 삐져나온 자릿수가 앞자리 수보다 클 경우
#                     numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
#                 else:
#                     break
#             elif len(str(numbers[j])) < len(str(numbers[j-1])): #앞 수의 자릿수가 더 크면
#                 if str(numbers[j-1])[len(str(numbers[j]))] > str(numbers[j])[len(str(numbers[j]))-1] : #자릿수가 많은 애의 삐져나온 자릿수가 앞자리 수보다 클 경우
#                     break
#                 else:
#                     numbers[j], numbers[j-1] = numbers[j-1], numbers[j] #스와프
#                     break
#             else:
#                 temp_j = str(numbers[j])[idx:]
#                 temp_jm1 = str(numbers[j-1])[idx:]
#                 if temp_j[0]< temp_jm1[0]: #앞자리 수 첫 자리가 더 클경우
#                     break 
#                 elif temp_j[0] > temp_jm1[0]: #뒥자리수 첫자리가 더 클 경우 
#                     numbers[j], numbers[j-1] = numbers[j-1], numbers[j] #스와프
#                 elif temp_j[0]==temp_jm1[0]:
#                     idx+=1
#                     inner_sort([numbers[j], numbers[j-1]], idx)
#                 else:
#                     break
#     return numbers[j-1], numbers[j]
##########----------------------------------################
# def innersort(a, b, idx = 1 ): # 들어오는 첫째 수와 둘째 수에 대해서
#     #(이 둘은 첫째 자리가 동일함)
#     if len(str(b)) > len(str(a)):
#         if str(a) < str(b)[idx]:
#             return b , a
#         if str(a) > str(b)[idx]:
#             return a, b
#         if str(a) == str(b)[idx]:
#             idx+=1
#             return innersort(a, b, idx)
#     if len(str(a)) >= len(str(b)):
#         if str(b) < str(a)[idx]:
#             return a , b
#         if str(b) > str(a)[idx]:
#             return b, a
#         if str(a) == str(b)[idx]:
#             idx+=1
#             return innersort(a, b, idx)

def innersort(a, b, idx = 1 ): # 들어오는 첫째 수와 둘째 수에 대해서
    #(이 둘은 첫째 자리가 동일함)
     
    if len(str(b)) > len(str(a)):
        if str(a)[idx-1] < str(b)[idx]:
            return True
        if str(a)[idx-1] > str(b)[idx]:
            return False
        
    if len(str(a)) >= len(str(b)):
        if str(b)[idx-1] < str(a)[idx]:
            return False
        if str(b)[idx-1] > str(a)[idx]:
            return True
        if str(a)[idx-1] == str(b)[idx]:
            idx+=1
            return innersort(a, b, idx)
    # if len(a) == len(b)

    # return innersort(a, b, idx )
def popping(pops):
    if len(pops) == 1:
        return pops
    else:
        stack = []
        final = []
        pop_sort = sorted(pops, key = lambda x: str(x)[0] , reverse = True)
        # 큰자리수 기준으로 정렬
        # idx = 0
        pops = []
        stack.append(pop_sort[0])
        for num in pop_sort[1:]:
            while len(stack) > 0 and str(stack[-1])[0] == str(num)[0] and (innersort(stack[-1], num)==True)  :
                pops.append(stack[-1])
                stack.pop()
            stack.append(num)
        stack.extend(popping(pops))
        return stack
def solution(numbers):
    
    stack = []
    final = []
    number_sort = sorted(numbers, key = lambda x: str(x)[0] , reverse = True)
    # 큰자리수 기준으로 정렬
    # idx = 0
    pops = []
    stack.append(number_sort[0])
    for num in number_sort[1:]:
        while len(stack) > 0 and stack[-1]!=num and str(stack[-1])[0] == str(num)[0] and (innersort(stack[-1], num)==True)  :
            pops.append(stack[-1])
            stack.pop()
        stack.append(num)
        if len(pops)>0:
            stack.extend(popping(pops))
            pops = []
    return "".join([str(num) for num in stack])
    # final.extend(solution(pops))



    # while idx != len(numbers):
       
    #     for i, num in enumerate(number_sort): # 정렬된 수 전체에 대해서
    #         if i == len(number_sort)-1: #만일 마지막 인덱스에 다다르게 되면
    #             pass #패스
    #         # 나머지 인덱스에 대해서
    #         elif num == number_sort[i+1]: #그 숫자가 다음 숫자랑 같은 경우에는 
    #             pass #정렬하지 않음
           
    #         elif str(num)[0] ==  str(number_sort[i+1])[0]: #첫째 자리가 같은 경우에는
    #             # 그 숫자의 자릿수마다 테스트 해서 올바른 배열을 배출 
    #             number_sort[i], number_sort[i+1] = innersort(num, number_sort[i+1])  
    #         else:
    #             pass
    #         idx +=1
    # for num in number_sort:
    #     answer+=str(num)
    # print(answer)
    # return answer
        # else :
        #     if str(num)[1]>str(num)[0]:
        #         answer+=num

# numbers =[3, 30, 34, 5, 9, 200, 21]
numbers =[3, 34300, 30001, 5,5, 9]
# numbers=[6,10,2]
# solution(numbers)

num = sorted(numbers, key = lambda x : str(x)[-1], reverse=True)
num2 = sorted(numbers, key = lambda x : int(x),reverse=True)
print(num)
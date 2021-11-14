   
number = "4177222222"
k=4



#못풀었음
# def solution(number, k):
#     real_k = k
#     k_list = list(number)
#     while real_k != 0:
#         for i, num in enumerate(k_list): 
#             if i == len(k_list)-1:
#                 k_list = k_list[:-1]
#                 real_k-=1
#                 break
#             elif num < k_list[i+1]:
#                 k_list.remove(num)
#                 real_k-=1
#                 break
            
#     return "".join(k_list)



# def solution(number, k):
#     num_list = list(number)
#     real_k = k
#     k_list = num_list.copy()
#     # while real_k != 0:
#     new = [k_list.remove(num) for i, num in enumerate(k_list) if num < k_list[i+1]] 
#     while new(len) != k:
#         new = new[:-1]
#             if i == len(k_list)-1:
#                 k_list.remove(k_list[-1])
#                 real_k-=1
#                 break
#             elif num < k_list[i+1]:
                
#                 real_k-=1
#                 break
            
#     return "".join(k_list)


# 스택으로 풀이 
def solution(number, k):
    stack = []
    number =  list(number)
    stack.append(number[0]) #첫째 항목을 넣고
    # k_list = list(number)
    for i in number[1:]: #나머지에 대해서
        while len(stack)>0 and  k > 0 and stack[-1] < i:
            #만일 스택에 값이 있거나, 더 이상 뺄수 있으며, 스택의 마지막 값이 들어올 값보다 작을 경우에
            stack.pop()
            #스택의 값을 삭제
            k-=1    
        stack.append(i)
    # k = k - (len(number) - len(stack))
    while k != 0:
        stack.pop()
        k-=1
    return "".join(stack)
solution(number,k)
                
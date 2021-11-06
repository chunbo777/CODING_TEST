   
number = "33443322"
k=4



#못풀었음
def solution(number, k):
    real_k = k
    k_list = list(number)
    while real_k != 0:
        for i, num in enumerate(k_list): 
            if i == len(k_list)-1:
                k_list = k_list[:-1]
                real_k-=1
                break
            elif num < k_list[i+1]:
                k_list.remove(num)
                real_k-=1
                break
            
    return "".join(k_list)



# def solution(number, k):
#     num_list = list(number)
#     real_k = k
#     k_list = num_list.copy()
#     # while real_k != 0:
#     new = [k_list.remove(num) for i, num in enumerate(k_list) if num < k_list[i+1]] 
#     while new(len) != k:
#         new = new[:-1]
            # if i == len(k_list)-1:
            #     k_list.remove(k_list[-1])
            #     real_k-=1
            #     break
            # elif num < k_list[i+1]:
                
            #     real_k-=1
            #     break
            
    return "".join(k_list)
solution(number,k)
                
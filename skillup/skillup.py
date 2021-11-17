# def solution(n):
#     final = []
#     for i, num in enumerate(range(2, n)):
#         temp = 2
#         final_temp = final
#         while True:
#             for k in final_temp:
#                 if num % k == 0:
#                     break        
#             # if num % temp !=0:
#             #     temp+=1
#             # else:
#             #     break
#         if num % temp == 0 and num != temp:
#             pass
#         else:
#             final.append(num)ty
#     return len(final)

# def solution1(n):
#     final = []
#     final.append(2)
#     sol = []
#     for num in range(3, n+1):
#         if final != []:
#             for k in final:
#                 if num % k == 0:
#                     sol.append(-1)
#                 else: 
#                     final.append(num)

def solution(n):


n = 10
solution1(n)
print(solution(n))
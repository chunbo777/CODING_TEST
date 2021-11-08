# def solution(people, limit):
#     for i, w in enumerate(people):
#         for k in people[i+1:]:
#             if limit - w >= k:
#                 n = w+k
#                 people.remove(w)
#                 people.remove(k)
#                 people.append(n)
#                 break
#     answer = len(people)
#     return answer

# def solution(people, limit):
#     people.sort()
#     temp =0
#     iter = 0
#     final = []
#     for i, p in enumerate(people):
#         if temp+p>limit or iter==2:
#             final.append(temp)
#             if i == len(people)-1:
#                 temp = p
#                 final.append(temp)
#                 break
#             temp = p
#             iter = 1
#         else:
#             temp+=p
#             iter+=1
        
#     return len(final)

def solution(people, limit):
    num = 0
    for i, p in enumerate(people):
        num1 = num+

people = [70, 50, 80, 50]
limit = 100
solution(people, limit)
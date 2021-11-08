# def solution(people, limit):
#     iter=1
#     while iter!=0:
#         iter=0
#         for i, w in enumerate(people):
#             for k in people[i+1:]:
#                 if limit - w >= k:
#                     n = w+k
#                     people.remove(w)
#                     people.remove(k)
#                     people.append(n)
#                     iter +=1
#                     break
                    
#     answer = len(people)
#     return answer

def solution(people, limit):
    p1 = people.sort()
    p2 = p1.reverse
    temp =0
    iter = 0
    final = []
    for i, (p, q) in enumerate(zip(p1, p2)):
        if temp+q>limit or iter==2:
            final.append(temp)
            if i == len(people)-1:
                temp = p
                final.append(temp)
                
            temp = p
            iter = 1
        else:
            temp+=q
            iter+=1
        
    return len(final)
        
            
        

people = [70, 50, 80, 50,30, 100, 60, 10, 20, 80]
limit = 100
solution(people, limit)
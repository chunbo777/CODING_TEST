import time
start= time.time()

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

# def solution(people, limit):
#     # people.sort()
#     temp =0
#     iter = 0
#     final = []
#     for i, p in enumerate(people):
#         if temp+p>limit or iter==2:
#             final.append(temp)
#             if i == len(people)-1:
#                 temp = p
#                 final.append(temp)
                
#             temp = p
#             iter = 1
#         else:
#             temp+=p
#             iter+=1
        
#     return len(final)
# def solution(people, limit):
#     final = []
#     cnt=0
#     p1 = sorted(people)
#     p2 = sorted(people, reverse=True)
#     for i in p2:
#         if cnt >=len(people):
#             break
#         if (limit - i) > 0 and (p1[0] + i) <= limit:
#             final.append(p1[0]+i)
#             cnt+=2
#             p1 = p1[1:]
#         else: #무거워서 혼자타기
#             final.append(i)
#             cnt+=1

#     return final  

from collections import deque
def solution(people, limit):
    final = deque([])
    cnt = 0
    p1 = deque(sorted(people))
    p2 = deque(sorted(people, reverse=True))    
    for i in p2:
        if cnt >= len(people):
            break
        if (limit - i) > 0 and (p1[0] + i) <= limit:
            final.append(p1[0]+i)
            cnt+=2
            p1.popleft()
        else: #무거워서 혼자타기
            final.append(i)
            cnt+=1
    return final
        
# def solution(people, limit):
#     final = []
#     final= np.array(final)
#     cnt=0
#     p1 = np.sort(np.array(people))
#     p2 = np.sort(np.array(people))[::-1]
#     for i in p2:
#         if cnt >=len(people):
#             break
#         if (limit - i) > 0 and (p1[0] + i) <= limit:
#             final = np.append(final, p1[0]+i)
#             cnt+=2
#             p1 = p1[1:]
#         else:
#             final = np.append(final, i)
#             cnt+=1

#     return len(final)     


people = [70, 50, 80, 50,30, 100, 60, 10, 20, 80,30]
limit = 100
print(solution(people, limit))
end = time.time()

print("time : ", end - start)

print("end")
#수도 코드
"""무조건 큰 애들부터 먼저 제 짝을 찾아 주는 경우를 생각하면 됨 
    피플 가운데 큰 애들 부터 시작
    만약에 작은 애들 가운데에 짝이 있으면 
    파이널 리스트에 합쳐서 어팬드
    없으면 
    따로 어팬드  
    그 작은 애는 삭제해 줘야함 혹은 리스트로 돌려야 함 
    for i in 큰 애 부터 :
        리미트 - 큰애 > 0 and 작은애[0]+ 큰애 <리미트:
        파이널.append(큰애, 작은애)
        작은애 = 작은애 [1:]     
    """

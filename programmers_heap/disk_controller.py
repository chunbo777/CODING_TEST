# import heapq

# def solution(jobs):
#     jobD ={}
#     idx = 0
#     jobs
#     for job, time in jobs:
#         jobD[job] = time-job #요청부터 종료까지 
#     # if idx == 0:
#     #     jobs += heapq.heapify(job)[0][1]
#     print(jobD)

#     heapq.heapify(jobs)
#     print(jobs)

#     for i in range(3):
#         a = heapq.heappop()
#         b = heapq.heappop()
#         c = heapq.heappop()
    
#         # 요청이 들어온 순서
#         if b[1] < c[1]: #c1의 길이가 더 길면 b1 중복
#             summ =  a[1]+ b[1]*2 +c[1] + (a[1]-b[0] + a[1] - c[0])
#         if b[1] >= c[1]: #b1의 길이가 더 길면 c1 중복 
#             summ =  a[1]+ b[1] +c[1]*2 + (a[1]-b[0] + a[1] - c[0])
    
#     print(jobs)    

import heapq
def solution(jobs):
    start = -1
    end = 0
    answer = 0
    idx = 0
    heap = []
    while len(jobs) > idx:
        for job in jobs:
            if start< job[0] <=end:
                heapq.heappush(heap, (job[1], job[0]))
        if len(heap) > 0:
            pops = heapq.heappop(heap)
            start = end
            end += pops[0]
            answer += (end-pops[1])#업무의 엔드포인트 - 해당 팝의 요청시간 
            idx += 1
        else: 
            end += 1
    answer = answer//len(jobs)

    return answer





jobs = [[0, 3], [1, 9], [2, 6],[3, 5], [4, 10]]
solution(jobs)

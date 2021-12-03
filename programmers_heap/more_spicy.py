import heapq

def solution(scoville, K):
    heap = []
    idx = 0
    while True : 
        if idx == 0 :
            for s in scoville:
                heapq.heappush(heap, s) #정렬
            if heap[0] >= K:
                return idx
        try:
            scoplus = heapq.heappop(heap) + (heapq.heappop(heap)*2)
            idx += 1
            if scoplus >= K and heap[0]>=K:
                return idx
            elif len(heap) <= 1:
                return -1
            else :
                heapq.heappush(heap, scoplus)
        except:
            return -1
            # scoville = list(heap)
            


    
    

scoville = [1,9,2, 10,10,10,10, 12]
K = 1
solution(scoville, K)
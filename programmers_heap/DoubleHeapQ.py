import heapq
"""이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 
큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요."""

def solution(operations):
    heap = []
    heap_re = []
    
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[2:]))
            heapq.heappush(heap_re, -int(operation[2:]))
        elif operation == "D -1":
            try :
                heap_re.remove(-(heapq.heappop(heap)))
            except:
                pass
        else: #D-1 
            try: 
                heap.remove(-(heapq.heappop(heap_re)))
            except:
                pass
    if len(heap) == 0:
        return [0,0]
    else:
        return [-(heapq.heappop(heap_re)), heapq.heappop(heap)]

# operations = ["I 16","D 1"]
operations = ["I 7","I 5","I -5","D -1"]
solution(operations)
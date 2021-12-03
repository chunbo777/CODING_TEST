import heapq
heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)

#최대 힙
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num)) #우선순위, 값

while heap:
  print(heapq.heappop(heap)[1])  # index 1
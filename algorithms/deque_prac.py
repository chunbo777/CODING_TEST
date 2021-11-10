# deque는 double ended queue의 줄임말
# stack과 queue를 합친 것, 양방향에서 데이터를 삽입 및 추출할 수 있는 자료형 

from collections import deque
deq1 = deque([1,2,3])
deq1.append(4)
deq1.appendleft(4)
deq1.pop()
deq1.popleft()
deq2 = deque(maxlen=4)
for i in range(6):
    deq2.append(i)
    print(deq2)
deq2.reverse()
deq2.count(2)
deq2.rotate(1)
print(deq1)


from collections import deque

# 인용 횟수가 많은 것들 부터 정렬함
# 해당 숫자와 pop 거리가 같을 때 까지 pop

def solution(citations):
    que = deque(sorted(citations))
    num = que[-1]
    pop_idx = 0
    while True:
        if que[-1] == num:
            que.pop()
            pop_idx +=1
            if pop_idx >= num:
                break
        if que[-1]!=num:
            num = que[-1]

    return num

# citations = [3,0,6,1,5]
citations = [3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,1,1,1,1,1,5,5,5,5,5]

solution(citations)


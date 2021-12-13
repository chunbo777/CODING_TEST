
"""
입국심사를 기다리는 사람 수 n, 
각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

# def solution(n, times):
#     answer = 0
#     return answer

# 이분 탐색으로 풀지 않는다면 
from collections import defaultdict

def solution(n, times):
    officiers = defaultdict(int)
    DoubleK = defaultdict(int)
    for t in times:
        officiers[t] = 0
        DoubleK[t] = 2*t
    offidx = 0
    for i in range(1, n+1):
        # 더 했을때 가장 작은 쪽이 미니멈 인덱스가 돼야함.
        if i == n :
            offidx = list(DoubleK.values()).index(min(DoubleK.values()))
        else:
            offidx = list(officiers.values()).index(min(officiers.values()))
        officiers[list(officiers.keys())[offidx]] += list(officiers.keys())[offidx]
    print(officiers)
    return max(officiers.values())


n = 6
times = [7, 10]
solution(n, times)

#return = 28


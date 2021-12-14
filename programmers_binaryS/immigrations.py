
"""
입국심사를 기다리는 사람 수 n, 
각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.
"""

""" 소요시간(=정답)의 min값과 max값을 정해두고 이 안에서 값의 범위를 좁혀가며 탐색하는 풀이다."""
# 이분 탐색으로 항상 최선의 선택을 한다면? 
def solution(n, times):
    start = 1
    end =   1000000000*n
    ans = 1
    while start <= end:
        mid = (start + end)//2 
        people = 0
        for time in times:
            people += mid//time
            if people >= n:
                break
        if people >= n:
            ans = mid
            end = mid -1
        else:
            start = mid + 1
    return ans 


# def solution(n, times):
#     answer = 0
#     return answer

# 이분 탐색으로 풀지 않는다면 
# from collections import defaultdict

# def solution(n, times):
#     officiers = defaultdict(int)
#     DoubleK = defaultdict(int)
#     for t in times:
#         officiers[t] = 0
#         DoubleK[t] = 2*t
#     offidx = 0
#     for i in range(1, n+1):
#         # 더 했을때 가장 작은 쪽이 미니멈 인덱스가 돼야함.
#         if i == n :
#             offidx = list(DoubleK.values()).index(min(DoubleK.values()))
#         else:
#             offidx = list(officiers.values()).index(min(officiers.values()))
#         officiers[list(officiers.keys())[offidx]] += list(officiers.keys())[offidx]
#     print(officiers)
#     return max(officiers.values())


n = 100
times = [7, 10, 8, 50, 3, 1]
solution(n, times)

#return = 28


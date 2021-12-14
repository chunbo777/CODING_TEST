
n, m = 4, 6
array = [19, 15, 10, 17]

#이진 탐색을 위한 시작점과 끝점 설정

#이진 탐색 수행
def solution(n, m, array):
    start = 0
    end = max(array)
    array.sort()
    while start<= end:
        mid = (start + end)//2
        if m == sum([i - mid if i > mid else 0 for i in array ]):
            return mid
        elif m > sum([i - mid if i > mid else 0 for i in array ]): # 좀 더 잘라야되는 경우
            end = mid -1
        else: #좀 덜 잘라야 되는 경우
            start = mid + 1

solution(n, m , array)

#이진 탐색 소스코드 구현 (재귀함수)
import numpy as np

def binary_search(array, target, start, end):
    if end - start <0:
        return None
    else:
        mid = (start + end)//2
   
    if array[mid] == target:
        return mid
    else:
        if array[mid] < target:
            return binary_search(array, target, mid + 1, end)
        else:
            return binary_search(array, target, start, mid - 1)

array = list(range(1,101))
target = 17
start = 0
end = 100
binary_search(array, target, start, end)

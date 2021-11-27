"""
arr의 길이 ≥ 3
arr 내 어떤 인덱스 i가 다음과 같은 조건을 모두 만족합니다.
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr의 마지막 원소
0 < i < arr의 길이 - 1

"""


def solution(arr):
    stack = []
    idx=1
    final = []
    while True: 
        stack.append(arr[idx-1])
        elm = arr[idx]
        pitch = 0
        while len(stack)>0 and stack[-1] < elm:
            stack.append(elm)
            idx += 1
            pitch = stack.index(stack[-1])
            if idx >= len(arr):
                break
            else:
                elm = arr[idx]
            
        while arr[idx-1] == elm:
            stack = []
            idx += 1
        if len(stack)>0 and stack[-1] > elm:
            while stack[-1]> elm:
                stack.append(elm)
                idx += 1
                try:
                    elm = arr[idx]
                except:
                    pass
        if len(stack) > 0:
            left =len(stack[:pitch])-1
            right = len(stack[pitch:])-2
            if left == 0 or right ==0:
                sample_length = left+right+1
            else:
                sample_length = left+right+2
            if sample_length > 0 :
                final.append(sample_length)
            stack = []
        if idx >= len(arr)-1:
            break
    return sum(final) % ((10^9)+7)
arr = [1, 2, 3, 2, 1, 4, 3, 2, 2, 1]
# arr = [0, 1, 2, 5, 3, 7]
solution(arr)
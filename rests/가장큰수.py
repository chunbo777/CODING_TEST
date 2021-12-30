"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"""
# from collections import deque 
# def solution(numbers):
#     numbers = sorted(numbers, key = lambda x: str(x)[0] , reverse = True)
#     if sum(numbers)>0:
#         stacks = deque()
#         right_que = deque()
#         idx = 0
#         while idx != len(numbers):
#             while stacks:
#                 if int(str(stacks[-1]) + str(numbers[idx])) > int(str(numbers[idx])+ str(stacks[-1])):
#                     break
#                 else:
#                     right_que.appendleft(stacks.pop())
#             stacks.append(numbers[idx])
#             stacks += right_que
#             right_que = deque([])
#             idx += 1
#         return "".join([str(s) for s in stacks])
        

        
#     else:
#         return '0'




def solution(numbers):
    numbers = sorted(numbers, key = lambda x: str(x)[0] , reverse = True)
    
    if sum(numbers) > 0 :
        for n in numbers:
            pass_idx = 0
            for i, num in enumerate(numbers):
                if i == 0 :
                    pass
                else:
                    if int(str(numbers[i-1]) + str(num)) >= int(str(num)+ str(numbers[i-1])): #현상 유지가 더 클 경우
                        pass_idx += 1
                        pass
                    else: #아닐 경우
                        numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            if pass_idx == len(numbers):
                break
        return "".join([str(n) for n in numbers])
    else:
        return "0"

#머지 솔트로 풀이

def merge_sort(numbers):
    if len(numbers) > 1:
        mid =  len(numbers)//2
        left_array  = numbers[:mid]
        right_array  = numbers[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        left_idx, right_idx, idx = 0, 0, 0
        while len(left_array) > left_idx and len(right_array) > right_idx:
            if int(str(left_array[left_idx])+ str(right_array[right_idx]))> int(str(right_array[right_idx])+str(left_array[left_idx])): #레프트인덱스가 작은 경우
                numbers[idx] =  left_array[left_idx]
                left_idx += 1
            else:
                numbers[idx] =  right_array[right_idx]
                right_idx+=1
            idx += 1
        numbers[idx:] =  left_array[left_idx:] if left_idx != len(left_array) else right_array[right_idx:]


def mergeSort(a):
    if len(a) > 1: # 배열의 길이가 1보다 클 경우 재귀함수 호출 반복
        mid = len(a)//2 # 2로 나눈 몫 (중간 값) 취함
        la, ra = a[:mid], a[mid:] # la 중간 값을 기준으로 왼쪽, ra 중간 값을 기준으로 오른쪽
        mergeSort(la) # 왼쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        mergeSort(ra) # 오른쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        li, ri, i = 0, 0, 0 # 정렬을 위한 변수 선언 (왼쪽, 오른쪽, 기준)
        while li < len(la) and ri < len(ra): # 서브 리스트의 정렬이 끝날 때까지 반복
            # if la[li] > ra[ri]: # 오른쪽 리스트의 값이 클 경우라면
            if int(str(la[li])+str(ra[ri])) > int(str(ra[ri])+str(la[li])):
                a[i] = la[li] # 왼쪽 리스트의 해당 인덱스의 값을 할당
                li += 1 # 왼쪽 리스트의 인덱스 하나 증가
            else: # 왼쪽 리스트의 값이 클 경우라면
                a[i] = ra[ri] # 오른쪽 리스트의 해당 인덱스의 값을 할당
                ri += 1 # 오른쪽 리스트의 인덱스 하나 증가
            i += 1 # 기준 인덱스 증가
        a[i:] = la[li:] if li != len(la) else ra[ri:]
      # 왼쪽 리스트의 인덱스의 값이 서브 리스트의 값과 같지 않을 경우라면(정렬 끝),
      # 왼쪽 서브 리스트의 값을 리스트에 덮어쓰기, 그렇지 않은 경우라면 오른쪽 서브 리스트의 값 할당       
numbers = [3, 30, 34, 5, 9]
# solution(numbers)
mergeSort(numbers)
print(numbers)
merge_sort(numbers)
print(numbers)

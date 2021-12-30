import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 6) # 1<= x < 10의 난수 5개 리스트로 생성
print(a) # 정렬 전 리스트
print('')
def mergeSort(a):
    if len(a) > 1: # 배열의 길이가 1보다 클 경우 재귀함수 호출 반복
        mid = len(a)//2 # 2로 나눈 몫 (중간 값) 취함
        la, ra = a[:mid], a[mid:] # la 중간 값을 기준으로 왼쪽, ra 중간 값을 기준으로 오른쪽
        mergeSort(la) # 왼쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        mergeSort(ra) # 오른쪽 서브 리스트의 값을 기준으로 병합정렬 재귀 호출
        li, ri, i = 0, 0, 0 # 정렬을 위한 변수 선언 (왼쪽, 오른쪽, 기준)
        while li < len(la) and ri < len(ra): # 서브 리스트의 정렬이 끝날 때까지 반복
            if la[li] < ra[ri]: # 오른쪽 리스트의 값이 클 경우라면
                a[i] = la[li] # 왼쪽 리스트의 해당 인덱스의 값을 할당
                li += 1 # 왼쪽 리스트의 인덱스 하나 증가
            else: # 왼쪽 리스트의 값이 클 경우라면
                a[i] = ra[ri] # 오른쪽 리스트의 해당 인덱스의 값을 할당
                ri += 1 # 오른쪽 리스트의 인덱스 하나 증가
            i += 1 # 기준 인덱스 증가
        a[i:] = la[li:] if li != len(la) else ra[ri:]
      # 왼쪽 리스트의 인덱스의 값이 서브 리스트의 값과 같지 않을 경우라면(정렬 끝),
      # 왼쪽 서브 리스트의 값을 리스트에 덮어쓰기, 그렇지 않은 경우라면 오른쪽 서브 리스트의 값 할당                                   
mergeSort(a)
print('')
print(a) # 정렬 후 리스트


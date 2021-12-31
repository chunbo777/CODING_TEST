"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

<<제한사항>>

컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.

입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""
# def find(setD, i, j, idx = 0):
#     if idx == 0 :
#         setD[idx] = {i, j}
#         idx += 1
    


# def solution(n, computers):
#     setD = dict()
#     for i, computer in enumerate(computers):
#         for j in range(0,n):
#             if computers[i][j] == 1 and i!=j:
#                 find(setD, i, j)

def dfs(i, computers, prev_i = None):
    if prev_i == None:
        for j in range(0, len(computers)):
            if i!=j and computers[i][j] == 1:
                dfs(j, computers, prev_i= i)
    else:
        for j in range(0, len(computers)):
            if i!=j and computers[i][j] == 1 and computers[prev_i][j] != 1:
                computers[prev_i][j] = 1
                computers[j][prev_i] = 1

def mapping(x, y, computers, visit, n):
    if x<0 or x>= n or y < 0 or y >=n:
        return
    if (computers[x][y] == 0)  or visit[x][y]:
        return 
    else:
        visit[x][y] = True
        mapping(x+1, y, computers, visit, n)
        mapping(x-1, y, computers, visit, n)
        mapping(x, y+1, computers, visit, n)
        mapping(x, y-1, computers, visit, n)
    
    return True

def solution(n, computers):
    total = 0
    visit = [[False]*n]*n
    for i in range(0, n):
        dfs(i, computers)
    for i in range(0, n):
        for j in range(0, n):
            if mapping(i,j,computers, visit, n) == True:
                total += 1
    return total
        


#     return

n = 4
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
#return 2

solution(n, computers)
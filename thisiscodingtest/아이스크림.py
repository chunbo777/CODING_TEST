import numpy as np
def solution(N, M, frame):
    """1)특정한 지점의 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
        2) 방문하지 않은 지점의 수를 센다? """
    """수도코드 
        0) 모든 맵의 visit맵을 만들기
        1) 초기 좌표 설정, 방문 설정
        2) 초기 좌표에서 상하좌우 확인 
        3) 만약 방문하지 않은 지점이 있으면 거기로가서 상하좌우 확안(DFS) - > 방문찍기
        4) 최종적으로 방문하지 않은 지점을 확인"""
    visited = np.zeros_like(np.asarray(frame), dtype=int)
    def dfs(i, j, frame, visited):  
        if 0 > i or i >= N or 0 > j or j >= M or frame[i][j]==1:
            return False
    
        if frame[i][j]==0 and visited[i][j] != 1: #그 지점이 0이면서 아직 방문하지 않은 지점이 있다면
            visited[i][j] = 1 # 그 지점을 방문
            frame[i][j] = 1
        else:
            return
        dfs(i+1, j, frame, visited) # 아래로 내려감
        dfs(i, j+1, frame, visited) # 우측
        dfs(i-1, j, frame, visited) # 위로 올라감
        dfs(i, j-1, frame, visited) # 좌측 
        return True
    cnt = 0
    for i in range(0, N):
        for j in range(0, M):
            if dfs(i,j, frame, visited) == True:
                cnt +=1 

    return cnt



N = 4
M = 5
frame = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]
solution(N, M, frame)
def solution(n, computers):  
    def zero(array):
        zeros = []
        for i in array:
            z1 = []
            for j in i:
                z1.append(0)
            zeros.append(z1)
        return zeros
    stack = []
    visit = zero(computers)

    def bfs(computers, start_i,start_j, stack, visit):
        while start_j <= n or start_i<= n :
            while computers[start_i][start_j] != 1: #우측으로만 이동 0의 짝을 찾아서~
                start_j += 1
                if start_j == n: # 끝에 도달하게 되면
                    start_j = 0 #좌우값은 초기화
                    start_i += 1 #행 값을 업뎃
                if start_i == n: # 끝에 도달하기 까지 짝이 없다면
                    return False  #리턴 팔스
            if start_i == start_j:
                visit[start_i][start_j] = 1
                start_j+=1
                pass
            else:
                
                stack.append(start_i)
                stack.append(start_j)
                while stack:
                    v1 = stack.pop()
                    v2 = stack.pop()
                    for i, k in enumerate(computers[v1]): #0과 만난 열의 그 행에 대해서
                        if k == 1 and visit[v2][i] == 0:
                            computers[v2][i]= 1
                            visit[v2][i] =1
                            stack.append(v2)
                            stack.append(i)
                        else:
                            pass
                start_j += 1
    bfs(computers, 0, 0, stack, visit)

        


n = 3	
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
#return =  2 
solution(n, computers)
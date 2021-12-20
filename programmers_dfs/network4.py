def solution(n, computers):
    def zero(array):
        zeros = []
        for i in array:
            z1 = []
            for j in i:
                z1.append(0)
            zeros.append(z1)
        return zeros
    x,y = 0,0
    stack = []
    visit = zero(computers)
    visiting= zero(computers)   
    idx = 0
    def bfs(x, y):
        nonlocal idx
        if idx > 0:
            if stack == []:
                return
            v, x = stack.pop()
            if visit[v][x] == 0:
                 #이전에 연결된 접점 
                visit[v][x] = 1
                # visit[x][v] = 1
            else:
                return
        for i, k in enumerate(computers[x]):
            if computers[x][i] == 1 and visit[x][i] == False:
                if x == i:
                    visit[x][i]= 1
                else:
                    if idx > 0:  #2회차부터는
                        if computers[x][i] == 1:
                            if v!=i and visit[v][i] == False:
                                # computers[v][i] ,computers[i][v] = 1, 1
                                computers[v][i] = 1
                                stack.append((v,i))
                            # visit[x][k], visit[k][x], visit[v][k], visit[k][v] = 1
                    else:
                        stack.append((x,i))
                        # visit[x][k], visit[k][x] = 1
           
        idx += 1
     
    def dfs(x, y):
        if x>n-1 or y > n-1 or x<0 or y<0:
            return
        if visiting[x][y] == 0:
            if computers[x][y] == 1:
                visiting[x][y] = 1
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
                return False
            else:
                # visiting[x][y] = 1
                return 
        else:
            return

    for i in range(n):
        for y in range(n):
            bfs(i, y)
            while stack:
                bfs(x, y)
    result = 0
    for x in range(n):
        for y in range(n):
            if dfs(x, y) == False:
                result += 1
    return result
    



       


n = 3
# computers = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1,0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#return =  2 
solution(n, computers)
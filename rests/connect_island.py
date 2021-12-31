"""n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 
모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 
예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 
또한 순서가 바뀌더라도 같은 연결로 봅니다.
즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.

입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
입출력 예 설명

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다"""


def find(D, element):
    idx = 0
    for key, value in D.items():
        if element in value and idx == 0 :
            key_set =  key
            idx += 1
        elif element in value:
            D[key_set] =  D[key_set].union(D[key])
            del D[key]
        else:
            pass       
    
    return key_set

def find2(D, start, end): #사이클 찾기
    for key, value in D.items():
        if start in value and end in value :
            return True
        else:
            pass
    return False

def union_sets(setD, start, end):
    start_keyset = find(setD, start)
    end_keyset =  find(setD, end)
    setD[start_keyset] =  setD[start_keyset].union(setD[end_keyset])
    del setD[end_keyset]
    
def solution(n, costs):
    costs =  sorted(costs, key = lambda x : x[2])
    island_map = [False] * n
    setD = dict()
    idx = 0
    total = 0
    for start, end, cost in costs:
        if not island_map[start] and not island_map[end]:
            # 둘다 방문이력이 없는 경우 => 새로운 셋 생성
            island_map[start] = True
            island_map[end] = True
            setD[idx] =  set({start, end})
            total += cost
            idx += 1
        elif island_map[start] and not island_map[end]: 
            #start는 방문 이력이 있는데 end는 없는 경우
            key_set = find(setD, start)
            start_end_Set = {start, end}
            setD[key_set] = setD[key_set].union(start_end_Set)
            total += cost
            island_map[end] = True
        elif not island_map[start] and island_map[end]: #반대
            
            key_set = find(setD, end)
            start_end_Set = {start, end}
            setD[key_set] = setD[key_set].union(start_end_Set)
            total += cost
            island_map[start] = True
        else:
            #둘다 방문이력이 있을 경우 
            if find2(setD, start, end):  # 사이클을 형성하는 경우
                continue
            else:     # 사이클이 아니라 서로 다른 셋에 있던 것이 연결되는 경우
                union_sets(setD, start, end)
                total += cost
        if max(map(len, setD.values())) == n:
            break
    return total

n = 5
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
costs = [[2,3,8],[0,2,2],[1,2,5],[1,3,1],[0,1,1], [0,4,7]]
costs = [[0,1,1], [0,2,4], [2,3,1],[3,4,1],[2,4,1]]
solution(n, costs)

#return 4
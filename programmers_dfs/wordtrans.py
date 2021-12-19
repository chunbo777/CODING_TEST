"""두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", 
words가 ["hot","dot","dog","lot","log","cog"]라면 
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요."""

"""
제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
"""

"""
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
"""

def solution(begin, target, words):
    if target not in words:
        return 0
    cnt =  0
    k = 0
    def find(begin, cnt, results = []):
        nonlocal k
        try:
            words_visited[words.index(begin)] = True
            cnt += 1
        except:
            pass
        if begin == target:
            k += 1
            return results, cnt
    
        split_begin = list(begin)
        for word in words:
            neg_cnt = 0
            for i, w in enumerate(split_begin):
                if word[i] !=  w:
                    neg_cnt +=1
                if neg_cnt > 1 :
                    break
                # 딱 하나가 차이나는데 마침 걔가 타겟이면 바로 리턴
        
                
            if neg_cnt == 1 and words_visited[words.index(word)] == False : #하나만 다른 경우
                
                results.append(word)
        
        return results, cnt                    
    
    if target not in words:
        return 0
    else:
        cnts = []
        results, cnt = find(begin, cnt)
        while results:
            # for result in results:

            results, cnt = find(results.pop(), cnt)
            if k == 1: # 타겟을 만났으면
                cnts.append(cnt)
                k = 0
                
        if results == [] and cnts == []:
            return 0

            # begin = find(begin)

    return min(cnts)        

begin = "hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log"]
words_visited = [False]*len(words)
solution(begin, target, words)
           
        #하나를 바꿔서 갈 수 있는 단어로 만들기

def solution(people, limit):
    
    for i, w in enumerate(people):
        for k in people[i+1:]:
            if limit - w >= k:
                n = w+k
                people.remove(w)
                people.remove(k)
                people.append(n)
                break
    answer = len(people)
    return answer

people = [70, 50, 80, 50]
limit = 100
solution(people, limit)
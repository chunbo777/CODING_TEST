from collections import Counter

def solution(clothes):
    TD =  dict(Counter([x for _, x in clothes]))
    ans = 1
    for value in list(TD.values()):
        ans = ans * (value+1)
        return ans -1

        






clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
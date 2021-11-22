from collections import Counter

def solution(clothes):
    TD =  dict(Counter([x for _, x in clothes]))
    ans = 1
    for value in list(TD.values()):
        ans = ans * (value+1)
        return ans - 1
    # values = []
    # for key, value in TD.items:
    #     values.append(values)
    
    # for cloth, classes in clothes:
    #     D[cloth] = classes 
        
    # setting = []
    # # for k, i in enumerate(clothes):
    # #     while True:
    # D = {}
    # for cloth, classes in clothes:
    #     if D[classes] == None:
    #         D[classes] = cloth
    #     else:

    #         D[classes] = cloth

        






clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
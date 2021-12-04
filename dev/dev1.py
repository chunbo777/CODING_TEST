import numpy as np

def solution(drum):
    drum = [list(d) for d in drum]
    posit = len(drum[0])
    k =0
    for p in range(posit):
        y = 0
        start = drum[y][p]
        star = 0
        while True:
            start, drum, y, p, star = direction(start, drum, y, p, star)
            if start == False:
                k +=1
                break
            if start == "a":
                break
    return k

def direction(start, drum, y, p, star = 0):
    try: 
        if start == "#":
            start = drum[y+1][p] #한 칸 내려가기
            y = y+1
        elif start == ">":
            start = drum[y][p+1]
            p = p+1
        elif start == "<":
            start = drum[y][p-1]
            p = p-1
        elif start == "*":
            start = drum[y+1][p]
            star += 1
            y += 1
            if star > 1 :
                return "a",drum,"c","d","e"
        
        return start, drum, y, p, star
    except:
        return False, drum, False, False, False

drum = ["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
print(solution(drum))
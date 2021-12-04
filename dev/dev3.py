
def solution(s):
    stack = []
    complexit = []
    s = list(s)
    for i in s:
        if len(stack) > 0:
            x = keyD[stack[-1]][0] - keyD[i][0]
            y = keyD[stack[-1]][1] - keyD[i][1]
            comp = abs(x) + abs(y)
            complexit.append(int(comp))
        stack.append(i)
    
    return comp1(complexit)

def comp1(complexit):
    comsum = 0
    for c in range(len(complexit)):
        for f in range(len(complexit)):
            try: 
                comsum += sum(complexit[f:c])
            except:
                pass
    return comsum

s = "tooth"
keyboard = ["qwertyuio","pasdfghjk", "lzxcvbnm0"]
key_list = [list(i) for i in keyboard]
keyD ={}
for i, key in enumerate(key_list):
    for j, k in enumerate(key):
        keyD[k] = [j,i]

solution(s)

print(keyD)

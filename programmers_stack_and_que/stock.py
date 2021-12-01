from collections import deque
# def solution(prices):
    # stack = []
    # i = 0
    # final = [] 
    # while prices[i]> prices[i+1]: 
    #     stack.append(prices[i])
    #     i += 1
    #     if i == len(prices)-1:
    #         break
    
    # while prices[i]==prices[i+1]:
    #     stack.append(0)
    #     i += 1
    #     if i == len(prices)-1:
    #         break
    # while prices[i]<prices[i+1]:
    #     stack.append(prices[i])
    #     i+=1
    #     if i == len(prices)-1:
    #         break
    # final.append([prices[i]- s for s in stack])
def solution(prices):
    final = []
    for i, price in enumerate(prices):
        idx = i
        stack= deque()
        while True:
            try:
                stack.append(prices[idx+1])
                if prices[idx+1] < price:
                    break
                idx+=1
            except:
                if i == len(prices)-1: #마지막 항목인 경우
                    stack.append(0)
                    break
                else: #끝까지 안떨어지는 경우
                    stack = prices[i+1:]
                    break

        final.append(len(stack)+1)

prices = [1,2,3,2,3]
solution(prices)


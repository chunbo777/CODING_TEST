from itertools import permutations

def solution(numbers):
    perm = []
    primes = []
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        perm.extend([int("".join(i)) for i in list(permutations(numbers, i))])
        perm = sorted(list(set(perm)))
    for k in perm:
        if is_prime_number(k) == True and(k not in [0,1]):
            primes.append(k)
        # k_idx =13
        # if k not in [0, 1] :
        #     if k in [2 ,3, 5, 7, 11]:
        #         primes.append(k)
                
        #     else:
        #         if (k%2==0) or (k%3==0) or (k%5==0) or (k%7==0) or (k%11==0) or (k%13)==0 :
        #             pass
        #         else:
        #             while True:
        #                 if k%k_idx==0 and k!=k_idx:
        #                     break
        #                 elif k%k_idx ==0 and k==k_idx:
        #                     primes.append(k)
        #                     break
        #                 else:
        #                     k_idx += 2
    return len(primes)


import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
                        

            
                





            

    
    print(perm)


numbers = "0134092"
solution(numbers)

def solution(brown, yellow):
    for x in range(3, brown+yellow):
       y = (brown + yellow)/ x
       if (brown + yellow)%x ==0 and (x-2)*(y-2) == yellow and y > x:
           return int(y), int(x)





brown = 10	
yellow = 2	
solution(brown, yellow)
#return = [4, 3]

"""Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요."""

#8	1	[3, 3]
#24	24	[8, 6]

#규칙 1 : x*y = brown + yellow 
#규칙 2 : (x-2)*(y-2) = yellow
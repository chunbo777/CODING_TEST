def solution(a, b):
    day = ['FRI','SAT','SUN', 'MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    k = (sum(month[:a-1]) +b) % 7
    return day[k-1]
    
    

a = 1
b = 7
solution(a,b)

def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["THU",'FRI','SAT','SUN',"MON","TUE","WED"]
    num = b
    
    for i in range(a):
        num += month[i]
    
    answer = day[num%7]
    
    return answer
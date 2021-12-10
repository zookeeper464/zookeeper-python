def solution(price, money, count):
    total = price*(count*(count+1)//2)
    remain = total - money
    answer =  max(0,remain)
    
    return answer
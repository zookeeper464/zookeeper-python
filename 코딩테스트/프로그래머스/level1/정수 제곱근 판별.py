def solution(n):
    from math import ceil
    
    answer = -1
    temp = ceil(n**(1/2))
    if temp*temp == n:
        answer = (temp+1)**2
    
    return answer
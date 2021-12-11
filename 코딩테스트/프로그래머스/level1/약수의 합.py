from math import ceil

def solution(n):
    answer = 0
    m = ceil(n**(1/2))
    if m**2 == n: answer += m
        
    for i in range(1,m):
        if n%i == 0:
            answer += i+n//i
    
    return answer
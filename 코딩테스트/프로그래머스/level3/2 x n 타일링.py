def solution(n):
    a,b = 1,2
    for i in range(n-2):
        a,b = b, (a+b)%1000000007    
    answer = b
    return answer
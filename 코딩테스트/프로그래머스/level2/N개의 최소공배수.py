def solution(arr):
    from math import gcd
    
    answer = 1
    for i in arr: answer = answer*i//gcd(answer,i)
        
    return answer
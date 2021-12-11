def solution(n, m):
    from math import gcd
    
    x = gcd(n,m)
    answer = [x, n*m//x]
    return answer
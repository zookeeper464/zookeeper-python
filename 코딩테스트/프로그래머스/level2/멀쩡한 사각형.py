def solution (w,h):
    from math import gcd
    
    answer = w*h -w -h + gcd(w,h)
    return answer
def solution(p):
    def make(st):
        a,s = 0, True
        
        for i in range(len(st)):
            if st[i] == '(': a += 1
            else: a -= 1

            if a<0: s = False
            if a == 0: return st[:i+1], st[i+1:],s

    if not p: return ""

    u,v,switch = make(p)
    
    if switch: return u + solution(v)
        
    answer = '('+solution(v)+')'
    
    l = len(u)
    for p in range(1,l-1):
        if u[p] == '(': answer += ')'
        else: answer += '('
    
    return answer
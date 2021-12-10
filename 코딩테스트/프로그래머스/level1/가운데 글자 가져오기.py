def solution(s):
    l = len(s)
    if l%2: answer = s[l//2]
    else: answer = s[l//2-1:l//2+1]
        
    return answer
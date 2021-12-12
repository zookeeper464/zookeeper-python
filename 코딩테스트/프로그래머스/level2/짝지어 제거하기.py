def solution(s):
    lst = []
    for i in range(len(s)):
        if lst and lst[-1] == s[i]: lst.pop()
        else: lst.append(s[i])
            
    if lst: answer = 0
    else: answer = 1
        
    return answer
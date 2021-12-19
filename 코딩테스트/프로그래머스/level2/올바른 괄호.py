def solution(s):
    stack = 0
    for i in s:
        if i == '(': stack += 1; continue
        stack -= 1
        if stack < 0: return False
    
    if stack == 0: return True
    return False
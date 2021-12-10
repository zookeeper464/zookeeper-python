def solution(s):
    answer = 0
    for i in s:
        if i in 'pP': answer += 1
        elif i in 'yY': answer -= 1
            
    if answer: return False
    else: return True
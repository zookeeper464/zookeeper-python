def solution(s):
    if len(s) not in (4,6): return False
    for i in s:
        if 48<=ord(i)<58: continue
        return False
    
    return True
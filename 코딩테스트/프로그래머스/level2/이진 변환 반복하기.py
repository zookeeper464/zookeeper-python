def solution(s):
    answer = [0,0]
    while len(s) != 1:
        answer[0] += 1
        ns = 0
        for i in s:
            if i == '0': answer[1] += 1
            else: ns += 1
        
        s = bin(ns)[2:]
        
    return answer
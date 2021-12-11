def solution(n):
    s = str(n)
    answer = [int(s[i]) for i in range(len(s)-1,-1,-1)]
    return answer
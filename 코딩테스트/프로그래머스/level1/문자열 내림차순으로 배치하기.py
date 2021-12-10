def solution(s):
    answer = ''.join(sorted(list(s), key = lambda x : -ord(x)))
    return answer
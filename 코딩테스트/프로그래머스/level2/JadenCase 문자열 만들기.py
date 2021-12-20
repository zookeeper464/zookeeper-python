def solution(s):
    s = s.lower()
    answer = ' '.join([i.capitalize() for i in s.split(' ')])
    return answer
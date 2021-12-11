def solution(x):
    y = sum([int(i) for i in str(x)])
    answer = False if x%y else True
    return answer
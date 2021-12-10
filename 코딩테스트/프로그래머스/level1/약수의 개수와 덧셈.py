def solution(left, right):
    s = {i**2 for i in range(33)}
    answer = 0
    for i in range(left,right+1):
        if i in s: answer -= i
        else: answer += i
    return answer
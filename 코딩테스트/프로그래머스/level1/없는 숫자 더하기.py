def solution(numbers):
    s = set(range(10))-set(numbers)
    answer = sum(s)
    return answer
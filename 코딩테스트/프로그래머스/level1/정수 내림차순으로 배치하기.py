def solution(n):
    lst = sorted(list(str(n)),reverse=True)
    answer = int(''.join(lst))
    return answer
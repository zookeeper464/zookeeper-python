def solution(arr, divisor):
    answer = set()
    for i in arr:
        if i%divisor == 0: answer.add(i)
    
    if answer: answer = sorted(list(answer))
    else: answer = [-1]
    return answer
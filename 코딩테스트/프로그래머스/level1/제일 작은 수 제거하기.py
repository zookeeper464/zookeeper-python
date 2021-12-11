def solution(arr):
    m = min(arr)
    answer = []
    for i in arr:
        if i != m:
            answer.append(i)
            
    if answer == []: answer.append(-1)
        
    return answer
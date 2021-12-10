def solution(numbers):
    answer = set()
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1,n):
            answer.add(numbers[i]+numbers[j])
            
    answer = sorted(list(answer))
    return answer
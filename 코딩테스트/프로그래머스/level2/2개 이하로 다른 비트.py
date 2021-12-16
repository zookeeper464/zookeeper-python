def solution(numbers):
    answer = []
    for n in numbers:
        l = len(bin(n))-2
        if l != len(bin(n+1))-2:
            answer.append(n+(1<<l-1))
            continue
        
        if n%2 == 0:
            answer.append(n+1)
            continue
        
        for i in range(l-1):
            if n&(1<<i+1) == 0:
                answer.append(n+(1<<(i)))
                break
            
    return answer
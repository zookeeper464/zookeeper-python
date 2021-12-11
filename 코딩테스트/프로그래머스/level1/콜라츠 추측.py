def solution(num):
    answer = 0
    while num != 1:
        num = num*3+1 if num%2 else num//2
        answer += 1
        if answer >= 500:
            answer = -1
            break
    
    return answer
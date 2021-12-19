def solution(n):
    answer = 0
    temp = 1
    while temp*(temp+1)//2<=n:
        if temp%2 and n%temp==0: answer += 1
        elif temp%2==0 and n%temp == temp//2: answer += 1
        temp += 1
        
    return answer
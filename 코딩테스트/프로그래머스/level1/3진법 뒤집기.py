def solution(n):
    lst=[]
    while n:
        lst.append(n%3)
        n //= 3
        
    answer = 0
    temp = 1
    l = len(lst)
    for i in range(l-1,-1,-1):
        answer += temp*(lst.pop())
        temp *= 3
    return answer
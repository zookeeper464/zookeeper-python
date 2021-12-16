def solution(brown, yellow):
    total,line = brown+yellow,brown//2+2
    for i in range(1,line//2+1):
        if i*(line-i) == total: answer = [line-i,i]
    
    return answer
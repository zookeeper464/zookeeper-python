def solution(n):
    p_list = [1]*(n+1)
    p_list[0],p_list[1] = 0,0
    for i in range(2,n):
        if p_list[i]:
            j = i*2
            while j<=n:
                p_list[j] = 0; j += i
    
    answer = sum(p_list)
    return answer
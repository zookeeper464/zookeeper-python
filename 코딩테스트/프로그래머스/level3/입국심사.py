def solution(n, times):
    answer = max(times)*n
    s = int(n//sum([1/i for i in times]))+1 # 최소 소요 시간
    e = s+max(times)
    
    while s<=e:
        m = (s+e)//2
        if n <= sum(m//x for x in times): e = m-1
        else: s = m+1
            
    answer = s
    return answer
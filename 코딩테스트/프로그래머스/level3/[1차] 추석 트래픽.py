def solution(lines):
    answer = 0
    in_dp = []
    out_dp = []
    
    for i in lines:
        _,t,d = i.split(' ')
        h,m,s = t.split(':')
        second = int(h)*3600000+int(m)*60000+int(float(s)*1000)
        d = int(float(d[:-1])*1000)
        
        out_dp.append(second+998)
        in_dp.append(second-d)
    
    in_dp.sort(reverse=True)
    out_dp.reverse()
    
    stack = 0
    while in_dp:
        if in_dp[-1]<=out_dp[-1]:
            stack += 1
            in_dp.pop()
            answer = max(stack,answer)
            
        else:
            stack -= 1
            out_dp.pop()
            
    return answer
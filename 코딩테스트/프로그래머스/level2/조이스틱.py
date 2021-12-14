def solution(name):
    lst = [min(91-ord(i),ord(i)-65) for i in name]
    l,idx = len(lst),0
    answer = 0
    
    while True:
        for i in range(l//2+2):
            if lst[(idx+i)%l]:
                idx = (idx+i)%l
                answer += lst[idx]+i
                lst[idx] = 0
                break
                
            if lst[(idx-i)%l]:
                idx = (idx-i)%l
                answer += lst[idx]+i
                lst[idx] = 0
                break
                
        if i == l//2+1:
            break
            
    return answer
def solution(number, k):
    answer = ''
    l = len(number)
    lst = list(map(int,number))
    dp = []
    for i in lst:
        if not dp or k == 0: dp.append(i); continue
        
        if dp[-1] < i:
            while k and dp and dp[-1] < i:
                dp.pop()
                k -= 1
            dp.append(i)
        
        else:
            dp.append(i)
    
    for _ in range(k):
        dp.pop()
        
    answer = ''.join(map(str,dp))
    return answer
def solution(info, query):
    def check(lst,num):
        l = len(lst)
        start,end = 0,l-1
        
        while start<=end:
            mid = (start+end)//2
            if lst[mid] >= num: start = mid+1
            else: end = mid-1
        return start
        
    
    answer = []
    dp = dict()
    dic = {'-':1,'cpp':2,"java":3,'python':5,'backend':7,'frontend':11,'junior':13,'senior':17,'chicken':19,'pizza':23}
    
    for i in info:
        a,b,c,d,num = i.split()
        a,b,c,d = dic[a],dic[b],dic[c],dic[d]
        num = int(num)
        temp = a*b*c*d
        if dp.get(temp): dp[temp].append(num)
        else: dp[temp] = [num]
    
    for key in dp:
        dp[key].sort(reverse = True)
    
    for i in query:
        a,_,b,_,c,_,d,num = i.split()
        a,b,c,d = dic[a],dic[b],dic[c],dic[d]
        num = int(num)
        temp = a*b*c*d
        cnt = 0
        
        for idx in dp:
            if idx%temp == 0:
                cnt += check(dp[idx],num)
        print()
        answer.append(cnt)
        
    return answer
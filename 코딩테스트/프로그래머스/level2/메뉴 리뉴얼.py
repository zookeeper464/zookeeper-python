def solution(orders, course):
    def dfs(idx,s):
        nonlocal l,num,string,dic
        if len(s) == num:
            if s in dic: dic[s] += 1
            else: dic[s] = 1
            return
        
        for i in range(idx,l):
            dfs(i+1,s+string[i])
    
    answer = []
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))
    orders.sort()
     
    for num in course:
        dic = dict()
        for string in orders:
            l = len(string)
            if l<num:
                continue
            elif l == num:
                if string in dic: dic[string] += 1
                else: dic[string] = 1
            else:
                dfs(0,'')
                
        if dic: m = max(dic.values())
        else: continue
        if m == 1: continue
            
        for i,v in dic.items():
            if v == m:
                answer.append(i)
                
    answer.sort()
    return answer
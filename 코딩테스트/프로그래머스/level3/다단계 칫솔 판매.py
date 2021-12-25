def solution(enroll, referral, seller, amount):
    class node:
        def __init__(self,name,parent,val=0):
            self.name = name
            self.parent = parent
            self.val = val
    
    dic = {'-' : node('-',None)}
    for name,parent in zip(enroll,referral):
        dic[name] = node(name,parent)
    
    for i,v in zip(seller,amount):
        name,val = i,v*100
        while dic[name].parent:
            temp = val//10
            if val == 0: break
            
            dic[name].val += val-temp
            val = temp
            name = dic[name].parent
    
    answer = [dic[e].val for e in enroll]
    
    return answer
def solution(files):
    def make_head(file):
        answer= ''
        for idx,i in enumerate(file):
            if (48<=ord(i)<58): break
            answer += i
        
        return idx,answer
    
    def make_number(idx,f):
        answer = ''
        for i in range(idx,min(len(f),idx+6)):
            if i == idx+5: break
                
            if (48<=ord(f[i])<58): answer += f[i]
            else: break
        
        return i, int(answer)
    
    answer,dp = [],[]
    for idx,f in enumerate(files):
        h_idx,head = make_head(f)
        n_idx,num = make_number(h_idx,f)
        tail = f[n_idx:]
        dp.append([head,num,idx])
    
    dp.sort(key = lambda x : (x[0].upper(),x[1],x[2]))
    for i in dp:
        answer.append(files[i[2]])
        
    return answer
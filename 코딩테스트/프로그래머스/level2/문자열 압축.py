def solution(s):
    l = len(s)
    answer = l
    for i in range(1,l//2+1):
        num,cnt,temp = 0,1,s[:i]
        for j in range(i,l,i):
            string = s[j:j+i]
            if temp == string:
                cnt += 1
            else:
                if cnt != 1:
                    num += len(str(cnt))+i
                else:
                    num += i
                temp = string
                cnt = 1
                
        if cnt == 1:
            num += len(string)
        else:
            num += i+len(str(cnt))
        
        if answer > num:
            answer = num
            
    return answer
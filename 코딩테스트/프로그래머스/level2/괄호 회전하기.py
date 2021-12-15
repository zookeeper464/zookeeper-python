def solution(s):
    answer = 0
    dic = {i:j for i,j in zip('({[]})',[1,2,3,-3,-2,-1])}
    stack,check,num = [],1,0
    for idx,i in enumerate(s):
        if dic[i] < 0:
            if stack and stack[-1]+dic[i] == 0:
                stack.pop()
            else:
                stack.append(dic[i])
                num = idx+1
        else:
            stack.append(dic[i])
    
    stack = []
    for i in range(-len(s)+num,num):
        if dic[s[i]] < 0:
            if stack and stack[-1]+dic[s[i]] == 0:
                stack.pop()
                if stack == []: answer += 1
            else:
                return 0
        else:
            stack.append(dic[s[i]])
            
    return answer
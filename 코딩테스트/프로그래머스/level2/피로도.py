def solution(k, dungeons):
    answer = 0
    def dfs (temp,num):
        nonlocal dungeons,answer
        for i in range(len(dungeons)):
            if i in temp or num < dungeons[i][0]:
                continue
            
            temp.append(i)
            dfs(temp,num - dungeons[i][1])
            temp.pop()
        
        answer = max(answer,len(temp))
        
    dfs([],k)
    return answer
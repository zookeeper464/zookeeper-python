def solution(N, number):
    def save(num,cnt):
        check[num] = cnt
        dp[cnt].add(num)
    answer = 0
    check = [0]*(number*N+1)
    dp = [set() for i in range(9)]

    for i in range(1,9):
        try: check[int(str(N)*i)] = i; dp[i].add(int(str(N)*i))
        except: break
    
    for i in range(2,9):
        for j in range(1,i//2+1):
            for x in dp[j]:
                for y in dp[i-j]:
                    if 0<x+y<len(check) and check[x+y]==0:
                        save(x+y,i)
                    if 0<x-y<len(check) and check[x-y]==0:
                        save(x-y,i)
                    if 0<y-x<len(check) and check[y-x]==0:
                        save(y-x,i)
                    if 0<x*y<len(check) and check[x*y]==0:
                        save(x*y,i)
                    if 0<x//y<len(check) and check[x//y]==0:
                        save(x//y,i)
                    if 0<y//x<len(check) and check[y//x]==0:
                        save(y//x,i)
                        
            if check[number]: break
                
    if check[number]: answer = check[number]
    else: answer = -1
        
    return answer
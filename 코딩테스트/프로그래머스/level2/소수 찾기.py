def solution(numbers):
    def dfs (nums):
        nonlocal l,st,dp
        if len(nums) == l:
            return
        
        for i in range(l):
            if i not in nums:
                nums.append(i)
                temp = int(''.join([numbers[i] for i in nums])) 
                if dp[temp]:
                    st.add(temp)
                dfs(nums)
                nums.pop()
    
    N = int('1'+'0'*len(numbers))
    dp = [1]*N
    dp[0],dp[1] = 0,0
    for i in range(2,N):
        if dp[i] == 0:
            continue
        
        j = i*2
        while j<N:
            dp[j] = 0; j += i
    
    l = len(numbers)
    st = set()
    dfs([])
    answer = len(st)
    return answer
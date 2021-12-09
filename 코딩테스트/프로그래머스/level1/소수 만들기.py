def solution(nums):
    answer = 0
    n = sum(nums)
    p_list = [1]*(n+1)
    p_list[0],p_list[1] = 0,0
    for i in range(2,n+1):
        if p_list[i]:
            j = 2*i
            while j<=n:
                if p_list[j]:
                    p_list[j] = 0
                j += i
    
    l = len(nums)
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                if p_list[nums[i]+nums[j]+nums[k]]:
                    answer += 1
    
    return answer
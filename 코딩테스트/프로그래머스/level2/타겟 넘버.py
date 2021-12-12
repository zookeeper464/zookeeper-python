def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx,num):
        nonlocal n,target,answer,numbers
        if idx == n:
            if target == num:
                answer += 1
            return
        
        dfs(idx+1,num+numbers[idx])
        dfs(idx+1,num-numbers[idx])
    dfs(0,0)
    return answer
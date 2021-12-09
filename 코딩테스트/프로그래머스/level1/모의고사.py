def solution(answers):
    nums = [0]*4
    answer = []
    ans2,ans3 = [1,3,4,5],[3,1,2,4,5]
    for idx,ans in enumerate(answers):
        if (idx%5)==ans-1: nums[1] += 1
        if (idx%2)==0 and ans==2: nums[2] += 1
        elif (idx%2)==1 and ans==ans2[(idx//2)%4]: nums[2] += 1
        if ans==ans3[(idx//2)%5]:nums[3] += 1
    
    m = max(nums)
    for i in range(1,4):
        if m == nums[i]:
            answer.append(i)
        
    return answer
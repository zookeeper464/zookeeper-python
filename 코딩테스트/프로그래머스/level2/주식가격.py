def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)]
    stack = []
    for idx in range(len(prices)):        
        while stack and prices[stack[-1]]>prices[idx]:
            temp =stack.pop()
            answer[temp] = idx-temp
            
        stack.append(idx)
                
    return answer
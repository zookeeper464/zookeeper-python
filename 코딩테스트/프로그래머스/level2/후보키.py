def solution(relation):
    answer_list = []
    n,m = len(relation),len(relation[0])
    
    for i in range(1, 1 << m):
        temp_set = set()
        
        for j in range(n):
            temp = ''
            
            for k in range(m):
                if i & (1 << k):
                    temp += relation[j][k]
            temp_set.add(temp)
        
        if len(temp_set) == len(relation):
            for num in answer_list:
                if (num & i) == num: break
                    
            else: answer_list.append(i)
                
    return len(answer_list)

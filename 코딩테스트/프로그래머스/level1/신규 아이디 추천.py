def solution(new_id):
    answer = []
    temp ='.'
    for i in range(len(new_id)):
        num = ord(new_id[i])
        if temp=='.' and new_id[i]=='.':
            continue
            
        elif 64<num<91:
            num += 32
            temp = chr(num)
            answer.append(temp)
            
        elif num not in (96,47) and (94<num<123 or 44<num<58):
            temp = chr(num)
            answer.append(temp)
    
    answer = answer[:15]
    if answer == []:
        answer.append('a')
        
    while answer[-1] =='.':
        answer.pop()
    
        
    while len(answer)<3:
        answer.append(answer[-1])
        
    answer = ''.join(answer)
    return answer
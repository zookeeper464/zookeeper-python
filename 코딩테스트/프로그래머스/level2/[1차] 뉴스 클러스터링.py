def solution(str1, str2):
    answer = 65536
    dic = dict()
    for i in range(len(str1)-1):
        temp = str1[i:i+2].lower()
        if not (96<ord(temp[0])<123 and 96<ord(temp[1])<123):
            continue
            
        if temp in dic: dic[temp][0] += 1
        else: dic[temp] = [1,0]
    
    for i in range(len(str2)-1):
        temp = str2[i:i+2].lower()
        if not (96<ord(temp[0])<123 and 96<ord(temp[1])<123):
            continue
            
        if temp in dic: dic[temp][1] += 1
        else: dic[temp] = [0,1]
    
    num1,num2 = 0,0
    for i in dic:
        if dic[i][0] and dic[i][1]: num1 += min(dic[i])
        if dic[i][0] or dic[i][1]: num2 += max(dic[i])
    
    if num2:
        answer = (answer*num1)//num2
        
    return answer
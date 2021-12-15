def solution(clothes):
    answer = 1
    
    dic = {i:1 for _,i in clothes}
    for j,i in clothes: dic[i] += 1
    for i in dic: answer *= dic[i]
        
    answer -= 1
    return answer
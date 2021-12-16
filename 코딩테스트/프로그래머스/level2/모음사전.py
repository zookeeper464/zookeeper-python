def solution(word):
    answer = 0
    dic = {i:j for j,i in enumerate('AEIOU')}
    
    for i, n in enumerate(word):
        answer += ((5**(5-i) -1)/(5 -1) *dic[n]) +1
        
    return answer
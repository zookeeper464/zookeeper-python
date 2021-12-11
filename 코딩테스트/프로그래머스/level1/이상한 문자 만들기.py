def solution(s):
    answer = []
    lst = s.split(' ')
    for l in lst:
        temp = []
        for idx,x in enumerate(l):
            temp.append(x.lower() if idx%2 else x.upper())
        
        word = ''.join(temp)
        answer.append(word)
        
    answer = ' '.join(answer)
    return answer
def solution(participant, completion):
    s = list(set(participant)-set(completion))
    if s:
        return s[0]
    
    dic = {i:0 for i in participant}
    for i in participant:
        dic[i] += 1
    for i in completion:
        dic[i] -= 1
    for i in dic:
        if dic[i]:
            return i
    
    return None
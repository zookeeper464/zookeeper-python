def solution(skill, skill_trees):
    answer=0
    dic = {chr(i):-1 for i in range(65,91)}
    for idx,s in enumerate(skill):
        dic[s] =idx
    
    for s in skill_trees:
        temp = 0
        for i in s:
            if dic[i] < temp: pass
            elif dic[i] == temp: temp += 1
            else: break
        else: answer += 1
    return answer
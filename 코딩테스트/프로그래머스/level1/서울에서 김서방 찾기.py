def solution(seoul):
    for idx,i in enumerate(seoul):
        if i == 'Kim': break 
    answer = f'김서방은 {idx}에 있다'
    return answer
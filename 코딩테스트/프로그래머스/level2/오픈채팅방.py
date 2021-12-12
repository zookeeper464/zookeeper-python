def solution(record):
    answer = []
    dp = []
    dic = dict()
    for i in record:
        ll = i.split()
        if len(ll) != 3:
            dp.append([1,ll[-1]])
            continue
        
        io,uid,name = ll
        if io == 'Change': dic[uid] = name
        else:
            dic[uid] = name
            dp.append([0,uid])
    
    for io,uid in dp:
        if io: answer.append(f'{dic[uid]}님이 나갔습니다.')
        else: answer.append(f'{dic[uid]}님이 들어왔습니다.')
    return answer
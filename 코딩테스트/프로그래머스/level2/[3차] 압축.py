def solution(msg):
    answer = []
    dic = {chr(64+i):i for i in range(1,27)}
    temp,cnt = msg[0],27
    for i in range(1,len(msg)):
        if temp+msg[i] in dic: temp += msg[i]; continue
        dic[temp+msg[i]] = cnt; cnt += 1;answer.append(dic[temp])
        temp = msg[i];
    answer.append(dic[temp])
    return answer
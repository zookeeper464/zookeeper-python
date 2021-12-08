def solution(s):
    dic = {'zero':'0','one':'1','two':'2',
    'three':'3','four':'4','five':'5','six':'6',
    'seven':'7','eight':'8','nine':'9'}

    answer = ''
    temp = ''
    for i in s:
        if ord(i)>95:
            temp += i
            if dic.get(temp):
                answer += dic[temp]
                temp = ''
        else:
            answer += i
    return int(answer)
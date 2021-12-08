def solution(lottos, win_nums):
    cnt = min(5,lottos.count(0))
    num = 6-max(0,len(set(lottos)&set(win_nums))-1)
    answer = [num-cnt,num]
    return answer
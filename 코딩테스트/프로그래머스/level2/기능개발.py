def solution(progresses, speeds):
    from math import ceil
    days = [-1]
    answer = []
    for i in range(len(speeds)):
        day = ceil((100-progresses[i])/speeds[i])
        if days[-1] < day:
            days.append(day)
            answer.append(1)
        else:
            answer[-1] += 1
    
    return answer
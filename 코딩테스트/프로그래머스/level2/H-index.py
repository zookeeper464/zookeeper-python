def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for idx,h in enumerate(citations):
        answer = max(answer,min(idx+1,h))
    return answer
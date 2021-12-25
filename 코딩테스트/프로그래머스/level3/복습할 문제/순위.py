def solution(n, results):
    from collections import defaultdict
    
    win, lose = defaultdict(set), defaultdict(set)
    for a,b in results:
            lose[b].add(a)
            win[a].add(b)

    for i in range(1,n+1):
        for winner in lose[i]:
            win[winner].update(win[i])
            
        for loser in win[i]:
            lose[loser].update(lose[i])

    answer = 0
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer += 1
            
    return answer
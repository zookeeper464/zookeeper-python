from collections import deque
import sys
input = sys.stdin.readline

def solution(lst):
    N = lst.popleft()
    lst.append(0); lst.appendleft(0)
    lst = list(lst)
    check,square = [0], 0
    
    for i in range(1, N+2):
        while (lst[check[-1]] > lst[i]):
            # check[-1]에 대한 높이가 현재 높이보다 높을 때만 들어와서 판단한다.
            # 즉 h보다 작은 막대가 들어올 경우 이전까지 쌓인 막대들로 구성하여 계산
            # check 이 빈 리스트가 되지 않는 이유는 높이가 0인 막대가 들어오지 않기 때문
            h = check.pop()
            square = max(square,(i-1-check[-1])*lst[h])
            # h에 대하여 i~check[-1]까지 길이 곱 비교
            
        check.append(i)

    answer.append(square)
    return

answer = []
while True:
    lst = deque(map(int,input().split()))
    if (lst[0] == 0): break
    solution(lst)

print(*answer,sep='\n')
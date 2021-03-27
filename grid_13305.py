n = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
#모든 입력값 입력

answer = 0
need_dist = 0
oil_cost = cost[0]
#계산에 필요한 변수 설정

for i in range(n-1):
  need_dist += distance[i]
  
  if oil_cost > cost[i+1] or i == n-2:
    answer += oil_cost * need_dist
    need_dist = 0
    oil_cost = cost[i+1]
  #비용이 더 저렴해 지는 지역이 나오면 이전까지 거리와 기름 가격을 곱한 뒤 새롭게 거리를 측정, 오일가격 설정한다.

print(answer)

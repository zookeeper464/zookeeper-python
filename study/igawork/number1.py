# number 1

# 테스트 횟수 : c
c = int(input())
# 시간을 저장하는 리스트 : answer
answer = []

for _ in range(c):
  # 아이들의 수 : n, 놀이기구의 수 : m
  n,m = map(int,input().split())
  # 놀이기구의 소요시간 t
  t = list(map(int,input().split()))
  unit = sum([1/t[i] for i in range(m)])
  start = int(n/unit)
  # answer >= n/unit임을 이용한다.
  end = start*2

  # 이분탐색 알고리즘을 활용한다.
  while start <= end:
    mid = (start + end) // 2
    num = sum([mid//t[i] for i in range(m)])
    
    if num == n:
      end = mid - 1
    elif num < n:
      start = mid + 1
    else:
      end = mid -1
  
  # 이분 탐색을 마친 값을 answer에 추가한다.
  # 모든 놀이기구를 타야 하므로 이를 조건에 추가한다.
  max_time = max(t)
  answer.append(max(start,max_time))

# 탐색을 완료한 뒤 c의 크기에 따라 값을 세로로 출력한다.
print(*answer,sep='\n')

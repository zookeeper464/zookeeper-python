n = int(input())

answer =[]
for i in range(n):
  a, b = input().split()
  m = len(a)
  sol = "Distances:"
  for j in range(m):
    temp = (ord(b[j]) - ord(a[j]) + 26) % 26
    # 각 자리마다 순환하도록 하는 거리 계산
    
    sol += f" {str(temp)}"
  answer.append(sol)

for i in answer:
  print(i)

answer = []
n = int(input())
for i in range(n):
  a, b = map(int,input().split())
  answer.append(a+b)
for i in range(5):
  print(f"Case #{i+1}: {answer[i]}")

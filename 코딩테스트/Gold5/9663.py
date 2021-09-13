n = int(input())
row = [True]*n
right_down = [True]*(2*n-1)
left_down = [True]*(2*n-1)
answer = 0

def check (cnt):
  global answer
  if cnt == n:
    answer += 1
  
  for i in range(n):
    if row[i] and right_down[cnt-i] and left_down[i+cnt]:
      row[i] = right_down[cnt-i] = left_down[i+cnt] = False
      check (cnt+1)
      row[i] = right_down[cnt-i] = left_down[i+cnt] = True

check(0)
print(answer)

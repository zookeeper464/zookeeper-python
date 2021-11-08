P,G = int(input()), int(input())
p_list = [i for i in range(P+1)]
answer = 0

def check (num):
  n = p_list[num]
  if n == 0:
    return False
  elif n == num:
    p_list[num] -= 1
    return True
  
  temp = check(p_list[num])
  p_list[num] -= 1
  return temp

for i in range(G):
  g = int(input())
  temp = check(g)
  if temp:
    answer += 1
    continue

  break

for _ in range(i+1,G):
  g = int(input())

print(answer)

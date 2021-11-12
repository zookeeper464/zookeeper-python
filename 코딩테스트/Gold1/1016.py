from math import ceil

mi,mx = map(int,input().split())
mx += 1
answer = mx - mi
mx_p = ceil(mx**0.5)
mi_p = ceil(mi**0.5)
v_list = [1] * mx_p
p_list = []

for i in range(2,mx_p):
  if v_list[i] == 0:
    continue
  
  if i**2>=mx:
    break

  p_list.append(i**2)
  for j in range(i*2,mx_p,i):
    v_list[j] = 0

p_set = set()
for i in p_list:
  for j in range(max(1,ceil(mi/i)),mx//i+1):
    if i*j in p_set:
      continue
    
    if i*j>=mx:
      break
    
    p_set.add(i*j)
    answer -= 1

print(answer)

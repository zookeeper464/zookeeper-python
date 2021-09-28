n = int(input())
lst = sorted(list(map(int,input().split())))
save,answer, start, end = [lst[0],lst[-1]],abs(lst[0]+lst[-1]), 0,n-1

while end>start:
  temp = lst[start]+lst[end]
  if answer > abs(temp):
    save = [lst[start],lst[end]]
    answer = abs(temp)
  if temp > 0:
    end -= 1
  elif temp <0:
    start += 1
  else:
    break
  
print(*save)

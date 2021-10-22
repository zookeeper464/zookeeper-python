n = int(input())
p_list = []
check_list = [1] * (n+1)
check_list[0],check_list[1] = 0,0

for i in range(2,n+1):
  if check_list[i]:
    p_list.append(i)
    for j in range(2,(n//i)+1):
      check_list[i*j] = 0

def check():
  answer = 0
  l = len(p_list)
  if l == 0:
    return answer
  start,end = 0,1
  temp = p_list[start]

  while start<end:
    if temp<n:
      if end == l:
        break
      temp += p_list[end]
      end += 1

    else:
      if temp == n:
        answer += 1
      temp -= p_list[start]
      start += 1

  return answer

print(check())

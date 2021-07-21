n = int(input())
answer = 0
for _ in range(n):
  s = input()
  lst = [0] * 26
  temp = ""
  cnt = 1
  for i in s:
    if temp == i:
      pass
    else:
      if lst[ord(i)-97] == 0:
        lst[ord(i)-97] += 1
        temp = i
      else:
        cnt = 0
        break
  answer += cnt

print(answer)

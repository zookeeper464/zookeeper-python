s = input()
temp = s[0]
cnt = 1
for i in s:
  if temp != i:
    cnt += 1
    temp = i

cnt //= 2
print(cnt)

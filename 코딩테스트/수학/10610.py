s = input()
cnt = 0
zero = False
for i in s:
  cnt += int(i)
  if i == "0":
    zero = True

if zero and cnt%3==0:
  s = list(s)
  s.sort(reverse = True)
  print(int("".join(s)))
else:
  print(-1)

s = input()
if len(s)<2: s = "0" + s
a, b = int(s[0]), int(s[1])
count = 0
while True:
  count += 1
  a, b = b, (a+b)%10
  if s == str(a)+str(b):
    break
print(count)

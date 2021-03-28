import sys
input = sys.stdin.readline

s = input()

num1 = 0
num0 = 0

temp = s[0]
for i in s:
  if temp == i:
    pass
  else:
    if temp == "1":
      temp = "0"
      num1 += 1
    else:
      if temp == "0":
        temp ="1"
        num0 +=1

print(min(num1,num0))

s = input()

def ck (a):
  if a in "ABC":
    return 3
  elif a in "DEF":
    return 4
  elif a in "GHI":
    return 5
  elif a in "JKL":
    return 6
  elif a in "MNO":
    return 7
  elif a in "PQRS":
    return 8
  elif a in "TUV":
    return 9
  elif a in "WYXZ":
    return 10

answer = 0
for i in s:
  answer += ck(i)

print(answer)

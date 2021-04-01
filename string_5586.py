s = input()
sol1 = 0
sol2 = 0
n = len(s)
#필요한 입력값 입력

for i in range(n):
  if s[i] == "J" and i < n-2:
    if s[i+1]+s[i+2] == "OI":
      sol1 += 1
      #JOI에 해당하는 단어면 sol1에 추가
  elif s[i] == "I" and i < n-2:
    if s[i+1]+s[i+2] == "OI":
      sol2 += 1
      #IOI에 해당하는 단어면 sol2에 추가

print(sol1)
print(sol2)

n = int(input())
wlst = []
tlst = []
for _ in range(n):
  a,b=map(int,input().split())
  wlst.append(a)
  tlst.append(b)

answer = []
for i in range(n):
  temp = 1
  for j in range(n):
    if wlst[j]>wlst[i] and tlst[j]>tlst[i]:
      temp += 1
  answer.append(str(temp))

print(" ".join(answer))

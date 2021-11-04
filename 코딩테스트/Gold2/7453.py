n = int(input())
A,B,C,D = [],[],[],[]
for _ in range(n):
  a,b,c,d = map(int,input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

dic = dict()
for a in A:
  for b in B:
    if dic.get(a+b): dic[a+b] += 1
    else: dic[a+b] = 1
    
answer = 0

for c in C:
  for d in D:
    num = c+d
    if dic.get(-num):
      answer += dic[-num]

print(answer)

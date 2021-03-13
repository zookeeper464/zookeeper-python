n=input()
answer=bin(int(n[0]))
answer=answer[2:]

for i in n[1:]:
  a=bin(int(i))
  a=a[2:]
  while len(a)<3:
    a="0"+a
  answer=answer+a
print(answer)

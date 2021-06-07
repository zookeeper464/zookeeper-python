lst = [list(input()) for _ in range(5)]
nlst = [len(lst[i]) for i in range(5)]

answer = ""
m = max(nlst)
for i in range(m):
  for j in range(5):
    if i<nlst[j]:
      answer += lst[j][i]

print(answer)

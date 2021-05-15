lst = input().split("-")
answer = sum(list(map(int,lst[0].split("+"))))

for i in range(1,len(lst)):
  answer -= sum(list(map(int,lst[i].split("+"))))

print(answer)

lst1 = []
lst2 = []
#필요한 변수 입력

for i in range(10):
  lst1.append(int(input()))
for i in range(10):
  lst2.append(int(input()))
#점수 입력

lst1.sort()
lst2.sort()
#정렬

print(sum(lst1[-3:]), end = " ")
print(sum(lst2[-3:]))

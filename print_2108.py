import sys
input = sys.stdin.readline

n = int(input())

lst = []
dic = {}
for i in range(n):
  temp = int(input())
  lst.append(temp)
  if temp in dic.keys():
    dic[temp] += 1
  else:
    dic[temp] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1],x[0]))
lst.sort()

print(round(sum(lst)/len(lst)))
if n%2 == 1:
  print(lst[n//2])
else:
  print(round((lst[n//2]+lst[n//2+1])/2))
if n == 1:
  print(lst[0])
elif dic[1][1] == dic[0][1]:
  print(dic[1][0])
else:
  print(dic[0][0])
print(lst[-1]-lst[0])

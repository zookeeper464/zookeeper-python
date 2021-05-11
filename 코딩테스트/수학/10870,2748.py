lst = [0,1]
n = int(input())
for i in range(n-1):
  lst.append(lst[-1]+lst[-2])
print(lst[-1])

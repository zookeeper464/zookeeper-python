n = int(input())
f = int(input())
m = n-n%100
temp = m+f-(m-1)%f-1
print(str(temp)[-2:])

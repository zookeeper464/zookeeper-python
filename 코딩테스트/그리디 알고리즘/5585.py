lst = [500,100,50,10,5,1]
n = 1000 - int(input())
answer = 0

for i in lst:
  if n>i:
    answer += n//i
    n = n%i
    
print(answer)

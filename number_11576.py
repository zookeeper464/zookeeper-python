a, b = map(int,input().split())
n = int(input())
lst = list(map(int,input().split()))
#필요한 변수 입력

temp = 0
for i in range(n):
  temp += lst[n-i-1]*(a**i)
#a진법에 맞추어서 10진법으로 바꿔준다.

answer = []
while temp:
  answer.append(temp%b)
  temp = temp//b
#10진법에서 b진법으로 바꿔준다.

print(" ".join(list(map(str,answer[::-1]))))

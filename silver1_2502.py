d, k = map(int,input().split())
#입력 처리

lst = [1,0,0,1]
for i in range(3,d+1):
  lst[0],lst[1],lst[2],lst[3] = lst[2],lst[3],lst[0]+lst[2],lst[1]+lst[3]
  #필요한 변수 설정
  
a = 1
while True:
  temp = k-a*lst[2]
  if temp%lst[3]==0:
    b = temp//lst[3]
    break
  a += 1
  #출력하기 위한 수 찾는 알고리즘

print(a)
print(b)

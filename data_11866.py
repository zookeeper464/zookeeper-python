from collections import deque

n, k = map(int,input().split())
lst =[]
for i in range(n):
  lst.append(i+1)
q= deque(lst)
lst = []
#필요한 변수들 생성

for i in range(n):
  for i in range(k-1):
    temp = q.popleft()
    q.append(temp)
    #순서가 다른 숫자들은 뒤로 보낸다.
  temp = q.popleft()
  lst.append(str(temp))
  #순서에 맞는 숫자는 빼내어 따로 저장한다.


print("<", end = "")
print(", ".join(lst), end = "")
print(">")

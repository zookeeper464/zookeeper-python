lst = []
for i in range(8):
  lst.append([i+1,int(input())])
#필요한 변수 입력

lst.sort(key = lambda x : x[1])
answer = 0
sol = []
for i in range(3,8):
  answer += lst[i][1]
  sol.append(lst[i][0])
sol.sort()
#조건에 맞는 정렬

print(answer)
for i in sol:
  print(i, end = " ")

lst = sorted([(i+1,int(input())) for i in range(8)], key=lambda x : (x[1],x[0]))
answer, temp = [], 0

for i in range(3,8):
  answer.append(lst[i][0])
  temp += lst[i][1]

answer.sort()
print(temp)
print(*answer)

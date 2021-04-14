perfect = []
pg = []

for i in range(1,8):
  perfect.append((2**i)*(2**(i+1)-1))
  temp = []
  for j in range(i):
    temp.append(2**j)
    temp.append((2**j)*(2**(i+1)-1))
  temp.append(2**i)
  temp.sort()
  pg.append(temp)
#필요한 완전수와 그 수들의 약수를 저장

lst = []
while True:
  s = int(input())
  if s == -1:
    break
  lst.append(s)
#필요한 변수 입력

for i in lst:
  if i in perfect:
    print(f"{i} =", " + ".join(list(map(str,pg[perfect.index(i)]))))
  #완전수라면 조건에 맞게 출력
  else:
    print(f"{i} is NOT perfect.")
  #아니면 다음과 같이 출력

answer = []
#출력하고자 하는 값 저장소
i = 1
#케이스 순서
while True:
  l,p,v = map(int,input().split())
  if (l,p,v) == (0,0,0):
    break
  #입력받은 값이0,0,0이면 탈출
  turn = v//p
  remainder = min(v%p,l)
  answer.append(f"Case {i}: {turn * l + remainder}")
  #케이스에 해당하는 값 처리
  i += 1
  #케이스 순서 처리
for i in answer:
  print(i)

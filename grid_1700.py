n, k = map(int, input().split())
lst = list(map(int, input().split()))
if n >= k:
  x = False
  print(0)
else:
  x = True
  code = []
  i = 0
  while len(code) < n:
    if lst[i] not in code:
      code.append(lst[i])
    i += 1
    if i == k:
      x = False
      print(0)
      break
#코드에 콘센트를 다 꼽아도 남는다면 0 출력 아니면 다음 실행

if x:
  answer = 0
  #코드가 부족하면 실행
  for i in range(n,k):
    if lst[i] in code:
      pass
    else:
      temp = 0
      for j in range(n):
        try:
          if temp < lst[i+1:].index(code[j]):
            temp = lst[i+1:].index(code[j])
            switch = j
          else:
            pass
            #i보다 큰 인덱스 중 v에 해당하는 인덱스를 구하고 그 인덱스 중 가장 큰 인덱스를 넣는다. 콘센트 순서가 가장 늦은 j를 고른다.
        except:
          temp = -1
          switch = j
          break
          #만약 j인덱스에 해당하는 콘센트가 이후에 안나온다면 제거준비
      code[switch] = lst[i]
      #제거 준비된 자리에 새로운 콘센트 넣기
      answer += 1

  print(answer)

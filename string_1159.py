n = int(input())
lst = [0] * 26
for i in range(n):
  s = ord(input()[0])-97
  lst[s] +=1
#입력값들을 모두 입력
    
answer = ''
for i in range(26):
  if lst[i] >= 5:
    answer += chr(i+97)
#선출이 가능한 철자를 모두 출력

if answer:
  print(answer)
else:
  print("PREDAJA")
  #선출이 없다면 항복 출력

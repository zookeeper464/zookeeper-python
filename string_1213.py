s = input()
#입력해야 하는 값 입력

answer = [0] * 26
for i in s:
  answer[ord(i)-65] += 1
#문자를 숫자로 바꾸어 갯수 저장

x = True
stack = 0
for i in range(26):
  if answer[i]%2 == 0:
    pass
  else:
    stack +=1
  if stack == 2:
    x = False
    break
#펠린드롬 여부 저장

l = ""
if x:
  if stack == 0:
    for i in range(26):
      l += chr(i+65) * (answer[i]//2)
    print(l+l[::-1])
  #모든 문자가 짝수라면 사전순서에 맞게 펠린드롬 생성
  else:
    for i in range(26):
      if answer[i]%2 == 0:
        l +=chr(i+65) * (answer[i]//2)
      else:
        l += chr(i+65) * (answer[i]//2)
        k = chr(i+65)
    print(l+k+l[::-1])
  #한문자가 홀수라면 이를 한개 제외한 나머지를 사전순서에 맞게 그리고 그 문자를 가운데 넣은 펠린드롬 생성
else:
  print("I'm Sorry Hansoo")
#조건에 맞게 출력

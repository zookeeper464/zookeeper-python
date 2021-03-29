s = input()
#입력값 입력

answer = ""
for i in s:
  o = ord(i)
  if o == 32 or 47 < o < 58:
     answer += chr(o)
  #수와 빈칸은 패스
  elif 96 < o < 123:
    o = ((o +13 -97)%26 + 97)
    answer += chr(o)
  elif 64 < o < 91:
    o = ((o +13 -65)%26 + 65)
    answer += chr(o)
  #소문자와 대문자는 다음 혹은 이전 13번째 문자로 변환
  
print(answer)

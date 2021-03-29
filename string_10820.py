import sys
input = sys.stdin.readlines

words = input()
#입력값 입력

answer = []
for s in words:
  s = s.rstrip("\n")
  lst = [0,0,0,0]
  for i in s:
    o = ord(i)
    if o == 32:
      lst[3] += 1
    elif 47 < o < 58:
      lst[2] += 1
    elif 96 < o < 123:
      lst[0] += 1
    elif 64 < o < 91:
      lst[1] += 1
    #각 문자의 종류에 따른 분류
  answer.append(list(map(str,lst)))
  #lst의 숫자를 문자로 변환하여 저장

for i in answer:
  print(" ".join(i))

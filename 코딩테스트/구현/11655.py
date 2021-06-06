# 1 : 49, a : 97, A : 65
s = input()
answer = ""

for i in s:
  if ord(i) < 60:
    answer += i
  elif 60<=ord(i)<95:
    answer += chr((ord(i)-65+13)%26+65)
  elif ord(i)>95:
    answer += chr((ord(i)-97+13)%26+97)

print(answer)

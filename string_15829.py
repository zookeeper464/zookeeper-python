n = int(input())
s = input()
#입력해야 하는 값 입력

answer = 0
for i in range(n):
  answer += (ord(s[i])-96)*(31**i)
  answer %= 1234567891
# 자리에 맞는 값과 문자에 맞는 값 계산, 1234567891로 나눈 나머지로 계산

print(answer)

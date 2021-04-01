s1 = input()
s2 = input()

lst1 = [0] * 26
num1 =0
lst2 = [0] * 26
num2 = 0
clst = [0] * 26
cnum = 0
#필요한 변수 입력

for i in s1:
  lst1[ord(i) - 97] += 1
#처음 입력값에 대한 갯수 리스트 생성

for i in s2:
  lst2[ord(i) - 97] += 1
#나중 입력값에 대한 갯수 리스트 생성

for i in range(26):
  m = min(lst1[i],lst2[i])
  clst[i] = m
# 겹치는 부분에 대한 갯수 리스트 생성

num1 = sum(lst1)
num2 = sum(lst2)
cnum = sum(clst)
#갯수에 대한 변수 설정

print(num1+num2 - cnum*2)

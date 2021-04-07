n = int(input())
s = input()
lst = []
for i in range(n):
  lst.append(int(input()))
compute = []
#입력 변수 입력

for word in s:
  if word == "+":
    temp2 = compute.pop()
    temp1 = compute.pop()
    compute.append(temp1+temp2)
  #입력값이 +이면 뒤에 숫자 두개를 +처리

  elif word == "-":
    temp2 = compute.pop()
    temp1 = compute.pop()
    compute.append(temp1-temp2)
  #입력값이 -이면 뒤에 숫자 두개를 +처리

  elif word == "*":
    temp2 = compute.pop()
    temp1 = compute.pop()
    compute.append(temp1*temp2)
  #입력값이 *이면 뒤에 숫자 두개를 +처리

  elif word == "/":
    temp2 = compute.pop()
    temp1 = compute.pop()
    compute.append(temp1/temp2)
  #입력값이 /이면 뒤에 숫자 두개를 +처리

  else:
    compute.append(lst[ord(word)-65])
  #입력된 문자의 순서에 맞춰서 입력된 숫자 추가

print(format(compute[0],"0.2f"))
#소숫점 둘째 자리 까지 출력

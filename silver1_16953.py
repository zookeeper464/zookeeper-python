a,b = map(int,input().split())
#입력값 처리

cnt = 1
#출력값 설정

while b != a:
  #b를 a로 만들기 위한 반복문 설정

  cnt += 1
  #반복문 1회 반복시 카운트 증가

  if b%2==0:
    b //= 2
    #2로 나눠진다면 나누기

  else:
    b -= 1
    #홀수라면 1을 뺀다.

    if b%10 == 0:
      b //= 10
      #1을 뺀 다음 10의 배수일 경우 10으로 나눠준다.
      #이것은 조건 2에 해당한다.

    else:
      cnt = -1
      break
      #만약 조건2로 홀수를 처리하지 못한다면 cnt를 -1로 바꾸어 탈출한다.

  if b < a:
    cnt = -1
    break
    #조건에 맞추어 계속 변형하는데 a로 도착하지 못한다면 cnt를 -1로 바꾸어 탈출한다.

print(cnt)
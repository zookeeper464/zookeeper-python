n = int(input())
s = []

for i in range(n):
  s.append(list(input().strip()))
#기본 입력값 설정

a = [0 for i in range(26)]
for i in s:
  li = len(i)
  for j in range(li):
    a[ord(i[j]) - 65] += 10 ** (li - j - 1)
# 아스키 코드를 이용한 코드 정리, 자릿수를 각 아스키 코드값에 해당하는 인덱스에 넣는다.

a.sort(reverse=True)
#문자의 종류는 의미가 없고 자릿수가 중요하므로 자릿수가 큰 순서대로 정렬한다.

result, cnt = 0, 9
for i in a:
  result += cnt * i
  cnt -= 1
#정렬된 순서대로 값을 9부터 입력한다.

print(result)

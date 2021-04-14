import sys
from math import gcd

input = sys.stdin.readline

lst =[]
n = int(input())
for i in range(n):
  lst.append(int(input()))
#필요한 변수 입력

x = abs(lst[-1]-lst[0])
for i in range(1,n):
  x = gcd(x,abs(lst[i-1]-lst[i]))
#나머지 정리를 사용하여 각 수들의 차이를 가지고 최대공약수를 산출한다.

m = min(lst)
answer = []
for i in range(1,int(x**0.5)+1):
  if x%i == 0:
    answer.append(i)
    answer.append(x//i)
    #루트x까지만 계산하고 나누는 수와 짝을 이루는 수를 모두 더한다.

answer = list(set(answer)-{1})
#중복을 제거한다.

answer.sort()
#정렬

print(" ".join(map(str,answer)))

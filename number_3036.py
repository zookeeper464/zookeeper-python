import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
temp = lst[0]
lst = lst[1:]
#변수 입력

for i in lst:
  g = gcd(temp,i)
  print(f"{temp//g}/{i//g}")


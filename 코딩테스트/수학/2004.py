n , m = map(int,input().split())

def cnt (n):
  answer = 0
  while n//5!=0:
    n //= 5
    answer += n
  return answer

temp = cnt(n)-cnt(m)-cnt(n-m)
print(temp)

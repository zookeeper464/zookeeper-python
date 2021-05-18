a,b = map(int,input().split())

def ck (n):
  i = 1
  cnt = 0
  answer = 0
  while cnt+i<=n:
    answer += i**2
    cnt += i
    i += 1
  answer += (n-cnt)*i
  return answer

print(ck(b)-ck(a-1))

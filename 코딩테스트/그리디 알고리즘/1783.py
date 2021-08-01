n,m = map(int,input().split())

def check (n,m):
  if n == 1 or m == 1:
    return 1

  elif n == 2:
    return min(4,(m+1)//2)

  else:
    if m < 4:
      return m
    elif m < 7:
      return 4
    else:
      return m-2
print(check(n,m))

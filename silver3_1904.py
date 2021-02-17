N=int(input())

def num(n):
  if n==1:
    return(1)
  elif n==2:
    return(2)
  else:
    return num(n-1)+num(n-2)

print(num(N))

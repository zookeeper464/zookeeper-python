N=int(input())
input_list=[0]
for i in range(N):
  a=int(input())
  input_list.append(a)

def stair (n):
  global input_list
  if n==1 or n==0:
    return input_list[n]
  elif n==2:
    a=input_list[1]+input_list[2]
    return a
  else:
    a=max(input_list[n]+stair(n-2), input_list[n]+input_list[n-1]+stair(n-3))
    return a

print(stair(N))

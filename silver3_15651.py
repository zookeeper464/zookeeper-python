N,M = [int(x) for x in input().split(" ")]
answer = []

def route ():
  global N,M
  for i in range(1,N+1):
    answer.append(str(i))
    if (len(answer) >= M):
      print(" ".join(answer))
    else:
      route()
    answer.pop()

route()

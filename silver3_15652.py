N,M = [int(x) for x in input().split(" ")]
answer = []

def route ():
  global N,M
  if (answer): start = int(answer[-1])
  else: start = 1

  for i in range(start,N+1):
    answer.append(str(i))
    if (len(answer) == M):
      print(" ".join(answer))
    else:
      route()
    answer.pop()

route()

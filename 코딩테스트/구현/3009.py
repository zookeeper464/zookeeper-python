xlst, ylst = [], []

for _ in range(3):
  x, y = map(int,input().split())
  if x in xlst:
    xlst.remove(x)
  else:
    xlst.append(x)

  if y in ylst:
    ylst.remove(y)
  else:
    ylst.append(y)

for i in xlst+ylst:
  print(i, end=" ")

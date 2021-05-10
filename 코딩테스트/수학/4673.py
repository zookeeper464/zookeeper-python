lst = [False for i in range(10001)]
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        a = l*2+k*11+j*101+i*1001
        if a>10000:
          pass
        else:
          lst[a] = True

for i in range(10001):
  if not lst[i]:
    print(i)

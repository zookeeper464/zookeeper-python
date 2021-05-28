lst = [True for i in range(10000)]
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        n = 2*l+11*k+101*j+1001*i
        if n<10000:
          lst[n] = False

for i in range(1,10000):
  if lst[i]:
    print(i)

N,M = [int(x) for x in input().split(" ")]

six = []
one = []
num = N%6
for _ in range(M):
  s,o = [int(x) for x in input().split(" ")]
  six.append(s)
  six.append(6*o)
  one.append(o*num)
  one.append(s)

print((N//6)*min(six)+min(one))


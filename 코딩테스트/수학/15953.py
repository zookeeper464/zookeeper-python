l1 = [0,500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6+[0]*80
l2 = [0,512]+[256]*2+[128]*4+[64]*8+[32]*16+[0]*34

t = int(input())
answer = []
for i in range(t):
  a,b = map(int,input().split())
  answer.append((l1[a]+l2[b])*10000)

for i in answer:
  print(i)

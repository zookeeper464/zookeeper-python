a,b,v = map(int,input().split())
answer = (v-a)//(a-b)+1
if (v-a)%(a-b) ==0: pass
else: answer += 1
print(answer)

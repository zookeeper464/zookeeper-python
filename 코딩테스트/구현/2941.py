s = input()
answer = 0
for i in ["c=","c-","dz=","d-","lj","nj","s=","z="]:
  n = len(s)
  s = s.replace(i,"")
  answer += (n-len(s))//len(i)
answer += len(s)
print(answer)

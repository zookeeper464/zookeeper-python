s = input().split('-')
try:
  answer = sum(list(map(int,s[0].split('+'))))
except: 
  answer = int(s[0])
for i in s[1:]:
  try:
    answer -= sum(list(map(int,i.split('+'))))
  except: 
    answer -= int(i)
print(answer)

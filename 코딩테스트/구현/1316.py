n = int(input())
answer = n
for _ in range(n):
  s = input()
  st = set(s[0])
  for j in range(1,len(s)):
    if s[j] in st and s[j] != s[j-1]:
      answer-=1
      break
    if s[j] not in st:
      st.add(s[j])
print(answer)

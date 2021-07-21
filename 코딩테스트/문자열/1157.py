s = input().upper()
lst = [[i,0] for i in range(26)]
for i in s:
  lst[ord(i)-65][1] += 1

lst.sort(key = lambda x : -x[1])
if lst[0][1] == lst[1][1]:
  print('?')
else:
  print(chr(lst[0][0]+65))

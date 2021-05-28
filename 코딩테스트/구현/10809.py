#97#122
s = input()
for i in range(97,123):
  try:
    index = s.find(chr(i))
  except:
    index = -1
  print(index, end=" ")

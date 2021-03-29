answer = []
while True:
  s = input()
  if s == "0":
    break
  if s == s[::-1]:
    answer.append("yes")
  else:
    answer.append("no")

for i in answer:
  print(i)

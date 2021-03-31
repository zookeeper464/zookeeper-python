n = int(input())

dic = {}
for i in range(n):
  s, io = input().split()
  if io == "enter":
    dic[s] = True
  else:
    dic[s] = False
#입력 부분 설정, 입장과 퇴장 입력

lst = []
for i in dic.items():
  if i[1]:
    lst.append(i[0])
lst.sort(reverse = True)
#남아있는 사람 lst에 모으고 정렬

for i in lst:
  print(i)

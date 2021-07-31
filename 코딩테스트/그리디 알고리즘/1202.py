n,k = map(int,input().split())
dia_dict = dict()

for _ in range(n):
  a,b = map(int,input().split())
  dia_dict[a] = b

bag_list = []
for _ in range(k):
  m = int(input())
  bag_list.append(m)

key_list = list(dia_dict.keys())
bag_list.sort(reverse=True)
key_list.sort()
dia = [True] * n
answer = 0

for _ in range(k):
  temp = bag_list.pop()
  val = 0
  idx = -1
  for i in range(n):
    if temp>= key_list[i]:
      if dia[i] and val < dia_dict[key_list[i]]:
        val = dia_dict[key_list[i]]
        idx = i
        dia[i] = False
    else:
      break
  if idx >-1:
    dia[idx] = False
    answer += val

print(answer)

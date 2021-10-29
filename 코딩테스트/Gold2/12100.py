from collections import deque

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

def move_left(lst):
  return_list = []
  for r in range(n):
    temp = None
    temp_list = deque()
    for c in range(n-1,-1,-1):
      if lst[r][c] == 0:
         pass
      elif temp == None:
        temp = lst[r][c]

      elif temp == lst[r][c]:
        temp_list.appendleft(temp*2)
        temp = None
      else:
        temp_list.appendleft(temp)
        temp = lst[r][c]

    if temp:
      temp_list.appendleft(temp)

    return_list.append([0]*(n-len(temp_list))+list(temp_list))
  
  return return_list

def move_right(lst):
  return_list = []
  for r in range(n):
    temp = None
    temp_list = []
    for c in range(n):
      if lst[r][c] == 0:
        pass
      elif temp == None:
        temp = lst[r][c]

      elif temp == lst[r][c]:
        temp_list.append(temp*2)
        temp = None
      else:
        temp_list.append(temp)
        temp = lst[r][c]

    if temp:
      temp_list.append(temp)

    return_list.append(temp_list+[0]*(n-len(temp_list)))
  
  return return_list

def move_up(lst):
  return_list = []
  for c in range(n):
    temp = None
    temp_list = []
    for r in range(n):
      if lst[r][c] == 0:
        continue
      elif temp == None:
        temp = lst[r][c]

      elif temp == lst[r][c]:
        temp_list.append(temp*2)
        temp = None
      else:
        temp_list.append(temp)
        temp = lst[r][c]

    if temp:
      temp_list.append(temp)

    return_list.append(temp_list+[0]*(n-len(temp_list)))
  
  return list(zip(*return_list))

def move_down(lst):
  return_list = []
  for c in range(n):
    temp = None
    temp_list = deque()
    for r in range(n-1,-1,-1):
      if lst[r][c] == 0:
        continue
      elif temp == None:
        temp = lst[r][c]

      elif temp == lst[r][c]:
        temp_list.appendleft(temp*2)
        temp = None
      else:
        temp_list.appendleft(temp)
        temp = lst[r][c]

    if temp:
      temp_list.appendleft(temp)

    return_list.append([0]*(n-len(temp_list))+list(temp_list))
  
  return list(zip(*return_list))

q = deque([lst])
for _ in range(5):
  for _ in range(len(q)):
    now_list = q.popleft()
    q.append(move_left(now_list))
    q.append(move_right(now_list))
    q.append(move_up(now_list))
    q.append(move_down(now_list))

answer = 0
for _ in range(len(q)):
  temp = q.popleft()
  for r in range(n):
    for c in range(n):
      if answer < temp[r][c]:
        answer = temp[r][c]

print(answer)

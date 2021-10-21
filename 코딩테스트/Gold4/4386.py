from heapq import heappop, heappush

def roll(r,c):
  temp = (v_list[r][0]-v_list[c][0])**2
  temp += (v_list[r][1]-v_list[c][1])**2
  temp = temp**(1/2)
  return round(temp,5)

def check():
  hq = e_list[0][:]
  visited = set([0])
  answer = 0

  while len(visited)<n:
    val,num = heappop(hq)
    if num not in visited:
      answer += val
      visited.add(num)
    else:
      continue

    for next_val,next_num in e_list[num]:
      if next_num not in visited:
        heappush(hq,[next_val,next_num])
  
  return answer

n = int(input())
v_list = []
for _ in range(n):
  x,y = map(float,input().split())
  v_list.append([x,y])

e_list = [[] for _ in range(n)]
for i in range(n):
  for j in range(i+1,n):
    temp = roll(i,j)
    heappush(e_list[i],[temp,j])
    heappush(e_list[j],[temp,i])

    
print(round(check(),2))

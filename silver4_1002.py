N=int(input())
location_list=[]

def checker(lists):
  a=(lists[0]-lists[3])**2
  b=(lists[1]-lists[4])**2
  c=(lists[2]+lists[5])**2
  d=(lists[2]-lists[5])**2
  return [a+b-c,d-a-b]

for i in range(N):
  temp=input().split()[:6]
  temp=list(map(int,temp))
  location_list.append(temp)

for i in location_list:
  if checker(i)[0]<0 and checker(i)[1]<0:
    print(2)
  elif checker(i)[0]*checker(i)[1]==0:
    print(1)
  else:
    print(0)

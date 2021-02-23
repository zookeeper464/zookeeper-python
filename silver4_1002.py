N=int(input())
location_list=[]

def dist(lists):
  a=(lists[0]-lists[3])**2
  b=(lists[1]-lists[4])**2
  return (a+b)**(1/2)

for i in range(N):
  temp=list(map(int,input().split()))[:6]
  location_list.append(temp)

for i in location_list:
  a,b=max(i[2],i[5]),min(i[2],i[5])
  if dist(i)==0 and a==b:
    print(-1)
  elif dist(i)<a+b and dist(i)>a-b:
    print(2)
  elif dist(i)==a+b or dist(i)==a-b:
    print(1)
  elif dist(i)>a+b or dist(i)<a-b:
    print(0)

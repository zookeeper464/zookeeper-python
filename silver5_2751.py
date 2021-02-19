def heapify(unsorted, index, heap_size):
  largest=index
  l_index=2*index+1
  r_index=2*index+2
  
  if l_index<heap_size and unsorted[l_index]>unsorted[largest]:
    largest=l_index

  if r_index<heap_size and unsorted[r_index]>unsorted[largest]:
    largest=r_index
  
  
  if largest!=index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
  n=len(unsorted)
  for i in range(n//2-1, -1,-1):
    heapify(unsorted,i,n)
    
  for i in range(n-1,0,-1):
    unsorted[0],unsorted[i]=unsorted[i],unsorted[0]
    heapify(unsorted,0,i)
    
  return unsorted

N=int(input())
val_list=[]
for i in range(N):
  a=int(input())
  val_list.append(a)

lst=heap_sort(val_list)
for i in lst:
  print(i)

lst = list(map(int,input().split()))
def check (lst):
  if lst[1]>lst[0]:
    for i in range(1,len(lst)):
      if lst[i]<lst[i-1]:
        return "mixed"
    return "ascending"
  elif lst[1]<lst[0]:
    for i in range(1,len(lst)):
      if lst[i]>lst[i-1]:
        return "mixed"
    return "descending"

print(check(lst))

val=input()

list_val=list(val)
list_val.sort()
list_val=list_val[::-1]
val="".join(list_val)
print(val)

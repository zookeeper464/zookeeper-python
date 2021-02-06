N=int(input())
temp_list=[]
for i in range(N):
    a=int(input())
    if a not in temp_list:
        temp_list.append(a)
new_list=sorted(temp_list)
for i in new_list:
    print(i)
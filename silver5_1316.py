def remake(char):
    temp_list=list(char)
    new_list=[]
    new_list.append(temp_list[0])
    for i in temp_list:
        if i != new_list[-1]:
            new_list.append(i)
    new_str = "".join(new_list)
    return new_str

def checker(char):
    length=len(char)
    for i in range(length):
        for j in range(length):
            if i!=j and char[i]==char[j]:
                return 0
    return 1

num=int(input())
new_list=[]
count=0
for i in range(num):
    new_str=input()
    new_list.append(new_str)
for i in new_list:
    i=remake(i)
    count+=checker(i)
print(count)

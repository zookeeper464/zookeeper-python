def checker(char):
    length=len(char)
    
    for i in range(length):
        if "dz=" in char:
            length-=1
        for i in ["c=","c-","d-","lj","nj","s=","z="]:
            if i in char:
                char=char.replace(i,"",1)
                length-=1
    print(length)

char=input()
checker(char)
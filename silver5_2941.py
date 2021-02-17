def checker(char):
    length=len(char)
    if "dz=" in char:
        length-=char.count("dz=")
    for i in ["dz=","c=","c-","d-","lj","nj","s=","z="]:
        if i in char:
            n=char.count(i)
            char=char.replace(i," ")
            length-=n
    print(length)

char=input()
checker(char) 

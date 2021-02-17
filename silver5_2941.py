def checker(char):
    length=len(char)

    for i in range(length):
        if "dz=" in char:
            length-=1
        for i in ["c=","c-","d-","lj","nj","s=","z="]:
            if i in char:
                n=char.count(i)
                char=char.replace(i," ")
                length-=n
                print(char)
    print(length)

char=input()
checker(char) 

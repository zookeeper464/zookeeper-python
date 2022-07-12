string = ""
txt = ""

def KMP(string, txt):
    M,N = len(string), len(txt)
    lps = [0]*M
    computeLPS(string, txt)

    i,j = 0, 0 
    while i < N:
        if string[j] == txt[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            j = lps[j-1]

def LPS(string, lps):
    leng,i = 0, 1
    while i < len(pat):
        if string[i] == string[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

def subString(Str,n):
    l=[]
    for Len in range(1,n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            l.append(Str[i:j+1])
    return l

s=input()
l=subString(s,len(s))
k=max([len(set(list(i))) for i in l])
print(k)

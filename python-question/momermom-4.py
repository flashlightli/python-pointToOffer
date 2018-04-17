def part(L,p,r):
    x = L[r]
    i = p-1
    for j in range(p,r):
        if L[j]<=x:
            i+=1
            L[i],L[j]=L[j],L[i]
        print(L)
    L[i+1],L[r]=L[r],L[i+1]
A=[3,1,7,2,6,8,4,5]
part(A,0,len(A)-1)
print(A)

#generator-based coroutine     实现原理
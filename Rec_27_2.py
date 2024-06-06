n=int(input("Enter the no. of soldiers: "))
k=int(input("Enter the skip: "))
positions=[1]*n
i=0

def check(i,n,positions):
    count=0
    while i<n:
        if positions[i]!=0:
            count+=1
        i+=1
    return count

def find(i,n,positions):
    while i<n:
        if positions[i]!=0:
            return i
        i+=1
    return

def R27(i,n,k,positions):
    if i<n:
        positions.pop(k)
        if check(i,n,positions)>1:
            return R27(i+k,n,k,positions)
        pos=find(i,n,positions)
    i%=n
    return R27((i,n,k,positions))

R27(i,n,k,positions)
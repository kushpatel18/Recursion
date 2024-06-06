n=int(input("Enter a number: "))
i=1
arr=[0]*n

def R7(i,n,arr):
    if i<=n:
        arr[i-1]=i
        R7(i+1,n,arr)
    return  arr

print(R7(i,n,arr))
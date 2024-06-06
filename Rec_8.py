i=0
arr=[1,2,3,4,5]
n=len(arr)-1
def R8(i,n,arr):
    if i<=n:
        print(arr[i],end=" ")
        R8(i+1,n,arr)

R8(i,n,arr)

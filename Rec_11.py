i=-1
arr=[1,2,3,4,5]
n=-len(arr)
def R11(i,n,arr):
    if i>=n:
        print(arr[i],end=" ")
        R11(i-1,n,arr)

R11(i,n,arr)

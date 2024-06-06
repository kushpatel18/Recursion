arr=[1,2,3,4,5,3]
i=len(arr)-1
k=int(input("Enter a value: "))
def R15(i,k,arr):
    if arr[i]!=k:
        return R15(i-1,k,arr)
    return i

print(R15(i,k,arr))

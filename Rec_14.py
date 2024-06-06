i=0
arr=[1,2,3,4,5]
k=int(input("Enter a value: "))
def R14(i,k,arr):
    if arr[i]!=k:
        return R14(i+1,k,arr)
    return i

print(R14(i,k,arr))

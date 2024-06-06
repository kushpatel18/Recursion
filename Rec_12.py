i=0
arr=[1,2,3,4,5]
k=int(input("Enter a number: "))
def R12(i,k,arr):
    if i!=k:
        return R12(i+1,k,arr)
    return arr[k]

print(R12(i,k,arr))

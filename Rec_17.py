arr=[1,2,3,4,5,3,5,5,3,5,2,4,3]
i=0
n=len(arr)-1
value=int(input("Enter a value: "))

def R17(i,value,n,arr):

    if i<=n:
        if arr[i]==value:
            return i
        return R17(i+1,value,n,arr)
    return

print("Found at index: ",R17(i,value,n,arr))
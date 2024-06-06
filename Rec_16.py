arr=[1,2,3,4,5,3,5,5,3,5,2,4,3]
i=0
count=0
n=len(arr)-1
value=int(input("Enter a value: "))

def R16(i,count,value,n,arr):

    if i<=n:
        if arr[i]==value:
            count+=1
        return R16(i+1,count,value,n,arr)
    return count

print(R16(i,count,value,n,arr))
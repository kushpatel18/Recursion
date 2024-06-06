i=0
arr=[1,2,3,4,5]
n=arr[-1]
temp=1

def R9(i,n,temp,arr):
    if arr[i]!=n:
        temp+=1
        return R9(i+1,n,temp,arr)
    return  temp
print(R9(i,n,temp,arr))

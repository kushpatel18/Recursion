n=int(input("Enter a number of terms: "))
fibonacci=[0]*n
i=0

def Fibonacci(n):

    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return Fibonacci(n-1)+Fibonacci(n-2)

def R26(i,n,fibonacci):

    if i<=n-1:
        fibonacci[i]=Fibonacci(i)
        return R26(i+1,n,fibonacci)
    return fibonacci



print(R26(i,n,fibonacci))
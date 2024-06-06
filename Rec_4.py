n=int(input("Enter a number: "))
fact=1


def R4(fact,n):
    if n>1:
        return R4(fact*n,n-1)
    return  fact


print(f"Factorial of {n} is: {R4(fact,n)}")
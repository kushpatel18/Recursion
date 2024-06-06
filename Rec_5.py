x=int(input("Enter the number: "))
n=int(input("Enter the power: "))
temp=x

def R5(x,n,temp):
    if n>1:
        return R5(x*temp,n-1,temp)
    return x


print(f"{x}^{n}: {R5(x,n,temp)}")
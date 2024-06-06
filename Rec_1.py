n=int(input("Enter a number: "))

def R1(n):
    if n>0:
        print(n)
        return R1(n-1)
    return
R1(n)
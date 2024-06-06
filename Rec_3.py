n=int(input("Enter a number: "))


def R3(n):
    if n>0:
        print(n,end=" ")
        R3(n-1)
    if n==0:
        print()
        return
    print(n,end=" ")

R3(n)
n=int(input("Enter a number: "))


def R6(n):
    if n<=0:
        return
    print(n)
    R6(n-1)
    print(n)
    R6(n-1)
    print(n)

R6(n)





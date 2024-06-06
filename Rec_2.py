n = int(input("Enter a number: "))
i = 1


def R2(i, n):
    if i <= n:
        print(i)
        return R2(i + 1, n)
    return


R2(i, n)

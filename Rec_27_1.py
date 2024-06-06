n=int(input("Enter the no. of disks: "))

def R27(n,t1,t3,t2):
    if n==1:
        print(f"{n} [{t1} -> {t2}]")
        return

    R27(n-1,t1,t2,t3)
    print(f"{n} [{t1} -> {t2}]")
    R27(n-1,t3,t1,t2)

R27(n,'10','12','11')







        




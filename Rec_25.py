n=int(input("Enter a number: "))
sum=0

def R25(n,sum):

    if n!=0:
        rem=n%10
        sum+=rem
        return  R25(n//10,sum)
    return sum

print(R25(n,sum))
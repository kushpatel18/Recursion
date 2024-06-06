n=int(input("Enter a number: "))
rev=0

def R20(n,rev):

    if n!=0:
        rem=n%10
        rev=rev*10+rem
        return  R20(n//10,rev)
    return rev

if n==R20(n,rev):
    print("Palindrome")
else:
    print("Not a Palindrome")
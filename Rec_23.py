n=int(input("Enter a number: "))
count=0

def R23(n,count):

    if n!=0:
        rem=n%10
        count+=1
        return  R23(n//10,count)
    return count

print(R23(n,count))
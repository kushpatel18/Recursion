str1=input("Enter a string: ")
n=len(str1)-1
i=0
num=0


def atoi(str1,i,n,num):

    if i<=n:
        num=num*10+int(str1[i])
        return atoi(str1,i+1,n,num)
    return num

print("Number is: ",atoi(str1,i,n,num))
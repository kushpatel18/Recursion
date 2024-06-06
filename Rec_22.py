str1=input("Enter a string: ")
str2=input("Enter a string: ")
n1=len(str1)
n2=len(str2)
i=0
str_copy=""
print(str_copy)


def R22(i,n1,str1,str_copy):

    if i<=n1-1:
        str_copy+=str1[i]
        return R22(i+1,n1,str1,str_copy)
    return str_copy

str2=R22(i,n1,str1,str_copy)
print(str2)
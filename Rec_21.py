str1=input("Enter a string: ")
n=len(str1)-1
i=0
rev_str=""


def R21(str1,i,n,rev_str):

    if i<=n:
        rev_str+=str1[n-i]
        return R21(str1,i+1,n,rev_str)
    return rev_str

print(R21(str1,i,n,rev_str))
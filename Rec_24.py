str1=input("Enter a string: ")
length=0
i=0
str1+="\0"

def R24(i,str1,length):

    if str1[i]!="\0":
        length+=1
        return  R24(i+1,str1,length)
    return length

print(R24(i,str1,length))
str1=input("Enter a string: ")
str2=input("Enter a string: ")

x=str1[0:2]
str1=str1.replace(str1[0:2], str2[0:2])
str2=str2.replace(str2[0:2],x)

print(str1)
print(str2)
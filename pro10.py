strng=input("Enter the string :")
list = list(strng)
lngth=len(strng)
temp=list[0]
list[0]=list[lngth-1]
list[lngth-1]=temp
str=""
final=str.join(list)
print(final)

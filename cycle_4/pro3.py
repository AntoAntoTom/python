def check():
	str1=input("enter the string :")
	str2=input("enter the string :")
	n=int(input("enter :"))
	if(str1[0:n]==str2[0:n]):
		return True
	else:
		return False
flag=check()
if(flag):
	print("same")
else:
 	print("diff")

strng=input("Enter the sentence :").split(" ")
dict={}
for i in strng:
	if  i in dict:
		dict[i]=dict[i]+1
	else:
		dict[i]=1
print(dict)

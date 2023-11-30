a=int(input("Enter the limet :"))
list=[]
for i in range(a):
	strng=input("Enter the string :")
	list.append(strng)
count=0
for i in  list:
	for j in i:
		if j=='a':
			count+=1
print(count)

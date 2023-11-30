a=int(input("Enter the limet :"))
list =[]
for i in range(a) :
	n=int(input("Enter the element :"))
	if n>100:
		list.append("over")
	else :
		list.append(n)
for i in list :
	print(i)

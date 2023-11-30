a=int(input("Enter the limet in first list :"))
list1=[]
for i in range(a):
	n=int(input("Enter the element :"))
	list1.append(n)
b=int(input("Enter the limet in second list :"))
list2=[]
for i in range(b):
	n=int(input("Enter the element :"))
	list2.append(n)
sum1=0
sum2=0
if a==b:
	print("length of the 2 list is :",a)
else:
	 print("length of first list :",a," & second list :",b)

for i in list1:
	sum1+=i

for i in list2:
	sum2+=i
if sum1==sum2:
	print("sum of both list is same,which is ",sum1)
else :
	print("sum of both list are diierent,which are",sum1,",",sum2)
list=[]
for i in list1:
	for j in list2:
		if i==j :
			if i not in list:
				list.append(i)
print("The elemente which were common in list were,",list)

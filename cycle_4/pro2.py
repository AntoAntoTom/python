def oddEven(num):
	if num%2==0:
		return "even"
	else:
		return "odd"
a=int(input("enter number :"))
print("the number ",a," is ",oddEven(a))

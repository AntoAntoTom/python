num_list=input("enter :").split(',')
odd_list=[]
for i in num_list:
	if int(i)%2!=0:
		odd_list.append(int(i))
print(odd_list)

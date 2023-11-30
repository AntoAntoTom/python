color_list1=input("Enter the first set of colours :").split(' ')
color_list2=input("Enter the second set of colours :").split(' ')
result=[item for item in color_list1 if item not in color_list2]
print(result)

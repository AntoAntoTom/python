num_list = input("Enter the numbers :").split(',')
numbers=[]
for i in  num_list:
	numbers.append(int(i)) 

positive_numbers = [num for num in numbers if num > 0]
print("positive no. =",positive_numbers)
squares = [x**2 for x in numbers]
print("the squares =",squares)
word = input("Enter a word :")
vowels = [char for char in word if char in 'aeiouAEIOU']
print("the vowels in the word",word,"is",vowels)
ordinal_values = [ord(char) for char in word]
print(ordinal_values)

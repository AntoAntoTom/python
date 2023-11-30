def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        print(f"'{char}': {count}")
input_string = input("Enter a string: ")
count_characters(input_string)

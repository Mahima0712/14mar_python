# ask the user for the dictionary and number of top values to find
my_dict = eval(input("Enter a dictionary: "))
num_top_values = int(input("Enter the number of top values to find: "))

# sort the dictionary by value in descending order and get the first n items
highest_n = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:num_top_values]

# print the highest n values
print(f"The highest {num_top_values} values in the dictionary are:")
for key, value in highest_n:
    print(f"{key}: {value}")
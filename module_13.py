# ask the user for the dictionary and sorting order
my_dict = eval(input("Enter a dictionary: "))
sort_order = input("Sort by ascending (a) or descending (d) order? ")

# sort the dictionary by value
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=(sort_order == 'd'))

# print the sorted dictionary
print("The sorted dictionary is:")
for key, value in sorted_dict:
    print(f"{key}: {value}")
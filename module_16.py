list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

# Creating an empty dictionary to store frequencies
freq_dict = {}

# Iterating over each number in the list
for num in list:
    # If the number is not in the dictionary, set its frequency to 1
    if num not in freq_dict:
        freq_dict[num] = 1
    # If the number is already in the dictionary, increment its frequency by 1
    else:
        freq_dict[num] += 1

# Printing the frequencies of each number in the list
for num, freq in freq_dict.items():
    print(num, ":", freq)
def unique_list(list):
    # Create an empty list to store unique elements
    unique_lst = []
    # Iterate over the elements in the input list
    for element in list:
        # If the element is not already in the unique list, append it
        if element not in unique_lst:
            unique_lst.append(element)
    # Return the unique list
    return unique_lst

# Example usage
list = [1,2,3,3,4,4,4,5,5,5]
print("Original list:", list)
unique_lst = unique_list(list)
print("Unique list:", unique_lst)
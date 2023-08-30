def find_unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Input a list from the user
input_string = input("List: ")
input_list = [int(item) for item in input_string.split()]

# Calling the function with the input list
unique_elements = find_unique_elements(input_list)

# Printing the result
print("Unique elements:", unique_elements)

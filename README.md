Task-3: Unique Elements

Question: Write a function that takes a list as input and returns a new list containing only the unique elements in the same order they appeared.

Code:

def find_unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list
    
input_string = input("List: ")
input_list = [int(item) for item in input_string.split()]

unique_elements = find_unique_elements(input_list)

print("Unique elements:", unique_elements)

Logic:
1. Defining function named find_unique_elements that takes an input_list as its parameter.
2. Getting list from the user with an input_string.
3. Creating an empty list named unique_list to store the unique elements.
4. Go through each item in the input list and check if it is present in unique list already.
5. After all items, function returns unique list.
6. Print result.



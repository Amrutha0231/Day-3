Task-1: File Word Counter
Question: Write a program that reads a text file and counts the occurrences of each word. Ignore punctuation and consider case-insensitivity.

Code:

import string
def main():
    file_name = input("File: ")

    try:
        with open(file_name, 'r') as file:
            word_count = {}
            
            for line in file:
                words = line.lower().split()

                for word in words:
                    word = word.strip(string.punctuation)
                    
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

            print("Word frequency:", word_count)
    except FileNotFoundError:
        print("File not found.")
if __name__ == "__main__":
    main()

Description:
1. The program asks the user to enter the name of the text file.
2. The program attempts to open the file with the name provided by the user using a with statement.
3. Inside the with block, a dictionary named word_count is initialized.
4. This dictionary will store the frequency of each word encountered in the text.
5. The program reads the file line by line using a for loop where each line is stored in the line variable.
6. It checks if the word is already present in the word_count dictionary. If it is, the frequency count will increase by 1.
7. If not, a new entry for that word is created with frequency 1.
8. Once all the words in the file have been processed, the program prints the resulting word frequency.


Task-2: Fibonacci Sequence Generator

Question: Create a program that generates the Fibonacci sequence up to a given number of terms.

Code:

n = int(input("Enter the number of terms: "))
fibonacci_sequence = [0, 1]
while len(fibonacci_sequence) < n:
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)
print("Fibonacci sequence:", fibonacci_sequence)

Logic:
1. The program asks the user to enter the number of terms for input.
2. Start sequence with 0 and 1.
3. Program then adds new terms by taking the sum of the previous two.
4. Repeat till sequence reaches desired number of terms.
5. Print the sequence.


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



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

# File Word Counter
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



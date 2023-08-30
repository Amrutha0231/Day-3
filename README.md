Task-4: Word Frequency in a Sentence

Question: Create a program that takes a sentence and a list of words as input. The program should count the frequency of each word in the sentence.

Code:

sentence = input("Enter a sentence: ")

word_list = input("Enter words separated by spaces: ").lower().split()

word_frequency = {}

for word in sentence.lower().split():
    if word in word_list:
        word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word frequency:", word_frequency)

Logic:
1. Program takes the input sentence from the user.
2. Program asks the user to enter words and stores them in the input word list.
3. The program processes the sentence and word list.
4. It counts the frequency of the input words in the sentence.
5.  The program prints this dictionary as the output.

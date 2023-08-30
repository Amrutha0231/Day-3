# Input sentence
sentence = input("Enter a sentence: ")

# Input words as a list
word_list = input("Enter words separated by spaces: ").lower().split()

# Count word frequency
word_frequency = {}

for word in sentence.lower().split():
    if word in word_list:
        word_frequency[word] = word_frequency.get(word, 0) + 1

# Printing the word frequency result
print("Word frequency:", word_frequency)
